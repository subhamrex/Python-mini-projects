from vpython import *


# Install vpython for 3D Animation

def welcome():
    text(text="Welcome")

def sphere_shrink_test():
    sph = sphere(pos=vector(0, 0, 0), color=vector(1, 2, 5), shininess=1, opacity=0.6, radius=2, size=vector(1, 1, 1),
                 texture=textures.stucco)
    i = 1
    dx = 0.1
    while i <= 1000:
        rate(10)  # no. of loops per second
        sph.pos.x = sph.pos.x + dx
        i += 1


def sphere_wall_test():
    my_sphere = sphere(pos=vector(0, 0, 0, ), radius=0.25, color=vector(1, 2, 4), shininess=1)
    wall1 = box(pos=vector(2, 0, 0), size=vector(0.1, 1, 1), color=vector(3, 4, 4))
    wall2 = box(pos=vector(-2, 0, 0), size=vector(0.1, 1, 1), color=vector(3, 4, 4))
    edge1 = wall1.pos.x - wall1.size.x / 2
    edge2 = wall2.pos.x - wall2.size.x / 2
    i = 1
    dx = 0.1
    while i <= 1000:
        rate(10)
        if (my_sphere.pos.x + my_sphere.radius >= edge1) or (my_sphere.pos.x - my_sphere.radius <= edge2):
            dx = -dx
        my_sphere.pos.x = my_sphere.pos.x + dx
        i = i + 1


if __name__ == "__main__":
    choice = input("1.Welcome\n2.sphere shrink\n3.sphere bounces on wall\n")

    if choice == "1":
        welcome()

    elif choice == "2":
        sphere_shrink_test()

    elif choice == "3":
        sphere_wall_test()

    else:
        print("Wrong Choice")
