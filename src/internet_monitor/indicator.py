#!/usr/bin/python

import signal
import gi
import threading
import time
import os
import requests  # Para verificar conexão com a internet

gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3
from PyQt5.QtWidgets import QApplication

# Variável global para armazenar o tempo limite em minutos
check_interval = 30
stop_checking = False  # Controle para encerrar a thread de verificação


def quit(source):
    global stop_checking
    stop_checking = True  # Para a thread de verificação
    Gtk.main_quit()


def open_spinbutton_dialog(source):
    """Função que cria e exibe uma janela modal com um Gtk.SpinButton."""
    global check_interval

    dialog = Gtk.Dialog(
        title="Adjust Value",
        modal=True  # Define como janela modal
    )
    dialog.add_buttons(Gtk.STOCK_OK, Gtk.ResponseType.OK, Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL)
    
    # Adicionando um SpinButton
    adjustment = Gtk.Adjustment(value=check_interval, lower=1, upper=200, step_increment=1, page_increment=10, page_size=0)
    spin_button = Gtk.SpinButton(adjustment=adjustment, climb_rate=1, digits=0)
    spin_button.set_numeric(True)

    # Layout do conteúdo
    box = dialog.get_content_area()
    label = Gtk.Label(label="Escolha o tempo limite (em minutos):")
    box.add(label)
    box.add(spin_button)

    dialog.show_all()
    
    # Capturar a resposta do usuário
    response = dialog.run()
    if response == Gtk.ResponseType.OK:
        check_interval = int(spin_button.get_value())
        print(f"Tempo limite atualizado para: {check_interval} minutos")
    elif response == Gtk.ResponseType.CANCEL:
        print("Configuração cancelada pelo usuário.")
    
    dialog.destroy()


def check_internet_and_restart():
    """Função que verifica conexão com a internet e reinicia o computador após X minutos."""
    global check_interval, stop_checking

    while not stop_checking:
        try:
            # Tenta se conectar ao Google para verificar a internet
            response = requests.get("https://www.google.com", timeout=5)
            if response.status_code == 200:
                print("Internet OK")
            else:
                raise Exception("Falha na conexão")
        except Exception as e:
            print("Sem internet. Iniciando contagem...")
            time_without_internet = 0
            while time_without_internet < check_interval and not stop_checking:
                time.sleep(60)  # Espera um minuto
                time_without_internet += 1
                try:
                    # Verifica novamente
                    response = requests.get("https://www.google.com", timeout=5)
                    if response.status_code == 200:
                        print("Internet restaurada.")
                        break
                except:
                    print(f"Aguardando... ({time_without_internet} minutos sem internet de {check_interval})")

            # Reinicia o computador se o tempo limite for atingido
            if time_without_internet >= check_interval:
                print("Reiniciando o computador por falta de internet...")
                
                if os.name == 'nt':
                    os.system("shutdown /r /t 0")
                else:
                    os.system("reboot")

        time.sleep(60)  # Verifica a cada minuto


def main():
    global stop_checking

    # Criação do indicador
    indicator = AppIndicator3.Indicator.new(
        "meu-indicador",                       # ID do indicador
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'logo.png'), 
        AppIndicator3.IndicatorCategory.APPLICATION_STATUS
    )

    # Criação do menu
    menu = Gtk.Menu()

    # Adicionando SpinButton (abre janela modal)
    item_spin = Gtk.MenuItem(label="Configurar Tempo Limite")
    item_spin.connect("activate", open_spinbutton_dialog)
    menu.append(item_spin)

    # Adicionando Exit
    item_quit = Gtk.MenuItem(label="Sair")
    item_quit.connect("activate", quit)
    menu.append(item_quit)

    # Mostrar o menu
    menu.show_all()

    # Associar o menu ao indicador
    indicator.set_menu(menu)

    # Exibir o indicador
    indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)

    # Iniciar thread para verificar a internet
    thread = threading.Thread(target=check_internet_and_restart, daemon=True)
    thread.start()

    # Manter o aplicativo rodando
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Gtk.main()
    stop_checking = True


if __name__ == '__main__':
    main()

