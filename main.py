import os
import pyvips


# 待处理图像文件夹路径
src_dir = r"C:\Users\19367\Desktop\img"

# 存放切割后图片的总文件夹路径
dst_dir = r"C:\Users\19367\Desktop\dzi"

# 批量处理图像
for item in os.scandir(src_dir):
    if item.is_file():
        # 文件路径
        file_path = item.path
        # 文件后缀是否是.tif
        tif_bool = file_path.endswith(".tif")
        if tif_bool:
            # 打开待处理图像
            image = pyvips.Image.new_from_file(file_path)
            # 文件名称(不包含后缀)
            print(item.name)
            file_name = item.name.split(".")[0]
            # 生成 DZI
            # 第一个参数：DZI 文件夹的路径，将在此处生成 DZI 文件
            # suffix：生成的 DZI 图像文件的后缀名
            # tile_size：DZI 图像的图块大小
            # overlap：DZI 图像的图块之间的重叠区域大小
            image.dzsave(os.path.join(dst_dir, file_name), suffix='.jpg', tile_size=512, overlap=1)
