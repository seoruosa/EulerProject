TRIANGLE = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

with open("p067_triangle.txt", 'r') as f:
    TRIANGLE = f.read()
# linha 4, el 18
# pos da seq, 
# 0
# 1, max of (children + max of children)
# 2, max of children
# 3, 18
# https://www.codementor.io/@leandrotk100/everything-you-need-to-know-about-tree-data-structures-pynnlkyud


# el[3][0]=18 -> parents = el[2][0]=17
# el[3][1]=35 -> parents = el[2][0]=17, el[2][1]=47
# el[3][2]=87 -> parents = el[2][1]=47, el[2][2]=82
# el[3][3]=10 -> parents = el[2][2]=82

# el[2][0]=17 -> children = el[3][0]=18, el[3][1]=35
# el[2][1]=47 -> children = el[3][1]=35, el[3][2]=87
# el[2][2]=82 -> children = el[3][2]=87, el[3][3]=10

class Node:
    """
    Class that define a node
    """

    def __init__(self, value):
        self.left = None
        self.data = int(value)
        self.right = None
        self.sumList = [int(value)]
    
    def configureChildren(self, left=None, right=None):
        self.left = left
        self.right = right
    
    def data(self):
        return self.data

    def __str__(self):
        return f"{self.data}"

class TriangleTree:
    """
    Class tree will provide a tree as well as utility functions.
    """
    def __init__(self, triangle_string=''):
        self.tree = []
        if triangle_string!='':
            for line in TRIANGLE.splitlines():
                l = []
                for e in line.split(' '):
                    l.append(Node(int(e)))
                    # l.append(int(e))
                self.tree.append(l)

    def configureParents(self, i, j):
        left_parent, right_parent = self.parents(i, j)
        if left_parent!=None:
            left_parent.configureChildren(right=self.tree[i][j])
        if right_parent!=None:
            right_parent.configureChildren(left=self.tree[i][j])
    
    def configChildrenOfAllNodes(self):
        # for i in range(0, len(self.tree)):
        for i in range(len(self.tree)-1, -1, -1):
            for j in range(0, len(self.tree[i])):
                left, right = self.parents(i, j)
                if left != None:
                    left.configureChildren(right=self.tree[i][j])
                if right != None:
                    right.configureChildren(left=self.tree[i][j])

    def maxSumOfAllNodes(self):
        for i in range(len(self.tree)-2, -1, -1):
            for j in range(0, len(self.tree[i])):
                for k in range(len(self.children(i,j)[0].sumList)):
                    self.tree[i][j].sumList.append(self.tree[i][j].data + max(self.children(i,j)[0].sumList[k], self.children(i,j)[1].sumList[k]))

    def height(self):
        return len(self.tree)

    def width(self, i, j=0):
        return len(self.tree[i])

    def children(self, i, j):
        if ((i<self.height()-1) & (i>=0)):
            return (self.tree[i+1][j],self.tree[i+1][j+1])
        else:
            return None

    def parents(self, i, j):
        if i==0:
            return (None, None)
        elif j==0:
            return (None, self.tree[i-1][j])
        elif j== self.width(i,j)-1:
            return (self.tree[i-1][-1], None)
        else:
            return (self.tree[i-1][j-1], self.tree[i-1][j])

    def node_value(self, i, j):
        return self.tree[i][j]
    
    def close(self):
        del self
    
    
def main():
    tree = TriangleTree(TRIANGLE)
    tree.configChildrenOfAllNodes()
    tree.maxSumOfAllNodes()



    for i in range(tree.height()-1):
        for j in range(tree.width(i)):
            print("{} -- {} {} {}".format(tree.node_value(i,j), *tree.children(i,j), tree.node_value(i,j).sumList))
    
    print(f"The maximum total is {max(tree.node_value(0,0).sumList)}")


    tree.close()


if __name__ == '__main__':
    main()