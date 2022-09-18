from chd_parser import parser

def includes(idl_path):
  included_filepaths = []
  included_filenames = []
  f = open(idl_path, 'r')
  lines = []
  for line in f:
    if line.find('include') >= 0:
      if line.find('"') >= 0:
        file = line[line.find('"')+1:line.rfind('"')].strip()
      elif line.find('<') >= 0:
        file = line[line.find('<')+1:line.rfind('>')].strip()
      included_filenames.append(file)
  def get_fullpath(idl_path):
    if os.path.basename(idl_path) in included_filenames:
      included_filepaths.append(idl_path)
      included_filenames.remove(os.path.basename(idl_path))

  #self.for_each_idl(get_fullpath, find_all=True)
  #if len(included_filenames) > 0:
  #    raise exception.IDLCanNotFindException()

  return included_filenames

par = parser.CHDParser()

all_files = par.parse("/mnt/c/Users/chao01.ma/ts/github/test_protobuf/protobuf-3.19.3/michaelma/bin/cxx2")

for item in all_files:
  print("{}".format(item))
  '''
  f = open(idl_path, 'r')
  lines = []
  line_number = 1
  for line in f:
      lines.append((line_number, idl_path, line))
      line_number = line_number + 1

  self.parse_lines(lines)
  '''

  print("{}".format(includes(item)))
  break
