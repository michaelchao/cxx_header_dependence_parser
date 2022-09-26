from chd_parser import parser
from string import Template

def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

def includes(filename, abs_filename):
  included_filepaths = []
  included_filenames = []
  if 'wrapper' in filename:
    return (filename, included_filenames)

  if '.pb.' in filename:
    return (filename, included_filenames)

  f = open(abs_filename, 'r')
  lines = []
  for line in f:
    if line.startswith("#"):
      if line.find('google') < 0 and line.find('proto') < 0:
        if line.find('include') >= 0:
          if line.find('"') >= 0:
            file = line[line.find('"')+1:line.rfind('"')].strip()
          elif line.find('<') >= 0:
            file = line[line.find('<')+1:line.rfind('>')].strip()
          included_filenames.append(file)
  def get_fullpath(abs_filename):
    if os.path.basename(abs_filename) in included_filenames:
      included_filepaths.append(abs_filename)
      included_filenames.remove(os.path.basename(abs_filename))

  #self.for_each_idl(get_fullpath, find_all=True)
  #if len(included_filenames) > 0:
  #    raise exception.IDLCanNotFindException()

  return (filename, included_filenames)

par = parser.CHDParser()

all_files = par.parse("/mnt/c/Users/chao01.ma/ts/github/test_protobuf/protobuf-3.19.3/michaelma/bin/cxx2")

graph = {}

template_string = '"$ONE" -- "$TWO";'
ss = Template(template_string)

for item in all_files:
  filename, abs_filename = item
  #print("{}".format(includes(filename, abs_filename)))
  key, value = includes(filename, abs_filename)
  graph[key] = value

dot_list = []

for key, value in graph.items():
  #print("{} : {}".format(key, value))
  for item in value:
    #print("DAG1: {}".format(find_all_paths(graph, key, item)))
    level1_lst = find_all_paths(graph, key, item)
    # [['bole_command_line_interface.cc', 'bole_strutil.h'], ['bole_command_line_interface.cc', 'bole_fileutil.h', 'bole_strutil.h']]
    for level2_lst in level1_lst:
      level3_lst = [level2_lst[i: i+2] for i in range(len(level2_lst) - 1)]
      for level4_lst in level3_lst:
        #print("    DAG2: {}".format(level4_lst))
        sss = ss.substitute(ONE=level4_lst[0], TWO=level4_lst[1])
        if sss not in dot_list:
          dot_list.append(sss)
      #if len(level2_lst):
      #  cur_item = ""
      #  net_item = ""
      #  for level2_lst_item in level2_lst:
      #  #  print("    DAG2: {}".format(level2_lst_item))
      #  #cur_item = level2_lst_item


for item in dot_list:
  print(item)