import cv2  # 导入opencv模块
import os
import time


def video_split(video_path, save_path):
    '''
    对视频文件切割成帧
    '''
    '''
    @param video_path:视频路径
    @param save_path:保存切分后帧的路径
    '''
    vc = cv2.VideoCapture(video_path)
    # 一帧一帧的分割 需要几帧写几
    c = 0
    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False
    while rval:
        rval, frame = vc.read()

        cv2.imwrite(save_path + "/" + str('%06d' % c) + '.jpg', frame)
        cv2.waitKey(1)
        c = c + 1


def make_video(path, size):
    # path = r'C:\Users\Administrator\Desktop\1\huaixiao\\'#文件路径
    filelist = os.listdir(path)  # 获取该目录下的所有文件名

    '''
    fps:
    帧率：1秒钟有n张图片写进去[控制一张图片停留5秒钟，那就是帧率为1，重复播放这张图片5次] 
    如果文件夹下有50张 534*300的图片，这里设置1秒钟播放5张，那么这个视频的时长就是10秒
    '''
    fps = 25
    #ffmpeg, content_weight
    # size = (591,705) #图片的分辨率片
    file_path = r"E:\Github\pytorch-AdaIN\output" + str(int(time.time())) + ".avi"  # 导出路径
    fourcc = cv2.VideoWriter_fourcc(*"XVID")  # 不同视频编码对应不同视频格式（例：'I','4','2','0' 对应avi格式）

    video = cv2.VideoWriter(file_path, fourcc, fps, size)

    for item in filelist:
        item = path + '/' + item
        img = cv2.imread(item)  # 使用opencv读取图像，直接返回numpy.ndarray 对象，通道顺序为BGR ，注意是BGR，通道值默认范围0-255。
        video.write(img)  # 把图片写进视频

    video.release()  # 释放


make_video("E:\\Github\\pytorch-AdaIN\\output\\inception_lamuse_style_1\\", (912,512))



def rename_file(file_path):
    for path, dirs, filenames in os.walk(file_path):
        for file in filenames:
            newFile = "b" + file
            os.rename(os.path.join(path, file), os.path.join(path, newFile))

#rename_file("D:\\Github\\pytorch-AdaIN\\frame\\sg_downtown_2.mp4")
# DATA_DIR = "D:\\Github\\pytorch-AdaIN\\video"  # 视频数据主目录
#
# SAVE_DIR = "D:\\Github\\pytorch-AdaIN\\frame"  # 帧文件保存目录
#
# start_time = time.time()
#
# for parents,dirs,filenames in os.walk(DATA_DIR):
#
#     # if parents == DATA_DIR:
#     #     continue
#
#     print("正在处理文件夹", parents)
#     path = parents.replace("\\", "//")
#     f = parents.split("\\")[1]
#
#     save_path = SAVE_DIR + "//"
#     # 对每视频数据进行遍历
#     for file in filenames:
#         print(file)
#         save_path_ = save_path + "/" + file
#         if not os.path.isdir(save_path_):
#             os.makedirs(save_path_)
#         video_path = DATA_DIR + "/" + file
#         video_split(video_path, save_path_)
#
# end_time = time.time()
# print("Cost time", start_time - end_time)