# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class LRUNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.count=0
        self.hash={}
        self.head=LRUNode(None, None)
        self.tail=LRUNode(None, None)
        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash:
            node=self.hash[key]
            self.popNode(node)
            self.pushToTail(node)
            return node.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hash:
            self.hash[key].val=value
            self.get(key)
        else:
            node=LRUNode(key,value)
            self.hash[key]=node
            self.pushToTail(node)
            self.count+=1
            if self.count>self.capacity:
                self.count-=1
                self.popHead()

    def popNode(self,node):
        p=node.prev
        n=node.next
        n.prev=p
        p.next=n

    def pushToTail(self,node):
        p=self.tail.prev
        p.next=node
        node.prev=p
        node.next=self.tail
        self.tail.prev=node

    def popHead(self):
        nodeToPop=self.hash[self.head.next.key]
        if nodeToPop==self.tail:
            return
        self.popNode(nodeToPop)
        del self.hash[nodeToPop.key]


