from PIL import Image
import random

X = 256
Y = 256

im = Image.new("RGBA", (X, Y), (0xfc, 0xfc, 0xf6))
new_colors = (0xf0, 0xf0, 0xf0)


for x in xrange(0, (X-1)):
    for y in xrange(0, (X-1)):
        # Determine whether we munge this pixel or not.
        munge_flag = random.randrange(0,100,1)
        
        if munge_flag > 89:
            print("Munged pixel %d, %d)" % (x,y))
            im.putpixel((x,y), new_colors)
            
try:
    im.save("images/bg.png")
except IOError:
    print("Couldn't save image.")
