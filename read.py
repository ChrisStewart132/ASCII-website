'''
script to read from a text file (fontsbyrange.txt) containing unicode ranges and font info
https://www.alanwood.net/unicode/fontsbyrange.html
''' 

file = open("fontsbyrange.txt")
categories = ""
category_navigation_html = ""
font_map = {}# category(str)->fonts(list)
range_to_font = {}# range(int,int)->fonts(list)
i = -1
while i != file.tell():# keep looping while the file index continues to move
    i = file.tell()
    line = file.readline()
    if "U+" in line:
        categories += line
        category = line
        # navigation button html generation
        try:
            s, e = category.split("(")[-1].split("-")
            title = category.split("U+")[0].strip()
            category_navigation_html += f'<div class="symbolBlock" style="width:226px;" onclick="loadPageRange({s}, {e}"><p class="btn">{title}</p></div>'
        except:
            print(category)
        t = line.split("U+")
        start, end = "0x" + t[-2].split()[0], "0x" + t[-1].split()[0]
    elif "Windows" in line:
        fonts = line.split(":")[-1].strip().split(", ")
        font_map[category] = fonts
        range_to_font[start+","+end] = fonts
file.close()

output = open("categories.txt", mode="w")
output.write(categories)
output.close()

output = open("font_map.txt", mode="w")
output.write(str(font_map))
output.close()

output = open("range_to_font.txt", mode="w")
output.write(str(range_to_font))
output.close()

output = open("category_navigation_html.txt", mode="w")
output.write(category_navigation_html)
output.close()

fonts = {}# map of font_name -> number of ranges compatible with
for key in range_to_font.keys():
    for font in range_to_font[key]:
        fonts[font] = fonts[font] + 1 if font in fonts else 1
sorted_fonts = sorted(fonts.items(), key=lambda item: item[1], reverse=True)
top_10_fonts = sorted_fonts[:10]
#print("top 10 fonts:", top_10_fonts)  
