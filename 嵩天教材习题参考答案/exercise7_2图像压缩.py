from PIL import Image
im = Image.open("/home/weizhong/Pictures/p1.jpg")
w,h = im.size
c = 6
im.thumbnail((w//c, h//c))
im.save('/home/weizhong/Pictures/p11.jpg','JPEG')

#or:
im2 = Image.open("/home/weizhong/Pictures/p1.jpg")
im2.resize((w//c,h//c)).save('/home/weizhong/Pictures/p12','JPEG')
