file = open("fontsbyrange.txt")
categories = ""# list of categories
#windows_fonts = {}# counts the windows fonts that cover the broadest ranges
i = -1
while i != file.tell():# keep looping while the file index continues to move
    i = file.tell()
    line = file.readline()
    if "U+" in line:
        categories += line
        
#for category in categories:
    #print(category)
file.close()

output = open("categories.txt", mode='w')
output.write(categories)
output.close()
