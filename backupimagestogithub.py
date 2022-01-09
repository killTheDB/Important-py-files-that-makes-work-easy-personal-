from os import listdir, read
from os.path import isfile, join
mypath = "D:\softwares\wallpapers"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)

readmefile = open('README.md', 'a')
readmefile.write("<div class=\"row\" style=\"display: flex\"> \n")
for image in onlyfiles:
    readmefile.write("<div class=\"column\" style=\"flex: 33.33%; padding: 5px\">")
    readmefile.write('\n')
    htmlcode = "<img src=\""+ image + "\" width=\"100%\"> <br>"
    readmefile.write(htmlcode)
    readmefile.write('\n')
    readmefile.write("</div> \n")

readmefile.write("</div>")
readmefile.close()
