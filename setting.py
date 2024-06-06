import tkinter as tk
import subprocess

def create_settings_window():
    window = tk.Tk()
    window.title("설정")
    window.geometry("400x600")

    tk.Label(window, text="설정창 내용").pack(pady=20)

    def back_to_start_page():
        window.destroy()  # 현재 창을 닫습니다.
        subprocess.run(["python", "start_page.py"])  # start_page.py를 다시 실행합니다.

    tk.Button(window, text="뒤로", command=back_to_start_page).pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_settings_window()