import pytest

import morpion as ttt

class TestZone:

    def testtrue(self): 
        assert 1

    def test_create_grid(self): #teste si la grille créee est vide
        b = ttt.create_grid()
        print(b)
        assert b == [[" ", " ", " "],
                     [" ", " ", " "],
             [" ", " ", " "]]
