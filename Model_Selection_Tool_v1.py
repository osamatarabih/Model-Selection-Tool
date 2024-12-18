import pandas as pd
import numpy as np
import os
import json

# Load configuration from file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Change working directory
os.chdir(config["working_dir"])

# Read available modeling framework catalog
available_models_file = config["available_models_file"]
Available_Models = pd.read_csv(available_models_file, encoding='unicode_escape')

# Add scoring columns
Available_Models['SimObj_S'] = Available_Models['Simulation Objectives'].apply(lambda x: len(x.split(',')) if isinstance(x, str) else 0)
Available_Models['Data_S'] = Available_Models['Data Requirements'].apply(lambda x: len(x.split(',')) if isinstance(x, str) else 0)
Available_Models['ModLimit_S'] = Available_Models['Model Limitations'].apply(lambda x: len(x.split(',')) if isinstance(x, str) else 0)

# Extract inputs from config
WaterBodyType = [config["water_body_type"]]
WatershedSize = [config["watershed_size"]]
WatershedType = config["watershed_type"]
Model_Parameters = config["model_parameters"]
Time_step = [config["time_step"]]
selected_objectives = config["simulation_objectives"]
Model_Complexity = [config["model_complexity"]]
Model_Availability = [config["model_availability"]]
Model_Limitations = config["model_limitations"]

Available_Models['Model Limitations'] = Available_Models['Model Limitations'].fillna('')

# Filter the models based on inputs
filtered_models = Available_Models[
    (Available_Models['Water Body Type'].str.contains('|'.join(WaterBodyType), case=False)) &
    (Available_Models['Watershed Size'].str.contains('|'.join(WatershedSize), case=False)) &
    (Available_Models['Watershed Type'].str.contains('|'.join(WatershedType), case=False)) &
    (Available_Models['Parameters'].str.contains('|'.join(Model_Parameters), case=False)) &
    (Available_Models['Time Step'].str.contains('|'.join(Time_step), case=False)) &
    (Available_Models['Simulation Objectives'].str.contains('|'.join(selected_objectives), case=False)) &
    (Available_Models['Model Complexity'].str.contains('|'.join(Model_Complexity), case=False)) &
    (Available_Models['Model Availability'].str.contains('|'.join(Model_Availability), case=False)) &
    (~Available_Models['Model Limitations'].str.contains('|'.join(Model_Limitations), case=False))
]

# Display the filtered models
if not filtered_models.empty:
    print("Here are the models matching your criteria:")
    print(filtered_models[['Model', 'Water Body Type', 'Watershed Size', 'Watershed Type', 'Parameters', 'Simulation Objectives', 'Model Complexity', 'Model Availability', 'Model Limitations']])
else:
    print("No models match your criteria.")

# Optimization Algorithm
max_simobj_s = Available_Models['SimObj_S'].max()
max_data_s = Available_Models['Data_S'].max()
max_modlimit_s = Available_Models['ModLimit_S'].max()

def calculate_total_score(row, w_S, w_D, w_L, max_data_s, max_modlimit_s):
    adjusted_data_s = (max_data_s - row['Data_S']) / max_data_s if max_data_s != 0 else 0
    adjusted_modlimit_s = (max_modlimit_s - row['ModLimit_S']) / max_modlimit_s if max_modlimit_s != 0 else 0
    total_score = (w_S * row['SimObj_S']) + (w_D * adjusted_data_s) + (w_L * adjusted_modlimit_s)
    return total_score

weights = config["weights"]
w_S = weights["SimObj_S"]
w_D = weights["Data_S"]
w_L = weights["ModLimit_S"]
total_weight = w_S + w_D + w_L
w_S /= total_weight
w_D /= total_weight
w_L /= total_weight

filtered_models = filtered_models.copy()
filtered_models['Total_Score'] = filtered_models.apply(
    calculate_total_score, axis=1,
    w_S=w_S, w_D=w_D, w_L=w_L,
    max_data_s=max_data_s, max_modlimit_s=max_modlimit_s
)

if not filtered_models.empty:
    best_model = filtered_models.loc[filtered_models['Total_Score'].idxmax()]
    print("Best Model:")
    print(best_model[['Model', 'Watershed Size', 'Watershed Type', 'Simulation Objectives', 'Total_Score']].to_string(index=False))
else:
    print("No optimal model found.")
