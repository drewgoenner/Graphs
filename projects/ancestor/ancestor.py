
from util import  Stack, Graph

def earliest_ancestor(ancestors, starting_node):
    #This will be a DFS, as we should only need to really search up and down
    #We will need to create the graph fist
    ancestor_tree = Graph()
    #Next, go through the ancestors
    for (parent, child) in ancestors:
    #add the vertices for each child and parent
    	ancestor_tree.add_vertex(parent)
    	ancestor_tree.add_vertex(child)
    #  connect children and parents in reverse
    	ancestor_tree.add_edge(child, parent)
    # initialize the queue
    stack = Stack()
    stack.push([starting_node])
    # pay attention to number of ancestors
    longest_path = 1
    #store the earliest ancestor
    earliest_ancestor = -1
    # while the queue has items in it
    while stack.size() > 0:
    	# pop one off the end and move to the next
    	path = stack.pop()
    	vertex = path[-1]
    	# path is longer or equal and value is smaller or if path is longer
    	if (len(path) >= longest_path and vertex < earliest_ancestor) or (len(path) > longest_path):
    	# set earliest ancestor equal to the vertex and set longest path to the length of path
    		earliest_ancestor = vertex
    		longest_path = len(path)
    	# add neighbor to path in back of queue
    	for neighbor in ancestor_tree.get_neighbors(vertex):
    		new_path = list(path)
    		new_path.append(neighbor)
    		stack.push(new_path)
    
    return earliest_ancestor
