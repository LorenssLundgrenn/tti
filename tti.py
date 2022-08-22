from PIL import Image, ImageFont, ImageDraw

def tti(article, font, fontSize, transparency=False):
    textHeight = font.getsize(article[0])[1]
    articleHeight = len(article) * textHeight
    articleWidth = 0
    for text in article:
        textWidth = font.getsize(text)[0]
        if textWidth > articleWidth:
            articleWidth = textWidth

    image = Image.new("RGB" if not transparency else "RGBA", (articleWidth, articleHeight))
    draw = ImageDraw.Draw(image)

    for i in range(len(article)):
        draw.text((0,textHeight * i), article[i], font=font, color=(255,255,255))

    return image

if __name__ == "__main__":
    import sys
    import os

    if sys.argv[1] == "fonts":
        print(os.listdir("./fonts"))
    else:
        showImage = False
        asText = False
        transparency = False
        fontSize = 14
        fontFile = "CONSOLA.TTF"
        path = "tti.png"
        defaultPath = True
        for argument in sys.argv:
            if argument == "show":
                showImage = True
            elif argument == "as_text":
                asText = True
            elif argument == "transparent":
                transparency = True

            argumentParts = argument.lower().split('=')
            if argumentParts[0] == "size":
                fontSize = int(argumentParts[1])
            elif argumentParts[0] == "font":
                fontFile = argumentParts[1].split('.')[0]
            elif argumentParts[0] == "path":
                path = argumentParts[1]
                defaultPath = False

        if not asText:
            file = open(sys.argv[1], "rt")
            article = file.read().split('\n')
            file.close()
            if defaultPath:
                path = sys.argv[1].split('.')[0]+".png"
        else:
            article = sys.argv[1].split('\\n')

        if fontFile.lower() == "default":
            font = ImageFont.load_default()
        else:
            font = ImageFont.truetype("./fonts/"+fontFile, fontSize)

        image = tti(article, font, fontSize, transparency)
        image.save(path)
        if showImage:
            image.show()
