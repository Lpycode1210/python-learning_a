#I want to see how to use my computer files using Python code, so let it run my pictures
import tkinter as tk
from PIL import Image, ImageTk
import time

# 创建一个 Tkinter 窗口
root = tk.Tk()
root.title("闪烁的图片")

# 加载图片
image_path = "D:/图虫/3.jpg"  # Access address
image = Image.open(image_path)  # open the picture
photo = ImageTk.PhotoImage(image)  # 将图片转换为 Tkinter 可用的格式
#Tkinter 是 Python 的标准 GUI 库，用于创建图形界面。通过 Pillow 加载了一张图片（比如通过 Image.open() 方法），\
# 那么 ImageTk.PhotoImage(image) 的作用是将这张图片转换为 Tkinter 的图像格式，这样就可以在 Tkinter 的窗口中显示这张图片了

# 创建一个标签来显示图片
label = tk.Label(root, image=photo)#创建一个 Tkinter 标签组件，并将图片绑定到标签上，用于在窗口中显示图片
label.image = photo  # 保持对图片的引用，防止被垃圾回收
label.pack()  # 将标签添加到窗口中

# 定义闪烁功能
def blink():
    while True:
        # 隐藏图片
        label.config(image="")
        root.update()
        time.sleep(0.5)  # 暂停 0.5 秒

        # 显示图片
        label.config(image=photo)
        root.update()
        time.sleep(0.5)  # 暂停 0.5 秒

#启动闪烁
blink()

# 运行 Tkinter 主循环
root.mainloop()#启动 Tkinter 的主事件循环，让窗口持续运行并等待用户操作




#Check whether the third-party module is successfully installed
# try:
#     from PIL import Image
#     print("Pillow 安装成功")
# except ImportError:
#     print("Pillow 未安装")