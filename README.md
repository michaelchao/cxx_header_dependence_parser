# Introduce

输出C/C++工程中所有源文件，头文件之间的依赖关系

# 将输出内容利用dot生成图片

## gv文件内容

```do
digraph G {
bgcolor = gray;
rankdir = LR;
ratio = auto;

... // 将输入内容粘贴到这儿

}
```

## 命令

```s
dot -Tpng -o <目标>.png <源>.gv
```

# Reference

- [python列表如何依次取2个元素？](https://www.zhihu.com/question/466249845)
- [Python Patterns - Implementing Graphs](https://www.python.org/doc/essays/graphs/)
- [Directed Acyclic Graph (DAG) Scheduler library](https://mindee.com/blog/directed-acyclic-graph-dag-scheduler-library/)
- [pydags - A lightweight DAG framework for Python](https://davidtorpey.com/2021/05/03/pydags.html)
- [‘hierarchical’ (or layered) drawings of directed graphs.](https://graphviz.org/docs/layouts/dot/#:~:text=dot%20%E2%80%98hierarchical%E2%80%99%20%28or%20layered%29%20drawings%20of%20directed%20graphs.,to%20avoid%20edge%20crossings%20and%20reduce%20edge%20length.)
- [Distance between edges and nodes in graphviz](https://stackoom.com/en/question/Ph7e)

# TODO

[] color for key node, for example the file contains **main()**
[] matched header and source files use same color, for example, A.h and A.cpp use same color
