# adding image and music
import pygame
import random
import  os

pygame.mixer.init()

pygame.init()

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(20, 124,14)
grey=(240, 124, 14)
blue=(20, 14,124)
light_green=(97 ,219, 97)
screen_with=800
screen_height=600
gameWindow=pygame.display.set_mode((screen_with,screen_height))

#add background image
backgroung_img=pygame.image.load("bg.jpg")
backgroung_img=pygame.transform.scale(backgroung_img,(screen_with,screen_height)).convert_alpha()

b_img=pygame.image.load("end.png")
b_img=pygame.transform.scale(b_img,(screen_with,screen_height)).convert_alpha()


#set title in game
pygame.display.set_caption("Snake game by Munawar ")
pygame.display.update()


#for updating game
clock=pygame.time.Clock()

#for displaying time in screen
font=pygame.font.SysFont(None,52)
def dispaly_score(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,(x,y))

#define the plot snake function
def plot_snake(gameWindow,color,snake_list,snake_size):
       for x,y in snake_list:
         pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

#define well come screen
def Wellcome_screen():
    exit_game=False
    while not exit_game:
        gameWindow.fill(light_green)
        dispaly_score("Wellcome to Snake Game by Munawar",grey,100,220)
        dispaly_score("Press Enter key to play", blue, 245, 290)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    #For background music
                    pygame.mixer.music.load("bg.mp3")
                    pygame.mixer.music.play()

                    GameLoop()
        pygame.display.update()
        clock.tick(45)

#while loop is started

def GameLoop():
    # define sanke list and sanke list
    snake_list = []
    snake_length = 1
    #game variables
    snake_x=45
    snake_y=55
    velocity_x=0
    velocity_y=0
    start_velocity=5
    snake_size=15
    exit_game=False
    game_over=False
    score=0
    fps=45   #fps means frame per second
    food_x = random.randint(20, screen_with / 2)  # random.randint() is a function that generate a number
    food_y = random.randint(20, screen_height / 2)

    #add hiscore
    with open("score.txt","r") as f:
        hiscore = f.read()

    while not exit_game:
        #adding hiscore in txt file
        with open("score.txt","w") as f:
            f.write(str(hiscore))
        #after game screen is white
        if game_over:
            gameWindow.fill(white)
            dispaly_score("Game is Over Press Enter to Continued ",blue,35,16)
            # after game screen is white

            if game_over:
                gameWindow.fill(black)
                dispaly_score("Game is Over! ", blue, 255, 220)
                dispaly_score(" Press Space bar to Continued ", green, 120, 270)
                for event in pygame.event.get():
                    #       print(event)
                    if event.type == pygame.QUIT:
                        exit_game = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                        #playing the game is intro
                         Wellcome_screen()
                        #if we ran GameLoop funtion the well screen is not display after enter key
                         # GameLoop()
        else:
            for event in pygame.event.get():
        #       print(event)
               if event.type==pygame.QUIT:
                   exit_game=True
           # handle the keys
               if event.type==pygame.KEYDOWN:
                   if event.key==pygame.K_RIGHT:
                       velocity_x=start_velocity
                       velocity_y=0

                   if event.key == pygame.K_LEFT:
                       velocity_x=-start_velocity
                       velocity_y=0

                   if event.key == pygame.K_UP:
                       velocity_y=-start_velocity
                       velocity_x=0

                   if event.key == pygame.K_DOWN:
                      velocity_y=start_velocity
                      velocity_x=0

                  #adding cheat code if press c button then score increase in 30
                   # if event.type==pygame.K_c:
                   #  score=score+30




            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y
        #abs is a function that gove absolute value
            #
            if abs(snake_x-food_x)<5 and abs(snake_y-food_y)<5:
             score=score+5
             pygame.mixer.music.load("food.mp3")
             pygame.mixer.music.play()
          #   print("Your Score :",score*5) #for printing the score in console

               #for generating random food in screen
             food_x = random.randint(20, screen_with /2)  # random.randint() is a function that generate a number
             food_y = random.randint(20, screen_height /2)
             snake_length=snake_length+5

            gameWindow.fill(white)
            # blit image
            gameWindow.blit(backgroung_img, (0, 0))
          #  print(hiscore)
            if score>int(hiscore):
                hiscore=score

            #printing the score in in window screen
            dispaly_score("Your Score:" + str(score) +" Hiscore is: "+str(hiscore), black, 300, 10)

           #appednding head of snake
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            #cutting the head when increasing length
            if len(snake_list)>snake_length:
                del snake_list[0]
            #if snake colide with sanke then game over
            if head in snake_list[:-1]:
                game_over=True

                #add game  over music
            # pygame.mixer.music.load("gameover.mp3")
            # pygame.mixer.music.play()

            #For game over function
            if snake_x<0 or snake_x > screen_with or snake_y<0 or snake_y>screen_height:
             game_over=True

            # pygame.mixer.music.load("gameover.mp3")
            # pygame.mixer.music.play()

            # print("Game is Over")


                #checked the snake list in console
        #print(snake_list)
             #draw the food in window
            pygame.draw.rect(gameWindow, blue, (food_x, food_y, snake_size, snake_size))
            #draw the snake shap in screen
           # pygame.draw.rect(gameWindow,red,(snake_x,snake_y,snake_size,snake_size))

           #ploding the snake in screen
            plot_snake(gameWindow,red,snake_list,snake_size)
            #This is require for change in window fill the window with white color
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
Wellcome_screen()
GameLoop()
