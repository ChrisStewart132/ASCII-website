'''
script to read from a text file (fontsbyrange.txt) containing unicode ranges and font info
https://www.alanwood.net/unicode/fontsbyrange.html
''' 

file = open("fontsbyrange.txt")
categories = ""
category_navigation_html = ""# html for all category navigation buttons on the tools page
font_map = {}# category(str)->fonts(list)
range_to_font = {}# range(int,int)->fonts(list)
index_to_category = {}# start/end->category, used to render symbol blocks marking the start and end of a category
start_to_end = {}

i = -1
while i != file.tell():# keep looping while the file index continues to move
    i = file.tell()# .tell == current file index
    line = file.readline()
    if "U+" in line:# category lines
        categories += line
        category = line
        # navigation button html generation
        try:
            s, e = category.split("(")[-1].split("-")
            e = e.replace(")", "")
            e = e.rstrip()
            title = category.split("U+")[0].strip()
            category_navigation_html += f'<div class="symbolBlockHidden" title="{title}" style="width:226px;" onclick="loadPageRange({s}, {e})"><p class="symbolCode">{s}-{e}</p><p class="btn">{title}</p></div>'
            index_to_category[s] = title
            index_to_category[e] = title
            start_to_end[s] = e
        except:
            print(category)
        t = line.split("U+")
        start, end = "0x" + t[-2].split()[0], "0x" + t[-1].split()[0]
        
    elif "Windows" in line:# windows fonts under category
        fonts = line.split(":")[-1].strip().split(", ")
        font_map[category] = fonts
        range_to_font[start+","+end] = fonts
        
file.close()
print(range_to_font)
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

output = open("index_to_category.txt", mode="w")
output.write(str(index_to_category))
output.close()

output = open("start_to_end.txt", mode="w")
output.write(str(start_to_end))
output.close()

fonts = {}# map of font_name -> number of ranges compatible with
for key in range_to_font.keys():
    for font in range_to_font[key]:
        fonts[font] = fonts[font] + 1 if font in fonts else 1
sorted_fonts = sorted(fonts.items(), key=lambda item: item[1], reverse=True)
top_10_fonts = sorted_fonts[:10]
#print("top 10 fonts:", top_10_fonts)  
