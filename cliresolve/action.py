import os


def to_alias_text(alias_map, delimiter):
    """alias_map -> alias_text
    """
    alias_text = []
    for alias, path in alias_map.items():
        alias_text.append(f'{alias}{delimiter}{path}\n')

    return alias_text


def to_alias_map(alias_text, delimiter):
    """alias_text -> alias_map
    """
    alias_map = dict()

    for row in alias_text:
        alias, path = row.split(delimiter)
        alias_map[alias] = path

    return alias_map


class RslvAction:
    def __init__(self):
        self._setup()
        self._create_alias_map()

    def _setup(self):
        self.cache_db = '.rslv.db'
        self.delimiter = " => "

        if not os.path.exists(self.cache_db):
            with open(self.cache_db, 'w'):
                pass

        self.alias_map = dict()

    def _create_alias_map(self):
        with open(self.cache_db, 'r') as f:
            table = f.read()
            alias_text = table.splitlines()
            self.alias_map = to_alias_map(alias_text, self.delimiter)

    def update_alias(self, alias, path):
        self.alias_map[alias] = path

        with open(self.cache_db, 'w') as f:
            f.writelines(to_alias_text(self.alias_map, self.delimiter))

        return self.alias_map

    def create_alias(self, alias, path):
        with open(self.cache_db, 'a') as f:
            f.write(f'{alias}{self.delimiter}{path}\n')
            self.alias_map[alias] = path

        return self.alias_map

    def handle_cli_register(self, alias, path):
        if self.alias_map.get(alias):
            self.update_alias(alias, path)
        else:
            self.create_alias(alias, path)

        return self.alias_map

    def handle_cli_list(self):
        print('Registered alias list:')

        for alias, path in self.alias_map.items():
            print(f'{alias}{self.delimiter}{path}')
