import tkinter as tk
from tkinter import ttk

class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="설정창 내용").pack(pady=20)

        # 사용자 프로필 버튼
        def open_user_profile():
            print("사용자 프로필 버튼 클릭됨")

        profile_button = tk.Button(self, text="사용자 프로필", command=open_user_profile)
        profile_button.pack(pady=10)

        # 사용자 성별 버튼
        def open_user_gender():
            print("사용자 성별 버튼 클릭됨")

        gender_button = tk.Button(self, text="사용자 성별", command=open_user_gender)
        gender_button.pack(pady=10)

        # 사용자 체형 버튼
        def open_user_body():
            print("사용자 체형 버튼 클릭됨")

        body_button = tk.Button(self, text="사용자 체형", command=open_user_body)
        body_button.pack(pady=10)

        # 뒤로 버튼
        back_button = ttk.Button(self, text="뒤로", command=lambda: controller.show_frame("StartPage"))
        back_button.pack(pady=10)