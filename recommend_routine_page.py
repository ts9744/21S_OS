import tkinter as tk
from tkinter import ttk
from data_manager import read_routine

class RecommendRoutinePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.title_label = tk.Label(self, text="추천 운동 루틴", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)

        self.progress_label = tk.Label(self, text="0/30", font=("Arial", 16))
        self.progress_label.pack(pady=10)

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.scroll_canvas = tk.Canvas(self.main_frame)
        self.scroll_canvas.pack(side=tk.LEFT, fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.scroll_canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")

        self.scroll_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scroll_canvas.bind("<Configure>", lambda e: self.scroll_canvas.config(scrollregion=self.scroll_canvas.bbox("all")))

        self.exercise_frame = tk.Frame(self.scroll_canvas)
        self.scroll_canvas.create_window((0, 0), window=self.exercise_frame, anchor="nw")

        self.complete_button = ttk.Button(self, text="운동 완료", command=self.complete_day)
        self.complete_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.back_button = ttk.Button(self, text="뒤로", command=lambda: controller.show_frame("StartPage"))
        self.back_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.current_day_index = 0
        self.routine = {}
        self.completed_days = 0

    def load_routine(self, body_type):
        file_path = ""
        if body_type == "4":  # 마름 체형
            file_path = "for_thin.txt"
        elif body_type == "3":  # 비만 체형
            file_path = "for_fat.txt"
        # Add other body types as needed

        self.routine = read_routine(file_path)
        self.completed_days = int(self.controller.user_data.get("CompletedDays", 0))
        self.current_day_index = self.completed_days
        self.show_day()

    def show_day(self):
        days = list(self.routine.keys())
        if days:
            current_day = days[self.current_day_index]
            self.progress_label.config(text=f"{self.current_day_index + 1}/30")
            for widget in self.exercise_frame.winfo_children():
                widget.destroy()

            self.exercises = self.routine[current_day]
            for exercise in self.exercises:
                exercise_label = tk.Label(self.exercise_frame, text=exercise, font=("Arial", 14))
                exercise_label.pack(anchor="w", pady=5, padx=10)

    def complete_day(self):
        if self.current_day_index < len(self.routine) - 1:
            self.current_day_index += 1
            self.controller.user_data["CompletedDays"] = self.current_day_index
            self.controller.save_data()
            self.show_day()

    def update(self):
        body_type = self.controller.user_data.get("BodyType", "1")
        self.load_routine(body_type)