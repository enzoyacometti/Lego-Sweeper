# Tarea 0: LegoSweeper :school_satchel:


## Consideraciones generales :octocat:

* El programa corre bien e implementé los menús de la forma más lógica posible según el enunciado, sin embargo, **carece de opción "volver"**.

* Es relevante notar que cuando se crea o se carga una partida, el primer menú de juego carece de opción "guardar partida", ya que no existe información relevante para guardar en ese instante. Sin embargo, **al descubrir una baldosa, inmediatamente se otorga esa opción**.

* Las partidas guardadas contienen la información de la siguiente manera, entre paréntesis la variable asignada a cada cosa:
  * Nombre de usuario (**_username_**)
  * Ancho de tablero (**_width_**)
  * Alto de tablero (**_height_**)
  * Número de legos (**_legos_**)
  * Posiciones donde existen legos (**_death_**)
  * Tablero completo/resuelto (**_table_completo_**)
  * Cantidad de posiciones descubiertas (**_history_len_**)
  * Posiciones descubiertas (**_history_**)

Como se observa, las últimas dos cosas son las únicas que varían en el tiempo, ya que todo lo anterior se crea de inmediato al inicio de una partida, por lo que, al guardar, estas dos cosas son las únicas que cambian.

* Las partidas ganadas y perdidas no se guardan en la carpeta "partidas" ya que han finalizado y sólo se da la opción de guardar el puntaje en el archivo ```puntaje.txt```.

* Los archivos relevantes son tres: ```main.py```, ```CreacionTableros.py``` y ```Guardado.py```:
  * ```main.py```: Programa principal que contiene el juego.
  * ```CreacionTableros.py```: Contiene la función "crear_tablero_juego(width, height)" que crea el tablero sobre el cual se jugará y, por otro lado la función "crear_tablero_completo(width, height, death)" la cual crea el tablero solucionario del juego.
  * ```Guardado.py```: Contiene la función "guardar_base(username, width, height, legos, death, table_completo)" la cual guarda todos los parámetros que se le ingresan, para más tarde guardar separadamente la cantidad de posiciones descubiertas y una lista con dichas posiciones.

* **¿Cómo funciona el programa?**
  * El código básicamente crea un **tablero completo** con todas las 'L' y los números correspondientes y un **tablero de juego** vacío. Cuando se selecciona una posición que pertenezca a "_death_" se cae en un lego y se pierde. Por otro lado, si no se cae en un lego, se toma esa posición del tablero completo y se reemplaza en el tablero de juego, siendo este último el que se imprime en pantalla.


### Cosas implementadas y no implementadas :white_check_mark: :x:

* **Inicio del programa**: Hecha completa (considerando que es lógica la asunción respecto a la opción de "guardar partida").
* **Flujo del Juego**: Sólo me faltó implementar la opción "volver atrás".
* **Término del Juego**: Hecha completa.
* **General**: Hecha completa.
* **Bonus**: No realizado.

## Ejecución :computer:
* El módulo principal de la tarea a ejecutar es  ```main.py```. 
* La carpeta ```partidas``` debería estar creada y vacía. 
* El archivo ```puntajes.txt``` se crea sólo, al finalizarse y guardar la primera partida.


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint()```
2. ```math```: ```ceil()```
3. ```os```: ```path.isfile()```, ```path.join()```, ```remove()```, ```write()```, ```open()```


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. No es lógico guardar una partida sobre la cual no se ha hecho nada (ya se haya creado o cargado), por esto el primer menú mostrado carece de la opción "guardar partida".

-------