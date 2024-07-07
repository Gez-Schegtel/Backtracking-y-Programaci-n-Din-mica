```markdown
# UNIVERSIDAD TECNOLÓGICA NACIONAL
## FACULTAD REGIONAL RESISTENCIA

**Ingeniería en Sistemas de Información**

### Materia: Complejidad y Técnicas de Diseño de Algoritmos

## Trabajo Práctico Integrador

### Grupo N° 6:

- Maldonado, Leandro Arian
- Ojeda Delio, Brian Bautista
- Schefer, Mauricio Nicolás
- Velazco Gez Schegtel, Juan Ignacio

---

## “Evaluación Booleana”

El problema que resolveremos es el problema de Boolean Parenthesization (también conocido simplemente como “Evaluación Booleana”), el cual se trata de encontrar todas las configuraciones de paréntesis existentes para que una proposición (compuesta por los operandos `TRUE` y `FALSE`, con operadores de conjunción (AND), disyunción (OR) y disyunción exclusiva (XOR)) de como resultado `TRUE` en su evaluación.

Supongamos que tenemos una proposición de la forma:

```
P = (T|F)((AND|OR|XOR)(T|F))^n-1
```

Es decir, una proposición de _n_ operandos, con _n >= 1_, todos ellos separados por operadores lógicos.

Definimos dos subconjuntos:
Por un lado, tenemos los **T(i,j)**, conjunto de soluciones para una sub proposición dentro de la proposición original, desde el elemento i-ésimo hasta el j-ésimo, de manera que esa subexpresión sea verdadera.
A su vez, también tenemos los **F(i,j)**, el conjunto de soluciones para una sub proposición dentro de la proposición original, desde el elemento i-ésimo hasta el j-ésimo, de forma que esa subexpresión sea falsa.

Nuestro objetivo es encontrar todos los **T(i,j)** de manera que obtengamos el conjunto **T(1,n)**, que contiene todas las posibles formas de agregar paréntesis a nuestra proposición de longitud n de manera que esta sea verdadera.

### Ejemplo

Consideremos la expresión:

```
T OR T AND F XOR T
```

Para esta expresión, tenemos cuatro formas de agregar paréntesis de manera que la expresión sea verdadera:

1. `T OR ((T AND F) XOR T)`
2. `T OR (T AND (F XOR T))`
3. `(T OR T) AND (F XOR T)`
4. `((T OR T) AND F) XOR T`

Y una forma de agregar paréntesis para que la expresión sea falsa:

```
(T OR (T AND F)) XOR T
```

Para facilitar la solución del problema, estos conjuntos **T(i,j)** y **F(i,j)** se pueden descomponer, cada uno, en varios otros conjuntos de soluciones para particiones más pequeñas de la proposición original. Supongamos que una partición **P(i,j)** se puede separar en dos sub proposiciones de la forma:

```
P(i,j) = P(i,k) * P(k,j)
```

donde el asterisco representa un operador lógico. En función de cuál sea el operador que una las sub proposiciones, los conjuntos **T(i,j)** y **F(i,j)** se pueden simplificar de distintas formas.

---

## Hipótesis

Dado un cadena de 4 valores de verdad obtendremos la cantidad de configuraciones diferentes de paréntesis que permiten que dicha cadena de como resultado verdadero. Se espera que la resolución utilizando programación dinámica sea más rápida que la técnica de backtracking.

## Resolución con Programación Dinámica

Para esta técnica, se arman las matrices **True** y **False**, poniendo en las filas y columnas los valores de verdad. Cada uno de los elementos de las matrices triangulares representa una combinación de valores de verdad, y el número en cada casilla representa el número de combinaciones de paréntesis que le dan a la expresión valor verdadero (o falso para la matriz F).


## Resolución con Backtracking

En la técnica de backtracking, partimos de la expresión completa, y vamos dividiendo en expresiones de dos en dos más pequeñas, hasta agotar las opciones. Al llegar a cada opción final de configuración de paréntesis, se analiza su valor de verdad y se devuelve el resultado, sumando ese resultado al conjunto de soluciones de ser verdadero.

---

## Conclusiones

Encontramos que Backtracking es una buena forma de entender y reflexionar acerca del programa, al poder apoyarnos en un método visual para confeccionar o encontrar las posibles soluciones, con ayuda de un árbol. Sin embargo, en expresiones muy extensas esta técnica no es eficiente y allí es cuando utilizar la programación dinámica se convierte en una necesidad. 

Con respecto a la elección de las técnicas, decidimos que no íbamos a abordar este problema con Algoritmos Voraces porque nuestro objetivo es encontrar todas las posibles configuraciones de paréntesis para evaluar la expresión booleana, y los Algoritmos Voraces o Greedy están diseñados para encontrar solamente una solución.
```
