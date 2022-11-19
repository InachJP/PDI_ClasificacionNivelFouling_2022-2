# PDI_ClasificacionNivelFouling_2022-2

### Estudiantes:
* Jonathan Pedraza 201930035-0
* Lucas Navarro 201930044-K
* Carlos Arredondo 201930026-1
* Vicente Tejos 201930017-2
* Robert Parra

### Complementos necesarios:
Dado que vamos a trabajar con una red neuronal convolucional, utilizaremos python3.0+, y Tensorflow+Keras.

### Funcionamiento y objetivo del programa:
Entrenaremos un modelo basado en Deep Learning para la clasificación de los niveles de fouling, utilizando el método de transfer learning, ocupando como base un modelo InceptionV3 más algunas capas extras.

Contamos con un dataset con +600 imágenes por cada clase (High, Mid, Low). Dataset original contaba con más de 1800 imágenes de la clase low pero debido a que estaban desbalanceadas las clases recurrimos a reducir el número de imágenes.
