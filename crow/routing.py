import heapq
import time

#crow modules
import config

class RoutingTable(object):
    """
        Binary Tree with K-buckets for leaves
    """
    def __init__(self):
        pass

class KBucket(object):
    def __init__(self, lowerRange, upperRange, k=config.K):
        self.nodes = dict()
        self.ranges = (lowerRange, upperRange)
        self.k = k

    def getNodes(self):
        return self.nodes.values()

    def removeNode(self, node_id):
        pass

    def addNode(self, NND):
        pass

    def isEmpty(self):
        return True if len(self.nodes) == 0 else False
