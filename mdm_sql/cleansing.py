
class CleansingSQL:
    def __init__(self, column_name):
        """
        Init Object CleansingSQL.

        Args:
            column_name (str): column name.
        """
        self.column_name = column_name

    def cleansing_remove_character(self, characters):
        """
        Remove unwanted characters from column.

        Args:
            characters (str): List characters remove (VD: "[ .,]").

        Returns:
            str: Query remove characters.
        """
        return f"REGEXP_REPLACE({self.column_name}, '{characters}', '')"
    
    def cleansing_convert_date(self, format_date):
        return f"TO_DATE({self.column_name}, '{format_date}')"


