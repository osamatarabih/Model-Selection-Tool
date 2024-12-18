# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 19:32:58 2024

@author: osamatarabih
"""

#This Script conduct a decision tree model to choose the optimal modeling framework
# Import needed packages
import pandas as pd
import numpy as np
import os

# Change working dir
os.chdir('C:/Osama Tarabih/Generalized Modeling Framework')

# Read available modeling framework catalog
Available_Models = pd.read_csv('./Available_Models.csv',encoding='unicode_escape')

# First A Score for specific model characteristics is determined to be used in the optimization if needed
Available_Models['SimObj_S'] = Available_Models['Simulation Objectives'].apply(lambda x: len(x.split(',')) if isinstance(x, str) else 0)
Available_Models['Data_S'] = Available_Models['Data Requirements'].apply(lambda x: len(x.split(',')) if isinstance(x, str) else 0)
Available_Models['ModLimit_S'] = Available_Models['Model Limitations'].apply(lambda x: len(x.split(',')) if isinstance(x, str) else 0)

# Water Body Type
print("Choose the Water Body Type by entering the corresponding number:")
print("1: Watershed")
print("2: Water Body (e.g., Lake, Reservoir, etc.)")

choice = input("Model Parameters (1, or 2): ")

if choice == "1":
    WaterBodyType = ["Watershed"]
elif choice == "2":
    WaterBodyType = ["Water Body"]
else:
    print("Invalid choice. Please select 1, or 2.")
    
print(f"You selected: {WaterBodyType}")

# Watershed Size
print("Choose the Watershed Size by entering the corresponding number:")
print("1: Small (field-scale)")
print("2: Medium")
print("3: Large")


choice = input("Model Parameters (1, 2 or 3): ")

if choice == "1":
    WatershedSize = ["Small"]
elif choice == "2":
    WatershedSize = ["Medium"]
elif choice == "3":
    WatershedSize = ["Large"]
else:
    print("Invalid choice. Please select 1, 2 or 3.")
    
print(f"You selected: {WatershedSize}")


# Watershed Type
print("Choose the Watershed Type by entering the corresponding number:")
print("1: Agricultural")
print("2: Urban")

choices = input("Enter the numbers corresponding to your choices (e.g., 1,2): ")

choices = [choice.strip() for choice in choices.split(',')]

WT_mapping = {
    "1": "Agricultural",
    "2": "Urban"
}

WatershedType = []

for choice in choices:
    if choice in WT_mapping:
        WatershedType.append(WT_mapping[choice])
    else:
        print(f"Invalid choice: {choice}")

if WatershedType:
    print(f"You selected: {', '.join(WatershedType)}")
else:
    print("No valid choices were made.")


# Model Parameters
print("Choose the model parameters by entering the corresponding number:")
print("1: Q only")
print("2: Q, TP, TN")
print("3: Q, TP, TN, TSS")

choice = input("Model Parameters (1, 2, or 3): ")

if choice == "1":
    Model_Parameters = ["Q"]
elif choice == "2":
    Model_Parameters = ["Q", "TP", "TN"]
elif choice == "3":
    Model_Parameters = ["Q", "TP", "TN", "TSS"]
else:
    print("Invalid choice. Please select 1, 2, or 3.")
    
print(f"You selected: {Model_Parameters}")

# Time Step
print("Choose the model time step by entering the corresponding number:")
print("1: Sub-daily")
print("2: Daily")
print("3: Monthyly")
print("4: Annual")
choice = input("Model Parameters (1, 2, or 3): ")

if choice == "1":
    Time_step = ["Sub-daily"]
elif choice == "2":
    Time_step = ["Daily"]
elif choice == "3":
    Time_step = ["Monthyly"]
elif choice == "4":
    Time_step = ["Annual"]
else:
    print("Invalid choice. Please select 1, 2, or 3.")
    
print(f"You selected: {Model_Parameters}")

#Simulation_Objectives
print("What are the Simulation Objectives? (Choose one or more by entering the numbers separated by commas):")
print("1: Screening Simulation")
print("2: Holistic Simulation")
print("3: BMP locations")
print("4: TMDL development")
print("5: Watershed management")
print("6: BMP cost estimation")

choices = input("Enter the numbers corresponding to your choices (e.g., 1,3,4): ")

choices = [choice.strip() for choice in choices.split(',')]

objectives_mapping = {
    "1": "Screening Simulation",
    "2": "Holistic Simulation",
    "3": "BMP locations",
    "4": "TMDL development",
    "5": "Watershed management",
    "6": "BMP cost estimation"
}

selected_objectives = []

for choice in choices:
    if choice in objectives_mapping:
        selected_objectives.append(objectives_mapping[choice])
    else:
        print(f"Invalid choice: {choice}")

if selected_objectives:
    print(f"You selected: {', '.join(selected_objectives)}")
else:
    print("No valid choices were made.")

# Model_Complexity
print("Choose the Degree of model Complexity by entering the corresponding number:")
print("1: Simple")
print("2: Medium")
print("3: Complex")

choice = input("Model Complexity (1, 2, or 3): ")

if choice == "1":
    Model_Complexity = ["Simple"]
elif choice == "2":
    Model_Complexity = ["Medium"]
elif choice == "3":
    Model_Complexity = ["Complex"]
else:
    print("Invalid choice. Please select 1, 2, or 3.")
    
print(f"You selected: {Model_Complexity}")

# Asking if the model has to be Open Access (expecting "yes" or "no")
while True:
    Model_Availability_choice = input("Does it have to be Open Source? (yes or no): ").strip().lower()
    
    # Check if the input is valid
    if Model_Availability_choice in ["yes", "no"]:
        break  # Exit loop if the input is valid
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

Model_Availability = ["Open source"] if Model_Availability_choice == "yes" else ["Open source", "Not open source"]
# Output the result
print(f"You answered: {Model_Availability_choice}")

# Model_Limitations
print("What are the Model limitations you will not tolerate? (Choose one or more by entering the numbers separated by commas):")
print("1: manual calibration")
print("2: can not be coupled with optimization algorithm")
print("3: poor groundwater simulation")
print("4: poor sediment simulation")
print("5: sensitive to parameter calibration")
print("6: limited developer and community support")
print("7: No limitations")

choices = input("Enter the numbers corresponding to your choices (e.g., 1,3,4): ")

choices = [choice.strip() for choice in choices.split(',')]

Limitations_mapping = {
    "1": "manual calibration",
    "2": "can not be coupled with optimization algorithm",
    "3": "poor groundwater simulation",
    "4": "poor sediment simulation",
    "5": "sensitive to parameter calibration",
    "6": "limited developer and community support",
    "7": "No limitations"
}

Model_Limitations = []

if "7" in choices:
    Model_Limitations.append(Limitations_mapping["7"])
else:
    for choice in choices:
        if choice in Limitations_mapping and choice != "7":
            Model_Limitations.append(Limitations_mapping[choice])
        else:
            print(f"Invalid choice: {choice}")

if Model_Limitations:
    print(f"You selected: {', '.join(Model_Limitations)}")
else:
    print("No valid choices were made.")


# Fill NaN values in 'Model Limitations' with an empty string
Available_Models['Model Limitations'] = Available_Models['Model Limitations'].fillna('')

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
    print(filtered_models[['Model', 'Water Body Type', 'Watershed Size', 'Watershed Type','Parameters', 'Simulation Objectives', 'Model Complexity', 'Model Availability', 'Model Limitations']])
else:
    print("No models match your criteria.")


#### Optimization Algorithm
# Calculate the maximum word counts in each column (max score)
max_simobj_s = Available_Models['SimObj_S'].max()
max_data_s = Available_Models['Data_S'].max()
max_modlimit_s = Available_Models['ModLimit_S'].max()

# Define the score adjustment function
def calculate_total_score(row, w_S, w_D, w_L, max_data_s, max_modlimit_s):
    # Normalize Data_S and ModLimit_S based on their maximum values
    adjusted_data_s = (max_data_s - row['Data_S']) / max_data_s if max_data_s != 0 else 0
    adjusted_modlimit_s = (max_modlimit_s - row['ModLimit_S']) / max_modlimit_s if max_modlimit_s != 0 else 0
    
    # Calculate the total score
    total_score = (w_S * row['SimObj_S']) + (w_D * adjusted_data_s) + (w_L * adjusted_modlimit_s)
    return total_score

# Prompt the user to input weights
w_S = float(input("Enter the weight for Simulation Objectives (SimObj_S): "))
w_D = float(input("Enter the weight for Data Requirements (Data_S): "))
w_L = float(input("Enter the weight for Model Limitations (ModLimit_S): "))

# Normalize weights to ensure they sum to 1
total_weight = w_S + w_D + w_L
w_S /= total_weight
w_D /= total_weight
w_L /= total_weight

# Make an explicit copy of filtered_models to avoid SettingWithCopyWarning
filtered_models = filtered_models.copy()

# Apply the optimization to the dataset
filtered_models['Total_Score'] = filtered_models.apply(
    calculate_total_score, axis=1, 
    w_S=w_S, w_D=w_D, w_L=w_L, 
    max_data_s=max_data_s, max_modlimit_s=max_modlimit_s
)

# Find the model with the highest total score
best_model = filtered_models.loc[filtered_models['Total_Score'].idxmax()]

# Print the best model in a clean format
print("Best Model:")
print(best_model[['Model', 'Watershed Size', 'Watershed Type', 'Simulation Objectives', 'Total_Score']].to_string(index=False))
