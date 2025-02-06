import pygame.display
import pygame.mouse
import serial
import time
import pygame
import base64
import io
#keyboard = Controller()
ser = serial.Serial('COM4', 9600)  # Replace 'COM3' with your Arduino port
#time.sleep(2)  # Wait for the serial connection to establish
# Define the background colour 
# using RGB color coding. 
def position_in_grid(x, y, size=700):
    center = size // 2  # Center coordinate (350, 350)
    margin = 50  # Define center area size (adjustable)

    # Check if the point is in the center region
    if center - margin <= x <= center + margin and center - margin <= y <= center + margin:
        return "Middle"
    
    # Cardinal directions
    elif x < center - margin and center - margin <= y <= center + margin:
        return "Left"
    elif x > center + margin and center - margin <= y <= center + margin:
        return "Right"
    elif y < center - margin and center - margin <= x <= center + margin:
        return "Up"
    elif y > center + margin and center - margin <= x <= center + margin:
        return "Down"

    # Diagonal directions
    elif x < center and y < center:
        return "Top-Left"
    elif x > center and y < center:
        return "Top-Right"
    elif x < center and y > center:
        return "Bottom-Left"
    elif x > center and y > center:
        return "Bottom-Right"
pygame.init()
background_colour = (255, 255, 255) 

# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((700, 700)) 

# Set the caption of the screen 
pygame.display.set_caption('Joystick Tester') 
icon = pygame.image.load("C:\\Users\\logan\\Documents\\kanye.png")
pygame.display.set_icon(icon)
# Fill the background colour to the screen 
screen.fill(background_colour) 
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set background color
screen.fill(WHITE)

# Draw a dot (small circle) at (250, 200)
dot_radius = 3  # Small radius to make it look like a dot
# Update the display using flip 
pygame.display.flip() 

MOVE_DOT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_DOT, 100)  # 1000 ms = 1 second

# Variable to keep our game loop running 
running = True

# game loop 
while running: 
    #line = f"X: {pygame.mouse.get_pos()[0]} Y: {pygame.mouse.get_pos()[1]}"
    line = ser.readline().decode('utf-8').rstrip()
    #print(line)
    Xval = int(line.split(": ")[1].split(" ")[0])
    Yval = int(line.split("Y: ")[1])
    #position = position_in_grid(Xval, Yval)
    #print(line)
    for event in pygame.event.get(): 
        screen.fill(WHITE)  
        print(' X: '+ str(Xval) + ' Y: ' + str(Yval))
        #font = pygame.font.Font('freesansbold.ttf', 32)
        #text = font.render(position_in_grid(Xval, Yval), True, (0, 0, 0), (255, 255, 255))
        #textRect = text.get_rect()
        #textRect.center = (350, 50)
        #screen.blit(text, textRect)
        #text2 = font.render(' X: '+ str(Xval) + ' Y: ' + str(Yval), True, (0, 0, 0), (255, 255, 255))
        #textRect2 = text.get_rect()
        #textRect2.center = (350, 100)
        #screen.blit(text2, textRect2)
        dot_position = ((700 - Xval), Yval)  # (x, y)
        pygame.draw.circle(screen, RED, dot_position, dot_radius) 
        pygame.display.flip()
        if event.type == pygame.QUIT: 
            running = False
