import pygame
from datetime import date
import time
import random
from button import Button
from door import Door
from safe import Safe
from key import Key
from correctkey import CorrectKey

black = pygame.image.load("BIG BLACK RECT.png")
black_x = -1000
black_y = 0

correct_key = CorrectKey(-300,-300)
key1 = Key(-300,-300)
key2 = Key(-300,-300)
key3 = Key(-300,-300)
key4 = Key(-300,-300)
key5 = Key(-300,-300)
key6 = Key(-300,-300)
key7 = Key(-300,-300)
key8 = Key(-300,-300)


coord_list = [(58,135), (203,135), (337,135), (58,360), (203,360), (337,360), (58,600), (203, 600), (337,600)]
key_list = ['key1', 'key2', 'key3','key4','key5','key6','key7','key8','correct_key']
show_keys = False
def arrange_keys():
    random.shuffle(key_list)
    count = 0
    for x in key_list:
        if x == 'correct_key':
            break
        else:
            count+=1

    correct_key_coord = coord_list[count]
    correct_key.move(correct_key_coord[0],correct_key_coord[1])

    count = 0
    for x in key_list:
        if x == 'key1':
            break
        else:
            count+=1
    key1_coord = coord_list[count]
    key1.move(key1_coord[0], key1_coord[1])

    count = 0
    for x in key_list:
        if x == 'key2':
            break
        else:
            count += 1
    key2_coord = coord_list[count]
    key2.move(key2_coord[0], key2_coord[1])

    count = 0
    for x in key_list:
        if x == 'key3':
            break
        else:
            count += 1
    key3_coord = coord_list[count]
    key3.move(key3_coord[0], key3_coord[1])

    count = 0
    for x in key_list:
        if x == 'key4':
            break
        else:
            count += 1
    key4_coord = coord_list[count]
    key4.move(key4_coord[0], key4_coord[1])

    count = 0
    for x in key_list:
        if x == 'key5':
            break
        else:
            count += 1
    key5_coord = coord_list[count]
    key5.move(key5_coord[0] , key5_coord[1])

    count = 0
    for x in key_list:
        if x == 'key6':
            break
        else:
            count += 1
    key6_coord = coord_list[count]
    key6.move(key6_coord[0],key6_coord[1])

    count = 0
    for x in key_list:
        if x == 'key7':
            break
        else:
            count += 1
    key7_coord = coord_list[count]
    key7.move(key7_coord[0],key7_coord[1])

    count = 0
    for x in key_list:
        if x == 'key8':
            break
        else:
            count += 1
    key8_coord = coord_list[count]
    key8.move(key8_coord[0],key8_coord[1])

# set up pygame modules
pygame.init()
pygame.font.init()
pygame.mixer.init()
explosion_sound = pygame.mixer.Sound('explosion.mp3')
title_screen = pygame.image.load("title screen.png")
my_font = pygame.font.SysFont('Times New Roman', 50)
other_font = pygame.font.SysFont('Arial', 20)
pygame.display.set_caption("DON'T PRESS THE BUTTON")
size = (1000, 800)
screen = pygame.display.set_mode(size)
bg = pygame.image.load("background.png")
run = True
button = Button(440, 400)
d = Door(70,195, 'door.png')
backdoor = Door(70,195,'green rect.png')
explosion = pygame.image.load("explosion.png")
exposition = pygame.image.load("exposition_screen.png")
r = 245
g = 240
b = 240
button_pressed = 0
display_button_pressed = my_font.render(str(button_pressed), True, (0,0,0))
start_time = time.time()
timer_run = False
this = 0
secret_ending = False
display_instruct = other_font.render(" ", True, (0,0,0))
instruct = True
that = 0
slide_in = False
start = False
display_timer = my_font.render(' ', True, (0, 0, 0))
display_counter = my_font.render(' ', True, (0,0,0))
display_this = my_font.render('Click to start', True, (0,0,0))
timer = 0
display_achievement = other_font.render(' ', True, (0,0,0))
insert = True
safe = Safe(-300,-300)
safe_open = False
wrong_key = 0
explode = False
pre_start = False
set_time = False
set_time2 = True
# -------- Main Program Loop -----------
while run:
   if start == True and timer_run == True:
       current_time = time.time()
       secs = current_time - start_time
       timer = 40 - round(secs)
       if timer <= 0:
           display_timer = my_font.render(' ', True, (0, 0, 0))
           timer_run = False
       else:
           if black_x >= 0:
               display_timer = my_font.render(' ', True, (0,0,0))
           else:
                display_timer = my_font.render(str(timer), True, (0, 0, 0))

   # --- Main event loop
   for event in pygame.event.get():  # User did something

      # position = pygame.mouse.get_pos() #temporary code to get mouse coordinates
       #mouse_x = position[0] - 40
       #mouse_y = position[1] - 20
       #mouse_pos = other_font.render(str(position), True, (0,0,0))

       if event.type == pygame.QUIT:  # If user clicked close
           run = False
       if event.type == pygame.MOUSEBUTTONUP:
           if pre_start == True:
                start = True
                timer_run = True
                if set_time2 == True:
                   set_time = True
                   set_time2 = False


           pre_start = True
           if button.rect.collidepoint(event.pos):
             if timer_run == True:
                 if button.image_num == 0:
                    button.button_pressed()
                 elif button.image_num == 1:
                    button.button_unpressed()
                    button_pressed +=1
             display_button_pressed = my_font.render(str(button_pressed), True, (0, 0, 0))

           if backdoor.rect.collidepoint(event.pos):
             if secret_ending == True:
                 slide_in = True

           if safe.rect.collidepoint(event.pos):
               if safe_open == True:
                   print('YOU ESCAPED')
                   f = open('achievements', 'r')
                   data = f.readlines()
                   for x in data:
                       if x == "you escaped":
                           achieved = True
                   if achieved == False:
                       f = open("achievements", "a")
                       f.write("you escaped")


           if correct_key.rect.collidepoint(event.pos):
               safe.safe_open()
               safe_open = True
               correct_key.move(-300,-300)

           if key1.rect.collidepoint(event.pos):
               key1.move(-300,-300)
               wrong_key += 1
               display_counter = my_font.render(str(wrong_key), True, (255, 0, 0))

           if key2.rect.collidepoint(event.pos):
               key2.move(-300,-300)
               wrong_key+=1
               display_counter = my_font.render(str(wrong_key), True, (255, 0, 0))

           if key3.rect.collidepoint(event.pos):
               key3.move(-300,-300)
               wrong_key+=1
               display_counter = my_font.render(str(wrong_key), True, (255, 0, 0))

           if key4.rect.collidepoint(event.pos):
               key4.move(-300,-300)
               wrong_key+=1
               display_counter = my_font.render(str(wrong_key), True, (255, 0, 0))

           if key5.rect.collidepoint(event.pos):
               key5.move(-300,-300)
               wrong_key+=1
               display_counter = my_font.render(str(wrong_key), True, (255, 0, 0))

           if key6.rect.collidepoint(event.pos):
               key6.move(-300,-300)
               wrong_key+=1
               display_counter = my_font.render(str(wrong_key), True, (255, 0, 0))

           if key7.rect.collidepoint(event.pos):
               key7.move(-300,-300)
               wrong_key+=1
               display_counter = my_font.render(str(wrong_key), True, (255, 0, 0))

           if key8.rect.collidepoint(event.pos):
               key8.move(-300,-300)
               wrong_key+=1
               display_counter = my_font.render(str(wrong_key), True, (255, 0, 0))

   if set_time == True:
       start_time = time.time()
       set_time = False
   if start == True:
       if black_x == 0:
           d.move_left(1000)
           backdoor.move_left(1000)
           button.move(-300, -100)
           bg = pygame.image.load("minigame-bg.png")
           instruct = False
           display_instruct = other_font.render(" ", True, (0, 0, 0))
           display_button_pressed = my_font.render(' ', True, (0, 0, 0))
           display_timer = my_font.render(' ', True, (0, 0, 0))
           safe.move(650,450)
           arrange_keys()
       if black_x >= 0 and safe_open == False:
           display_achievement = other_font.render(' ', True, (0,0,0))
       if slide_in == True:
           if that <= 2000:
               black_x += 5
           else:
               slide_in = False

       if timer_run == False and button_pressed == 0 and button.image_num == 1:
           button_pressed += 1
           button.button_unpressed()
           display_button_pressed = my_font.render(str(button_pressed), True, (0, 0, 0))

       if timer == 20 and button_pressed == 38: #secret ending
           secret_ending = True

       if secret_ending == True:
           if wrong_key == 3:
               print('EXPLOSION')
               explode = True
               f = open('achievements', 'r')
               data = f.readlines()
               for x in data:
                   if x == "you exploded":
                       achieved = True
               if achieved == False:
                   f = open("achievements", "a")
                   f.write("you exploded")

       if secret_ending == True:
           achieved = False
           if this <= 50:
               d.move_left(5)
               this += 1

           if this >= 50 and instruct == True:
               display_instruct = other_font.render("Click here ^", True, (0,0,0))

           f = open('achievements', 'r')
           data = f.readlines()
           for x in data:
               if x == "door opened":
                   achieved = True
           if achieved == False:
               f = open("achievements", "a")
               if insert == True:
                   f.write("door opened")
                   insert = False
               if black_x >= 0:
                   display_achievement = other_font.render(' ', True, (0,0,0))
               else:
                   display_achievement = other_font.render("You opened the door", True, (0,0,0))

       if timer_run == False and secret_ending == False:
           achieved = False
           if button_pressed == 0:
               #good ending
               f = open('achievements' , 'r')
               data = f.readlines()
               for x in data:
                   if x == "good ending":
                       achieved = True
               if achieved == False:
                   f = open("achievements", "a")
                   f.write("good ending")
                   display_achievement = other_font.render("you unlocked the Good Ending", True, (0, 0, 0))


           else:
               #bad ending
               f = open('achievements' , 'r')
               data = f.readlines()
               for x in data:
                   if x == "bad ending":
                       achieved = True
               if achieved == False:
                   f = open("achievements", "a")
                   f.write("bad ending")
                   display_achievement = other_font.render("you unlocked the Bad Ending", True, (0, 0, 0))

   screen.fill((r,g,b))
   screen.blit(bg, (0,0))
   screen.blit(button.image, button.rect)
   screen.blit(display_button_pressed, (500,0))
   screen.blit(display_timer, (0,0))
   screen.blit(backdoor.image, backdoor.rect)
   screen.blit(display_instruct, (70,630))
   screen.blit(d.image, d.rect)
   screen.blit(display_achievement, (0, 700))
   screen.blit(safe.image, safe.rect)
   #screen.blit(mouse_pos, (mouse_x, mouse_y))
   if pre_start == False:
        screen.blit(title_screen, (150,200))
        screen.blit(display_this, (150,400))
   screen.blit(correct_key.image, correct_key.rect)
   screen.blit(key1.image,key1.rect)
   screen.blit(key2.image,key2.rect)
   screen.blit(key3.image,key3.rect)
   screen.blit(key4.image,key4.rect)
   screen.blit(key5.image,key5.rect)
   screen.blit(key6.image,key6.rect)
   screen.blit(key7.image,key7.rect)
   screen.blit(key8.image,key8.rect)
   if explode == True:
       screen.blit(explosion, (0,0))
       pygame.mixer.Sound.play(explosion_sound)
   screen.blit(black, (black_x, black_y))
   screen.blit(display_counter, (900,0))
   if start == False and pre_start == True:
       screen.blit(exposition, (200,200))
   pygame.display.update()


