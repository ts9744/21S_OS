import tkinter as tk

class UserProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="사용자 체형").pack(pady=20)

        # 사용자 키 입력
        tk.Label(self, text="키 (cm)").pack(pady=5)
        self.height_entry = tk.Entry(self)
        self.height_entry.pack(pady=5)

        # 사용자 몸무게 입력
        tk.Label(self, text="몸무게 (kg)").pack(pady=5)
        self.weight_entry = tk.Entry(self)
        self.weight_entry.pack(pady=5)

        # 저장 버튼
        save_button = tk.Button(self, text="저장", command=self.save_user_data)
        save_button.pack(pady=10)

        # 뒤로 버튼
        back_button = tk.Button(self, text="뒤로", command=lambda: controller.show_frame("SettingsPage"))
        back_button.pack(pady=10)

    def save_user_data(self):
        height = self.height_entry.get()
        weight = self.weight_entry.get()

        with open("user_data.txt", "w") as file:
            file.write(f"Height: {height}\n")
            file.write(f"Weight: {weight}\n")

        print(f"Saved height: {height}, weight: {weight}")