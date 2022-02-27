![alt text](https://github.com/bartoz1/RaspberryDisplay/blob/main/demo_display.png?raw=true)
# Raspberry Pi Oled System Monitoring

Simple python module for displaying information about Raspberry Pi on SH1106 display.
### Displayed info
* Memory used / memory available [MB]
* Memory usage [%]
* CPU temperature [C]
* CPU usage [%]
* IP adress
* Result of MySQL query (optional)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install git+https://github.com/bartoz1/RaspberryDisplay.git#egg=raspberrydisplay
```

## Usage

```bash
python -m raspberrydisplay
```
When the button is clicked, the display shows information for 5 seconds and then turns off. This time can be changed in the config.ini file.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
