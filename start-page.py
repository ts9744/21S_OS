import tkinter as tk
from tkinter import ttk

class startPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("start Page")
        self.geometry("400x600")

        # 화면 중상단: 아바타
        self.avatar_label = tk.Label(self, text="Avatar", font=("Arial", 20))
        self.avatar_label.pack(pady=50)

        # 화면 하단: 추천 운동 루틴, 설정, 커스텀 버튼
        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack(side=tk.BOTTOM, pady=20)

        self.recommend_button = ttk.Button(self.bottom_frame, text="추천 운동 루틴", command=self.recommend_routine)
        self.recommend_button.grid(row=0, column=0, padx=10)

        self.settings_button = ttk.Button(self.bottom_frame, text="설정", command=self.open_settings)
        self.settings_button.grid(row=0, column=2, padx=10)

        self.custom_button = ttk.Button(self.bottom_frame, text="커스텀", command=self.custom_routine)
        self.custom_button.grid(row=0, column=1, padx=10)

    def recommend_routine(self):
        print("추천 운동 루틴 버튼 클릭됨")

    def open_settings(self):
        print("설정 버튼 클릭됨")

    def custom_routine(self):
        print("커스텀 버튼 클릭됨")

if __name__ == "__main__":
    app = startPage()
    app.mainloop()