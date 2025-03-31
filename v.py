import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 设置随机种子以便复现结果
np.random.seed(0)

# 创建一个模拟的三维体积图像
# 这里我们创建一个 64x64x64 的体积数据，使用随机数填充
volume_size = 64
volume_image = np.random.rand(volume_size, volume_size, volume_size)


# 可视化三维体积图像的某个切片
def visualize_3d_slice(volume, slice_index, axis=0):
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')

    # 选择要可视化的轴
    if axis == 0:
        x, y = np.meshgrid(np.arange(volume.shape[1]), np.arange(volume.shape[2]))
        z = volume[slice_index, :, :]
    elif axis == 1:
        x, z = np.meshgrid(np.arange(volume.shape[0]), np.arange(volume.shape[2]))
        y = volume[:, slice_index, :]
    else:
        y, z = np.meshgrid(np.arange(volume.shape[1]), np.arange(volume.shape[2]))
        x = volume[:, :, slice_index]

    ax.plot_surface(x, y, z, cmap='viridis')
    ax.set_title(f'Slice at index {slice_index} along axis {axis}')
    plt.show()


# 可视化中间切片
visualize_3d_slice(volume_image, volume_size // 2, axis=0)