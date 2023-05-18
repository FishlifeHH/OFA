from PIL import Image
from io import BytesIO
import base64


def img2base64(path: str) -> str:
    img = Image.open(path)  # path to file
    img_buffer = BytesIO()
    img.save(img_buffer, format=img.format)
    byte_data = img_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)  # bytes
    base64_str = base64_str.decode("utf-8")  # str
    return base64_str


def base642img(img_path: str, base64_path: str):
    try:
        with open(base64_path, mode='r') as f:
            content = ''
            for line in f:
                content += line
        imgdata = base64str2img(content)
        with open(img_path, mode='wb') as f:
            f.write(imgdata)
    except Exception as e:
        print(f"base64_to_img error:{e}")


def base64str2img(base64_str: str):
    return base64.b64decode(base64_str)
