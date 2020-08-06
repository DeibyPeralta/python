#   manejo de archivos
from io import open

#   creo archivo y escribo en el
"""
archivo_text = open("archivo.txt","w")# creo archivo modo write
frase="escribo en el archivo"
archivo_text.write(frase)# agrego el texto al archivo
archivo_text.close()    """

#   lectura y escritura

archivo_text = open("archivo.txt","r+")# lectura y escritura
lineas_text=archivo_text.readlines()
lineas_text[3]="4     linea que agrego\n"
archivo_text.seek(0)#posicion del archivo
archivo_text.writelines(lineas_text)
archivo_text.close()

#   agregar info
"""
archivo_text = open("archivo.txt","a")# archivo agrega
archivo_text.writelines("agrego texto")"""



#   lee la info del archivo linea a linea
"""
archivo_text = open("archivo.txt","r")# archivo modo read
lineas_text=archivo_text.readlines()
archivo_text.close()
print(lineas_text)  """     


#   lee la info del archivo
"""
archivo_text = open("archivo.txt","r")# archivo modo read
texto=archivo_text.read()
archivo_text.close()
print(texto)    """   