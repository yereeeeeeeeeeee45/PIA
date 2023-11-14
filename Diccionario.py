edades = {"Juan":25,"Maria":30,"Pedro":22}
persona = {
    "nombre":"Ana",
    "edad":28,
    "ciudad":"Madrid"
}
print(edades["Juan"])  
print(persona["ciudad"])
edades["Maria"]=31
persona["edad"]=29
edades["Laura"]=23
persona["profecion"] = "Ingeniera"
del edades["Pedro"]
persona.pop("ciudad")
if"Laura"in edades:
 print("Laura esta en el diccionario")
claves =edades.keys()
valores=edades.values()
print(len(persona))