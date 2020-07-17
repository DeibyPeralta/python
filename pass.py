nombre="este texto es largo"
contador=0

for i in nombre:
    if i==" ":
        continue
    contador+=1

print("sin espacio: ", contador)
print("con espacio: ",len(nombre))

"""for letra in "python":
        if letra == "h":
            continue # ignora si esta la h

        print("letra: ",letra)  """