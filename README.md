f = open(idl_path, 'r')
lines = []
line_number = 1
for line in f:
    lines.append((line_number, idl_path, line))
    line_number = line_number + 1

self.parse_lines(lines)

https://www.zhihu.com/question/466249845
https://www.python.org/doc/essays/graphs/
https://mindee.com/blog/directed-acyclic-graph-dag-scheduler-library/
https://davidtorpey.com/2021/05/03/pydags.html
https://graphviz.org/docs/layouts/dot/#:~:text=dot%20%E2%80%98hierarchical%E2%80%99%20%28or%20layered%29%20drawings%20of%20directed%20graphs.,to%20avoid%20edge%20crossings%20and%20reduce%20edge%20length.

dot -Tpng -o process.png test.gv


'''
    for line in f:
      if line.startswith("#"):
        if line.find('google') < 0 and line.find('proto') < 0:
          if line.find('include') >= 0:
            if line.find('"') >= 0:
              file = line[line.find('"')+1:line.rfind('"')].strip()
            elif line.find('<') >= 0:
              file = line[line.find('<')+1:line.rfind('>')].strip()
            included_filenames.append(file)
    #def get_fullpath(abs_filename):
    #  if os.path.basename(abs_filename) in included_filenames:
    #    included_filepaths.append(abs_filename)
    #    included_filenames.remove(os.path.basename(abs_filename))

    #self.for_each_idl(get_fullpath, find_all=True)
    #if len(included_filenames) > 0:
    #    raise exception.IDLCanNotFindException()
'''