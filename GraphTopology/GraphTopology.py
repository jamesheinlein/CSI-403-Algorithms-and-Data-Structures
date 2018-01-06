
def determine_topology(adj):

    n_vertices = len(adj.keys())
    vertex_classes = {}

    # determine the distribution of degrees among vertices
    for vertex, edges in adj.items():
        n_edges = len(edges)
        if n_edges not in vertex_classes.keys():
            vertex_classes[n_edges] = set()
        vertex_classes[n_edges].add(vertex)

    degrees = vertex_classes.keys()

    # determine topology formed based on the distribution of degrees among vertices
    if not len(degrees) > 2 and 0 not in degrees:

        if 1 in degrees and len(vertex_classes[1]) == 2 and \
           2 in degrees and len(vertex_classes[2]) == n_vertices - 2:
            return "bus"

        elif 2 in degrees and len(vertex_classes[2]) == n_vertices:
            return "ring"

        elif 1 in degrees and len(vertex_classes[1]) == n_vertices - 1 and \
             n_vertices - 1 in degrees and len(vertex_classes[n_vertices - 1]) == 1:
            return "star"

    return "irregular"

def validate_input(inpoo):
    # assert single key 'inList'
    assert 'inList' in inpoo.keys()
    assert len(inpoo.keys()) == 1

    # assert validity of edges
    edges = inpoo['inList']
    assert all([isinstance(e, dict) for e in edges])
    assert all([len(e.keys()) == 1 for e in edges])
    assert all(['connected' in e.keys() for e in edges])
    assert all([len(e['connected']) == 2 for e in edges])
    assert all([not isinstance(e, str) for e in edges])

def create_adj(edges):
    adj = {}
    for edge in edges:
        adj[edge[0]] = set()
        adj[edge[0]].add(edge[1])

    for edge in edges:
        if edge[1] not in adj.keys():
            adj[edge[1]] = set()
        adj[edge[1]].add(edge[0])

    return adj


def main():
    inpoo = {}
    inpoo['bus'] = [[('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')],
                    [('c', 'd'), ('a', 'b'), ('d', 'e'), ('b', 'c')]]

    inpoo['ring'] = [[('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a')],
                     [('a', 'b'), ('c', 'd'), ('b', 'c'), ('d', 'a')]]

    inpoo['star'] = [[('a', 'f'), ('b', 'f'), ('c', 'f'), ('d', 'f'), ('e', 'f')]]

    adj = create_adj(inpoo['star'][0])
    print(determine_topology(adj))



if __name__ == '__main__':
    main()

