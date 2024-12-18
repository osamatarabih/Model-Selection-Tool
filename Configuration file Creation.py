# Configuration file
import json

# Define the JSON data
config_data = {
    "working_dir": "C:/Osama Tarabih/Generalized Modeling Framework",
    "available_models_file": "./Available_Models.csv",
    "water_body_type": "Watershed",
    "watershed_size": "Medium",
    "watershed_type": ["Agricultural"],
    "model_parameters": ["Q", "TP", "TN"],
    "time_step": "Daily",
    "simulation_objectives": ["Screening Simulation", "TMDL development"],
    "model_complexity": "Medium",
    "model_availability": "Open source",
    "model_limitations": ["manual calibration", "poor sediment simulation"],
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
