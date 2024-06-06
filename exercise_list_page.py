import tkinter as tk
from tkinter import ttk

class ExerciseListPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.controller.title("Exercise List")
        self.controller.geometry("400x600")

        self.title_label = tk.Label(self, text="운동 추가", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)

        self.search_label = tk.Label(self, text="운동 검색", font=("Arial", 12))
        self.search_label.pack(pady=5)

        self.search_entry = ttk.Entry(self)
        self.search_entry.pack(pady=5)

        self.filter_label = tk.Label(self, text="모두 (510)", font=("Arial", 12))
        self.filter_label.pack(pady=5)

        self.exercise_listbox = tk.Listbox(self)
        self.exercise_listbox.pack(fill="both", expand=True, pady=5)

        exercises = ["글루트 브릿지", "글루트 브릿지 · 덤벨", "글루트 브릿지 어브덕션", "글루트 킥백", "글루트 킥백 · 밴드", "글루트 햄 레이즈"]
        for exercise in exercises:
            self.exercise_listbox.insert(tk.END, exercise)

        self.add_button = ttk.Button(self, text="추가", command=self.add_exercise)
        self.add_button.pack(pady=10)

        self.back_button = ttk.Button(self, text="뒤로", command=self.go_back)
        self.back_button.pack(pady=10)

    def add_exercise(self):
        selected_exercise = self.exercise_listbox.get(tk.ACTIVE)
        self.controller.get_page("WorkoutAddPage").add_exercise(selected_exercise, "1 세트 x 5회")
        self.controller.show_frame("WorkoutAddPage")

    def go_back(self):
        self.controller.show_frame("WorkoutAddPage")