import yaml
import json

# Load the index.yaml file
with open('./index.yaml', 'r') as index_file:
    index_data = yaml.safe_load(index_file)

# Convert to catalog.json format
catalog_data = {
    "charts": index_data["entries"]
}

# Write the catalog.json file
with open('./catalog.json', 'w') as catalog_file:
    json.dump(catalog_data, catalog_file, indent=2)
