# Proyecto-3-Katas-Python
Distintos ejercicios Python

Data: En algunos ejercicios he usado ayuda de ChatGPT como orientación, pero siempre he querido hacerlos lo más personales posible. Hay muchas maneras de hacer los ejercicios, y me gusta tratar de encontrar mi solución. En algunos ejercicios veremos como hago el trabajo de dos formas.

## Ejercicio 1: 
    Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

        - 1: Necesitaba quitarme los espacios, opté por remplazarlos por nada " " por "".

        - 2: Para contar correctamente la frecuencia de las letras, sin que contase letras extras en mayúsculas, lo que hice fue usar la función lower()

        - 3: Cree un diccionario vacio y con un for cree un nuevo diccionario, donde la clave es el valor de Index y el value lo coge el count sobre la palabra de Index.

## Ejercicio 2:
    Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

        - 1: Cree una lista de números

        - 2: Use la función map() como solicita el ejercicio para dar una lista con el doble de cada valor usando lambda donde "numero" va recorriendo la lista y multiplicandose por 2.
        
        - 3: Imprimo la lista antigua y la nueva para ver la diferencia de las listas y contrastar que funciona.

## Ejercicio 3:
    Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

        - 1: Le pedí a ChatGPT que me hiciese una lista de X frutas, pereza mortal, ahorro de tiempo y efectividad.

        - 2: Cree la función tal como comenta, cree una lista vacía que rellenar y utilicé un for dentro de la función para recorrer la lista de frutas una a una.

        - 3: Dentro del for, puse un if para revisar si contiene el texto que busco. De todas las opciones que me salian de "index" utilice un __contains__ que cumplia con el proposito que necesitaba.

        - 4: Si cada palabra incluia la palabraObjetivo se añadía en la lista que retorna la función para luego ser impresa.

## Ejercicio 4:
    Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().
        
       No estoy seguro si la solución aportada es la que se solicita, pero lo que hice fue coger dos listas y hacer la resta de Elemento1Lista1 con Elemento1Lista2 y consecutivamente con una función lambda y map().

## Ejercicio 5:
    Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.

        Paso 1: Crear una lista de valores tipo float
                Crear una variable notaAprobado

        Paso 2: Crear función con sus devidos parámetros y salidas.

        Paso 3: Calcular la media: utilicé la función sum para sumar todos los valores de la lista y luego calculé la longitud con len.

        Paso 4: Para no sacar todos los decimales, utilicé la función round para reducir a dos decimales.

        Paso 5: Comprobar si la media es igual o superior a la nota límite. En cualquier caso, saco una tupla con la nota y si está suspendido o aprobado.

        Puse dos ejemplos, uno aprobado y otro suspendido, por eso se ven dos listas.

## Ejercicio 6:
    Escribe una función que calcule el factorial de un número de manera recursiva.

        Este ejercicio lo realicé con ayuda de ChatGPT y a mi manera.

        Opción #1: no es recursiva, pero realiza la acción.

            a. Inicializo una variable con el valor entregado.

            b. Generé un rango del valor entregado menos 1 hasta 0 dando pasos de -1 en -1 y utilizo un for para recorrerlo.

            c. El for multiplica ese valor con su anterior. Por ejemplo: 5*4*3*2*1

            d. En el caso de que el valor entregado sea 0, se asigna 1, debido a que el factorial de 0 es 1.

        Opción #2: de manera recursiva

            a. Si el valor es 1 o 0, entregamos el mismo valor
            b. Si el valor es superior lo multiplico por la misma función con un valor inferior al de la primera vez.

            Ejemplo: 5 * 5-1 * 4-1 * 3-1 * 2-1 * 1

        Las dos opciones son buenas, me parece más sencilla la primera, tal vez porque sea la forma en que piensa mi mente.

## Ejercicio 7:
    Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

        La verdad, no sé si es lo que había que hacer.

        a. Crear Tuple
        
        b. usar map con lambda un a que recorra Tuple y lo meta en un list.

## Ejercicio 8:
    Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.

        Me ayudé de la web de prometeo, teniamos un ejemplo que me vino de cine. Es curioso la cantidad de Exceptions que existen.

        a. Solicito los datos y Calculo los resultadoss
        b. Revisa las exceptions y guardo la exception en una variable
        c. Muestro un texto por consola en el caso que corresponda y filtro los decimales en dos digitos mediante el uso de un printf y :.2f

## Ejercicio 9:
    Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().

        Se crean dos listas de textos, una la da el ejercició, la otra ChatGPT para agilizar.

        Se busca mediante una función filter que la variable de la lista no exista en listaAnimal. Devolvemos una lista que luego mostramos por pantalla.

## Ejercicio 10:
    Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

        En este ejercicio utilicé una formula parecida al Ejercicio 5.

        En el caso de estar vacía la lista doy un mensaje por pantalla de ello. En caso contrario, calculo la suma total y la divido por la cantidad de elementos para sacar el promedio.

## Ejercicio 11:
    Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

        Se introduce la edad comprendida entre 0 y 120 años.
        En el caso de que se introduzca una letra salta una except "Value Error".
        En el caso de que el valor sea superior a 120 o inferior a 0 hacemos saltar un error personalizado ValueError.

## Ejercicio 12:
    Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().

        Esta explicado en el mismo ejercicio. Pero vamos se reduce a..

        a. Filtramos la frase quitandole todos los simbolos que me vienen a la mente.
        b. Dividimos la frase en palabras y las metemos en una lista con split()
        c. Contamos los elementos de la lista con la funcion len, esto me ayude de la IA.

## Ejercicio 13:
  Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().

    a. Usamos la función set() para quitar letras duplicadas y usamos sorted para ordenarlas.
    b. Como ya no hay letras repetidas, usamos un lambda para coger las letras y generamos un tuple con cada letra con su minus y su mayus.


## Ejercicio 14:
  Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().

        a. Nos aseguramos de que la letra a comparar esté en mínusculas
        
        b. Nos aseguramos de que las palabras a comparar también estén en minúsculas. Para ello pasamos una función list() combinada con map() y hacemos una lambda que coja palabra por palabra y la vaya "minisculizando"
        
        c. Usamos una función lambda que recorra la lista de palabras "listaLower" y busque solo la primera letra de cada palabra con [:1] y la comparamos con el filtro letraLower, si son iguales la meto en la lista.

        d. Mostramos las palabras que empiezen por l.

## Ejercicio 15:
    Crea una función lambda que sume 3 a cada número de una lista dada.

        Este es parecido al de multiplicar la lista por dos (Ejercicio 2). Se usa el mismo procedimiento lógico, salvo que en vez de multiplicar por 2, le sumamos 3.

        Ojalá todos los ejercicios fueran como este.... T_T

## Ejercicio 16:
    Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().

        Nada, este es como los anteriores...

        a. Quito , y . con replace
        b. Divido la frase en palabras con .split()
        c. Recorro la lista con lambda y compruebo la longitud de cada palabra con el parametro numFiltro.

## Ejercicio 17:
    Crea una función que tome una lista de dígitos y devuelva el número . Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().

        Aquí me ayudé un poco de GPT, pero es bastante sencillo.

        Al final usamos reduce() donde a es el primer elemento, y b el siguiente, luego a es el resultado y b el siguiente.. y lo que hacemos es:
            5*10 = 50+7 = 57
            57*10 = 570+2 = 572
            572*10 = 5720+2 = 5722
            5722*10 = 57220+1 = 57221
            57221*10 = 572210+3 = 572213

## Ejercicio 18:
    Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.

        a. Creamos la lista de estudiantes, edad y calificación
        b. filtramos con filter() los estudiantes cuya calificación sea superior o igual a 90.

## Ejercicio 19:
    Crea una función lambda que filtre los números impares de una lista dada.

        Lo que he hecho aquí es sacar el resto de la división del número entre 2 (par) y si es diferente de 0 entendemos que es impar, por lo que lo filtramos con filter() y lo sacamos a una lista con list().

## Ejercicio 20:
    Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().

        Filtramos la lista en la que el tipo de la variable sea distinto a un String.

## Ejercicio 21:
    Crea una función que calcule el cubo de un número dado mediante una función lambda.

        Aquí me ayudé de GPT ya que no sabía como hacer funcionar la función lambda sin un iterable.

## Ejercicio 22:
    Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().

        Parecido a un ejercicio anterior.

        Usamos reduce()
        4*7 = 28
        28*2 = 56
        56*9 = 504
        504*5 = 2520

## Ejercicio 23:
    Concatena una lista de palabras. Usa la función reduce().

        Parecido al anterior pero concatenando en vez de multiplicando.

## Ejercicio 24:
    Calcula la diferencia total en los valores de una lista. Usa la función reduce().

        Este me ayude de ChatGPT porque no entendía el enunciado, al final restamos toda la lista, luego la sumamos y mostramos la diferencia de extremos.

## Ejercicio 25:
    Crea una función que cuente el número de caracteres en una cadena de texto dada.

        .... ¿Hace falta explicarlo? ...

## Ejercicio 26:
    Crea una función lambda que calcule el resto de la división entre dos números dados.  

        Se crea un función lambda con dos parámetros, y ejecuta el resto.

        Llamamos a la función en el propio print y hemos pedido los datos antes de todo.

## Ejercicio 27:
    Crea una función que calcule el promedio de una lista de números.

        Muy parecido a otros anteriores. Sumamos la lista, contamos la longitud, y sacamos promedio.

## Ejercicio 28:
    Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

        a. Creamos la lista
        b. Creamos una lista tuple de vistos
        c. Creamos un for que recorre elementos item por item, si no lo hemos visto, lo añadimos al tuple. En el caso de que lo hayamos visto, metemos el valor en duplicado y terminamos el for. Mostrando aquel que está duplicado.

## Ejercicio 29:
    Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.

        Este ejercicio está explicado en el mismo.

## Ejercicio 30:
    Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

        a. Creamos las Variables a comparar
        b. Revisamos si las variables en minusculas con la funcion lower() son iguales. Una de ellas le damos la vuelta con [::-1]
 
## Ejercicio 31:
    Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.

    
## Ejercicio 32:

## Ejercicio 33:

## Ejercicio 34:

## Ejercicio 35:

## Ejercicio 36:

## Ejercicio 37:

## Ejercicio 38:

## Ejercicio 39:

## Ejercicio 40:

