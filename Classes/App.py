import pygame

from random import randint
from time import sleep
from tkinter import Tk, Label, Button, GROOVE, CENTER
from pygame.locals import K_RIGHT, K_LEFT, K_DOWN, K_UP, K_ESCAPE

from Classes.Apple import Apple
from Classes.Game import Game
from Classes.Player import Player


TIME_TO_SLEEP = 50 / 1000
CELL_SIZE = 44
START_SIZE = 3
START_POS_APPLE = [5, 5]

IMAGE_CELL = 'static/smile.png'
IMAGE_APPLE = 'static/apple.png'


class App(object):

    window_width = 800      # the width of the game field
    window_height = 600     # the height of the game filed
    player = 0
    apple = 0

    def __init__(self):
        """init the game"""
        self.running = True         # the snake can move

        self.game = Game()
        self.player = Player(START_SIZE, CELL_SIZE)
        self.apple = Apple(START_POS_APPLE[0], START_POS_APPLE[1], CELL_SIZE)

        pygame.init()
        self._display_surf = pygame.display.set_mode((self.window_width, self.window_height), pygame.HWSURFACE)
        self.image_surf = pygame.image.load(IMAGE_CELL).convert()
        self.apple_surf = pygame.image.load(IMAGE_APPLE).convert()

        pygame.display.set_caption("Snake")     # the caption of the game

    def on_loop(self):
        """
        check the collisions in the game;
        check the snake has eaten an apple:
            create new apple;
            add new cell to the snake's body;
        check the snake is out of the game field.
        """
        self.player.update()

        # check if the are collisions between the head and the body of the snake
        for i in range(1, self.player.length):
            if self.game.is_collision(self.player.x[i], self.player.y[i], self.player.x[0], self.player.y[0]):
                self.running = False

        # check if the snake has eaten an apple
        if self.game.is_collision(self.apple.x, self.apple.y, self.player.x[0], self.player.y[0]):

            # create new apple
            appl_appeared = False
            while not appl_appeared:

                appl_appeared = True
                self.apple.x = randint(0, 17) * CELL_SIZE
                self.apple.y = randint(0, 12) * CELL_SIZE

                # check the apple has not been appeared in the snake
                for i in range(self.player.length):
                    if self.game.is_collision(self.apple.x, self.apple.y, self.player.x[i], self.player.y[i]):
                        appl_appeared = False
                        break

            # add new cell to the snake's body
            self.player.length += 1
            self.player.x.append(self.player.x[self.player.length - 2])
            self.player.y.append(self.player.y[self.player.length - 2])

        # check the snake is out of the game field
        if self.game.is_out(self.player.x[0], self.player.y[0], self.window_width, self.window_height):
            self.running = False

    def on_render(self):
        """
        draw the surface, the snake and an apple
        """
        self._display_surf.fill((0, 0, 0))
        self.apple.draw(self._display_surf, self.apple_surf)
        self.player.draw(self._display_surf, self.image_surf)

        pygame.display.flip()

    def on_cleanup(self):
        """
        call the Tkinter widget when it is the player has lost the game.
        """

        def exit_(event):
            """
            destroy everything and exit the application.

            :param event: to call the function by some event (clicking on the button.
            """
            pygame.quit()
            root.destroy()

        root = Tk()
        root["bg"] = "#262626"

        label = Label(root, anchor=CENTER, height=3, width=50, relief=GROOVE, font="Calibri 14", bg="#E31E00",
                      fg="black")

        label["text"] = 'You lose!!!\nYou have received the {} level.\nCongratulations!!!'.format(self.game.level)
        button = Button(root, bg="black", activebackground="#E6E6E6", fg="white", relief=GROOVE, text="Exit", width=10)

        label.grid(row=0, column=0, columnspan=3)
        button.grid(row=1, column=2)

        button.bind("<Button-1>", exit_)
        root.mainloop()

    def on_execute(self):
        """
        to check the movement of the snake;
        to move it.
        """
        while self.running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if keys[K_RIGHT]:
                self.player.move_right()
            if keys[K_LEFT]:
                self.player.move_left()
            if keys[K_UP]:
                self.player.move_up()
            if keys[K_DOWN]:
                self.player.move_down()
            if keys[K_ESCAPE]:
                self.running = False

            self.on_loop()
            self.on_render()

            sleep(TIME_TO_SLEEP)

        self.on_cleanup()
