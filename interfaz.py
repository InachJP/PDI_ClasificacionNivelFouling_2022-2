#!/usr/bin/python3
	
#Bibliotecas importantes
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import random
import tensorflow as tf
from PIL import Image
import os
import numpy as np



# Variables utiles para el archivo del modelo y la carpeta de fotos de testing que estan fuera del dataset de entrenamiento
modelo_file = ""
photos_dir=""

#Funcion que muestra el predict y el etiquetado del archivo
def clasificacion(predict,archivo):
    arch = archivo.split("_")
    if int(predict[0])==1:
        return "low",arch[0]
    elif int(predict[1])==1:
        return "mid",arch[0]
    elif int(predict[2])==1:
        return "high",arch[0]
    else:
        return predict, arch[0]

# Clase para realizar  la interfaz
class FileChooserWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Interfaz")

        box = Gtk.Box(spacing=6)
        self.add(box)

        #Cada boton llama a su funcion especifica
        #Boton para seleccionar la carpeta de imagenes
        button1 = Gtk.Button(label="Seleccionar Carpeta De Imagenes")
        button1.connect("clicked", self.on_folder_clicked)
        box.add(button1)
        #Boton para seleccionar el archivo del modelo preentrenado
        button2 = Gtk.Button(label="Seleccionar Modelo")
        button2.connect("clicked", self.on_file_clicked)
        box.add(button2)
        #Boton para correr el modelo
        button3 = Gtk.Button(label="Correr Modelo")
        button3.connect("clicked", self.modelo_cliente)
        box.add(button3)
        
    #Funcion que genera un dialog o un recuadro para seleccionar el archivo del modelo
    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
            title="Porfavor selecciona el archivo del modelo", parent=self, action=Gtk.FileChooserAction.OPEN
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OPEN,

            Gtk.ResponseType.OK,
        )

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            global modelo_file
            #Se establece el valor del archivo seleccionado por el usuario
            modelo_file = dialog.get_filename()
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def on_folder_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
            title="Porfavor Seleccione una Carpeta",
            parent=self,
            action=Gtk.FileChooserAction.SELECT_FOLDER,
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Seleccionar", Gtk.ResponseType.OK
        )
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select clicked")
            print("Folder selected: " + dialog.get_filename())
            global photos_dir
            #Se establece el valor de la carpeta seleccionada por el usuario
            photos_dir = dialog.get_filename()
            image = Gtk.Image()
            image.set_from_file(dialog.get_filename())
            
            self.add(image)
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
        dialog.destroy()
        
    # Codigo cliente para cargar el modelo
    def modelo_cliente(self,window):
        global modelo_file
        # Se carga el modelo seleccionado por el usuario
        model = tf.keras.models.load_model(modelo_file)
        global photos_dir
        # Lista de fotos del directorio
        dir_list = os.listdir(photos_dir)
        # Cantidad total de fotos
        cant = len(os.listdir(photos_dir ))

        # For para obtener un random de 10 fotos
        for i in range(0,10):
            # Random para obtener una foto de 0 hasta la cantidad de fotos
            rand = random.randint(0,cant)
            # Se abre la foto
            img = Image.open(photos_dir +"/" + dir_list[rand])
            # Se realiza un reescalado a la foto para que el modelo pueda obtenerlo
            img = img.resize((224, 224))
            # Se convierte la imagen a arreglo para que pueda ser leida por el modelo
            img = np.array(img)
            img = np.expand_dims(img, 0)
            # Se realiza la prediccion y se pasa a la funcion de clasificacion para obtener 
            # el resultado de la prediccion de manera mas legible y el etiquetado del archivo
            retorno = clasificacion(model.predict(img)[0],dir_list[rand])
            # Se muestra por pantalla la prediccion y el etiquetado
            print("La prediccion dice que es: ", retorno[0], " y en realidad es: ", retorno[1])
            


win =FileChooserWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
