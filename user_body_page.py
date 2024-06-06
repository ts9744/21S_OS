import tkinter as tk

class UserBodyPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="사용자 체형").pack(pady=20)

        self.body_type_var = tk.StringVar(value="1")  # 기본값은 "1" (일반적인 체형)으로 설정

        # 일반적인 체형 버튼
        tk.Radiobutton(self, text="일반적인 체형", variable=self.body_type_var, value="1").pack(pady=5)
        # 근육질 체형 버튼
        tk.Radiobutton(self, text="근육질 체형", variable=self.body_type_var, value="2").pack(pady=5)
        # 복부 비만 체형 버튼
        tk.Radiobutton(self, text="복부 비만 체형", variable=self.body_type_var, value="3").pack(pady=5)

        # 저장 버튼
        save_button = tk.Button(self, text="저장", command=self.save_body_type)
        save_button.pack(pady=10)

        # 뒤로 버튼
        back_button = tk.Button(self, text="뒤로", command=lambda: controller.show_frame("SettingsPage"))
        back_button.pack(pady=10)

    def save_body_type(self):
        body_type = self.body_type_var.get()

        with open("user_data.txt", "a") as file:
            file.write(f"BodyType: {body_type}\n")

        print(f"Saved body type: {body_type}")