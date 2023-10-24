from PIL import Image

# 读取 PNG 图像
png_image = Image.open('icon.png')

# 将 PNG 图像保存为 ICO 文件
png_image.save('icon.ico', format='ICO')
