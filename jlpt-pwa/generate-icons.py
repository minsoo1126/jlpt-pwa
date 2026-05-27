from PIL import Image, ImageDraw, ImageFont
import os

def make_icon(size):
    img = Image.new('RGB', (size, size), '#7F77DD')
    draw = ImageDraw.Draw(img)
    text = 'あ'
    font_size = int(size * 0.55)
    try:
        font = ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc', font_size)
    except:
        try:
            font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', font_size)
        except:
            font = ImageFont.load_default()
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (size - tw) / 2 - bbox[0]
    y = (size - th) / 2 - bbox[1]
    draw.text((x, y), text, fill='white', font=font)
    img.save(f'/home/claude/jlpt-pwa/icon-{size}.png')
    print(f'icon-{size}.png created')

for s in [192, 512]:
    make_icon(s)
