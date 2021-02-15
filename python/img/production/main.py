import glob
import argparse
import cv2
import numpy as np
from itertools import product  # 迭代器
from tqdm import tqdm  # 进度条


def parasArgs():
    parser = argparse.ArgumentParser("拼接图片")
    parser.add_argument('--targetpath', type=str, default='example/1.jpg', help='目标图像路径')
    parser.add_argument('--outputpath', type=str, default='output/1.jpg', help='输出图像的路径')
    # parser.add_argument('--sourcepath', type=str, default='C:/Users/z/Downloads/ImageSpider-master/img', help='用来拼接图像的所有源文件路径')
    parser.add_argument('--sourcepath', type=str, default='../reptiles_imgs/images', help='用来拼接图像的所有源文件路径')
    parser.add_argument('--blocksize', type=str, default=3, help='像素大小')

    args = parser.parse_args()
    return args


# 读取所有源文件并计算对应颜色平均值
def readSourceImage(sourcepath, blocksize):
    print('开始读取图像')
    # 合法图像列表
    sourceimages = []
    # 平均颜色列表
    avgcolors = []

    for path in tqdm(glob.glob("{}/*.jpg".format(sourcepath))):

        image = cv2.imread(path, cv2.IMREAD_COLOR)
        try:
            if image.shape[-1] != 3:
                continue
            # 缩放尺寸
            image = cv2.resize(image, (blocksize, blocksize))
            avgcolor = np.sum(np.sum(image, axis=0), axis=0) / (blocksize * blocksize)
            sourceimages.append(image)
            avgcolors.append(avgcolor)
        except Exception:
            print('')

    print("结束读取")
    return sourceimages, np.array(avgcolors)


def main(args):
    targetimage = cv2.imread(args.targetpath)
    outputimage = np.zeros(targetimage.shape, np.uint8)

    sourceimags, avgcolors = readSourceImage(args.sourcepath, args.blocksize)
    print('开始制作')
    for i, j in tqdm(product(range(int(targetimage.shape[1] / args.blocksize)),
                             range(int(targetimage.shape[0] / args.blocksize)))):
        block = targetimage[j * args.blocksize:(j + 1) * args.blocksize, i * args.blocksize:(i + 1) * args.blocksize, :]
        avgcolor = np.sum(np.sum(block, axis=0), axis=0) / (args.blocksize * args.blocksize)
        distances = np.linalg.norm(avgcolor - avgcolors, axis=1)

        idx = np.argmin(distances)
        outputimage[j * args.blocksize:(j + 1) * args.blocksize, i * args.blocksize:(i + 1) * args.blocksize, :] = \
            sourceimags[idx]

    cv2.imwrite(args.outputpath, outputimage)
    print('制作完成')


if __name__ == '__main__':
    main(parasArgs())
