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
    import json

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
        for i in range(len(sys.argv)):
            if sys.argv[i] == "show":
                showImage = True
            elif sys.argv[i] == "as_text":
                asText = True
            elif sys.argv[i] == "transparent":
                transparency = True

            argumentParts = sys.argv[i].lower().split('=')
            if argumentParts[0] == "size":
                fontSize = int(argumentParts[1])
            elif argumentParts[0] == "font":
                fontFile = argumentParts[1].split('.')[0]
            elif argumentParts[0] == "path":
                path = argumentParts[1]
                defaultPath = False

        if asText:
            article = sys.argv[1].split('\\n')
        else:
            file = open(sys.argv[1], "rt")
            article = file.read().split('\n')
            file.close()
            if defaultPath:
                path = sys.argv[1].split('.')[0]+".png"

        if fontFile.lower() == "default":
            font = ImageFont.load_default()
        else:
            font = ImageFont.truetype("./fonts/"+fontFile, fontSize)

        if sys.argv[1].split('.')[-1] == "json" and not asText:
            jsonData = {}
            file = open(sys.argv[1], "rt")
            jsonData = json.loads(file.read())
            file.close()

            articles = jsonData["frames"]
            for i in range(len(jsonData["frames"])):
                articles[i] = tti(articles[i].split('\n'), font, fontSize, transparency)

            path = path.split('.')[0] + ".gif"
            articles[0].save(path, save_all=True, append_images=articles[1:], duration=jsonData["interval"], loop = 0)

        else:
            image = tti(article, font, fontSize, transparency)
            image.save(path)

        if showImage:
            os.system("start " + path)
