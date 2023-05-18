import json
from PIL import Image
from io import BytesIO
import base64
import sys


def img2base64(path: str) -> str:
    img = Image.open(path)  # path to file
    img_buffer = BytesIO()
    img.save(img_buffer, format=img.format)
    byte_data = img_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)  # bytes
    base64_str = base64_str.decode("utf-8")  # str
    return base64_str


f = open("ffair_annotation.json", "r")  # 下载的眼底数据集里的json文件
js = f.read()
pyobj = json.loads(js)
# original = sys.stdout
max_image_size = 0
max_caption_size = 0
# 根据格式转换成tsv文件
for stage in pyobj:
    if stage != 'train':
        continue
    stage_data = pyobj[stage]
    sys.stdout = open(stage + ".tsv", "w")
    # stage_data对应每个阶段里面的数据集（字典）
    for case in stage_data:
        case_report = stage_data[case]
        max_caption_size = max(max_caption_size, len(case_report["En_Report"].strip('\n')))
        # case_report 对应阶段内一个case里面的数据（字典）
        for image_path in case_report["Image_path"]:
            # 路径原格式 case_x/y.jpeg
            image_name = image_path[image_path.find("/") + 1:]
            image_id = image_path[image_path.find("_") + 1:image_path.find("/")] + "0" + image_name[:image_name.find(".")]
            image_str = img2base64('FFAIR/' + image_path)
            max_image_size = max(max_image_size, len(image_str))
            tsv_str = image_id + '\t' + image_id + '\t' + case_report["En_Report"].strip('\n') + '\t\t' + image_str
            print(tsv_str)
            # if stage == 'train':
            #    break # 只取每个train第一张图
sys.stdout = open('maxl.txt', 'w')
print(max_image_size)
print(max_caption_size)

