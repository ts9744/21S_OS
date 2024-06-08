import os

# User data management
def read_user_data():
    user_data = {}
    if os.path.exists("user_data.txt"):
        with open("user_data.txt", "r", encoding="utf-8") as file:
            for line in file:
                key, value = line.strip().split(": ", 1)
                user_data[key] = value
    return user_data

def save_user_data(user_data):
    with open("user_data.txt", "w", encoding="utf-8") as file:
        for key, value in user_data.items():
            file.write(f"{key}: {value}\n")

# Custom list management
def read_custom_list():
    exercises = []
    if os.path.exists("custom_list.txt"):
        with open("custom_list.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(" - ")
                if len(parts) == 4:
                    name, sets, reps, weight = parts
                    exercises.append((name, sets, reps, weight))
                else:
                    name = parts[0]
                    exercises.append((name, "", "", ""))
    return exercises

def save_custom_list(exercises):
    with open("custom_list.txt", "w", encoding="utf-8") as file:
        for name, sets, reps, weight in exercises:
            file.write(f"{name} - {sets} - {reps} - {weight}\n")

# Routine management
def read_routine(file_path):
    routine = {}
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            current_day = None
            for line in file:
                if line.startswith("Day"):
                    current_day = line.strip()
                    routine[current_day] = []
                elif current_day:
                    routine[current_day].append(line.strip())
    return routine