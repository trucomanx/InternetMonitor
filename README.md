# internet-monitor

Program that reboot when pass X minuts.

## Install from source
Installing internet_monitor client program

```bash
git clone https://github.com/trucomanx/InternetMonitor.git
cd InternetMonitor
pip install -r requirements.txt
cd src
python3 setup.py sdist
pip install dist/internet_monitor-*.tar.gz
```

## Add a program to the Linux start session

Adding bar indicator to Linux start session (`~/.config/autostart/internet-monitor-indicator.desktop`)

```bash
curl -fsSL https://raw.githubusercontent.com/trucomanx/InternetMonitor/main/install_linux_indicator_session.sh | sh
```

## Using


```bash
internet-monitor
```

