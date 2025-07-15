import os
import csv
import json

def convert_all_csv_to_json(input_dir, output_dir):
    """
    Converts all CSV files in input_dir to JSON files in output_dir.
    """
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):
            csv_path = os.path.join(input_dir, filename)
            json_filename = filename.replace('.csv', '.json')
            json_path = os.path.join(output_dir, json_filename)

            with open(csv_path, mode='r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(csv_file)
                data = list(reader)

            with open(json_path, mode='w', encoding='utf-8') as json_file:
                json.dump(data, json_file, indent=4)

            print(f"Converted: {filename} → {json_filename}")

# Example usage (can be customized in a separate runner script)
if __name__ == "__main__":
    # Replace these with your own paths or handle with command-line args
    input_folder = r"path/to/input_folder"
    output_folder = r"path/to/output_folder"
    convert_all_csv_to_json(input_folder, output_folder)
