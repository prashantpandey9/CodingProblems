class Query:
    def __init__(self, table):
        self.table = table
        self.filters = []
        self.selected_columns = list(table.columns.keys())

    def select(self, *columns):
        if columns:
            self.selected_columns = columns
        return self

    def where(self, condition):
        self.filters.append(condition)
        return self

    def execute(self):
        results = self.table.rows
        for condition in self.filters:
            results = [row for row in results if condition(row)]
        return [{col: row[col] for col in self.selected_columns} for row in results]
