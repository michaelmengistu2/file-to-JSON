import pandas as pd
import json
import os

def excel_to_json(input_excel_file, output_dir):
    # Read all sheets into a dictionary of DataFrames
    sheets = pd.read_excel(input_excel_file, sheet_name=None, engine='openpyxl')

    # Make sure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    for sheet_name, df in sheets.items():
        # Convert DataFrame to a list of dictionaries
        data = df.to_dict(orient='records')

        # Create a valid filename for each sheet
        filename = f"{sheet_name}.json".replace(" ", "_")
        output_path = os.path.join(output_dir, filename)

        # Write JSON to file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

        print(f"Converted sheet '{sheet_name}' to {filename}")

# Example usage
excel_to_json("path/to/your_file.xlsx", "path/to/output_folder")
