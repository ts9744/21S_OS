import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class StartPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Start Page")
        self.geometry("400x600")
        self.configure(bg="#f0f0f0")

        self.avatar_frame = tk.Frame(self, bg="#f0f0f0")
        self.avatar_frame.pack(pady=50)

        try:
            # Try to load the avatar image
            self.avatar_image = Image.open("avatar.png")
            self.avatar_image = self.avatar_image.resize((100, 100), Image.ANTIALIAS)
        except FileNotFoundError:
            # Use a default image if avatar.png is not found
            self.avatar_image = Image.new('RGB', (100, 100), color=(73, 109, 137))
        
        self.avatar_photo = ImageTk.PhotoImage(self.avatar_image)
        
        self.avatar_label = tk.Label(self.avatar_frame, image=self.avatar_photo, bg="#f0f0f0")
        self.avatar_label.pack()

        self.bottom_frame = tk.Frame(self, bg="#f0f0f0")
        self.bottom_frame.pack(side=tk.BOTTOM, pady=20)

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12), padding=10)

        self.profile_button = ttk.Button(self.bottom_frame, text="사용자 프로필", command=self.open_user_profile)
        self.profile_button.grid(row=0, column=0, padx=10)
        
        self.gender_button = ttk.Button(self.bottom_frame, text="사용자 성별", command=self.open_user_gender)
        self.gender_button.grid(row=0, column=1, padx=10)
        
        self.body_button = ttk.Button(self.bottom_frame, text="사용자 체형", command=self.open_user_body)
        self.body_button.grid(row=0, column=2, padx=10)

    def open_user_profile(self):
        profile_window = tk.Toplevel(self)
        profile_window.title("사용자 프로필")
        profile_window.geometry("300x200")
        tk.Label(profile_window, text="사용자 프로필 정보").pack(pady=20)
        print("사용자 프로필 버튼 클릭됨")

    def open_user_gender(self):
        gender_window = tk.Toplevel(self)
        gender_window.title("사용자 성별")
        gender_window.geometry("300x200")
        tk.Label(gender_window, text="사용자 성별 정보").pack(pady=20)
        print("사용자 성별 버튼 클릭됨")

    def open_user_body(self):
        body_window = tk.Toplevel(self)
        body_window.title("사용자 체형")
        body_window.geometry("300x200")
        tk.Label(body_window, text="사용자 체형 정보").pack(pady=20)
        print("사용자 체형 버튼 클릭됨")

if __name__ == "__main__":
    app = StartPage()
    app.mainloop()