import turtle
turtle.shape('turtle')
a = 6
step = 10
for k in range(10):

    for i in range(20):
         turtle.forward(a)
         turtle.left(16)
         a = a + a/110
         
    k = k+1
    
