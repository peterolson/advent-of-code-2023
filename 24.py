from skspatial.objects import Line, Plane
from z3 import Int, Solver, Real

with open("input/24.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    
def parse_hailstone(line):
    position, velocity = line.split(" @ ")
    position = position.split(", ")
    velocity = velocity.split(", ")
    position = [float(p) for p in position]
    velocity = [float(v) for v in velocity]
    return position, velocity

hailstones = [parse_hailstone(line) for line in lines]

def get_intersection(p1, v1, p2, v2):
    line_a = Line(point=p1, direction=v1)
    line_b = Line(point=p2, direction=v2)
    try:
        p_intersection = line_a.intersect_line(line_b)
    except ValueError:
        # Parallel lines
        return None
    
    def get_time_to_intersection(p, v):
        for i, (pi, vi) in enumerate(zip(p, v)):
            if vi == 0:
                continue
            return (p_intersection[i] - pi) / vi
        
    t1 = get_time_to_intersection(p1, v1)
    t2 = get_time_to_intersection(p2, v2)
    
    return p_intersection, t1, t2


test_area = [200000000000000, 400000000000000]

def is_in_test_area(x,y):
    epsilon = 0
    min, max = test_area
    min -= epsilon
    max += epsilon
    return min <= x <= max and min <= y <= max

total = 0

for i, hailstone in enumerate(hailstones):
    print(i)
    (px1, py1, pz1), (vx1, vy1, vz1) = hailstone
    for j, other_hailstone in enumerate(hailstones[i+1:]):
        (px2, py2, pz2), (vx2, vy2, vz2) = other_hailstone
        intersection = get_intersection((px1, py1), (vx1, vy1), (px2, py2), (vx2, vy2))
        if intersection is None:
            continue
        (x,y), t1, t2 = intersection
        if not is_in_test_area(x,y):
            continue
        if t1 < 0:
            continue
        if t2 < 0:
            continue
        total += 1

print("Total:")      
print(total)

x = Real('x')
y = Real('y')
z = Real('z')
vx = Real('vx')
vy = Real('vy')
vz = Real('vz')
t0 = Real('t0')
t1 = Real('t1')
t2 = Real('t2')
t3 = Real('t3')

(h0_x, h0_y, h0_z), (h0_vx, h0_vy, h0_vz) = hailstones[0]
(h1_x, h1_y, h1_z), (h1_vx, h1_vy, h1_vz) = hailstones[1]
(h2_x, h2_y, h2_z), (h2_vx, h2_vy, h2_vz) = hailstones[2]
(h3_x, h3_y, h3_z), (h3_vx, h3_vy, h3_vz) = hailstones[3]

s = Solver()
s.add(t0 >= 0, t1 >= 0, t2 >= 0,
      x + vx * t0 == h0_x + h0_vx * t0,
        y + vy * t0 == h0_y + h0_vy * t0,
        z + vz * t0 == h0_z + h0_vz * t0,
        x + vx * t1 == h1_x + h1_vx * t1,
        y + vy * t1 == h1_y + h1_vy * t1,
        z + vz * t1 == h1_z + h1_vz * t1,
        x + vx * t2 == h2_x + h2_vx * t2,
        y + vy * t2 == h2_y + h2_vy * t2,
        z + vz * t2 == h2_z + h2_vz * t2,
        x + vx * t3 == h3_x + h3_vx * t3,
        y + vy * t3 == h3_y + h3_vy * t3,
        z + vz * t3 == h3_z + h3_vz * t3)
s.check()
m = s.model()
x = m[x].as_long()
y = m[y].as_long()
z = m[z].as_long()
print(x+y+z)