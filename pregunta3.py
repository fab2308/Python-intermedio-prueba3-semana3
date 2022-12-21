with open("correos.txt", "r") as tf:
    lines = tf.read().splitlines()
print(lines)

correo = input("Ingrese el correo que desea buscar: ")

indice = lines.index(correo)
if correo in lines:
    print('La posicion del correo es la', indice, 'en la lista')
else:
    return("Devolver -1") 

print("El total de elementos de la lista es de: ", len(lines))


parts = correo.partition('@')
print("El proveedor del correo es: {}".format(parts[2]))


correos_de_mismo_proveedor = input("Ingrese el proveedor de correo que desea buscar: ")
indice_correos = lines.index(correos_de_mismo_proveedor)
print('Todos los correos con este el proveedor', indice_correos, 'en la lista')

