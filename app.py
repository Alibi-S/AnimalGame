import pygame
import game_config as gc

from pygame import display, event, image
from animal import Animal
from time import sleep

def find_index(x, y): #нахождение по координатам индекса позиции, чтоб через индекс найти картинку
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    # print(row, " = ", y)
    # print(col, " = ", x)
    index = row * gc.NUM_TILES_SIDE + col
    return index

pygame.init()

display.set_caption('Game') # text on the top op the program / name of program
screen = display.set_mode((512, 512)) # size of program window

matched = image.load("other_assets/matched.png") # just image
# screen.blit(matched, (0, 0))
# display.flip()

running = True

tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)] # Добавление всех животных

# for i in range(0, gc.NUM_TILES_TOTAL):
#     print(tiles[i].name)

current_images = []

while running:
    current_events = event.get()

    for e in current_events:
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            index = find_index(mouse_x, mouse_y)
            # print(index) # position from 1 to 15
            if index not in current_images:
                current_images.append(index)
            if len(current_images) > 2:
                current_images = current_images[1:]
                # Если больше двух картинок то мы просто
                # сохраняем два последних, то есть в текущий
                # #момент открыты могут быть только две картики


    screen.fill((255, 255, 255)) #background

    total_skipped = 0

    for i , tile in enumerate(tiles):
        image_i = tile.image if tile.index in current_images else tile.box
        if not tile.skip:#выводим только скип-фолс, не найденные
            screen.blit(image_i, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
        else:
            total_skipped +=1
    if len(current_images) == 2:
        idx1, idx2 = current_images
        if (tiles[idx1].name == tiles[idx2].name):#& (tiles[idx1].index != tiles[idx2].index):
            sleep(0.4)  # time library - замедлить удаление чтоб увидеть

            tiles[idx1].skip = True
            tiles[idx2].skip = True
            # skipaem krch esli  в настоящий момент открыты два одинаковых, из-за скипа они не выводятся на экран

            screen.blit(matched, (0, 0))
            display.flip()
            sleep(0.4)

            current_images = []

    if total_skipped == len(tiles):
        running = False

    display.flip()


print('Goodbye!')
raise SystemExit
