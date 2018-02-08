import os
import PIL     # 图像处理库
import numpy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation  # 更新图片的方法
import time

need_update = False


def get_screen_image():
    # adb（Android手机驱动）系统运行adb驱动功能截取当前屏幕
    os.system('adb shell screencap -p /sdcard/screen.png')
    # 将 screen.png文件拷贝至电脑当前文件夹
    os.system("adb pull /sdcard/screen.png")
    return numpy.array(PIL.Image.open('screen.png'))


def jump_to_next(point1, point2):
    x1,y1 = point1; x2,y2 = point2
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
    os.system('adb shell input swipe 320 410 320 410 {}'.format(int(distance * 1.35)))


def onclick(event, call=[]):    # [(x,y),(x1,y1)] 绑定鼠标单击事件
    global need_update
    call.append((event.xdata, event.ydata))
    if len(call) == 2:
        jump_to_next(call.pop(), call.pop())
        need_update = True


# 更新图片/重新绘图
def update_screen(frame):
    global need_update
    if need_update:
        time.sleep(1)
        update_image = plt.imshow(get_screen_image(), animatex=True)
        update_image.set_array(get_screen_image())
        need_update = False
    return update_image,


def main():
    # 创建一个对象
    figure = plt.figure()
    # 把获取的图片画在坐标轴上
    plt.imshow(get_screen_image(), animated=True)
    # 定义一个事件
    figure.canvas.mpl_connect('button_press_event', onclick)
    ani = FuncAnimation(figure, update_screen(), time=50, blit=True)
    plt.show()


if __name__ == '__main__':
    main()