#!/usr/bin/python3
	

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class FileChooserWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Interfaz")

        box = Gtk.Box(spacing=6)
        self.add(box)

        button2 = Gtk.Button(label="Seleccionar Carpeta De Imagenes")
        button2.connect("clicked", self.on_folder_clicked)
        box.add(button2)
        button3 = Gtk.Button(label="Seleccionar Modelo")
        button3.connect("clicked", self.on_file_clicked)
        box.add(button3)

    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
            title="Please choose a file", parent=self, action=Gtk.FileChooserAction.OPEN
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
            image = Gtk.Image()
            image.set_from_file(dialog.get_filename())
            
            self.add(image)
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
        dialog.destroy()

win =FileChooserWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
