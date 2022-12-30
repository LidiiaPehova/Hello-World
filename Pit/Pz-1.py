from PIL import Image, ImageFilter 
 
img = Image.open('Table.jpg') 
img_blur = img.filter(ImageFilter.BLUR) 
img1 = img.convert('1') 
imgL = img.convert('L') 
imgLA = img.convert('LA') 
 
img1.save('img1.png') 
imgL.save('imgL.jpeg') 
imgLA.save('imgLA.png') 
img_blur.save('img_blur.jpeg')

(width, height) = img1.size
data = list(img1.getdata())
f = open('pz1.txt', 'w')
count = 0
# print(type(data))
# print((width, height))
for i in data:
    if i == 255:
        f.write('1')
    if i == 0:
        f.write('0')
    count += 1
    if count == width:
        count = 0
        f.write('\n')
f.close()