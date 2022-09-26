#! -*- coding: utf-8 -*-

import os, sys
import re
from string import Template
from . import dag

DOT_TEMPLATE_STRING = '"$ONE" -- "$TWO";'
DTSI = Template(DOT_TEMPLATE_STRING)

class CHDParser():
  def __init__(self, verbose=False):
    pass


  def parse(self, root_path="./", pass_suffixs=[], exclude_names=[]):
    '''

    '''
    self.__root_path = root_path
    self.__pass_suffixs = pass_suffixs
    self.__exclude_names = exclude_names
    all_files = []
    all_files = self.__collect_targets(root_path, all_files)
    return self.__collect_dot(all_files)


  def __collect_targets(self, path, all_files):
    '''
      return [(filename, path_filename), (filename, path_filename), ...]
    '''
    file_list = os.listdir(path)
    for file in file_list:
        cur_path = os.path.join(path, file)
        if os.path.isdir(cur_path):
            self.__collect_targets(cur_path, all_files)
        else:
            if any(file.endswith(keyword) for keyword in self.__pass_suffixs):
              all_files.append((file, os.path.join(path, file)))

    return all_files


  def __collect_includes(self, filename, abs_filename):
    '''

    '''
    included_filenames = []

    if any(keyword in filename for keyword in self.__exclude_names):
      return (filename, included_filenames)

    f = open(abs_filename, 'r')

    for line in f:
      if line.startswith("#"):
        if line.find('include') >= 0:
          if line.find('"') >= 0:
            file = line[line.find('"')+1:line.rfind('"')].strip()
            included_filenames.append(file)
          elif line.find('<') >= 0:
            file = line[line.find('<')+1:line.rfind('>')].strip()
            included_filenames.append(file)
          else:
            pass

    return (filename, included_filenames)


  def __collect_dot(self, all_files):
    '''

    '''
    global DTSI
    graph = {}
    dot_list = []
    for item in all_files:
      filename, abs_filename = item

      key, value = self.__collect_includes(filename, abs_filename)
      graph[key] = value

      for key, value in graph.items():
        for item in value:
          level1_lst = dag.find_all_paths(graph, key, item)
          for level2_lst in level1_lst:
            level3_lst = dag.find_compos(level2_lst)
            for level4_lst in level3_lst:
              s = DTSI.substitute(ONE=level4_lst[0], TWO=level4_lst[1])
              if s not in dot_list:
                dot_list.append(s)

    return dot_list
