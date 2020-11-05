import cv2, random, ast

original = 'niana.png'
encrypted = 'encrypted.jpg'
filedict = "dict.txt"

img = cv2.imread(original,cv2.IMREAD_COLOR)
dimensions = img.shape
x, y = dimensions[0], dimensions[1]

cold = {}
for i in range(x):
    for j in range(y):
        (b, g, r) = img[i, j]
        cold.update({(i,j) : (r,g,b)})

ck = list(cold.keys())
temp = ck[:] # make a copy
random.shuffle(ck) # shuffle
cv = list(cold.values())

revcold={}
for m in range(x*y):
    revcold.update({ck[m] : cv[m]})

file_object  = open(filedict, "w")
file_object.write(str(revcold))
file_object.close()

readict = open(filedict).read()
astdict = ast.literal_eval(str(readict))

rk = list(revcold.keys())
rv = list(revcold.values())

for n in range(x*y):
    try:
        img[rk[n][0], rk[n][1]] = (rv[n][2], rv[n][1], rv[n][0])
    except Exception as e:
        pass

cv2.imshow('image', img)
cv2.waitKey(0)  # millisecond, use 0 for infinite time
cv2.destroyAllWindows()
cv2.imwrite(encrypted, img)
