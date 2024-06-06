import tkinter as tk

class UserBodyPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="사용자 체형").pack(pady=20)

        self.body_type_var = tk.StringVar()
        self.body_type_var.set(self.controller.user_data.get("BodyType", "1"))

        body_types = [("일반적인 체형", "1"), ("근육질 체형", "2"), ("복부 비만 체형", "3")]

        for text, value in body_types:
            tk.Radiobutton(self, text=text, variable=self.body_type_var, value=value).pack(anchor=tk.W)

        tk.Button(self, text="저장", command=self.save_body_type).pack(pady=10)
        tk.Button(self, text="뒤로", command=lambda: controller.show_frame("SettingsPage")).pack(pady=10)

    def save_body_type(self):
        self.controller.user_data["BodyType"] = self.body_type_var.get()
        print("체형 저장:", self.controller.user_data["BodyType"])
        self.controller.save_data()