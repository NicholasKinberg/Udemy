from queue import Queue
import unittest
# two queues: order queue and processing queue, one for ordering, one for taking nodes out of DAG and putting into order in order queue
class GraphNode:
    def __init__(self, value):
        self.value = value
        self.outgoing = [] # outgoing initialized as empty list that we will treat as queue
        self.incoming = 0 # beginning node?
    
    def addEdge(self, node):
        self.outgoing.append(node) # calling empty list that we will treat as queue (FIFO)

class Graph:
    def __init__(self):
        self.nodes = [] # initialize empty list
    
    def addNode(self, node):
        self.nodes.append(node) # are we developing two systems, one for queuing, another for processing?
    
    def topologicalSort(graph):
        order = Queue() # initialize order queue
        process_next = Queue() # initialize processing queue

        for node in graph.nodes:
            for out in node.outgoing:
                out.incoming += 1 # for each node for each out going into outgoing queue, increase incoming variable by 1
        
        for node in graph.nodes:
            if node.incoming == 0:
                process_next.put(node) # put node in queue
        
        while process_next.qsize() > 0: # while processing queue size is greater than zero...
            node = process_next.get() # assign node to processing queue, get() command retrieves value of key
            for out in node.outgoing:
                out.incoming -= 1 # as outgoing queue lengthens, incoming queue shortens
                if out.incoming == 0:
                    process_next.put(out)
            order.put(node)
        
        if order.qsize() == len(graph.nodes):
            return order
        else:
            return None
        
