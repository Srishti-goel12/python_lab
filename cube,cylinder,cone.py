import math

# Cube
def cube_volume(a):
    return a ** 3

def cube_surface_area(a):
    return 6 * a * a


# Cuboid
def cuboid_volume(l, b, h):
    return l * b * h

def cuboid_surface_area(l, b, h):
    return 2 * (l*b + b*h + h*l)


# Cylinder
def cylinder_csa(r, h):
    return 2 * math.pi * r * h

def cylinder_tsa(r, h):
    return 2 * math.pi * r * (r + h)

def cylinder_volume(r, h):
    return math.pi * r * r * h


# Cone
def cone_csa(r, l):
    return math.pi * r * l

def cone_tsa(r, l):
    return math.pi * r * (r + l)

def cone_volume(r, h):
    return (1/3) * math.pi * r * r * h


# Sphere
def sphere_surface_area(r):
    return 4 * math.pi * r * r

def sphere_volume(r):
    return (4/3) * math.pi * r ** 3


# Hemisphere
def hemisphere_csa(r):
    return 2 * math.pi * r * r

def hemisphere_tsa(r):
    return 3 * math.pi * r * r

def hemisphere_volume(r):
    return (2/3) * math.pi * r ** 3