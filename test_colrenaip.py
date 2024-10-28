# test_colrenaip.py
import io
import sys
from colrenaip import print_colored

def test_red_color(capfd):
    print_colored("red.test")
    captured = capfd.readouterr()
    assert captured.out == "\033[31mtest\033[0m\n"

def test_invalid_format(capfd):
    print_colored("invalid_format")
    captured = capfd.readouterr()
    assert captured.out == "Invalid format. Use 'color.text'.\n"
