import os


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
            rows = table.splitlines()
            for row in rows:
                _alias, _path = row.split("=>")
                self.alias_map[_alias] = _path

    def update_alias(self, alias, path):
        self.alias_map[alias] = path

        data = []
        for _alias, _path in self.alias_map.items():
            data.append(f'{_alias}{self.delimiter}{_path}\n')

        with open(self.cache_db, 'w') as f:
            f.writelines(data)

        return self.alias_map

    def create_alias(self, alias, path):
        with open(self.cache_db, 'a') as f:
            f.write(f'{alias}{self.delimiter}{path}\n')
            self.alias_map[alias] = path

        return self.alias_map

    def alias_register(self, alias, path):
        if self.alias_map.get(alias):
            self.update_alias(alias, path)
        else:
            self.create_alias(alias, path)

        return self.alias_map
