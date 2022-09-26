#! -*- coding: utf-8 -*-

from chd_parser import parser
from chd_parser import dot_writer

par = parser.CHDParser()

root_path = ""
pass_suffixs = [".h", ".hpp", ".cpp", ".c", "cxx", "cc"]
exclude_names = ["wrapper", ".pb."]

dot_list = par.parse(root_path, pass_suffixs, exclude_names)

writer = dot_writer.DotWriter("./test.gv")
writer.write(dot_list)