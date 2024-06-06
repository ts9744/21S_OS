import tkinter as tk
from tkinter import ttk

class WorkoutAddPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.controller.title("Workout Add Page")
        self.controller.geometry("400x600")

        self.time_label = tk.Label(self, text="04:42", font=("Arial", 12))
        self.time_label.pack(pady=10)

        self.title_label = tk.Label(self, text="새 훈련 1", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)

        self.desc_label = tk.Label(self, text="첫 번째 운동을 추가하세요", font=("Arial", 14), justify=tk.CENTER)
        self.desc_label.pack(pady=20)

        self.add_button = ttk.Button(self, text="+ 운동 추가", command=self.add_exercise)
        self.add_button.pack(pady=20)

        self.exercise_frame = tk.Frame(self)
        self.exercise_frame.pack(fill="both", expand=True)

        self.exercises = []

        self.save_button = ttk.Button(self, text="저장", command=self.save_workout)
        self.save_button.pack(pady=10)

    def add_exercise(self):
        exercise_name = "글루트 브릿지"
        exercise_sets = "1 세트 x 5회"
        self.exercises.append((exercise_name, exercise_sets))
        self.refresh_exercises()

    def refresh_exercises(self):
        for widget in self.exercise_frame.winfo_children():
            widget.destroy()

        for exercise in self.exercises:
            frame = tk.Frame(self.exercise_frame)
            frame.pack(fill="x", pady=5)

            exercise_name = tk.Label(frame, text=exercise[0], font=("Arial", 14))
            exercise_name.pack(side="left", padx=10)

            exercise_sets = tk.Label(frame, text=exercise[1], font=("Arial", 12))
            exercise_sets.pack(side="right", padx=10)

    def save_workout(self):
        print("운동 저장")