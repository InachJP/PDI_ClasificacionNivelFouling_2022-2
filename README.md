# PDI_ClasificacionNivelFouling_2022-2

### Estudiantes:
* Jonathan Pedraza 201930035-0
* Lucas Navarro 201930044-K
* Carlos Arredondo 201930026-1
* Vicente Tejos 201930017-2
* Robert Parra


# Manual de Instalacion
Instalar las bibliotecas necesarias:

`pip install tensorflow`

`pip install keras`

`pip install pillow`

Instalacion de dependencias necesarias para la interfaz:

`sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0`


# Manual De Usuario

Bajar el dataset de testing del Drive

Bajar uno de los modelos de entrenamiento del OneDrive

Ejecutar el archivo de interfaz:

`python interfaz.py`

Se abrira la interfaz:

![Interfaz Abierta](/imagenes_manual/interfaz_apertura.png "Interfaz")


Se hace click en Seleccionar Carpeta De Imagenes para seleccionar la carpeta del dataset:

![Interfaz Boton Seleccionar Dataset](/imagenes_manual/interfaz_seleccionar_dataset.png "Interfaz Seleccionar Dataset")

Se busca la carpeta que contiene las fotos del dataset a predecir (se debe entrar a la carpeta que contiene las fotos y aprear seleccionar):

![Interfaz Buscar y Seleccionar Dataset](/imagenes_manual/interfaz_buscar_seleccionar_carpeta.png "Interfaz Buscar y Seleccionar Dataset")

Se hace click en Seleccionar Modelo:

![Interfaz Boton Seleccionar Modelo](/imagenes_manual/interfaz_seleccionar_modelo.png "Interfaz Boton Seleccionar Modelo")

Se busca donde esta el Modelo Preentrenado

![Interfaz Buscar y Seleccionar Modelo](/imagenes_manual/interfaz_buscar_seleccionar_modelo.png "Interfaz Buscar y Seleccionar Modelo")

Se procede a correr el modelo

![Interfaz Boton Correr Modelo](/imagenes_manual/interfaz_correr_modelo.png "Interfaz Boton Correr Modelo")

Ejemplo de Salida Del Modelo

![Salida del Modelo](/imagenes_manual/salida_ejemplo.png "Salida del Modelo")
