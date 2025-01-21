import figuras as fg

cubo = fg.Cubo(3)

print(cubo.volumen())
print(cubo.area())

cuboide = fg.Cuboide(3, 4, 2)

print(cuboide.volumen())
print(cuboide.area())


esfera = fg.Esfera(2)


print(round(esfera.volumen(),2))
print(round(esfera.area(),2))


# print(cuboide.anchura)
# print(type(esfera))
# print(type(esfera.radio))

# print(fg.Esfera(2).area())



# https://es.onlinemschool.com/math/assistance/figures_volume/
# https://es.onlinemschool.com/math/assistance/figures_area/