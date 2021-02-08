import os
import sys

from . import __delimiter__, __cache_file__
from .util import to_alias_map, to_alias_text
from .format import print_msg, print_error, print_alias_map


class RslvAliasNotFoundError(NotImplementedError):
    pass


class RslvAction:
    """rslv action class

    Process rslv command and make effect
    """

    def __init__(self):
        self._setup()
        self._create_alias_map()

    def _setup(self):
        if not os.path.exists(__cache_file__):
            with open(__cache_file__, 'w'):
                pass

        self.alias_map = dict()

    def _create_alias_map(self):
        with open(__cache_file__, 'r') as f:
            table = f.read()
            alias_text = table.splitlines()
            self.alias_map = to_alias_map(alias_text, __delimiter__)

    def update_alias(self, alias, path):
        self.alias_map[alias] = path

        with open(__cache_file__, 'w') as f:
            f.writelines(to_alias_text(self.alias_map, __delimiter__))

        return self.alias_map

    def create_alias(self, alias, path):
        with open(__cache_file__, 'a') as f:
            f.write(f'{alias}{__delimiter__}{path}\n')
            self.alias_map[alias] = path

        return self.alias_map

    def remove_alias(self, alias):
        self.alias_map.pop(alias)

        with open(__cache_file__, 'w') as f:
            f.writelines(to_alias_text(self.alias_map, __delimiter__))

        return self.alias_map

    def handle_cli_register(self, alias, path):
        """rslv register command

        e.g.
        rslv -r @react "path/to/react"
        """
        abs_path = os.path.abspath(path)

        if self.alias_map.get(alias):
            self.update_alias(alias, abs_path)
        else:
            self.create_alias(alias, abs_path)

        print_msg("register ok")

        return self.alias_map

    def handle_cli_unregister(self, alias):
        """rslv unregister command

        e.g.
        rslv -R @react
        """
        if self.alias_map.get(alias):
            self.remove_alias(alias)
            print_msg("unregister ok")
        else:
            print_error(f"alias `{alias}` no exist")

    def handle_cli_expand(self, alias):
        """rslv expand command

        e.g.
        rslv -e cd @react
        """
        path = self.alias_map.get(alias)
        if path:
            sys.stdout.write(path)
        else:
            _alias, *_paths = alias.split('/')
            _path = self.alias_map.get(_alias)
            if _path:
                for p in _paths:
                    _path += ('/' + p)
                sys.stdout.write(_path)
            else:
                sys.stdout.write(alias)

    def handle_cli_list(self):
        """rslv list command

        e.g.
        rslv -l
        @preact => a/b/c/preact
        @react => path/to/react
        """
        if len(self.alias_map) == 0:
            print_error("empty alias list. use `rslv -r @alias \"/path/to/resource/\"`")
            return

        print_alias_map(self.alias_map)

    def handle_cli_change(self, old, new):
        """rslv change command

        e.g.
        rslv -r @react @preact
        """
        # print(old, new)
        old_alias_path = self.alias_map.get(old)
        new_alias_path = self.alias_map.get(new)
        
        if new_alias_path:
            print_error(f"alias `{new}` => `{new_alias_path}` already existed")
            return
        
        if not old_alias_path:
            print_error(f"alias `{old}` no existed")
            return

        self.alias_map.pop(old)
        self.alias_map[new] = old_alias_path
        self.update_alias(new, old_alias_path)
        print_msg("change ok")

