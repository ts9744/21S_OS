import tkinter as tk
from tkinter import ttk
from data_manager import read_custom_list, save_custom_list

class WorkoutAddPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.controller.title("Workout Add Page")
        self.controller.geometry("400x600")

        self.title_label = tk.Label(self, text="훈련", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)

        self.exercise_frame = tk.Frame(self)
        self.exercise_frame.pack(fill="both", expand=True)

        self.exercises = read_custom_list()

        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack(pady=10)

        self.add_button = ttk.Button(self.buttons_frame, text="+ 운동 추가", command=lambda: controller.show_frame("ExerciseListPage"))
        self.add_button.grid(row=0, column=0, padx=10)

        self.start_button = ttk.Button(self.buttons_frame, text="시작", command=self.start_workout)
        self.start_button.grid(row=0, column=1, padx=10)

        self.delete_button = ttk.Button(self.buttons_frame, text="삭제", command=self.delete_exercise)
        self.delete_button.grid(row=0, column=2, padx=10)

        self.back_button = ttk.Button(self, text="뒤로", command=self.go_back)
        self.back_button.pack(pady=10)

        self.refresh_exercises()

    def add_exercise(self, name, detail):
        self.exercises.append((name, detail))
        self.refresh_exercises()
        save_custom_list(self.exercises)

    def delete_exercise(self):
        selected_index = self.exercise_listbox.curselection()
        if selected_index:
            self.exercises.pop(selected_index[0])
            self.refresh_exercises()
            save_custom_list(self.exercises)

    def refresh_exercises(self):
        for widget in self.exercise_frame.winfo_children():
            widget.destroy()

        self.exercise_listbox = tk.Listbox(self.exercise_frame)
        self.exercise_listbox.pack(fill="both", expand=True)

        for exercise in self.exercises:
            self.exercise_listbox.insert(tk.END, f"{exercise[0]} - {exercise[1]}")

    def start_workout(self):
        print("운동 시작")

    def go_back(self):
        self.controller.show_frame("CustomPage")