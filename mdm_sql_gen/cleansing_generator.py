from LIBPY_MDM.mdm_sql import CleansingSQL
from LIBPY_MDM.mdm_sql_gen.builders import CleansingBuilder
from LIBPY_MDM.common import read_config
from typing import List


class GeneratorRule:
    def __init__(self, config_rule):
        self.config_rule = config_rule
        self.lst_cleansing = read_config.group_cleansing_by_action(self.config_rule["cleansing"])
        self.table_name = self.config_rule['table_name']

    def generator_cleansing_sql(self) -> List[str]:    
        logics_query = []
        # create part logic 
        for type, item_config in self.lst_cleansing.items():
            logic_type_part = []
            list_column = self.config_rule['list_column']
            for col_config in item_config:
                logic_type_part.append(self.create_logic_part(config_col = col_config, cleansing_type = type))

                list_column = [item for item in list_column if item != col_config['column_name']]

            builder = CleansingBuilder(column_select = list_column, table_name = self.table_name)
            query = builder.add_logic_part(logic_type_part).build()
            logics_query.append(query)
            
        return logics_query

    def create_logic_part(self, config_col, cleansing_type) -> str:
        column_name = config_col['column_name']
        cleansing = CleansingSQL(column_name)

        if cleansing_type == "cleantp_remove_pattern":
            characters = config_col['characters']
            return f"{cleansing.cleansing_remove_character(characters)} AS {column_name}"
        
        elif cleansing_type == "cleantp_format_datetime":
            format_date = config_col['format_date']
            return f"{cleansing.cleansing_convert_date(format_date)} AS {column_name}"

    