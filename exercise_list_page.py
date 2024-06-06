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

        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.update_list)
        self.search_entry = ttk.Entry(self, textvariable=self.search_var)
        self.search_entry.pack(pady=5)

        self.filter_label = tk.Label(self, text="모두", font=("Arial", 12))
        self.filter_label.pack(pady=5)

        self.list_frame = tk.Frame(self)
        self.list_frame.pack(fill="both", expand=True, pady=5)

        self.scrollbar = tk.Scrollbar(self.list_frame, orient=tk.VERTICAL)
        self.exercise_listbox = tk.Listbox(self.list_frame, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.exercise_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.exercise_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.exercises = self.read_exercise_list()
        self.filtered_exercises = self.exercises.copy()
        self.update_list()

        self.add_button = ttk.Button(self, text="추가", command=self.add_exercise)
        self.add_button.pack(pady=10)

        self.back_button = ttk.Button(self, text="뒤로", command=self.go_back)
        self.back_button.pack(pady=10)

    def load_exercises(self):
        for exercise in self.filtered_exercises:
            self.exercise_listbox.insert(tk.END, exercise)

    def read_exercise_list(self):
        exercises = []
        try:
            with open("exercise_list.txt", "r", encoding="utf-8") as file:
                for line in file:
                    exercises.append(line.strip())
        except FileNotFoundError:
            print("exercise_list.txt 파일을 찾을 수 없습니다.")
        return exercises

    def update_list(self, *args):
        search_term = self.search_var.get().lower()
        self.filtered_exercises = [exercise for exercise in self.exercises if search_term in exercise.lower()]
        self.exercise_listbox.delete(0, tk.END)
        for exercise in self.filtered_exercises:
            self.exercise_listbox.insert(tk.END, exercise)

    def add_exercise(self):
        selected_exercise = self.exercise_listbox.get(tk.ACTIVE)
        self.controller.get_page("WorkoutAddPage").add_exercise(selected_exercise, "1 세트 x 5회")
        self.controller.show_frame("WorkoutAddPage")

    def go_back(self):
        self.controller.show_frame("WorkoutAddPage")