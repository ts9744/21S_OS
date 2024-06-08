import tkinter as tk
import os

class UserGenderPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="사용자 성별").pack(pady=20)

        self.gender_var = tk.StringVar(value="0")  # 기본값은 "0" (남자)로 설정

        # 남자 버튼
        tk.Radiobutton(self, text="남자", variable=self.gender_var, value="0").pack(pady=5)
        # 여자 버튼
        tk.Radiobutton(self, text="여자", variable=self.gender_var, value="1").pack(pady=5)

        # 저장 버튼
        save_button = tk.Button(self, text="저장", command=self.save_gender_data)
        save_button.pack(pady=10)

        # 뒤로 버튼
        back_button = tk.Button(self, text="뒤로", command=lambda: controller.show_frame("SettingsPage"))
        back_button.pack(pady=10)

    def save_gender_data(self):
        gender = self.gender_var.get()
        
        # 현재 데이터 읽기
        user_data = {}
        if os.path.exists("user_data.txt"):
            with open("user_data.txt", "r") as file:
                for line in file:
                    if ": " in line:
                        key, value = line.strip().split(": ", 1)
                        user_data[key] = value
        
        # 성별 데이터 업데이트
        user_data["Gender"] = gender
        
        # 데이터 저장
        with open("user_data.txt", "w") as file:
            for key, value in user_data.items():
                file.write(f"{key}: {value}\n")

        print(f"Saved gender: {gender}")
        self.controller.update_all_frames()