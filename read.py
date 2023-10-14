'''
script to read from a text file (fontsbyrange.txt) containing unicode ranges and font info
https://www.alanwood.net/unicode/fontsbyrange.html
''' 

file = open("fontsbyrange.txt")
categories = ""
font_map = {}# category(str)->fonts(list)
range_to_font = {}# range(int,int)->fonts(list)
i = -1
while i != file.tell():# keep looping while the file index continues to move
    i = file.tell()
    line = file.readline()
    if "U+" in line:
        categories += line
        category = line
        t = line.split('U+')
        start, end = '0x' + t[-2].split()[0], '0x' + t[-1].split()[0]
    elif "Windows" in line:
        fonts = line.split(":")[-1].split()
        font_map[category] = fonts
        range_to_font[(start, end)] = fonts
file.close()

output = open("categories.txt", mode='w')
output.write(categories)
output.close()

output = open("font_map.txt", mode='w')
output.write(str(font_map))
output.close()

output = open("range_to_font.txt", mode='w')
output.write(str(range_to_font))
output.close()
