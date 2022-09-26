#! -*- coding: utf-8 -*-

class DotWriter :
  def __init__(self, target_file):
    self.__target_file = target_file

  def write(self, lines):
    lines2 = [li + '\n' for li in lines]
    with open(self.__target_file, mode='w', encoding='utf-8') as fd:
      dot_begin = ["digraph G {\n", 'graph [pad="10", ranksep="10", nodesep="0.25"];\n', "bgcolor = gray;\n", "rankdir = LR;\n", "ratio = auto;\n"]
      fd.writelines(dot_begin)
      fd.writelines(lines2)
      fd.write("}\n")
