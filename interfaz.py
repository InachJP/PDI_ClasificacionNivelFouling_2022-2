#!/usr/bin/python3
	

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import random
import tensorflow as tf
from PIL import Image
import os
import numpy as np




modelo_file = ""
photos_dir=""
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

class FileChooserWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Interfaz")

        box = Gtk.Box(spacing=6)
        self.add(box)

        button1 = Gtk.Button(label="Seleccionar Carpeta De Imagenes")
        button1.connect("clicked", self.on_folder_clicked)
        box.add(button1)
        button2 = Gtk.Button(label="Seleccionar Modelo")
        button2.connect("clicked", self.on_file_clicked)
        box.add(button2)
        button3 = Gtk.Button(label="Correr Modelo")
        button3.connect("clicked", self.modelo_cliente)
        box.add(button3)
        

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
            photos_dir = dialog.get_filename()
            image = Gtk.Image()
            image.set_from_file(dialog.get_filename())
            
            self.add(image)
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
        dialog.destroy()
        
    def modelo_cliente(self,window):
        global modelo_file
        model = tf.keras.models.load_model(modelo_file)
        global photos_dir
        dir_list = os.listdir(photos_dir)
        #plt.figure()
        cant = len(os.listdir(photos_dir ))

        for i in range(0,10):
            rand = random.randint(0,cant)
            img = Image.open(photos_dir +"/" + dir_list[rand])
            img = img.resize((224, 224))
            img = np.array(img)
            img = np.expand_dims(img, 0)
            retorno = clasificacion(model.predict(img)[0],dir_list[rand])
            print("La prediccion dice que es: ", retorno[0], " y en realidad es: ", retorno[1])
            #plt.imshow(Image.open(photos_dir+'/' + dir_list[rand]))
            #plt.axis('off')
            #plt.title('\n\n{}'.format("La prediccion dice que es: ", retorno[0], " y en realidad es: ", retorno[1]), fontdict={'size': 16})
            #plt.show()


win =FileChooserWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
