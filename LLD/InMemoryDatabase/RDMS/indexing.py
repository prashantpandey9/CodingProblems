class Indexing:
    def __init__(self, table, column_name):
        self.table = table
        self.column_name = column_name
        self.index = {}
        self._build_index()
    
    def _build_index(self):
        for i, row in enumerate(self.table.rows):
            value = row[self.column_name]
            if value not in self.index:
                self.index[value] = []
            
            self.index[value].append(i)
    
    def lookup(self, value):
        return [self.table.rows[i] for i in self.index.get(value, [])]