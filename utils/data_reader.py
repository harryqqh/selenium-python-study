
import os
import json

class DataReader:
    """Utility class for handling test data operations."""

    def read_json(self, file_path):
        """Read data from a JSON file and return as Python object."""
        try:
            with open(file_path, encoding='utf-8') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found at: {file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in file: {file_path}")
    
    def read_data_from_json(self, filename):
        """Read data from a JSON file located in the 'datasets' directory."""
        default_json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'datasets', 'vacancy.json')        
        json_path =  default_json_path
        return self.read_json(json_path)

    def get_vacancy_data(self, path_to_json=None):
        return self.read_data_from_json(path_to_json)