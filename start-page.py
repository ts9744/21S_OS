import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from setting import SettingsPage
from user_profile_page import UserProfilePage
from user_gender_page import UserGenderPage
from user_body_page import UserBodyPage
from custom_page import CustomPage
from workout_add_page import WorkoutAddPage
from exercise_list_page import ExerciseListPage
from recommend_routine_page import RecommendRoutinePage
from start_workout_page import StartWorkoutPage  # 여기 추가
import avatar_loader  # 아바타 로드 모듈 불러오기
from data_manager import read_user_data, save_user_data

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.controller.title("Start Page")
        self.controller.geometry("400x600")

        self.top_label = tk.Label(self, text="21s-Routine", font=("Arial", 24, "bold"))
        self.top_label.pack(pady=10)

        self.top_frame = tk.Frame(self)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.avatar_label = tk.Label(self.top_frame, font=("Arial", 20))
        self.avatar_label.pack(expand=True)  # 중간에 위치하게 설정

        self.user_info_frame = tk.Frame(self.top_frame)
        self.user_info_frame.pack(pady=10)

        self.user_info_label = tk.Label(self.user_info_frame, text="", font=("Arial", 14))
        self.user_info_label.pack()

        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack(side=tk.BOTTOM, pady=20)

        self.recommend_button = ttk.Button(self.bottom_frame, text="추천 운동 루틴", command=lambda: controller.show_frame("RecommendRoutinePage"))
        self.recommend_button.grid(row=0, column=0, padx=10)

        self.settings_button = ttk.Button(self.bottom_frame, text="설정", command=lambda: controller.show_frame("SettingsPage"))
        self.settings_button.grid(row=0, column=2, padx=10)

        self.custom_button = ttk.Button(self.bottom_frame, text="커스텀", command=lambda: controller.show_frame("CustomPage"))
        self.custom_button.grid(row=0, column=1, padx=10)

        self.update_avatar()
        self.update_user_info()

    def update_avatar(self):
        avatar_loader.load_avatar(self.controller, self.avatar_label)

    def update_user_info(self):
        height = float(self.controller.user_data.get("Height", "0"))
        weight = float(self.controller.user_data.get("Weight", "0"))
        bmi = weight / ((height / 100) ** 2) if height > 0 else 0
        self.user_info_label.config(text=f"키: {height} cm, 몸무게: {weight} kg, BMI: {bmi:.2f}")

    def recommend_routine(self):
        print("추천 운동 루틴 버튼 클릭됨")

    def update(self):
        self.update_avatar()
        self.update_user_info()

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.frames = {}
        self.user_data = read_user_data()
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for F in (StartPage, SettingsPage, UserProfilePage, UserGenderPage, UserBodyPage, CustomPage, WorkoutAddPage, ExerciseListPage, RecommendRoutinePage, StartWorkoutPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        frame.update()

    def get_page(self, page_name):
        return self.frames[page_name]

    def save_data(self):
        save_user_data(self.user_data)

    def get_page(self, page_name):
        return self.frames[page_name]

    def save_data(self):
        save_user_data(self.user_data)

if __name__ == "__main__":
    app = App()
    app.protocol("WM_DELETE_WINDOW", app.save_data)  # 창을 닫을 때 데이터를 저장
    app.mainloop()