import os
import re
from natsort import ns, natsorted

sorcePath = 'C:\\Users\\15257\\Desktop\\2月月报 - 副本'
directPath = 'C:\\Users\\15257\\Desktop\\000000近期勿删\\21年2月上程实习月报证明\\2月月报集'
sorceFileFormat = '.doc'
directFileFormat = '.pdf'

# 获取该目录下所有文件，存入列表中
sorceFileList = os.listdir(sorcePath)
sorceFileList = natsorted(sorceFileList)
directFileList = os.listdir(directPath)
directFileList = natsorted(directFileList)


n = 0
for i in sorceFileList:
    # 设置旧文件名（就是路径+文件名）
    oldname = directPath + os.sep + directFileList[n]  # os.sep添加系统分隔符

    # 设置新文件名
    newname = directPath + os.sep + re.sub(r'\..*$', "", sorceFileList[n]) + directFileFormat

    os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名

    n += 1