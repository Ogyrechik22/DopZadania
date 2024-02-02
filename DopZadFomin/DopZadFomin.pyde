# a = 0
# b = 100
# c = 0
# d = 0
# z = 100
# z2 = 450
# z3 = 830
# e = 25
# r = 25
# e1 = 2.9
# r1 = 3.2
# def setup():
#     size(1000,1000)
#     background(1)
#     frameRate(100)
# def draw():
#     global a,b,c,d,z,z2,z3,r1,e1,e,r
#     rect(z,100,70,30)
#     rect(z2,100,70,30)
#     rect(z3,100,70,30)
#     if mousePressed == True:
#         if mouseX > 100 and mouseX < 170 and mouseY > 100 and mouseY < 130:
#             background(1)
#             ellipse(b,a,50,50)
#             a += 3.0
#             if a > 1000:
#                 a = 25
#                 b = random(25,975)
#         elif mouseX > 450 and mouseX < 520 and mouseY > 100 and mouseY < 130:
#             background(1)
#             line(0,0,d,c)
#             frameRate(10)
#             stroke(random(0,255),random(0,255),random(0,255))
#             c = random(1,1000)
#             d = random(1,1000)
#             fill(1)
#         elif mouseX > 830 and mouseX < 900 and mouseY > 100 and mouseY < 130:
#             background(1)
#             ellipse(e,r,50,50)
#             e = e + e1
#             r = r + r1
#             if r > 975:
#                 r1 = -3.2
#             if r < 24:
#                 r1 = 3.2
#             if e > 950:
#                 e1 = -2.9
#             if e < 24:
#                 e1 = 2.9
# x = 500
# y = 500
# def setup():
#     size(1000,1000)
#     background(1)
#     frameRate(90)
#     rectMode(CENTER)
# def draw():
#     global x,y
#     rect(x,y,100,100)
#     rect(10,22,10,10)        
#     rect(22,22,10,10)
#     rect(34,22,10,10)
#     rect(22,10,10,10)
#     if mousePressed == True:
#         if mouseX > 9 and mouseX < 21 and mouseY > 21 and mouseY < 32:
#             x -= 1
#         if mouseX > 22 and mouseX < 33 and mouseY > 21 and mouseY < 32:
#             y += 1
#         if mouseX > 33 and mouseX < 44 and mouseY > 21 and mouseY < 32:
#             x += 1
#         if mouseX > 22 and mouseX < 33 and mouseY > 9 and mouseY < 21:
#             y -= 1
b = int(random(1,3))
e = 100
f = 500
g = 900
def setup():
    size(1000,1000)
    frameRate(100)
    background(1)
    rectMode(CENTER)
    fill(255)
    textSize(25)
def draw():
    global b,e,f,g
    if b == 1:
        ellipse(100,100,90,60)
        rect(e,100,100,70)
        rect(f,100,100,70)
        rect(g,100,100,70)
        if mousePressed == True:
            if mouseX > 50 and mouseX < 150 and mouseY > 65 and mouseY < 135:
                noLoop()
                fill(1)
                text('Here',69,110)
                fill(1)
                text('You Win!', 450, 500)
            if mouseX > 450 and mouseX < 550 and mouseY > 65 and mouseY < 135:
                noLoop()
                text('You Lose!', 450, 500)
                text('Here',69,110)
            if mouseX > 850 and mouseX < 950 and mouseY > 65 and mouseY < 135:
                noLoop()
                text('You Lose!', 450, 500)
                text('Here',69,110)
    if b == 2:
        ellipse(500,100,90,60)
        rect(e,100,100,70)
        rect(f,100,100,70)
        rect(g,100,100,70)
        if mousePressed == True:
            if mouseX > 50 and mouseX < 150 and mouseY > 65 and mouseY < 135:
                noLoop()
                text('You Lose!', 450, 500)
                text('Here',479,110)
            if mouseX > 450 and mouseX < 550 and mouseY > 65 and mouseY < 135:
                noLoop()
                text('You Win!', 450, 500)
                text('Here',479,110)
            if mouseX > 850 and mouseX < 950 and mouseY > 65 and mouseY < 135:
                noLoop()
                text('You Lose!', 450, 500)
                text('Here',479,110)
    if b == 3:
        ellipse(900,100,90,60)
        rect(e,100,100,70)
        rect(f,100,100,70)
        rect(g,100,100,70)
        if mousePressed == True:
            if mouseX > 50 and mouseX < 150 and mouseY > 65 and mouseY < 135:
                noLoop()
                text('You Lose!', 450, 500)
            if mouseX > 450 and mouseX < 550 and mouseY > 65 and mouseY < 135:
                noLoop()
                text('You Lose!', 450, 500)
            if mouseX > 850 and mouseX < 950 and mouseY > 65 and mouseY < 135:
                noLoop()
                text('You Win!', 450, 500)
