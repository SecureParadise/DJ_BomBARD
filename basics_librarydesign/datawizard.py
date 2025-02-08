# File: datawizard.py

class DataWizard:
    """
    A library for simplifying data manipulation and analysis tasks.
    """
    
    def __init__(self, data):
        """
        Initialize the DataWizard with data.
        :param data: A list of dictionaries representing tabular data.
        """
        if not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
            raise ValueError("Data must be a list of dictionaries.")
        self.data = data

    def filter_rows(self, condition):
        """
        Filter rows based on a condition.
        :param condition: A lambda function that takes a row and returns True or False.
        :return: A new DataWizard instance with filtered rows.
        """
        filtered_data = [row for row in self.data if condition(row)]
        return DataWizard(filtered_data)

    def sort_by(self, column, reverse=False):
        """
        Sort rows by a specific column.
        :param column: The column to sort by.
        :param reverse: Sort in descending order if True.
        :return: A new DataWizard instance with sorted rows.
        """
        if not all(column in row for row in self.data):
            raise ValueError(f"Column '{column}' not found in all rows.")
        sorted_data = sorted(self.data, key=lambda x: x[column], reverse=reverse)
        return DataWizard(sorted_data)

    def get_column(self, column):
        """
        Extract a column as a list.
        :param column: The column to extract.
        :return: A list of values from the specified column.
        """
        if not all(column in row for row in self.data):
            raise ValueError(f"Column '{column}' not found in all rows.")
        return [row[column] for row in self.data]

    def summary(self):
        """
        Generate a summary of the dataset.
        :return: A dictionary with summary statistics.
        """
        num_rows = len(self.data)
        columns = {key: set() for row in self.data for key in row.keys()}
        for row in self.data:
            for key, value in row.items():
                columns[key].add(type(value).__name__)
        column_types = {key: list(types) for key, types in columns.items()}
        return {
            "num_rows": num_rows,
            "columns": column_types
        }
