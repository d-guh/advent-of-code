#!/usr/bin/env python3
# Day 8: Playground, Part 1

import collections

FILE_PATH = "../.input"

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, i):
        if self.parent[i] == i:
            return i

        self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]
    
    def unite(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        if irep != jrep:  # if not in same circuit
            self.parent[irep] = jrep

# Not euclidean distance, but faster, and accurate enough for ordering
def squared_distance(point1: (int, int, int), point2: (int, int, int)) -> int:
    #return ((point2[0] - point1[0]) ** 2) + ((point2[1] - point1[1]) ** 2) + ((point2[2] - point1[2]) ** 2)
    return sum((a - b) ** 2 for a, b in zip(point1, point2))  # A bit more generic/easy to expand

def main():
    junction_boxes = []

    with open(FILE_PATH, 'r') as junction_boxes_file:
        for line in junction_boxes_file:
            line = line.rstrip('\n')
            junction_boxes.append(tuple(map(int, line.split(','))))
    junction_boxes = tuple(junction_boxes)  # Convert to tuple, prevents modifying initial list, could improve operation speed?

    num_boxes = len(junction_boxes)
    all_pairs = []
    for i in range(num_boxes):
        for j in range(i+1, num_boxes):
            dist = squared_distance(junction_boxes[i], junction_boxes[j])
            all_pairs.append((dist, i, j))

    all_pairs.sort()
    #print(f"DEBUG: Total possible pairs: {len(all_pairs)}")

    uf = UnionFind(num_boxes)

    # This seems to work OK, maybe should be tracking actual connections made vs redundant checks, but leaving for now
    for dist, i, j in all_pairs[:1000]:
        uf.unite(i, j)

    circuit_sizes = collections.Counter()
    for i in range(num_boxes):
        root = uf.find(i)
        circuit_sizes[root] += 1

    all_sizes = sorted(circuit_sizes.values(), reverse=True)
    #print(f"DEBUG: Total separate circuits: {len(all_sizes)}")

    top_3 = all_sizes[:3]
    product = 1
    for size in top_3:
        product *= size

    #print(f"DEBUG: 3 largest: {top_3}")
    print(f"Product: {product}")

if __name__ == "__main__":
    main()
