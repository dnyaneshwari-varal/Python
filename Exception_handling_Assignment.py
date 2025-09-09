
def circle(r):
    area=3.14*(r*r)
    dia=2*r
    circ=2*3.14*r
    return area,dia,circ
    



try:
  radius=int(input("Enter radius of circle: "))
  if radius<0:
      
      raise ValueError("Enter positive radius")
  else:
    a,d,c=circle(radius)
    print("Area of circle: ",a)
    print("Diameter of circle: ",d)
    print("Circumference of circle is: ",c)
except Exception as e:   #what exception we raise it store in this e
      print(e)

print("Exit code")
