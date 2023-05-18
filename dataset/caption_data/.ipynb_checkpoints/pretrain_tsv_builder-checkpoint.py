import json
import sys
import utils
import random


def main():
    res = []
    sys.stdout = open('vision_language.tsv', 'w')
    f = open('ffair_annotation.json', 'r')
    js = f.read()
    pyobj = json.loads(js)
    train_stage = pyobj['train']
    for case in train_stage:
        case_report = train_stage[case]
        for image_path in case_report['Image_path']:
            image_name = image_path[image_path.find("/") + 1:]
            image_id = image_path[image_path.find("_") + 1:image_path.find("/")] + "0" + image_name[:image_name.find(".")]
            image_str = utils.img2base64('FFAIR/' + image_path)
            # pretrain 格式：id img_str
            tsv_str = image_id + '\t' + image_str + '\t' + case_report['En_Report'].strip('\n') + '\t\t\t\t' + 'ffa-ir' + '\t' + 'caption'
            res.append(tsv_str)
    random.shuffle(res)
    for s in res:
        print(s)


if __name__ == '__main__':
    main()

