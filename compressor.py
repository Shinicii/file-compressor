#!/usr/bin/env Python3
from collections import Counter
from heapq import heappush, heappop

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

#generate tree
def genTree(root):
    if root.isLeaf:
        return b'0' + root.v.to_bytes(1,'little')
    return genTree(root.left) + genTree(root.right) + b'1'

#generate code
def genCodes(root, code):
    if root.isLeaf:
        root.code = code
        codeMap[root.v] = code
        return
    genCodes(root.left, code + '0')
    genCodes(root.right, code + '1')

f = open("sample.txt",'a')
f.write("\n")
f.close()

#open file
f = open("sample.txt", 'rb')
out = open("temp.shin", 'wb')

memory = f.read()
heap = []

frequency = Counter(memory)

#pushing unique elements with frequency in the heap
for letter in frequency:
    leaf = Node(frequency[letter], letter)
    leaf.isLeaf = True
    heappush(heap, (frequency[letter], leaf))

#huffman encoding algo
while len(heap) >= 2:
    f1, left = heappop(heap)
    f2, right = heappop(heap)

    node = Node(f1 + f2, -1, '', left, right)
    heappush(heap, (node.f, node))

_, root = heappop(heap)

genCodes(root, '')
tree = genTree(root)

#write length of huffman tree
out.write(len(tree).to_bytes(4, 'little'))
out.write(tree)

byte = 0
packed = 0

for b in memory:
    code = codeMap[b]
    for bit in code:
        if packed == 8:
           out.write((byte & 0xFF).to_bytes(1,'little'))
           byte = 0
           packed = 0
        if bit == '1':
            byte |= (1 << packed)
            packed+=1
        else:
            packed +=1

if packed < 8:
    out.write((byte & 0xFF).to_bytes(1,'little'))
