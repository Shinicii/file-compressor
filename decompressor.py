#!/usr/bin/env Python3

class Node:
    def __init__(self, f, v, code='', left=None, right=None):
        self.left = left
        self.right = right
        self.v = v
        self.f = f
        self.isLeaf = False
        self.code = code

    def __lt__(self, other):
        return self.f < other.f

codeMap = {}

#generate code
def genCodes(root, code):
    if root.isLeaf:
        root.code = code
        codeMap[root.v] = code
        return
    genCodes(root.left, code + '0')
    genCodes(root.right, code + '1')

encode = open('temp.shin', 'rb')
data = encode.read()

stack = []

treeSize = (data[0] & 0xFF | data[1] & 0xFF << 8 | data[2] & 0xFF << 16 | data[3] & 0xFF << 24)
i, end = 4, 4 + treeSize

while i < end:
    if data[i] == 48:
        n = Node(-1, data[i+1], '', None, None)
        n.isLeaf = True
        stack.append(n)
        i += 2
    else:
        right = stack.pop()
        left = stack.pop()
        n = Node(-1, -1, '', left, right)
        stack.append(n)
        i += 1

root = stack.pop()
genCodes(root, '')

code = ''

pointer = root
out = open('output.txt', 'w')

while i < len(data):
    byte = data[i]
    for j in range(8):
        if pointer.isLeaf:
            out.write(chr(pointer.v))
            pointer = root
        if byte & (1 << j):
            pointer = pointer.right
        else:
            pointer = pointer.left
    i += 1
