import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CustomPage(tk.Frame):
    def __init__(self, parent, controller=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        if self.controller:
            self.controller.title("Custom Page")
            self.controller.geometry("400x600")
        else:
            parent.title("Custom Page")
            parent.geometry("400x600")

        # 상단 시간 표시
        self.time_label = tk.Label(self, text="03:49", font=("Arial", 12))
        self.time_label.pack(pady=10)

        # 메인 타이틀
        self.title_label = tk.Label(self, text="커스텀", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)

        # 이미지 로드
        self.load_image()

        # 설명 라벨
        self.desc_label = tk.Label(self, text="첫 번째 커스텀 운동을 만드세요\n나만의 루틴을 설정하세요", font=("Arial", 14), justify=tk.CENTER)
        self.desc_label.pack(pady=20)

        # 시작 버튼
        self.start_button = ttk.Button(self, text="+ 시작", command=self.start_custom)
        self.start_button.pack(pady=20)

    def load_image(self):
        # 이미지 로드 및 표시
        try:
            image = Image.open("custom_image.png")  # 이미지 파일 경로
            image = image.resize((150, 150), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            self.image_label = tk.Label(self, image=photo)
            self.image_label.image = photo
            self.image_label.pack(pady=10)
        except FileNotFoundError:
            self.image_label = tk.Label(self, text="이미지를 찾을 수 없습니다.", font=("Arial", 12))
            self.image_label.pack(pady=10)

    def start_custom(self):
        print("커스텀 시작 버튼 클릭됨")

# 이 부분은 독립적으로 테스트할 수 있도록 하는 코드입니다.
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Custom Page Test")
    root.geometry("400x600")
    CustomPage(root).pack(fill="both", expand=True)
    root.mainloop()