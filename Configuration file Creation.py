# Configuration file
import json

# Define the JSON data
config_data = {
    "working_dir": "C:/Osama Tarabih/Generalized Modeling Framework",
    "available_models_file": "./Available_Models.csv",
    "water_body_type": "Water body",
    "watershed_size": "Medium",
    "waterbody_size": "Medium",
    "watershed_type": ["Agricultural"],
    "waterbody_type": ["Coastal", "Estuarine", "Rivers", "Lakes"],
    "model_dimensions": "3D",
    "model_parameters": ["Water Levels", "Phosphorus", "Nitrogen", "algae"],
    "time_step": "Seconds",
    "simulation_objectives": ["Holistic Simulation", "sustainable water resource management", "flood risk assessment"],
    "model_complexity": "Complex",
    "model_availability": "Open source",
    "model_limitations": ["limited developer and community support"],
    "weights": {
        "SimObj_S": 0.4,
        "Data_S": 0.3,
        "ModLimit_S": 0.3
    }
}

# Save the data to a JSON file
with open('config.json', 'w') as json_file:
    json.dump(config_data, json_file, indent=4)

print("config.json has been created.")
