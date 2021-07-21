import cv2                                      
from skimage import io                          
import os
from tkinter import *
from PIL import Image
import numpy

def maim():
    videos_path = r'.\video'
    videos_name = os.listdir(videos_path)           

    for j, i in enumerate(videos_name):             
        path = r'C:\videos\%s' %(i[0:-4])
        with open('data.txt','w') as f:
            f.write(path)
        try:
            os.makedirs(path)
        except:
            print('12')
        video_path = os.path.join(videos_path, i)    
        if os.path.isdir(video_path):
            continue
        camera = cv2.VideoCapture(video_path)
        if camera.isOpened():                        
            print('Open')
        else:
            print('视频打开错误')

        a = 0                                        
        while True:
            success, frame_lwpCV = camera.read()     
            if success==False:                       
                break
            io.imsave(r'C:\videos\%s\%s.jpg' %(i[0:-4],a), frame_lwpCV)  
            a += 1
    camera.release()



def mkdir(path):
 
	folder = os.path.exists(path)
 
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
		print("---  new folder...  ---")
		print("---  OK  ---")
 
def fil_pic(image_name,int_i):
    image_obj = Image.open(image_name)
    width, height = image_obj.size
    image_obj = image_obj.convert('L')
    image_obj_l = image_obj.load()
    for i in range(width):
        for j in range(height):
            if i == width-1 or j == height-1:
                continue
            else:

                l_num = image_obj_l[i, j]
                next_num = image_obj_l[i+1, j+1]
                if abs(l_num-next_num) > int_i:
                    l_num = 0
                else:
                    l_num = 255
                image_obj_l[i, j] = l_num
    image_obj.save(image_name)

def image_to_txt(image_path, txt_path):
    txt_count = 1                                   # 用于命名txt文件
    fileList = os.listdir(image_path)             # 返回所有图片名称，是个字符串列表
    try:
        for file1 in fileList:                          # 遍历每一张图片
            img = Image.open(image_path + '\\'+ file1).convert('L') 
            # 这里使用到PIL库convert函数，将RGB图片转化为灰度图，参数'L'代表转化为灰度图
            charWidth = 140                             
            # 这个是设置你后面在cmd里面显示内容的窗口大小，请根据自己的情况，适当调整值
            img = img.resize((charWidth, 40))
            target_width, target_height = img.size
            data = numpy.array(img)[:target_height, :target_width]
            # 使用numpy库，将图像转化为数组
            with open(txt_path + '\\' + str(txt_count) + '.txt', 'w', encoding='utf-8') as f:
                txt_count += 1                      # 一张图对应一个txt文件，所以每遍历一张图，该值加一
                for row in data:
                    for pixel in row:
                        if pixel < 127:             # 如果灰度值小于127，也就是偏黑的，就写一个字符 '*'
                            f.write('*')
                        else:
                            f.write(' ')
                    f.write('\n')
    except PermissionError:
        pass

def run(txt_path):
    fileList = os.listdir(txt_path)
    for i in range(1, len(fileList)+1):         # 遍历所有的txt文件
        try:
            os.system('type ' + txt_path + '\\' + str(i) + '.txt')
            os.system('cls')
        except:
            print('ERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


if __name__ == "__main__":
    # image_path=input('请输入地址，要使用\\来表示')
    maim()
    with open('data.txt','r') as f:
        image_path = f.read()
        print(image_path)
    mkdir(image_path+r'\1txt')
    fileList = os.listdir(image_path)
    for i in fileList:
        print(i)
    image_to_txt(image_path,image_path+r'\1txt')
    run(image_path+r'\1txt')
    



