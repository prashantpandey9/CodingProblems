class Table:
    def __init__(self, name, columns):
        self.name = name
        self.columns = {col.name: col for col in columns}
        self.rows = []
        self.primary_key = None
        self.indexes = {}
    
    def set_primary_key(self, column_name):
        if column_name in self.columns:
            self.primary_key = column_name
        else:
            raise ValueError("Column does not exist in this table")
    
    def add_row(self, row_data):
        if len(row_data) != len(self.columns):
            raise ValueError("Row data does not match column count")
    
        row = dict(zip(self.columns.keys(), row_data))
        self.rows.append(row)
        return row

    def get_rows(self):
        return self.rows
    