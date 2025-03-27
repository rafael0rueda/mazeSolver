import time
from cell import *
from window import *

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win # window of the maze
        self._cells = [] # matriz with the cell of the maze
        self._create_cells()
        
    
    def _create_cells(self):
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                cell = Cell(self.win)
                column.append(cell)
            self._cells.append(column)
        
        self._break_entrance_and_exit()
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        xp1 = self.x1 + (i * self.cell_size_x)
        yp1 = self.y1 + (j * self.cell_size_y)
        xp2 = self.x1 + ((i + 1) * self.cell_size_x)
        yp2 = self.y1 + ((j + 1) * self.cell_size_y)
        self._cells[i][j].draw(xp1, yp1, xp2, yp2)
        self._animate()
    
    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        # allways let the star and finish of the maze in the same cell
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False

