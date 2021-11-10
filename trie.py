# Implementation of trie data structure
from collections import defaultdict
import random
import string
import re


def getwords(filename):
    res = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for l in lines:
            # res += [w.strip(string.punctuation).lower()
            #         for w in l.split()]
            res += [w.strip(string.punctuation).lower()
                    for w in re.findall(r"[\w']+", l)]
            # res += re.findall(r"[\w']+", l)
        return res


class keydefaultdict(defaultdict):
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        else:
            self[key] = val = self.default_factory(key)
            return val

class Trie(object):
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.child = keydefaultdict(Trie)
        self.visited = 0

    def add(self, word):
        pnode = self
        for char in word:
            cnode = pnode.child[char]
            cnode.parent = pnode
            pnode = cnode

    def match(self, prefix):
        pass

    def offspring(self):
        stack = [self]
        offsprings = []
        res = ''

        while stack:
            pnode = stack[-1]
            # print(f'Node {pnode.val}, visited {pnode.visited}')
            if not pnode.visited:
                pnode.visited = 1
                res += pnode.val if pnode.val != self.val else ''
                if pnode.child:
                    stack += list(pnode.child.values())
                else:
                    stack.pop()
                    pnode.visited = 0
                    offsprings.append(res[:])
                    res = res[:-1]
            else:
                stack.pop()
                pnode.visited = 0
                res = res[:-1]

        lineage = self.lineage()
        return [lineage + off for off in offsprings]

    def lineage(self):
        res = ''
        node = self
        while True:
            if node.parent is None:
                break
            else:
                res = node.val + res
                node = node.parent
        return res

    def __str__(self):
        return f'Node {self.val}'


def match(root, prefix):
    node = root
    for w in prefix:
        # defaultdict is used in Trie class
        # use in check
        if w in node.child:
            node = node.child[w]
        else:
            break
    print(node.offspring())


def traverse(root):
    # depth-first
    res = ''
    stack = [root]

    # Implement DFS using stack, first-in last-out
    while stack:
        # Access the last element
        pnode = stack[-1]
        # Check if already visited
        if not pnode.visited:
            pnode.visited = 1
            res += pnode.val if pnode.val != 'ROOT' else ''
            # Check if the node has children
            if pnode.child:
                stack += list(pnode.child.values())
            else:
                print(res)
                stack.pop()
                pnode.visited = 0
                res = res[:-1]
        else:
            stack.pop()
            pnode.visited = 0
            res = res[:-1]


def rand_print(root, attr):
    res = ''
    node = root
    while True:
        if node.child:
            res += str(getattr(node, attr)) + ' --> '
        else:
            res += str(getattr(node, attr))
            break
        node = random.choice(list(node.child.values()))
    print(res)


def main():
    # root = Trie('ROOT')
    # print(root)
    # root.add('pie')
    # node = root
    # res = ''
    # while True:
    #     if node.child:
    #         res += node.val + ' --> '
    #     else:
    #         res += node.val
    #         break
    #     node = list(node.child.values())[0]
    # print(res)

    root = Trie('ROOT')
    words = getwords('test_words.txt')
    # print(words)
    for w in words:
        root.add(w)

    # traverse(root)
    rand_print(root, 'val')

    print('\nTesting match:\n------')
    match(root, 'thi')
    return root

if __name__ == "__main__":
    root = main()
