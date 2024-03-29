# Deep-Zoom
使用 vips 将高分辨率大图像转换为 DZI 文件，用于 OpenSeadragon 进行在线预览。（图像金字塔）

## 准备工作
### 安装 pyvips
#### 第一步
```
pip install pyvips
```
##### 安装遇到的问题
- pip 安装第三方包时因 SSL 报错
解决方法：
1. 临时关闭代理、VPN 或者网络抓包等软件
2. 通过镜像源下载
  
- pip安装时 fatal error C1083: 无法打开包括文件: “io.h”: No such file or directory
解决方法：
1. 安装Windows 10 SDK
2. 在 windows 配置环境变量，在PATH中添加：
```
C:\Program Files (x86)\Windows Kits\10\Include\<你安装的版本>\ucrt
```

#### 第二步
下载一个支持 pyvips 的库 vips-dev
官网地址： https://github.com/libvips/libvips/releases

![image](https://github.com/WangHu17/Deep-Zoom/assets/39235304/1df4f450-81ce-4d1d-a826-e84ac302ea1a)
![image](https://github.com/WangHu17/Deep-Zoom/assets/39235304/e08b50b9-49e1-4b90-8390-7ae0e9a7353b)

- 解压
- 配置
- 找到 Python 安装的位置
- 找到 Python安装位置\Lib\site-packages\pyvips\__init__.py 文件
- 在 import os 后面加上如下两行
```
# 上面 vips-dev 解压后的 bin 绝对路径
vipshome = r'D:\pyvips\vips-dev-8.15\bin'
os.environ['PATH'] = vipshome + ';' + os.environ['PATH']
```
如图所示：

![image](https://github.com/WangHu17/Deep-Zoom/assets/39235304/afb26bcd-79ed-46df-b860-14f588669edd)

## 使用 vips
在 python 文件中 import pyvips 即可
