# Text to Speech Program

This package provides a text-to-speech client program to interact with the server `text-to-speech-program`.

## 1. Installing

### 1.1. Install the package pip

To install the package from `pypi`, follow the instructions below:


```bash
pip install clipboard-tts-client
```

Execute `which clipboard-tts-client` to see where it was installed, probably in `/home/USERNAME/.local/bin/clipboard-tts-client`.


### 1.2. Add clipboard-tts-client to the Linux start session

Adding client GUI program to Linux start session (`~/.config/autostart/clipboard-tts-client.desktop`)

```bash
curl -fsSL https://raw.githubusercontent.com/trucomanx/ClipboardTTSClient/main/install_linux_program_session.sh | sh
```

Adding bar indicator to Linux start session (`~/.config/autostart/clipboard-tts-indicator.desktop`)

```bash
curl -fsSL https://raw.githubusercontent.com/trucomanx/ClipboardTTSClient/main/install_linux_indicator_session.sh | sh
```

## 2. Using

If the program was not added to the Linux start session, then to start use the command below:

```bash
clipboard-tts-client
```

## 3. License

This project is licensed under the GPL license. See the `LICENSE` file for more details.
