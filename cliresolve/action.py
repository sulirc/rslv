import os
import sys

from . import __delimiter__, __cache_file__
from .util import to_alias_map, to_alias_text


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

    def handle_cli_register(self, alias, path):
        """rslv register command

        e.g.
        rslv -r @react "path/to/react"
        """
        if self.alias_map.get(alias):
            self.update_alias(alias, path)
        else:
            self.create_alias(alias, path)
        
        print("Register Ok")

        return self.alias_map

    def handle_cli_unregister(self, alias):
        """rslv unregister command

        e.g.
        rslv -R @react
        """
        print("Unregister Ok")

    def handle_cli_exec(self, alias):
        """rslv exec command

        e.g.
        rslv -e cd @react
        """
        path = self.alias_map.get(alias)
        if path:
            print(path, file=sys.stdout)
        else:
            origin_path = alias
            print(origin_path, file=sys.stdout)

    def handle_cli_list(self):
        """rslv list command

        e.g. 
        rslv -l
        @preact => a/b/c/preact
        @react => path/to/react
        """
        print("Registered alias list:")
        for alias, path in self.alias_map.items():
            print(f'{alias}{__delimiter__}{path}')
