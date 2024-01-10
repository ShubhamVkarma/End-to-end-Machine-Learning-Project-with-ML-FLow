import os
from mlProject.entity.config_entity import DataValidationConfig
import pandas as pd


class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config = config

    def validate_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_file)
            all_columns = list(data.columns)
            
            all_schema = self.config.all_schema.keys()

            for col in all_columns:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE,"w") as file:
                        file.write(f"validation status:{validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE,"w") as file:
                        file.write(f"vaildation status:{validation_status}")
                
            return validation_status
        except Exception as e:
            raise e