import heapq

class Node(object):
    """
        Low level node representation
    """
    def __init__(self, node_id, node_ip, node_port):
        self.id = node_id
        self.ip = node_ip
        self.port = node_port   #udp

    #uses XOR to determine the distance between each node
    def distanceToNode(self, target_node_id):
        return self.node_id ^ target_node_id

    # allow node state to be traversed as a tuple
    def __iter__(self):
        return iter((self.id, self.ip, self.port))

    def __str__(self):
        return "node_id: {}, node_ip: {}, node_port: {}".format(self.id, self.ip, self.port)


class NodeList(object):
    pass
