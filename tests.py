import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
    def test_break_entrance_and_exit(self):
        maze = Maze(0, 0, 10, 10, 5, 5)

        maze._create_cells()
        maze._break_entrance_and_exit()

        self.assertFalse(maze._cells[0][0].has_left_wall)
        self.assertFalse(maze._cells[-1][-1].has_right_wall)
       


if __name__ == "__main__":
    unittest.main()
