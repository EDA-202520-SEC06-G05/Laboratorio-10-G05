from DataStructures.Map import map_linear_probing as lp
from DataStructures.Graph import vertex as vt
from DataStructures.Graph import edge as ed

def new_graph(order):
    graph = {
        "vertices": lp.new_map(order, 0.7, None),
        "num_edges": 0
    }
    return graph

def insert_vertex(my_graph, key_u, info_u):
    vertex = vt.new_vertex(key_u, info_u)
    lp.put(my_graph["vertices"], key_u, vertex)
    return my_graph

def add_edge(my_graph, key_u, key_v, weight=1.0):
    vertex_u = lp.get(my_graph["vertices"], key_u)
    if vertex_u is None:
        raise Exception("El vertice u no existe")
    vertex_v = lp.get(my_graph["vertices"], key_v)
    if vertex_v is None:
        raise Exception("El vertice v no existe")
    edge_u_and_v = vt.get_edge(vertex_u, key_v)
    if edge_u_and_v is None:
        vt.add_adjacent(vertex_u, key_v, weight)
        my_graph["num_edges"]+=1
    else:
        ed.set_weight(edge_u_and_v, weight)
    return my_graph

def contains_vertex(my_graph, key_u):
    key = lp.get(my_graph["vertices"], key_u)
    if key is not None:
        return True
    else:
        return False

def order(my_graph):
    return my_graph["vertices"]["size"]

def size(my_graph):
    return my_graph["num_edges"]

    
