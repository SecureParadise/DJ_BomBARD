from datawizard import DataWizard

# Example usage
data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]

wizard = DataWizard(data)
filtered_wizard = wizard.filter_rows(lambda row: row["age"] > 30)
sorted_wizard = wizard.sort_by("age")
column = wizard.get_column("city")
summary = wizard.summary()

print("Filtered Data:", filtered_wizard.data)
print("Sorted Data:", sorted_wizard.data)
print("City Column:", column)
print("Summary:", summary)
