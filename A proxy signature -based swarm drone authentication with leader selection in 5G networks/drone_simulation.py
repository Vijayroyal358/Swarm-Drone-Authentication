import pygame
import random
import math
from collections import defaultdict

WIDTH = 800
HEIGHT = 600

#id variables
drone_id=1
leader_id=1

# Load images

background = pygame.image.load("graphics/background.png")

#image URLs
drone_img = "graphics/drone.png"
leader_imgs=["graphics/football.png", "graphics/player1.png", "graphics/player2.png"]

# Resize images
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Get image rectangles



class Leader(pygame.sprite.Sprite):
    direction=(1,1) #direction in x and y axis +1 or -1
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        #self.id="leader_"+str(id)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel=2
        self.vel_x = random.uniform(1, 1.5)
        self.vel_y = math.sqrt(self.vel**2 - self.vel_x**2)
        self.direction = random.randint(0, 360)
        self.priority=5 #Priority 1 to 5, 1 most important

    def update_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        self.rect.x += self.vel_x #* math.cos(math.radians(self.direction))
        self.rect.y += self.vel_y #* math.sin(math.radians(self.direction))
        if self.rect.x < 0:
            #self.direction = 180 - self.direction + random.randint(-5, 5)
            #Self.rect.x =5
            self.vel_x*=(-1)
            #self.vel_y=math.sqrt(self.vel**2 - self.vel_x**2)
        elif self.rect.x > WIDTH - self.rect.width:
            #self.direction = 180 - self.direction + random.randint(-5, 5)
            #Self.rect.x =WIDTH-5
            self.vel_x*=(-1)
            #self.vel_y=math.sqrt(self.vel**2 - self.vel_x**2)
        elif self.rect.y < 0:
            #self.direction = 360 - self.direction + random.randint(-5, 5)
            #self.rect.y =5
            self.vel_y*=(-1)
            #self.vel_x=math.sqrt(self.vel**2 - self.vel_y**2)
        elif self.rect.y > HEIGHT - self.rect.height:
            #self.direction = 360 - self.direction  + random.randint(-5, 5)
            #self.rect.y =HEIGHT-5
            self.vel_y*=(-1)
            #self.vel_x=math.sqrt(self.vel**2 - self.vel_y**2)

    def handle_click(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                # Do something when the sprite is clicked
                print("Sprite clicked")


class Drone(pygame.sprite.Sprite):
    direction=(1,1) #direction in x and y axis +1 or -1
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.direction = random.uniform(0, 360)
        self.leader=None
        self.angle_wrt_leader=0
        self.up=False
        self.priority=5

    def assign_leader(self, leader_obj):
        self.leader=leader_obj
        self.priority=leader_obj.priority

    def update(self, min_distance):
        global collision_count
        # Calculate the distance from the target
        if self.leader is not None:
            leader_x, leader_y = self.leader.rect.x, self.leader.rect.y
            target_x = leader_x + math.cos(math.radians(self.angle_wrt_leader)) * 100
            target_y = leader_y + math.sin(math.radians(self.angle_wrt_leader)) * 100
            
            dx = target_x - self.rect.x
            dy = target_y - self.rect.y
            distance = math.sqrt(dx**2 + dy**2)

            if distance > min_distance:
                self.rect.x += self.speed * dx / distance
                self.rect.y += self.speed * dy / distance


        
            # dx = self.leader.rect.x - self.rect.x
            # dy = self.leader.rect.y - self.rect.y
            # distance = math.sqrt(dx**2 + dy**2)

            # # Move towards the target if the distance is greater than the minimum distance
            # if distance > min_distance:
            #     angle = math.atan2(dy, dx)
            #     self.rect.x += self.speed*(math.cos(angle))
            #     self.rect.y += self.speed*(math.sin(angle))

        #Keep the minimum distance from other drones
        # for other_drone in drones:
        #     if other_drone != self:
        #         dx = other_drone.rect.x - self.rect.x
        #         dy = other_drone.rect.y - self.rect.y
        #         distance = math.sqrt(dx**2 + dy**2)
        #         if distance < min_distance:
        #             angle = math.atan2(dy, dx)
        #             self.rect.x -= self.speed*(math.cos(angle) * (min_distance - distance))
        #             self.rect.y -= self.speed*(math.sin(angle) * (min_distance - distance))

        #COLLISION AVOIDACE
        # collision_flag=0
        # for other_drone in drones:
        #     if other_drone != self:
        #         dx = other_drone.rect.x - self.rect.x
        #         dy = other_drone.rect.y - self.rect.y
        #         distance = math.sqrt(dx**2 + dy**2)
        #         if distance < min_distance and self.up==False:
        #             collision_flag=1
        #             other_drone.image=pygame.transform.scale(other_drone.image, (50, 50))
        #             other_drone.up=True
        # if collision_flag==0:
        #     self.image=pygame.transform.scale(self.image, (30, 30))
        #     self.up=False

        #COLLISION DETECTION
        # for other_drone in drones:
        #     if other_drone != self:
        #         dx = other_drone.rect.x - self.rect.x
        #         dy = other_drone.rect.y - self.rect.y
        #         distance = math.sqrt(dx**2 + dy**2)
        #         if distance < 2:
        #             collision_count+=1
        #             other_drone.kill()
        #             print(collision_count)
                    

        




# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DRONE SWARM COMMUNICATION")
clock = pygame.time.Clock()

# Create a list of drones
#drones = [Drone(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for i in range(10)]

# Set the minimum distance between drones
min_distance = 30

# Set the initial target position
target_x = WIDTH/2
target_y = HEIGHT/2

leader_group = pygame.sprite.Group()
drone_group = pygame.sprite.Group()

leaders = [Leader(x=random.randint(0, WIDTH), y=random.randint(0, HEIGHT), image=leader_imgs[i]) for i in range(3)]
drones = [Drone(x=random.randint(0, WIDTH), y=random.randint(0, HEIGHT), image="graphics/drone.png") for i in range(20)]

for leader in leaders:
    leader_group.add(leader)

for drone in drones:
    drone_group.add(drone)

distances=defaultdict(list)

collision_count=0

# Start the main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            for leader in leaders:
                #obj.handle_click(event)
                pos = pygame.mouse.get_pos()
                if leader.rect.collidepoint(pos):
                    # Do something when the sprite is clicked
                    print(leader.rect,"Sprite clicked")
                    # for distance, drone in distances[leader]:
                    #     drone.leader=None
                    distances[leader].clear()
                    for drone in drones:
                        #drone.leader=None
                        dx = drone.rect.x - leader.rect.x
                        dy = drone.rect.y - leader.rect.y
                        distance = math.sqrt(dx**2 + dy**2)
                        distances[leader].append((distance, drone))
                    distances[leader].sort(key=lambda x: x[0])
                    angles=[0, 120, 240]
                    for i, (distance, drone) in enumerate(distances[leader][:3]):
                        drone.leader=leader
                        drone.angle_wrt_leader=angles[i]
                        print(drone, "new leader is", leader)
                        


    #Random Movement of leader object
    leader_group.update()

    
    # Update the drones
    for drone in drones:
        drone.update(min_distance)


    # Clear the screen
    screen.fill((255, 255, 255))

    screen.blit(background, (0, 0))

    # # Draw the target
    # screen.blit(football, (target_x, target_y))

    # # Draw the drones
    for drone in drones:
        screen.blit(drone.image, (drone.rect.x, drone.rect.y))

    leader_group.draw(screen)
    #drone_group.draw(screen)

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()