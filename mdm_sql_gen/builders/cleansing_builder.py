
class CleansingBuilder:
    def __init__(self, column_select, table_name):
        self.column_select =  column_select
        self.table_name = table_name
        self.logic_cleansing = []
    
    def add_logic_part(self, logic_column):
        self.logic_cleansing = logic_column
        return self
    
    def build(self):
        columns_part = ", ".join(self.column_select)
        logics_part = ", ".join(self.logic_cleansing)
        return f"SELECT {columns_part}, {logics_part} FROM {self.table_name}"
