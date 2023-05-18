import imageio
import os
import utils


def create_gif(img_dir, image_list, gif_name, duration=0.05):
    frames = []
    if image_list[-1].startswith('.'):
        image_list.pop()
    # print(int(image_list[0][:image_list[0].find('.')]))
    # print(image_list[0].find('.'))
    image_list.sort(key=lambda x: int(x[:x.find('.')]))
    for image_name in image_list:
        print('image_name={0} img_dir={1}'.format(image_name, img_dir))
        img = imageio.imread(img_dir + '/' + image_name)
        if img.size == 768 * 768:
            frames.append(imageio.imread(img_dir + '/' + image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)


def main():
    try:
        for i in range(len(os.listdir('FFAIR/'))):
            img_dir = 'FFAIR/case_' + str(i)
            duration = 0.05 # 每秒20帧
            image_list = os.listdir(img_dir)
            gif_name = img_dir + '.gif'
            create_gif(img_dir, image_list, gif_name, duration)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
    # print(utils.img2base64('./FFAIR/case_0.gif'))
