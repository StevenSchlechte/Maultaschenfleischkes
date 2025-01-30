import json


class ImportData:
    def init(self, data_file: str):
        self.data_file = data_file
    
    def load_data(self) -> dict:
        with open(self.data_file, "r") as file:
            data = json.load(file)
        return data
        