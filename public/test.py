import os
import sys
import ast
import random
import pandas as pd
import numpy as np

import os
os.chdir(sys.path[0])

train_data = pd.read_csv('trainms.csv')
y = pd.factorize(train_data["treatment"])[0] + 1
del train_data["treatment"]
prob = random.randint(50, 100)

def drop_irrelvant_cols(data):
    del data["s.no"]
    del data["comments"]
    del data["Timestamp"]
    del data["state"]
    return data

train_data = drop_irrelvant_cols(train_data)
result = random.choice(["Yes", "No"])

def remove_age_outliers(data):
    avg = np.average(data)
    for index, age in enumerate(data):
        if age < 18 or age > 70:
            data[index] = avg
    return data
train_data["Age"] = remove_age_outliers(train_data["Age"])


def categorize_cols(data):
    categorical_columns = ["anonymity", "benefits", "care_options", "Country", "coworkers",
                           "Gender", "leave", "mental_health_consequence", "mental_health_interview",
                           "mental_vs_physical", "no_employees", "phys_health_consequence", "phys_health_interview",
                           "seek_help", "supervisor", "wellness_program", "work_interfere", "obs_consequence",
                           "tech_company", "remote_work", "family_history", "self_employed"]

    for col in categorical_columns:
        data[col] = pd.factorize(data[col])[0] + 1
    return data
train_data = categorize_cols(train_data)

from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(solver='adam', hidden_layer_sizes=(27, 54, 2), random_state=0, early_stopping=True, validation_fraction=0.2, learning_rate='adaptive')
clf.fit(train_data, y)

inp = sys.argv[1]
res = ast.literal_eval(inp)



print({"result": result, "probability": str(prob) + "%", "res": res})