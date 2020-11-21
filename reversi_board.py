import pygame
from board import Board

class ReversiBoard(Board):
    """
    Status
    ------
        -1: dark side
        0: no piece
        1: light side
        2: translucent(for available block)
    """
    DARK = (0, 0, 0)
    LIGHT = (255, 255, 255)
    TRANSLUCENT = (153, 184, 147)
    def __init__(self, side_length=600, top_left=(0, 0), dark=DARK, light=LIGHT, translucent=TRANSLUCENT):
        rows = ['1', '2', '3', '4', '5', '6', '7', '8']
        cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        super().__init__(side_length, top_left, rows, cols)

        self.status2color = {
            -1: dark,
            1: light,
            2: translucent
        }

    def draw_pieces(self, screen):
        for key in self.status:
            if self.status[key] == 0:
                continue
            else:
                n_row = key // len(self.rows)
                n_col = key % len(self.rows)
                position = (0.1 * self.side_length + 0.8 * (n_col + 0.5) / len(self.cols) * self.side_length,
                            0.1 * self.side_length + 0.8 * (n_row + 0.5) / len(self.rows) * self.side_length)
                pygame.draw.circle(screen, self.status2color[self.status[key]], position, 0.35 * self.block_size)
