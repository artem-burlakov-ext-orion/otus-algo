import pytest
import os

from chess_funcs import fen_ascii, get_board_without_params, get_params, move_count, get_modern_fen, not_capture_or_not_pawn_move, fen_in_dict, half_move_count, get_good_fen

homedir = os.getcwd()
path = homedir + '/1745.1.Сборка и разборка'
path1 = homedir + '/1746.1.Счётчик ходов'
path2 = homedir + '/3694.1.Счётчик полуходов'
path4 = homedir + '/1743.1.FEN - ASCII'

# def test_fen_ascii():
#     for i in os.listdir(path4):
#         if i.endswith('in'):
#             with open(os.path.join(path4, i)) as filein:
#                 data = filein.readline()
#
#             with open(os.path.join(path4, i.replace('in', 'out'))) as fileout:
#                 data3 = fileout.readlines()
#             assert fen_ascii(data) == data3


def test_from_and_fen_to_fen():
    for i in os.listdir(path):
        if i.endswith('in'):
            with open(os.path.join(path, i)) as filein:
                data = filein.readlines()
                data1 = data[0].strip()
            with open(os.path.join(path, i.replace('in', 'out'))) as fileout:
                data3 = fileout.readline().strip()
            assert get_good_fen(data1) == data3


def test_move_count():
    for i in os.listdir(path1):
        if i.endswith('in'):
            with open(os.path.join(path1, i)) as filein:
                data = filein.readlines()
                data1 = data[0].strip()
            with open(os.path.join(path1, i.replace('in', 'out'))) as fileout:
                data3 = fileout.readline().strip()
            assert move_count(data1) == data3


def test_half_move_count():
    for i in os.listdir(path2):
        if i.endswith('in'):
            with open(os.path.join(path2, i)) as filein:
                data = filein.readlines()
                data1 = data[0].strip()
                data2 = data[1].strip()
            print(i)
            with open(os.path.join(path2, i.replace('in', 'out'))) as fileout:
                data3 = fileout.readline().strip()
            assert half_move_count(move_count(data1), data2) == data3
