from PIL import Image, ImageTk
import os

def get_avatar_image(body_type):
    avatars_dir = "avatars"  # 아바타 이미지들이 저장된 폴더
    image_path = ""
    if body_type == "1":
        image_path = os.path.join(avatars_dir, "normal.png")
    elif body_type == "2":
        image_path = os.path.join(avatars_dir, "muscular.png")
    elif body_type == "3":
        image_path = os.path.join(avatars_dir, "obese.png")
    elif body_type == "4":
        image_path = os.path.join(avatars_dir, "thin.png")
    else:
        image_path = os.path.join(avatars_dir, "default.png")
    
    try:
        image = Image.open(image_path)
        return image
    except FileNotFoundError:
        return Image.open(os.path.join(avatars_dir, "default.png"))

def read_body_type_from_file():
    body_type = "1"  # 기본값
    if os.path.exists("user_data.txt"):
        with open("user_data.txt", "r") as file:
            for line in file:
                if line.startswith("BodyType:"):
                    body_type = line.strip().split(": ")[1]
                    break
    return body_type

def load_avatar(controller, label):
    body_type = read_body_type_from_file()
    avatar_image = get_avatar_image(body_type)

    # 이미지 크기 조정 (예: 150x150 픽셀)
    avatar_image = avatar_image.resize((150, 150), Image.LANCZOS)
    
    avatar_photo = ImageTk.PhotoImage(avatar_image)

    label.config(image=avatar_photo)
    label.image = avatar_photo