import tkinter as tk
from tkinter import ttk
from data_manager import read_custom_list

class StartWorkoutPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.title_label = tk.Label(self, text="Workout Routine", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)

        self.exercise_label = tk.Label(self, text="", font=("Arial", 16))
        self.exercise_label.pack(pady=20)

        self.timer_label = tk.Label(self, text="00:00", font=("Arial", 20))
        self.timer_label.pack(pady=10)

        self.start_button = ttk.Button(self, text="Start", command=self.start_exercise)
        self.start_button.pack(pady=10)

        self.next_button = ttk.Button(self, text="Next", command=self.next_exercise, state=tk.DISABLED)
        self.next_button.pack(pady=10)

        self.stop_button = ttk.Button(self, text="Stop", command=self.stop_exercise, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.back_button = ttk.Button(self, text="Back", command=self.go_back)
        self.back_button.pack(pady=10)

        self.exercises = read_custom_list()
        self.current_exercise_index = 0
        self.timer_seconds = 0

        self.update_exercise()

    def update_exercise(self):
        if self.current_exercise_index < len(self.exercises):
            exercise = self.exercises[self.current_exercise_index]
            self.exercise_label.config(text=f"{exercise[0]}\nSets: {exercise[1]}, Reps: {exercise[2]}, Weight: {exercise[3]}")
        else:
            self.exercise_label.config(text="Workout Complete!")
            self.start_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.DISABLED)

    def start_exercise(self):
        self.timer_seconds = 0
        self.update_timer()
        self.start_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.NORMAL)

    def update_timer(self):
        minutes, seconds = divmod(self.timer_seconds, 60)
        self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
        self.timer_seconds += 1
        self.timer = self.after(1000, self.update_timer)

    def next_exercise(self):
        self.after_cancel(self.timer)
        self.current_exercise_index += 1
        self.update_exercise()
        self.start_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)

    def stop_exercise(self):
        if hasattr(self, 'timer'):
            self.after_cancel(self.timer)
        self.timer_label.config(text="00:00")
        self.start_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)

    def go_back(self):
        self.stop_exercise()
        self.controller.show_frame("WorkoutAddPage")

    def reset_page(self):
        self.current_exercise_index = 0
        self.update_exercise()
        self.start_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)