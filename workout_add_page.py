import tkinter as tk
from tkinter import ttk
from data_manager import read_custom_list, save_custom_list

class WorkoutAddPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.controller.title("Workout Add Page")
        self.controller.geometry("600x600")

        self.title_label = tk.Label(self, text="훈련", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)

        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.left_frame = tk.Frame(self.main_frame)
        self.left_frame.pack(side=tk.LEFT, fill="both", expand=True)

        self.right_frame = tk.Frame(self.main_frame)
        self.right_frame.pack(side=tk.RIGHT, fill="both", expand=True)

        self.exercises = read_custom_list()

        self.add_button = ttk.Button(self.left_frame, text="+ 운동 추가", command=lambda: controller.show_frame("ExerciseListPage"))
        self.add_button.pack(pady=10)

        self.exercise_listbox = tk.Listbox(self.left_frame)
        self.exercise_listbox.pack(fill="both", expand=True, padx=10)

        self.exercise_listbox.bind('<<ListboxSelect>>', self.on_select)

        self.set_label = tk.Label(self.right_frame, text="세트 수:")
        self.set_label.pack(pady=5)
        self.set_entry = ttk.Entry(self.right_frame)
        self.set_entry.pack(pady=5)

        self.reps_label = tk.Label(self.right_frame, text="횟수:")
        self.reps_label.pack(pady=5)
        self.reps_entry = ttk.Entry(self.right_frame)
        self.reps_entry.pack(pady=5)

        self.weight_label = tk.Label(self.right_frame, text="중량:")
        self.weight_label.pack(pady=5)
        self.weight_entry = ttk.Entry(self.right_frame)
        self.weight_entry.pack(pady=5)

        self.update_button = ttk.Button(self.right_frame, text="업데이트", command=self.update_exercise)
        self.update_button.pack(pady=10)

        self.buttons_frame = tk.Frame(self.left_frame)
        self.buttons_frame.pack(pady=10)

        self.delete_button = ttk.Button(self.buttons_frame, text="삭제", command=self.delete_exercise)
        self.delete_button.grid(row=0, column=0, padx=5)

        self.start_button = ttk.Button(self.buttons_frame, text="시작", command=self.start_workout)
        self.start_button.grid(row=0, column=1, padx=5)

        self.back_button = ttk.Button(self, text="뒤로", command=self.go_back)
        self.back_button.pack(pady=10)

        self.refresh_exercises()

    def add_exercise(self, name):
        self.exercises.append((name, "", "", ""))
        self.refresh_exercises()
        save_custom_list(self.exercises)

    def delete_exercise(self):
        selected_index = self.exercise_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.exercises.pop(index)
            self.refresh_exercises()
            save_custom_list(self.exercises)

    def on_select(self, event):
        selected_index = self.exercise_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            exercise = self.exercises[index]
            self.set_entry.delete(0, tk.END)
            self.set_entry.insert(0, exercise[1])
            self.reps_entry.delete(0, tk.END)
            self.reps_entry.insert(0, exercise[2])
            self.weight_entry.delete(0, tk.END)
            self.weight_entry.insert(0, exercise[3])

    def update_exercise(self):
        selected_index = self.exercise_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            sets = self.set_entry.get()
            reps = self.reps_entry.get()
            weight = self.weight_entry.get()
            self.exercises[index] = (self.exercises[index][0], sets, reps, weight)
            save_custom_list(self.exercises)

    def refresh_exercises(self):
        self.exercise_listbox.delete(0, tk.END)
        for exercise in self.exercises:
            self.exercise_listbox.insert(tk.END, exercise[0])

    def start_workout(self):
        for i, exercise in enumerate(self.exercises):
            sets = exercise[1]
            reps = exercise[2]
            weight = exercise[3]
            print(f"운동: {exercise[0]}, 세트: {sets}, 횟수: {reps}, 중량: {weight}")
        print("운동 시작")

    def go_back(self):
        self.controller.show_frame("CustomPage")

    def update(self):
        self.exercises = read_custom_list()
        self.refresh_exercises()