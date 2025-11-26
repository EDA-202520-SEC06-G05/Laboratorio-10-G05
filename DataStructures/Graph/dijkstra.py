from DataStructures.Map import map_linear_probing as lp
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.Graph import dijsktra_structure as ds
from DataStructures.Graph import digraph as dp
from DataStructures.List import array_list as al
import math 


def init_structure(graph, source):
    """
    Crea e inicializa la estructura utilizada para construcción del árbol de caminos
    de costo mínimo (Algoritmo de Dijkstra) a partir del vértice source
    """
    structure = ds.new_dijsktra_structure(source,lp.size(graph["vertices"]))
    vertices = dp.vertices(graph)

    for i in range(al.size(vertices)):
        vert = al.get_element(vertices, i)
        lp.put(structure["visited"], vert, {
            "marked": False,
            "edge_from": None,
            "dist_to": math.inf
        })

    lp.put(structure["visited"], source, {
        "marked": False,
        "edge_from": None,
        "dist_to": 0
    })

    pq.insert(structure["pq"], source, 0)
    return structure

def dijkstra(graph,source):
    if lp.contains(graph["vertices"],source):
        structure = init_structure(graph, source)
        key_priority = pq.get_first_priority(structure["pq"])
        pq.remove(structure["pq"])
        marked = None
    pass
    

