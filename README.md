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