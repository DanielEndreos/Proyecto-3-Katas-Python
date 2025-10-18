# Proyecto-3-Katas-Python
Distintos ejercicios Python

Data: En algunos ejercicios he usado ayuda de ChatGPT como orientación, pero siempre he querido hacerlos lo más personales posible. Hay muchas maneras de hacer los ejercicios, y me gusta tratar de encontrar mi solución. En algunos ejercicios veremos como hago el trabajo de dos formas.

## Ejercicio 1: 
`    Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

        - 1: Necesitaba quitarme los espacios, opté por remplazarlos por nada " " por "".

        - 2: Para contar correctamente la frecuencia de las letras, sin que contase letras extras en mayúsculas, lo que hice fue usar la función lower()

        - 3: Cree un diccionario vacio y con un for cree un nuevo diccionario, donde la clave es el valor de Index y el value lo coge el count sobre la palabra de Index.`

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

        He utilizado una función while para solicitar al usuario tantos nombres como sean posibles, teniendo que terminar con la palabra 'fin', da igual si es Fin, fIn, fiN... pongo en minúsculas con lower() y reviso que sea igual a 'fin'.

        Luego con una función if comparo si las condiciones que busco son las que necesito, en el caso de que sí añado el nombre a la lista en minúsculas y pongo en mayuscula la primera letra, si el nombre está vacio o no es alpha no lo añado a la lista, y en el caso de que sea fin, el while terminará y ya ejecutamos el código.

        En este momento pedimos al usuario que nombre quiere buscar y con una función if preguntamos si el nombre entregado en minusculas y con la primera letra en mayus está en la lista.

        En el caso de que se encuentre, mostramos un mensaje por pantalla y en el caso contrario pues mostramos un mensaje diciendo que el nombre no se encontraba en la lista.

## Ejercicio 32:
    Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

        Utilizamos la función next() que sirve para buscar el primer elemento que cumpla la condición.

        Utilizamos la funcion i for i in X if i["nombre] == nombreBuscado. 
        Con el for recorremos diccionario en diccionario, y buscando dentro del key "nombre" si se encuentra el target. 
        
        Caso "a": Encontramos el nombre. Next nos retornará el diccionario, donde encontramos las keys con sus valores.

        Caso "b": No encontramos el nombres. Next nos retornará la frase por defecto que hemos preparado.

        Por este motivo, como next nos puede retornar dos tipos distintos, no he declarado una salida de la función, aunque por lo que he visto, tampoco afecta directamente.
        
        Por el motivo mencionado anteriormente, he creado un if que compruebe si el valor entregado de la variable es un String o otra cosa, en este caso, diccionario. Dependiendo de cada cosa ejecutamos un print distinto.    
    
## Ejercicio 33:
    Crea una función lambda que sume elementos correspondientes de dos listas dadas.

        Creado una función lambda que suma a + b en lista A y lista B.

## Ejercicio 34:
    Crea la clase Arbol

            Define un árbol genérico con un tronco y ramas como atributos.
        Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
        Código a seguir:

          -  Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
          -  Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
          -  Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
          -  Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
          -  Implementar el método quitar_rama para eliminar una rama en una posición específica.
            Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.

        Caso de uso:
                a. Crear un árbol.
                b. Hacer crecer el tronco una unidad.
                c. Añadir una nueva rama.
                d. Hacer crecer todas las ramas una unidad.
                e. Añadir dos nuevas ramas.
                f. Retirar la rama situada en la posición 2.
                g. Obtener información sobre el árbol.


        Está practicamente todo explicado en el enunciado, pero generamos una class llamada Arbol.

        - Inicialización:
        Luego inicializamos la clase con la funcion __init__ siendo el parametro Self el propio arbol que se cree. 
        
        Self funciona como una variable local hará caso al caso individual y no al global. Arbol Pepito, Arbol José...

        Creamos el atributo tronco y le asignamos valor 1
        Creamos el atributo ramas y le asignamos formato lista.

        - Creación de las funciones solicitas

            - crecer_tronco(self)
                Llamamos a Self para que afecte a la instancia y sumamos 1 a tronco mediante +=

            - nueva_rama(self)
                Llamamos a self para que afecte a la instancia y usamos la función append(1) para generar una nueva rama. Esto añade un elemento en la lista con valor 1, y se añade al final.
            
            - crecer_ramas(self)
                Hacemos un for para recorrer la lista con una función range, donde añadimos a todas los elementos de la lista un +1

            - quitar_ramas(self, pos: int)
                En este caso realizamos una función pop() donde gracias al parámetro pos podemos quitar la rama solicitada.

            - info_arbol(self)
                Nos devuelve un print de la información actual del árbol.

            Por último hacemos las llamadas a los funciones de la clase para ejecutar el caso de uso.

            Ha sido un ejercicio muy divertido, me ha gustado más que los otros anteriores... la virgen...

## Ejercicio 35:
    Crea la clase UsuarioBanco
        Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
        Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
        Código a seguir:

            Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
            Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
            Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
            Implementar agregar_dinero para aumentar el saldo del usuario.

        Caso de uso:
                a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
                b. Agregar 20 unidades al saldo de Bob.
                c. Transferir 80 unidades de Bob a Alicia.
                d. Retirar 50 unidades del saldo de Alicia.
        --------------------------------------------------------

        Este ejercicio lo he disfrutado mil, como el del árbol.

        Al final, es muy parecido al árbol, creamos la clase usuario donde en este caso, en vez de inicializar las variables, he creado unos parámetros que se asignan al self para inicializar el usuario.

        Luego he creado las distintas funciones solicitadas, le he puesto algo de humor a los mensajes de consola. Al final consultamos saldos, comparamos y sacamos mensajes en caso de A o B.

        Luego realizo el caso de uso como se indica.

        Se podría añadir más azúcar, por ejemplo, podriamos crear una variable aleatoria random(), que dependiendo del valor que saque, mostrar un mensaje distinto de una lista de mensajes.

## Ejercicio 36:
    Crea una función llamada procesar_texto
        Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
        Código a seguir:

            Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
            Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
            Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
            Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción elegida.

        Caso de uso:
            Verificar el funcionamiento completo de procesar_texto.

    
        Este ejercicio le he puesto comentarios para separar las funciones, ya costaba leerlas...

        En este ejercicio he utilizado mucho los for y los if.

        - contar_palabras:
            Para contar palabras, he cogido el texto, lo he hecho un minus con lower(), luego un replace para quitar . y , y luego lo he separado por espacios con split(). De esta manera ya tenía una lista con palabras separadas.

            Luego he creado un diccionario vacio.

            He recorrido palabra por palabra con una función for y he utilizado la función get(), busca la clave en el diccionario, si no la encuentra la genera y le pone un valor por defecto, en este caso 0 pero a posterior le sumamos 1. Por ejemplo:

                - No existe: Creamos variable con valor 1
                - Existe: Cogemos el valor de la variable y le sumamos 1

            El resultado lo volvemos a guardar en su diccionario correspondiente.

        - reemplazar_palabras:
            Para reemplazar palabras he hecho la misma parte que contar palabras para sacar una lista de palabras y luego, he recorrido todas las palabras buscando si la palabra es igual a la palabra que quiero sacar, en el caso que sea así, añadimos la palabra que queremos meter, en caso contrario añadimos la palabra en cuestión.

            Luego juntamos de nuevo todas las palabras en una misma lista.

        - eliminar_palabra:
            Lo mismo que reemplazar, es decir, la misma lógica, solo guardamos las palabras que queremos y luego volvemos a juntar la lista. 

        - procesar_texto:
            Dependiendo de lo que queramos hacer, usamos una función o otra e introducimos unos parametros o otros, haciendo uso de *args.

        En este ejercicio me he dado cuenta que para identificar que algo es una tupla, si solo tiene un elemento, debe tener una , que separe con la NADAAAAAAA!


## Ejercicio 37:
    Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.

        Sencillo, le digo al usuario que debe introducir el formato de fecha y hora con un formato. Y separo las horas de los minutos y de los segundos mediante un split() teniendo en cuenta los ":".

        Luego uso la posición [0] que corresponde a la hora y comparo entre franjas horarias.

        No he creado ningún tipo de except porque no se solicita en el ejercicio y no quiero invertir más tiempo de lo necesario, son demasiados ejercicios... 

        Pero como todo... más dulce más azúcar

## Ejercicio 38:
    Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
            Reglas:
                    0 - 69: insuficiente
                    70 - 79: bien
                    80 - 89: muy bien
                    90 - 100: excelente

        Muy parecido al ejercicio anterior. En este caso si que he puesto un except en caso de que el valor introducido no sea numérico. 
        
        Luego se podría poner un fallo de error en caso de salirnos del valor solicitado, 0 o superior a 100. Pero bueno, luego hay un ejercicio así.

## Ejercicio 39:
    Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).

        Le pregunté a la IA como calcular las áreas, tenía claro la del rectángulo y circulo, pero el triangulo? JAH!

        Al final, la diferencia en este ejercicio respecto a los anteriores es la funcionalidad kwargs, muy interesante y curioso, el poder ampliar y reducir el contenido a entregar para luego usar en el interior.´

        Había creado una variable y un if dependiendo de la variable pero era complicado hacer print casos distintos, mucha duplicidad de cógido, así que lo he hecho de esta manera para ver los tres casos con variables distintas y mostrar resultados.
        
## Ejercicio 40:
    Escribe un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe:
        a. Solicitar al usuario el precio original de un artículo.
        b. Preguntar si tiene un cupón de descuento (respuesta sí o no).
        c. Si la respuesta es sí, solicitar el valor del cupón de descuento.
        d. Aplicar el descuento al precio original, siempre que el valor del cupón sea válido (mayor a cero).
        e. Mostrar el precio final de la compra, considerando o no el descuento.
        f. Usar estructuras de control de flujo (if, elif, else) para llevar a cabo las acciones.


    No hay mucho que explicar de este código, se ha hecho lo que se ha pedido paso a paso, se puede ver en el proceso.