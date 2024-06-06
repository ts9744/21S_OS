import tkinter as tk

class UserBodyPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="사용자 체형").pack(pady=20)

        self.body_type_var = tk.StringVar(value="1")  # 기본값은 "1" (일반적인 체형)으로 설정

        tk.Radiobutton(self, text="일반적인 체형", variable=self.body_type_var, value="1").pack(pady=5)
        tk.Radiobutton(self, text="근육질 체형", variable=self.body_type_var, value="2").pack(pady=5)
        tk.Radiobutton(self, text="복부 비만 체형", variable=self.body_type_var, value="3").pack(pady=5)
        tk.Radiobutton(self, text="마른 체형", variable=self.body_type_var, value="4").pack(pady=5)

        save_button = tk.Button(self, text="저장", command=self.save_body_type)
        save_button.pack(pady=10)

        back_button = tk.Button(self, text="뒤로", command=lambda: controller.show_frame("SettingsPage"))
        back_button.pack(pady=10)

    def save_body_type(self):
        body_type = self.body_type_var.get()
        self.controller.user_data["BodyType"] = body_type

        # 파일에 저장
        with open("user_data.txt", "w") as file:
            file.write(f"BodyType: {body_type}\n")

        print(f"Saved body type: {body_type}")

        # 메인 페이지를 다시 로드하여 업데이트
        self.controller.frames["StartPage"].update_avatar()