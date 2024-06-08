from PIL import Image, ImageTk
import os

def get_avatar_image(gender, body_type):
    avatars_dir = "avatars"  # 아바타 이미지들이 저장된 폴더
    image_path = ""
    
    if gender == "0":  # 남자
        gender_dir = "man"
    elif gender == "1":  # 여자
        gender_dir = "woman"
    else:
        gender_dir = "man"  # 기본값으로 남자

    if body_type == "1":
        image_path = os.path.join(avatars_dir, gender_dir, "normal.png")
    elif body_type == "2":
        image_path = os.path.join(avatars_dir, gender_dir, "muscular.png")
    elif body_type == "3":
        image_path = os.path.join(avatars_dir, gender_dir, "fat.png")
    elif body_type == "4":
        image_path = os.path.join(avatars_dir, gender_dir, "thin.png")
    else:
        image_path = os.path.join(avatars_dir, gender_dir, "default.png")
    
    try:
        image = Image.open(image_path)
        return image
    except FileNotFoundError:
        return Image.open(os.path.join(avatars_dir, gender_dir, "default.png"))

def read_user_data_from_file():
    user_data = {"BodyType": "1", "Gender": "0"}  # 기본값
    if os.path.exists("user_data.txt"):
        with open("user_data.txt", "r") as file:
            for line in file:
                key, value = line.strip().split(": ")
                user_data[key] = value
    return user_data

def load_avatar(controller, label):
    user_data = read_user_data_from_file()
    body_type = user_data.get("BodyType", "1")
    gender = user_data.get("Gender", "0")
    avatar_image = get_avatar_image(gender, body_type)

    # 이미지 크기 조정 (예: 150x150 픽셀)
    avatar_image = avatar_image.resize((150, 150), Image.LANCZOS)
    
    avatar_photo = ImageTk.PhotoImage(avatar_image)

    label.config(image=avatar_photo)
    label.image = avatar_photo