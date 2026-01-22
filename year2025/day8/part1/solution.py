#!/usr/bin/env python3
# Day 8: Playground, Part 1

import numpy as np

FILE_PATH = "../.temp"

def euclidean_distance(point1: (int, int, int), point2: (int, int, int)) -> int:
    return np.sqrt(np.sum(((point2[0] - point1[0]) ** 2, (point2[1] - point1[1]) ** 2, (point2[2] - point1[2]) ** 2)))

def main():
    junction_boxes = []

    with open(FILE_PATH, 'r') as junction_boxes_file:
        for line in junction_boxes_file:
            line = line.rstrip('\n')
            junction_boxes.append(tuple(map(int, line.split(','))))

    num_boxes = len(junction_boxes)

    all_pairs = []
    for i in range(num_boxes):
        for j in range(i+1, num_boxes):
            dist = euclidean_distance(junction_boxes[i], junction_boxes[j])
            all_pairs.append((dist, i, j))

    all_pairs.sort()

if __name__ == "__main__":
    main()
