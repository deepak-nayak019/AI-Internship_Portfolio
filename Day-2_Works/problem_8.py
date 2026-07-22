from datetime import datetime

# Function to save experiment details
def save_experiment_log(experiment_name, accuracy):
    # Get today's date
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Open file in append mode
    with open("experiments.log", "a") as file:
        file.write(f"{current_date} | Model: {experiment_name} | Accuracy: {accuracy}\n")


# -----------------------------------
# Save Three Fake Experiment Results
# -----------------------------------

save_experiment_log("LogisticRegression", 0.91)
save_experiment_log("DecisionTree", 0.87)
save_experiment_log("RandomForest", 0.95)


# -----------------------------------
# Read and Print the Entire Log File
# -----------------------------------

print("------ Experiment Log ------")

with open("experiments.log", "r") as file:
    print(file.read())