import os, sys
import re

class CHDParser():
  def __init__(self, verbose=False):
    pass

  def parse(self, path="./"):
    all_files = []
    return self.__collect_headers(path, all_files)

  def __collect_headers(self, path, all_files):
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 准备循环判断每个元素是否是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            self.__collect_headers(cur_path, all_files)
        else:
            if file.endswith(".h") or file.endswith(".cc"):
              all_files.append(os.path.join(path, file))

    return all_files
