def get_board_without_params(data):
    l = data.split('/')
    end = l[-1].split(' ', 5)[0]
    l.append(end)
    l.pop(-2)
    return l

def get_params(data):
    l = data.split('/')
    params = l[-1].split(' ', 5)[1:]
    params[0] = params[0].lower()
    params[1] = ''.join(sorted(params[1]))
    return params

def not_capture_or_not_pawn_move(data1, data2):
    d = fen_in_dict(data1)
    not_capture = d[data2[2:4]] is None
    not_pawn = d[data2[:2]] not in ('p','P')
    return not_capture and not_pawn


def get_modern_fen(data1):
    l = get_board_without_params(data1)
    newl = []
    for i in l:
        newi = ''
        for x in i:
            if x.isdigit():
                newsym = int(x)*('1')
                newi = newi + newsym
            else:
                newi = newi + x
        newl.append(newi)
    return newl

def fen_in_dict(data1):
    d = {}
    l = get_modern_fen(data1)
    for i in range(len(l)):
        for x in range(len(l[i])):
            if l[i][x].isdigit():
                d[f'{vertical_dict.get(x)}{8 - i}'] = None
            else:
                d[f'{vertical_dict.get(x)}{8 - i}'] = l[i][x]
    return d

vertical_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

#1743.1.FEN-ASCII
def fen_ascii(data):
    l = get_board_without_params(data)
    print('  +-----------------+')
    for i in range(8):
        s = ''
        for x in l[i]:
            if x.isdigit():
                x = int(x) * '.'
            s = s + x
        s = ' '.join(s)
        print(f'{8-i} | {s} |')
    print('  +-----------------+')
    print('    a b c d e f g h')


#1745.1.Сборка и разборка
def get_good_fen(bad_fen):
    l = get_board_without_params(bad_fen)
    params = get_params(bad_fen)
    new = []
    for i in l:
        if not i.isalpha():
            sum = 0
            s = ''
            for x in i:
                if x.isnumeric():
                    sum = sum + int(x)
                else:
                    if sum:
                        s = s + str(sum)
                        sum = 0
                    s = s + x
            if sum:
                s = s + str(sum)
            if not s:
                s = str(8 - len(i))
            new.append(s)
        else:
            if len(i)<8:
                i = i + str(8 - len(i))
            new.append(i)
    good_fen = '/'.join(new) + ' ' + ' '.join(params)
    return good_fen


#1746.1.Счетчик ходов
def move_count(data):
    l = get_board_without_params(data)
    params = get_params(data)
    if params[0] == 'b':
        params[0] = 'w'
        params[-1] = str(int(params[-1]) + 1)
    else:
        params[0] = 'b'
    l[-1] = l[-1] + ' ' + ' '.join(params)
    return '/'.join(l)

#3694.1.Счетчик полуходов
def half_move_count(data1, data2):
    params = get_params(data1)
    if not_capture_or_not_pawn_move(data1, data2):
        params[3] = str(int(params[3]) + 1)
    else:
        params[3] = '0'
    l = get_board_without_params(data1)
    l[-1] = l[-1] + ' ' + ' '.join(params)
    return '/'.join(l)