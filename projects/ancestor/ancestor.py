from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    ancestor_graph = Graph()
    for i in ancestors:
        ancestor_graph.add_vertex(i[0])
        ancestor_graph.add_vertex(i[1])
    for i in ancestors:
        ancestor_graph.add_edge(i[1], i[0])
    ancestor = ancestor_graph.earliest(starting_node)
    if ancestor[-1] == starting_node:
        return -1
    else:
        return ancestor[-1]


list_of_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                     (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(list_of_ancestors, 3)
