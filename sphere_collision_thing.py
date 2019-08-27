import math, pygame, random

def cosd(a):
    return math.cos(a*math.pi/180)

def sind(a):
    return math.sin(a*math.pi/180)

def circle(pos, rad, rot, vel, mass, color):
    return [pos, rad, [cosd(rot)*vel, sind(rot)*vel], mass, color]

class Data:
    def __init__(self):
        self.size = (640, 480)
        self.circles = self.random_circles(8, 4)

    def random_circles(self, ax, ay):
        cs = []
        for x in range(1, ax):
            for y in range(1, ay):
                cs.append(circle([x*self.size[0]/ax, y*self.size[1]/ay],
                                 random.randint(8, 32),
                                 random.randint(-180, 180),
                                 random.random()*2.5,
                                 0.5+random.random()*9.5,
                                 (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))
        return cs

data0 = Data()

def colliding(c0, c1):
    return math.sqrt((c1[0][0]-c0[0][0])**2+(c1[0][1]-c0[0][1])**2) < c0[1]+c1[1]

def atan3(y, x):
    return math.atan2(y, x)+math.pi*(x < 0)

bg_color = (255, 255, 255)
pygame.init()
surface = pygame.display.set_mode(data0.size)
pygame.display.set_caption("Collision Test")
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(30)
    collisions = []
    for c0 in range(len(data0.circles)):
        for c1 in range(c0+1, len(data0.circles)):
            if colliding(data0.circles[c0], data0.circles[c1]):
                collisions.append((c0, c1))
    for cs in collisions:
        v0 = math.sqrt(data0.circles[cs[0]][2][0]**2+data0.circles[cs[0]][2][1]**2)
        r0 = atan3(data0.circles[cs[0]][2][1], data0.circles[cs[0]][2][0])
        m0 = data0.circles[cs[0]][3]
        v1 = math.sqrt(data0.circles[cs[1]][2][0]**2+data0.circles[cs[1]][2][1]**2)
        r1 = atan3(data0.circles[cs[1]][2][1], data0.circles[cs[1]][2][0])
        m1 = data0.circles[cs[1]][3]
        ca = atan3(data0.circles[cs[1]][0][1]-data0.circles[cs[0]][0][1], data0.circles[cs[1]][0][0]-data0.circles[cs[0]][0][0])
        data0.circles[cs[0]][2][0] = (v0*math.cos(r0-ca)*(m0-m1)+2*m1*v1*math.cos(r1-ca))/(m0+m1)*math.cos(ca)+v0*math.sin(r0-ca)*math.cos(ca+math.pi/2)
        data0.circles[cs[0]][2][1] = (v0*math.cos(r0-ca)*(m0-m1)+2*m1*v1*math.cos(r1-ca))/(m0+m1)*math.sin(ca)+v0*math.sin(r0-ca)*math.sin(ca+math.pi/2)
        data0.circles[cs[1]][2][0] = (v1*math.cos(r1-ca)*(m1-m0)+2*m0*v0*math.cos(r0-ca))/(m1+m0)*math.cos(ca)+v1*math.sin(r1-ca)*math.cos(ca+math.pi/2)
        data0.circles[cs[1]][2][1] = (v1*math.cos(r1-ca)*(m1-m0)+2*m0*v0*math.cos(r0-ca))/(m1+m0)*math.sin(ca)+v1*math.sin(r1-ca)*math.sin(ca+math.pi/2)
    for c in range(len(data0.circles)):
        if abs(data0.circles[c][0][0]-data0.size[0]/2)+data0.circles[c][1] > data0.size[0]/2:
            data0.circles[c][2][0] = -data0.circles[c][2][0]
        if abs(data0.circles[c][0][1]-data0.size[1]/2)+data0.circles[c][1] > data0.size[1]/2:
            data0.circles[c][2][1] = -data0.circles[c][2][1]
    for c in range(len(data0.circles)):
        data0.circles[c][0][0] += data0.circles[c][2][0]
        data0.circles[c][0][1] += data0.circles[c][2][1]
    surface.fill(bg_color)
    for c in data0.circles:
        pygame.draw.circle(surface, c[4], (int(c[0][0]), int(c[0][1])), int(c[1]), 0)
    pygame.display.flip()
pygame.quit()
