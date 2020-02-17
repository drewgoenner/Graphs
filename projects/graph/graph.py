"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # TODO
        if vertex_id in self.vertices:
            print("WARNING: Vertex already exists")
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('No such vertex')


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # TODO
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # TODO
        #create empty queue
        queue = Queue()
        # create empty set to store visited
        visited = set()
        # add starting vertex_id to queue
        queue.enqueue(starting_vertex)
        # while queue not empty
        while queue.size() > 0:
        # dequeue the first vertex
            vertex = queue.dequeue()
        # if it hasn't been visited
            if vertex not in visited:
        # mark it as visited
                visited.add(vertex)
        # add all neighbors to back of queue
                for neighbor in self.get_neighbors(vertex):
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # TODO
        # create empty stack
        stack = Stack()
        # push starting id to the stack
        stack.push(starting_vertex)
        # create empty set to store visited
        visited = set()
        # while stack isn't empty
        while stack.size() > 0:
        # pop the first vertex
            vertex = stack.pop()
        # if it hasn't been visited
            if vertex not in visited:
        # mark it as visited
                visited.add(vertex)
        # push all neighbors to top of stack
                for neighbor in self.get_neighbors(vertex):
                    stack.push(neighbor)


    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # TODO
        # if first runthrough
        if visited is None:
        # create empty set to store visited
            visited = set()
        # add first vertex to visited
        visited.add(starting_vertex)
        # check each neighbor and run dft_recur on it if it hasn't been visited
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # TODO
        # create empty queue
        queue = Queue()
        # add starting vertex_id to the queue
        queue.enqueue([starting_vertex])
        # create empty set to store visited
        visited = set()
        # while queue not empty
        while queue.size() > 0:
        # dequeue the first path
            path = queue.dequeue()
        # snag the last vertex of path
            vertex = path[-1]
        # if it hasn't been visited
            if vertex not in visited:
        # check if it's the destination
                if vertex == destination_vertex:
        # return the path if it is
                    return path
        # mark it as visited
                visited.add(vertex)
        # add path to neighbors to the back of the queue
                for neighbor in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # TODO
        # create an empty stack
        stack = Stack()
        # push path to starting_vertex
        stack.push([starting_vertex])
        # create empty set to store visited
        visited = set()
        # while stack isn't empty
        while stack.size() > 0:
        # pop the first path
            path = stack.pop()
        # snag the last vertex in path
            vertex = path[-1]
        # if it hasn't been visited
            if vertex not in visited:
            # see if it's the destination
                if vertex == destination_vertex:
                # if it is return path
                    return path
                # mark it as visited
                visited.add(vertex)
            # add path to neighbors to the back of the queue
                for next_vert in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, target_value, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # TODO
        # on first runthrough
        if visited is None:
        # create empty set to store visited
            visited = set()
        # if there is no path, set empty list
        if path is None:
            path = []
        # add starting vertex id to visited
        visited.add(starting_vertex)
        # add starting vertex to path
        path += [starting_vertex]
        # if starting vertex is the target
        if starting_vertex == target_value:
        # return path
            return path
        # if it isn't, have it call itself on each neighbor not visited.
        for vert in self.get_neighbors(starting_vertex):
            if vert not in visited:
                new_path = self.dfs_recursive(vert, target_value, visited, path)
                if new_path:
                    return new_path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
