import json
import sys
sys.stdout = open("coco_test.json", "w") # 输出文件
f = open("ffair_annotation.json", "r") # 下载的眼底数据集里的json文件
js = f.read()
pyobj = json.loads(js)

annotations = []
images = []
id = 1
stage_data = pyobj["test"]
for case_report in stage_data.values():        # case_report 对应阶段内一个case里面的数据（字典）
    for image_path in case_report["Image_path"]:
        # 路径原格式 case_x/y.jpeg
        image_name = image_path[image_path.find("/") + 1:]
        image_id = image_path[image_path.find("_") + 1:image_path.find("/")] + "0" + image_name[:image_name.find(".")]
        annotations.append({"image_id": image_id, "caption": case_report["En_Report"], "id": id})
        images.append({"id": image_id, "file_name": "FFAIR/" + image_path})
        id += 1
# type, info, license可能需要根据具体模型改变
coco_json = {"annotations": annotations, "images": images, "type": "captions", "info": "dummy", "license": "dummy"}
print(json.dumps(coco_json, sort_keys=True))
sys.stdout = open('ffair_predict.json', 'w')
print(json.dumps(annotations, sort_keys=True))

