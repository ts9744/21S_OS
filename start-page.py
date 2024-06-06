import tkinter as tk
from tkinter import ttk

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.controller.title("Start Page")
        self.controller.geometry("400x600")

        # 화면 중상단: 아바타
        self.avatar_label = tk.Label(self, text="Avatar", font=("Arial", 20))
        self.avatar_label.pack(pady=50)

        # 화면 하단: 추천 운동 루틴, 설정, 커스텀 버튼
        self.bottom_frame = tk.Frame(self)
        self.bottom_frame.pack(side=tk.BOTTOM, pady=20)

        self.recommend_button = ttk.Button(self.bottom_frame, text="추천 운동 루틴", command=self.recommend_routine)
        self.recommend_button.grid(row=0, column=0, padx=10)

        self.settings_button = ttk.Button(self.bottom_frame, text="설정", command=lambda: controller.show_frame("SettingsPage"))
        self.settings_button.grid(row=0, column=2, padx=10)

        self.custom_button = ttk.Button(self.bottom_frame, text="커스텀", command=self.custom_routine)
        self.custom_button.grid(row=0, column=1, padx=10)

    def recommend_routine(self):
        print("추천 운동 루틴 버튼 클릭됨")

    def custom_routine(self):
        print("커스텀 버튼 클릭됨")

class SettingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="설정창 내용").pack(pady=20)

        back_button = ttk.Button(self, text="뒤로", command=lambda: controller.show_frame("StartPage"))
        back_button.pack(pady=10)

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.frames = {}
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for F in (StartPage, SettingsPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()