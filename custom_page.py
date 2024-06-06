import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CustomPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.controller.title("Custom Page")
        self.controller.geometry("400x600")


        self.title_label = tk.Label(self, text="커스텀", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)

        self.load_image()

        self.desc_label = tk.Label(self, text="커스텀 운동을 만드세요\n나만의 루틴을 설정하세요", font=("Arial", 14), justify=tk.CENTER)
        self.desc_label.pack(pady=20)

        self.start_button = ttk.Button(self, text="+ 시작", command=lambda: controller.show_frame("WorkoutAddPage"))
        self.start_button.pack(pady=20)

        self.back_button = ttk.Button(self, text="뒤로", command=lambda: controller.show_frame("StartPage"))
        self.back_button.pack(pady=10)

    def load_image(self):
        try:
            image = Image.open("custom_image.png")
            image = image.resize((150, 150), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            self.image_label = tk.Label(self, image=photo)
            self.image_label.image = photo
            self.image_label.pack(pady=10)
        except FileNotFoundError:
            self.image_label = tk.Label(self, text="이미지를 찾을 수 없습니다.", font=("Arial", 12))
            self.image_label.pack(pady=10)