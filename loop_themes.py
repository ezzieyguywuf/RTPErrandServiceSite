import os
from shutil import move

base = '/home/wolfie/Program/pelican-themes'
old = os.path.join(os.getcwd(), 'pelicanconf.py')
temp = os.path.join(os.getcwd(), 'temp_conf.py')
for fname in os.listdir(base):
    with open(old, 'r') as infile:
        with open(temp, 'w') as outfile:
            for line in infile:
                if not line[:5] == 'THEME':
                    outfile.write(line)
                else:
                    theme = os.path.join(base, fname)
                    outfile.write("THEME = '{}'\n".format(theme))
    os.remove(old)
    move(temp, old)
    os.system('pelican content')
    print("Current theme = {}".format(fname))
    input()
