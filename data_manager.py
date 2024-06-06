import os

# User data management
def read_user_data():
    user_data = {}
    if os.path.exists("user_data.txt"):
        with open("user_data.txt", "r", encoding="utf-8") as file:
            for line in file:
                key, value = line.strip().split(": ")
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
                name, detail = line.strip().split(" - ")
                exercises.append((name, detail))
    return exercises

def save_custom_list(exercises):
    with open("custom_list.txt", "w", encoding="utf-8") as file:
        for name, detail in exercises:
            file.write(f"{name} - {detail}\n")