class UnionFind:
  """
  Union-Find With path compression
  """

  def __init__(self, value):
    self.value = value
    self.parent = self
    self.next = self
    self.rank = 0

  def find(self):
    """
    returns root of set and performs path compression
    """
    path = []
    node = self
    while node is not node.parent:
      path.append(node)
      node = node.parent
    root = node
    for node in path:
      node.parent = root
    return root

  def union(self, other):
    """
    union by rank
    """
    selfRoot = self.find()
    otherRoot = other.find()
    if selfRoot is not otherRoot:
      selfRoot.next, otherRoot.next = otherRoot.next, selfRoot.next
      if selfRoot.rank < otherRoot.rank:
        selfRoot.parent = otherRoot.parent
        return "child"
      else:
        otherRoot.parent = selfRoot.parent
        if selfRoot.rank == otherRoot.rank:
          selfRoot.rank += 1
        return "parent"
    return "same_set"
  
  def add(self, value):
    self.union(UnionFind(value))

  def getElements(self):
    """
    generator for elements in the set
    """
    yield self.value
    node = self.next
    while node != self:
      yield node.value
      node = node.next

  def __str__(self):
    return f"{{{', '.join(map(str, self.getElements()))}}}"

  def __repr__(self):
    return str(self)

