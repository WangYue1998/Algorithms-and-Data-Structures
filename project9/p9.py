import random

# Custom Graph error
class GraphError(Exception): pass

class Graph:
    """
    Graph Class ADT
    """
    class Edge:
        """
        Class representing an Edge in the Graph
        """
        __slots__ = ['source', 'destination']

        def __init__(self, source, destination):
            """
            DO NOT EDIT THIS METHOD!
            Class representing an Edge in a graph
            :param source: Vertex where this edge originates
            :param destination: ID of Vertex where this edge ends
            """
            self.source = source
            self.destination = destination

        def __eq__(self, other):
            return self.source == other.source and self.destination == other.destination

        def __repr__(self):
            return f"Source: {self.source} Destination: {self.destination}"

        __str__ = __repr__

    class Path:
        """
        Class representing a Path through the Graph
        """
        __slots__ = ['vertices']

        def __init__(self, vertices=[]):
            """
            DO NOT EDIT THIS METHOD!
            Class representing a path in a graph
            :param vertices: Ordered list of vertices that compose the path
            """
            self.vertices = vertices

        def __eq__(self, other):
            return self.vertices == other.vertices

        def __repr__(self):
            return f"Path: {' -> '.join([str(v) for v in self.vertices])}\n"

        __str__ = __repr__

        def add_vertex(self, vertex):
            """
            Add a Vertex id to the path.
            Return None
            O(1) time complexity
            :param vertex: id
            :return: None
            """
            self.vertices.append(vertex)
            return None


        def remove_vertex(self):
            """
            Remove the most recently added Vertex id from the path.
            Return None
            O(1) time complexity
            :return: None
            """
            if self.is_empty() is False:
                self.vertices.pop()
            return None

        def last_vertex(self):
            """
            Return the last Vertex id added to the path
            If path is empty return None
            O(1) time complexity
            :return:last Vertex id
            """
            if self.is_empty() is True:
                return None
            else:
                return self.vertices[-1]

        def is_empty(self):
            """
            Check if the path is empty.
            Return Boolean
            O(1) time complexity
            :return: True or False
            """
            if len(self.vertices) == 0:
                return True
            else:
                return False

    class Vertex:
        """
        Class representing a Vertex in the Graph
        """
        __slots__ = ['ID', 'edges', 'visited', 'fake']

        def __init__(self, ID):
            """
            Class representing a vertex in the graph
            :param ID : Unique ID of this vertex
            """
            self.edges = []
            self.ID = ID
            self.visited = False
            self.fake = False

        def __repr__(self):
            return f"Vertex: {self.ID}"

        __str__ = __repr__

        def __eq__(self, other):
            """
            DO NOT EDIT THIS METHOD
            :param other: Vertex to compare
            :return: Bool, True if same, otherwise False
            """
            if self.ID == other.ID and self.visited == other.visited:
                if self.fake == other.fake and len(self.edges) == len(other.edges):
                    edges = set((edge.source.ID, edge.destination) for edge in self.edges)
                    difference = [e for e in other.edges if (e.source.ID, e.destination) not in edges]
                    if len(difference) > 0:
                        return False
                    return True

        def add_edge(self, destination):
            """
            Add an edge to the Vertex given the id of the destination Vertex.
            Return None
            O(1) time complexity
            :param destination:
            :return: None
            """
            self.edges.append(Graph.Edge(self, destination))
            return None

        def degree(self):
            """
            Return the number of outgoing edges (degree) of the Vertex
            O(1) time complexity
            :return: the number of outgoing edges
            """
            return len(self.edges)

        def get_edge(self, destination):
            """
            Returns the Edge that goes to a specified destination node.
            If the edge is not found, return None
            O(n) time complexity
            :param destination: destination node
            :return: Returns the Edge that goes to a specified destination node.
            """
            for edge in self.edges:
                if edge.destination == destination:
                    return edge

        def get_edges(self):
            """
            Returns a list of all of the edges.
            O(1) time complexity
            :return: a list of all of the edges
            """
            return self.edges

        def set_fake(self):
            """
            Set the vertex as a fake vertex.
            O(1) time complexity
            :return: no return
            """
            self.fake = True

        def visit(self):
            """
            Set the vertex as visited.
            O(1) time complexity
            :return: no return
            """
            self.visited = True

    def __init__(self, size=0, connectedness=1, filename=None):
        """
        DO NOT EDIT THIS METHOD
        Construct a random DAG
        :param size: Number of vertices
        :param connectedness: Value from 0 - 1 with 1 being a fully connected graph
        :param: filename: The name of a file to use to construct the graph.
        """
        assert connectedness <= 1
        self.adj_list = {}
        self.size = size
        self.connectedness = connectedness
        self.filename = filename
        self.construct_graph()

    def __eq__(self, other):
        """
        DO NOT EDIT THIS METHOD
        Determines if 2 graphs are IDentical
        :param other: Graph Object
        :return: Bool, True if Graph objects are equal
        """
        if len(self.adj_list) == len(other.adj_list):
            for key, value in self.adj_list.items():
                if key in other.adj_list:
                    if not self.adj_list[key] == other.adj_list[key]:
                        return False
                else:
                    return False
            return True
        return False

    def generate_edges(self):
        """
        DO NOT EDIT THIS METHOD
        Generates directed edges between vertices to form a DAG
        :return: A generator object that returns a tuple of the form (source ID, destination ID)
        used to construct an edge
        """
        random.seed(10)
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if random.randrange(0, 100) <= self.connectedness * 100:
                    yield [i, j]

    def get_vertex(self, ID):
        return self.adj_list.get(ID)

    def construct_graph(self):
        """
        Add all edges to a Graph.
        If a filename is provided, read from the file to construct the graph,
            otherwise use the generate_edges method to construct the graph.
        Do not accept graphs with a negative size or connectedness not in the range [0, 1]
        If provided with bad input, raise a GraphError.
        Both forms of input return data in the following format: [source, destination]
        Uses the dictionary self.adj_list to store vertices’ IDs as keys and their objects as values.
        Do NOT insert parallel edges in your graph.
        O(E) time complexity, E is the number of edges to insert.
        :return: no return
        """
        if self.filename is not None:
            file = open(self.filename)
            filelines = file.readlines()
            for line in filelines:
                line = line.split()
                source = int(line[0])
                destination = int(line[1])
                sour = self.Vertex(source)
                des = self.Vertex(destination)
                if source not in self.adj_list:
                    self.adj_list[source] = sour
                if  destination not in self.adj_list:
                    self.adj_list[destination] = des
                edge = self.adj_list[source].get_edge(destination)
                if edge is None:
                    self.adj_list[source].add_edge(destination)
                file.close()
        elif self.connectedness < 0 or self.connectedness > 1 or self.size <= 0:
            raise GraphError
        elif  self.filename is None:
            for i in self.generate_edges():
                source = i[0]
                destination = i[1]
                sour = self.Vertex(source)
                des = self.Vertex(destination)
                if source not in  self.adj_list:
                    self.adj_list[source] = sour
                if destination not in self.adj_list:
                    self.adj_list[destination] = des
                edge = self.adj_list[source].get_edge(destination)
                if edge is None:
                    self.adj_list[source].add_edge(destination)

    def BFS(self, start, target):
        """Breadth First Search given a start ID, find a path to the target ID.
        If the target node is not found, return an empty Path,
        otherwise, return a Path of vertex id's from the start vertex to the target vertex.
        If there are multiple paths, choose 1 path to return.
        O(V+E), V is the number of vertices, E is the number of edges
        :param start: start ID
        :param target: target ID
        :return: path or empty path
        """
        # the vertix did not exit
        if self.adj_list.get(start) is None:
            return[]
        qlist = []
        qlist.append([start])
        path = self.Path()
        while qlist:
            path.vertices = qlist.pop(0)
            end = path.vertices[-1]
            if end == target:
                return path
            for adj in self.adj_list.get(end, []).edges:
                new_p = list(path.vertices)
                new_p.append(self.adj_list.get(adj.destination).ID)
                self.adj_list.get(adj.destination).visit()
                qlist.append(new_p)
        #cannot find target
        return []

    def DFS(self, start, target, path=Path()):
        """
        Depth First Search with the same return specifications as BFS
        Must be recursive
        O(V+E), V is the number of vertices, E is the number of edges
        :param start: start ID
        :param target: target ID
        :param path: path
        :return:  path or empty path
        """
        if self.adj_list.get(target) is None:
            return path.vertices
        else:
            if path.last_vertex() is not start:
                path.add_vertex(start)
            for e in self.adj_list.get(start).edges:
                if path.last_vertex() is not start:
                    path.remove_vertex()
                v = e.destination
                ver = self.adj_list.get(v)
                if ver.visited is False:
                    ver.visit()
                    path.add_vertex(v)
                    if v == target:
                        return path
                    elif v != target and ver.degree() == 0:
                        path.remove_vertex()
                    elif v != target and ver.degree() != 0:
                        self.DFS(v, target, path)
                        if path.last_vertex() is target:
                            return path
        return path

def fake_emails(graph, mark_fake=False):
    """
    Finds all fake vertices in the Graph, sets them to be fake, and adds their IDs to a list.
    A Vertex is fake if the degree of the vertex is 0 (messages coming in, no messages going out).
    If mark_false is True, set the fake flag on each fake vertex.
    You are allowed to iterate over graph.adj_list ONLY in the scope of this method.
    Returns a list of fake vertex IDs.
    O(V(V+E)) time complexity, V is the number of vertices, E is the number of edges
    :param graph: Finds all fake vertices in the Graph
    :param mark_fake: flag
    :return: a list of fake vertex IDs
    """
    def check_fake_emails(start, emails=list()):
        """
        This is a nested function within fake_emails() DO NOT move it outside of fake_emails().
        Given a start Vertex ID, find all fake email addressses that can be reached from that ID
            and remove the edge connecting to the fake address.
        DO NOT access graph.adj_list directly, use accessors.
        Must be recursive.
        O(V+E) time complexity, V is the number of vertices, E is the number of edges
        :param start: a start Vertex ID
        :param emails: list
        :return: no return
        """
        sta = graph.get_vertex(start)
        if sta.visited is False:
            sta.visit()
            if sta.degree() == 0:
                if mark_fake is True:
                    sta.set_fake()
                emails.append(start)
                return emails

            for i in sta.edges[:]:  # copy
                d = i.destination
                des = graph.get_vertex(d)
                check_fake_emails(d, emails)
                if des.fake is True:
                    sta.edges.remove(i)  # remove edges
    fake = []
    for key, value in graph.adj_list.items():
        check_fake_emails(key, fake)
    return fake
