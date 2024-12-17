#!/usr/bin/python

import signal
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3
from PyQt5.QtWidgets import QApplication
import os


def quit(source):
    Gtk.main_quit()

def open_spinbutton_dialog(source):
    """Função que cria e exibe uma janela modal com um Gtk.SpinButton."""
    dialog = Gtk.Dialog(
        title="Adjust Value",
        modal=True  # Define como janela modal
    )
    dialog.add_buttons(Gtk.STOCK_OK, Gtk.ResponseType.OK, Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL)
    
    # Adicionando um SpinButton
    adjustment = Gtk.Adjustment(value=30, lower=0, upper=200, step_increment=1, page_increment=10, page_size=0)
    spin_button = Gtk.SpinButton(adjustment=adjustment, climb_rate=1, digits=0)
    spin_button.set_numeric(True)

    # Layout do conteúdo
    box = dialog.get_content_area()
    label = Gtk.Label(label="Escolha um valor:")
    box.add(label)
    box.add(spin_button)

    dialog.show_all()
    
    # Capturar a resposta do usuário
    response = dialog.run()
    if response == Gtk.ResponseType.OK:
        print(f"Valor escolhido: {spin_button.get_value()}")
    elif response == Gtk.ResponseType.CANCEL:
        print("Cancelado pelo usuário.")
    
    dialog.destroy()


def main():
    # Criação do indicador
    indicator = AppIndicator3.Indicator.new(
        "meu-indicador",                       # ID do indicador
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'logo.png'), 
        AppIndicator3.IndicatorCategory.APPLICATION_STATUS
    )

    # Criação do menu
    menu = Gtk.Menu()

    # Adicionando SpinButton (abre janela modal)
    item_spin = Gtk.MenuItem(label="Open SpinButton")
    item_spin.connect("activate", open_spinbutton_dialog)
    menu.append(item_spin)

    # Adicionando Exit
    item_quit = Gtk.MenuItem(label="Exit")
    item_quit.connect("activate", quit)
    menu.append(item_quit)

    # Mostrar o menu
    menu.show_all()

    # Associar o menu ao indicador
    indicator.set_menu(menu)

    # Exibir o indicador
    indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)

    # Manter o aplicativo rodando
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Gtk.main()

if __name__ == '__main__':
    main()

