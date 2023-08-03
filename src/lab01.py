import math

def heronFormula(a,b,c):
  s = (a+b+c) / 2
  area = math.sqrt(s*(s-a)*(s-b)*(s-c))
  print("El área del triángulo es: ",area)

def cosineTheorem(side1,side2,targetSide):
  targetDegree = math.degrees(math.acos((targetSide**2 - side1**2 - side2**2) / (-2*side1*side2)))
  return round(targetDegree,2)
  
print("Ingrese los lados del triángulo")
sideA = float(input("Ingrese el lado A: "))
sideB = float(input("Ingrese el lado B: "))
sideC = float(input("Ingrese el lado C: "))

heronFormula(sideA,sideB,sideC)
degrees = []
degrees.append(cosineTheorem(sideC,sideB,sideA))
degrees.append(cosineTheorem(sideA,sideC,sideB))
degrees.append(cosineTheorem(sideA,sideB,sideC))


print("Los ángulos son del triángulo son:\n- Vértice A:",str(degrees[0])+"\n- Vértice B:",str(degrees[1])+"\n- Vértice C:",str(degrees[2]))