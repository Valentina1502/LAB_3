import math
ax = float(input("Pls, enter Ax "))
ay = float(input("Pls, enter Ay "))
bx = float(input("Pls, enter Bx "))
by = float(input("Pls, enter By "))
cx = float(input("Pls, enter Cx "))
cy = float(input("Pls, enter Cy "))
dx = float(input("Pls, enter Dx "))
dy = float(input("Pls, enter Dy "))
s1=math.fabs((ax-bx)*(cy-by)-(ay-by)*(cx-bx))/2
s2=math.fabs((ax-cx)*(dy-cy)-(ay-cy)*(dx-cx))/2
print("Area of the quadrilateral = ", s1+s2)