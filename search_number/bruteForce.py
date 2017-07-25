import networkx as nx
import itertools

def getWidth(order):
    '''
    Given a graph G, and it's edge ordering, returns
    the linear width of that ordering.
    
    INPUT
    order: An edge ordering of G

    OUTPUT
    width: The width of order
    '''
    #We make a left and the right set of nodes incident to 1-j (left) 
    #and j + 1 - len(order) (right)

    left = set()
    right = set.union(*order)
    width = len(left.intersection(right))

    #Move the sets along by one and construct the new node lists
    for i in xrange(len(order) - 1):
        left = left.union(order[i])
        right = set.union(*(order[i + 1:]))
        print 'For i = ', i, 'left = ', left, 'and right= ', right

        newWidth = len(left.intersection(right))

        if newWidth > width:
            width = newWidth

    return width

def linearWidth(G):
    '''
    Given a graph, calculates the linear width of the graph
    by brute force.

    INPUT
    G: A networkx graph

    OUTPUT
    width: The linear width of G
    '''
    #Treat the edges of G as a set
    edges = G.edges()

    for i in xrange(len(edges)):
        edges[i] = set(edges[i])

    #Get all possible edge orderings
    orderings = list(itertools.permutations(edges))

    #Find the least width edge ordering
    leastWidth = getWidth(orderings[0])
    leastOrdering = orderings[0]

    for order in orderings:
        
        width = getWidth(order)
        print 'The width of: ', order, 'is: ', width

        if width < leastWidth:
            leastWidth = width
            leastOrdering = orderings[0]

    return [leastOrdering, leastWidth]

