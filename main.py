#!/usr/bin/python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Handler:

    def about_button_is_clicked(self, button):
        ## The ".run()" method is used to launch the about window.
         ouraboutwindow.run()
        ## This is just a workaround to enable closing the about window.
         ouraboutwindow.hide()
    def apply_button_is_clicked(self, button):
        comboboxtext = builder.get_object("comboboxtext1")
        print(comboboxtext.get_active_text())

    def cancel_button_is_clicked(self, button):
        window.destroy()

## Nothing new here.. We just imported the 'ui.glade' file.
builder = Gtk.Builder()
builder.add_from_file("ui.glade")
builder.connect_signals(Handler())

ournewbutton1 = builder.get_object("button1")
ournewbutton2 = builder.get_object("button2")
ournewbutton3 = builder.get_object("button3")

window = builder.get_object("window1")

## Here we imported the Combo Box widget in order to add some change on it.
ourcomboboxtext = builder.get_object("comboboxtext1")

## Here we defined a list called 'default_text' which will contain all the possible items in the Combo Box Text widget.
default_text = [" integrated ", " dedicated ", " hybrid "]

## This is a for loop that adds every single item of the 'default_text' list to the Combo Box Text widget using the '.append_text()' method.
for x in default_text:
  ourcomboboxtext.append_text(x)

## The '.set.active(n)' method is used to set the default item in the Combo Box Text widget, while n = the index of that item.
ourcomboboxtext.set_active(0)

## We just imported the about window here to the 'ouraboutwindow' global variable.
ouraboutwindow = builder.get_object("aboutdialog1")

## Give that developer a cookie !
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()