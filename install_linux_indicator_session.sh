#!/bin/bash

# Defina as variáveis que você deseja substituir
HOME_DIR=$HOME  # Diretório home do usuário
PROGRAM_PATH=$(which internet-monitor-indicator)
PYTHON_NAME=$(python3 --version | awk '{print "python" $2}' | sed 's/\.[0-9]*$//')

# Caminho para o arquivo de serviço
SERVICE_FILE="$HOME_DIR/.config/autostart/internet-monitor-indicator.desktop"

# Conteúdo do arquivo de serviço (substitua os placeholders)
SERVICE_CONTENT="[Desktop Entry]
Type=Application
Name=Internet Monitor Indicator
Exec=$PROGRAM_PATH
X-GNOME-Autostart-enabled=true
Icon=$HOME_DIR/.local/lib/$PYTHON_NAME/site-packages/internet_monitor/icons/logo.png
Comment=Converts clipboard text to speech
Terminal=false
Path=$HOME_DIR
Categories=Utility;AudioVideo;
StartupNotify=true
"

# Cria o arquivo de serviço temporário e escreve o conteúdo nele
echo "$SERVICE_CONTENT" | tee $SERVICE_FILE > /dev/null

