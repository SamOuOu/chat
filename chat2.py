def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='UTF-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return(lines)

def convert(lines):
    preson = None
    allen_word = 0
    viki_word = 0
    allen_sicker = 0
    viki_sicker = 0
    allen_img = 0
    viki_img = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖' :
                allen_sicker += 1
            elif s[2] == '圖片':
                allen_img += 1
            else:
                for m in s[2:]:
                    allen_word += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖' :
                viki_sicker += 1
            elif s[2] == '圖片':
                viki_img += 1
            else:
                for m in s[2:]:
                    viki_word += len(m)
    print('allen說了', allen_word, '個字', '傳了', allen_sicker, '個貼圖', '傳了', allen_img, '張圖片')
    print('viki說了', viki_word, '個字', '傳了', viki_sicker, '個貼圖', '傳了', viki_img, '張圖片')

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('-LINE-Viki.txt')
    lines = convert(lines)
    #write_file('out.txt', lines)

main()