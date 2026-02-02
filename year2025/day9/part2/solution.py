#!/usr/bin/env python3
# Day 9: Movie Theater, Part 2

FILE_PATH = "../.input"

def main():
    red_tiles = []
    with open(FILE_PATH, 'r') as red_tile_file:
        for line in red_tile_file:
            line.rstrip('\n')
            x, y = line.split(',')
            red_tiles.append(tuple(map(int, line.split(','))))

    #print(f"DEBUG: red_tiles: {red_tiles}")

    num_red_tiles = len(red_tiles)
    edges = []
    for i in range(num_red_tiles):
        edges.append((red_tiles[i], red_tiles[(i + 1) % num_red_tiles]))

    #print(f"DEBUG: edges: {edges}")

    # Coordinate compression (also removes duplicates)
    xs = sorted(list(set(v[0] for v in red_tiles)))
    ys = sorted(list(set(v[1] for v in red_tiles)))

    #print(f"DEBUG: xs: {xs}")
    #print(f"DEBUG: xs: {ys}")
    
    x_map = {x: i for i, x in enumerate(xs)}
    y_map = {y: i for i, y in enumerate(ys)}

    #print(f"DEBUG: x_map: {x_map}")
    #print(f"DEBUG: x_map: {y_map}")

    num_x = len(xs)
    num_y = len(ys)

    cell_inside = [[False] * (num_y - 1) for _ in range(num_x - 1)]

    #print(f"DEBUG: cell_inside (init): {cell_inside}")

    # Scanline (determines inside/outside)
    for iy in range(num_y - 1):
        y_mid = (ys[iy] + ys[iy+1]) / 2.0
        x_intersections = []
        for v1, v2 in edges:
            if min(v1[1], v2[1]) <= y_mid <= max(v1[1], v2[1]):
                if v1[0] == v2[0]:  # Vertical edge
                    x_intersections.append(v1[0])
        
        x_intersections.sort()
        #print(f"DEBUG: x_intersections: {x_intersections}")
        for i in range(0, len(x_intersections), 2):
            x_start = x_intersections[i]
            x_end = x_intersections[i+1]
            for ix in range(num_x - 1):
                if x_start <= xs[ix] and xs[ix+1] <= x_end:
                    cell_inside[ix][iy] = True

    #print(f"DEBUG: cell_inside (after): {cell_inside}")

    # 2D Prefix sum (checks if solid)
    prefix_sum = [[0] * num_y for _ in range(num_x)]
    #print(f"DEBUG: prefix_sum (init): {prefix_sum}")
    for ix in range(num_x - 1):
        for iy in range(num_y - 1):
            prefix_sum[ix+1][iy+1] = (int(cell_inside[ix][iy]) 
                                    + prefix_sum[ix][iy+1] 
                                    + prefix_sum[ix+1][iy] 
                                    - prefix_sum[ix][iy])

    #print(f"DEBUG: prefix_sum (after): {prefix_sum}")

    # Other edge case checks (1D line etc.)
    def is_h_seg_valid(ix, y_idx):
        if y_idx > 0 and cell_inside[ix][y_idx-1]: return True
        if y_idx < num_y - 1 and cell_inside[ix][y_idx]: return True
        y_val = ys[y_idx]
        for v1, v2 in edges:
            if v1[1] == v2[1] == y_val:
                if min(v1[0], v2[0]) <= xs[ix] and xs[ix+1] <= max(v1[0], v2[0]):
                    return True
        return False

    def is_v_seg_valid(x_idx, iy):
        if x_idx > 0 and cell_inside[x_idx-1][iy]: return True
        if x_idx < num_x - 1 and cell_inside[x_idx][iy]: return True
        x_val = xs[x_idx]
        for v1, v2 in edges:
            if v1[0] == v2[0] == x_val:
                if min(v1[1], v2[1]) <= ys[iy] and ys[iy+1] <= max(v1[1], v2[1]):
                    return True
        return False

    h_seg_valid = [[is_h_seg_valid(ix, y_idx) for ix in range(num_x-1)] for y_idx in range(num_y)]
    v_seg_valid = [[is_v_seg_valid(x_idx, iy) for iy in range(num_y-1)] for x_idx in range(num_x)]

    #print(f"DEBUG: h_seg_valid: {h_seg_valid}")
    #print(f"DEBUG: v_seg_valid: {v_seg_valid}")

    # Check all possible rectangles
    max_area = 0
    for i in range(num_red_tiles):
        for j in range(i, num_red_tiles):
            r1, r2 = red_tiles[i], red_tiles[j]
            x_min, x_max = min(r1[0], r2[0]), max(r1[0], r2[0])
            y_min, y_max = min(r1[1], r2[1]), max(r1[1], r2[1])
            
            ix1, ix2 = x_map[x_min], x_map[x_max]
            iy1, iy2 = y_map[y_min], y_map[y_max]
            
            valid = True
            if ix1 < ix2 and iy1 < iy2:
                count = prefix_sum[ix2][iy2] - prefix_sum[ix1][iy2] - prefix_sum[ix2][iy1] + prefix_sum[ix1][iy1]
                expected = (ix2 - ix1) * (iy2 - iy1)
                if count != expected:
                    valid = False
            elif ix1 < ix2:  # Horizontal Line
                for ix in range(ix1, ix2):
                    if not h_seg_valid[iy1][ix]:
                        valid = False; break
            elif iy1 < iy2:  # Vertical Line
                for iy in range(iy1, iy2):
                    if not v_seg_valid[ix1][iy]:
                        valid = False; break
            
            if valid:
                area = (x_max - x_min + 1) * (y_max - y_min + 1)
                if area > max_area:
                    max_area = area
                    best_coords = (r1, r2)

    #print(f"DEBUG: best_coords: {best_coords}")
    print(f"Largest area: {max_area}")

if __name__ == "__main__":
    main()
