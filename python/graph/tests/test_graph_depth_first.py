from graph import __version__
from graph.graph import Graph, Vertex

def test_depth_one():
        G5 = Graph()
        a = G5.add_node('a')
        b = G5.add_node('b')
        c = G5.add_node('c')
        d = G5.add_node('d')
        e = G5.add_node('e')
        f = G5.add_node('f')
        G5.add_edge(a, d)
        G5.add_edge(a, c)
        G5.add_edge(c, a)
        G5.add_edge(b, d)
        G5.add_edge(d, b)
        G5.add_edge(d, e)
        assert G5.graph_depth_first(a) == ['a', 'd', 'b', 'e', 'c']

def test_depth_two():
    G5 = Graph()
    a = G5.add_node('a')
    b = G5.add_node('b')
    c = G5.add_node('c')
    d = G5.add_node('d')
    e = G5.add_node('e')
    f = G5.add_node('f')
    G5.add_edge(a, d)
    G5.add_edge(a, c)
    G5.add_edge(c, a)
    G5.add_edge(b, d)
    G5.add_edge(d, b)
    G5.add_edge(d, e)
    assert G5.graph_depth_first(f) == 'verteix has no adjecent'