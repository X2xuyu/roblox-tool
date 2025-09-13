from PIL import Image
img = Image.open("logo.png").convert("RGBA")
img.save("app.ico", sizes=[(256,256),(128,128),(64,64),(32,32),(16,16)])
print("app.ico generated")