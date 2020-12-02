# Course:  CS 261
# Author: Christopher Vo
# Assignment: 6
# Description: implementation of UndirectedGraph class and its functions


class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        TODO: Write this implementation
        """
        if v in self.adj_list: #if key already exists
            return
        else:
            self.adj_list[v] = []
        
    def add_edge(self, u: str, v: str) -> None:
        """
        TODO: Write this implementation
                if v not in self.adj_list:
            self.adj_list[v] = []
            self.adj_list[v].append(u)
        else:
            if u not in self.adj_list[v]:
                self.adj_list[v].append(u)
        """

        if u not in self.adj_list:  # if vertex is not already in dictionary
            self.adj_list[u] = []

        if v not in self.adj_list[u]:  # check if u is in [v]
            self.adj_list[u].append(v)

        if v in self.adj_list:  # check if u in dict()
            if u not in self.adj_list[v]:  # check if v in [u]
                self.adj_list[v].append(u)

        elif v not in self.adj_list:  # check if u in dict()
            self.adj_list[v] = []
            self.adj_list[v].append(u)


    def remove_edge(self, v: str, u: str) -> None:
        """
        TODO: Write this implementation
        """
        if v in self.adj_list: #if v is in dict()
            if u in self.adj_list[v]: #if u is in dict[v]
                self.adj_list[v].remove(u)

        if u in self.adj_list: #if u is in dict()
            if v in self.adj_list[u]: #if v is in dict[u]
                self.adj_list[u].remove(v)
        

    def remove_vertex(self, v: str) -> None:
        """
        TODO: Write this implementation
        """
        other_v = []
        if v in self.adj_list: # if v is in dict()
            for i in range(len(self.adj_list[v])):
                other_v.append(self.adj_list[v][i])
            del self.adj_list[v] #remove key from dict()
            for i in range(len(other_v)):
                self.adj_list[other_v[i]].remove(v) #go through other keys and remove v
        else: #if v not in dict()
            return

    def get_vertices(self) -> []:
        """
        TODO: Write this implementation
        """

        return list(self.adj_list.keys())


    def get_edges(self) -> []:
        """
        TODO: Write this implementation
        """

        pairs = []
        for vertex in self.adj_list:
            for i in self.adj_list[vertex]:
                if (i, vertex) not in pairs:
                    pairs.append((vertex, i))
        return pairs

    def is_valid_path(self, path: []) -> bool:
        """
        TODO: Write this implementation
        """
        if len(path) == 1:
            if path[0] not in self.adj_list:
                return False

        for i in range(len(path) - 1):
            if path[i+1] not in self.adj_list[path[i]]:
                return False

        return True


    def dfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        if v_start not in self.adj_list:
            return []

        stack = []
        visited = []
        stack.append(v_start)
        while len(stack) != 0:
            v = stack.pop()
            print('v = ' + str(v))
            if v not in visited:
                visited.append(v)

                if v == v_end:
                    break

                for vertex in self.adj_list[v]:
                    stack.append(vertex)
                print('stack = ')
                print(stack)
                print('visited = ')
                print(visited)

        return visited


       

    def bfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        

    def count_connected_components(self):
        """
        TODO: Write this implementation
        """
      

    def has_cycle(self):
        """
        TODO: Write this implementation
        """
       

   


if __name__ == '__main__':


    """

    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    print(g)
    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')


    print("\nPDF - method count_connected_components() example 1")
    print("---------------------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print(g.count_connected_components(), end=' ')
    print()


    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
        'add FG', 'remove GE')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print('{:<10}'.format(case), g.has_cycle())
    """
