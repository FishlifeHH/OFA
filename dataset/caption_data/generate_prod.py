import sys
import utils
import os
import time


def main():
    img_path = sys.argv[1]
    f = open('test_prod.tsv', 'w')
    sys.stdout = f
    image_id = '123456'
    image_str = utils.img2base64(img_path)
    tsv_str = image_id + '\t' + image_id + '\t' + 'no need for evaluate,just for result' + '\t\t' + image_str
    print(tsv_str)
    f.flush()
    f.close()
    os.system('bash ../../run_scripts/caption/evaluate_prod.sh > ' + str(time.time()) + '.txt')


if __name__ == '__main__':
    main()
