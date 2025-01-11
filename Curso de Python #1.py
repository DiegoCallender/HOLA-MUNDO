the_worl_is_flat=True;
if the_worl_is_flat:
    print("Tranquilo, la tierra no es plana");

palabra="Python";

print(palabra[2:5]);   

# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
#-6  -5  -4  -3  -2  -1

#La Cadena de Python no se puede Modificar EJ: >> palabra[0]="J" << nos daria error 
#Si se necesita una Cadena nueva, se debe de crear una

print("J" + palabra[1:]);

print(palabra[:2]+ "py");

#La función len() reotrna la longitud de la cadena

print(len(palabra));

palabra2="Diego_Callender_Alejando_Callender"

print(len(palabra2));

#nombre_usuario=input("Dime tu nombre y te dire cuantas letras tiene. Nombre: ");

#print(len(nombre_usuario));

#Listas

cubos=[1,8,27,65,125];

#[1   8  27  65  125] 
# 0   1   2  .3   4   
#-6  -5  -4  -3  -2  

#Las listas se colocan entre [] y estas si pueden ser modificadas, y tambien inician en 0s

print(cubos); #Se quiere modificar el 65 por 64

cubos[3]=64;

print(cubos);

#Si se quiere añadir un elemento nuevo a la lista, se usa el comando list.append(), lo que lo colocara al final de la lista

cubos.append(6**3);
cubos.append(7**3);
print(cubos);

rgb=["Red","Green","Blue"];
rgba=rgb;

print(rgb==rgba);

#Bluces
#Serie de Fibonacci

a,b=0,1;
while a < 10:
    print(a)
    a,b=b,a+b

#Se puede usar el parametro end para que no tengamos un salto de linea

a,b=0,1;
while a < 10:
    print(a,end=",")
    a,b=b,a+b

#Sentencia "IF"

x=int(input("Por favor, coloca un entero: "))

if x < 0:
    x=0
    print("El numero negativo se cambio a 0");
elif x==0:                                               #elif es una abreviatura para "else if". Se usara si se quiere hablar de condiciones especificas.
    print("Cero");
elif x==1:
    print("Uno");
else:                                                    #else se usara, de manera opcional, para especificar que sucede con todo lo demas que no intregra if o elif.
    print("Mas");

#Sentecia "FOR"

lista_palabras=["Diego","Gato","Esternoncleidomastoideo"];

for w in lista_palabras:                                       #La variable w se usa para indicar cada entrada de la lista "palabras"
    print(w, len(w));

for palabras in lista_palabras:
    print(palabras, len(palabras));                            #Ejemplo de lo mencionado anteriormente

#Tambien se puede usar para modificar colecciones

usuarios={"Hans":"activo","Leon":"Inactivo","Shala":"Activo"}

#Iterando sobre una copia

for usuario, status in usuarios.copy().items():
    if status == "Inactivo":
        del usuarios[usuario];

#Creando una nueva Coleccion

usuarios_activos= {}
for usario, status in usuarios.items():
    if status== "Activo":
        usuarios_activos[usuario]=status;