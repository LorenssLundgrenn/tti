A simple program that converts plain text into an image
this program was made to easily display large ascii art that does not fit in a regular text editor

run the program from the command line:
required: 
    first argument has to specify the data to work with, this arg will be treated as a file path by default
    if first argument is equal to "fonts", a list of available fonts will be displayed and program will end
optional (no specific arg order beyond first arg):
    as_text - treats arg1 as plain text data instead of a file path, \n character is supported
    show - opens image after program process
    size=<int> - set font size
    font=<string> - set font
    path=<string> - set output image path