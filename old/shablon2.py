from PIL import Image, ImageDraw, ImageFont

# texts = input().split()
texts = "шаблон 123456789 2123456789 3123456789 4123456789 5123456789 6123456789 7123456789".split()
shablon, \
text_one, \
text_two, \
text_three, \
text_four, \
text_five, \
text_six, \
text_seven = texts

im = Image.open('shablon6_ref.jpg')

print(im.width, "ширина", im.height, 'высота')

font = ImageFont.truetype('Intro Regular.ttf', size=100)
font_2 = ImageFont.truetype('Intro Regular.ttf', size=40)

draw_text = ImageDraw.Draw(im)

draw_text.text((35, 30), shablon, font=font, fill=(102, 102, 102))
draw_text.text((250, 365), text_one, font=font_2, fill=(102, 102, 102))
draw_text.text((685, 365), text_two, font=font_2, fill=(102, 102, 102))
draw_text.text((460, 740), text_three, font=font_2, fill=(102, 102, 102))
draw_text.text((320, 600), text_four, font=font_2, fill=(102, 102, 102))
draw_text.text((460, 330), text_five, font=font_2, fill=(102, 102, 102))
draw_text.text((600, 600), text_six, font=font_2, fill=(102, 102, 102))
draw_text.text((460, 500), text_seven, font=font_2, fill=(102, 102, 102))

#im.show()
im.save("image.png")
