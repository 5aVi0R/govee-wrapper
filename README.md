# govee-wrapper

## What is it?
A python wrapper for the official Govee api

## Installation

##### Dependencies
 - requests

##### Local

`pip install git+https://github.com/5aVi0R/govee-wrapper.git@v<version>#egg=govee-wrapper`

##### PyPI
coming soon...

## Getting Started
##### Create Instance
`device = Govee("<api_key>,"<mac_address>","<model_number>")`

##### Commands List

`device.get_commands()`

`device.get_all_devices()`

`device.get_brightness()`

`device.get_color()`

`device.is_on()`

`device.is_online()`

`device.is_retrieveable()`

`device.is_controllable()`

`device.turn_on()`

`device.turn_off()`

`device.set_color()`

`device.set_brightness()`
## Capabilities
- Turn a device on or off
- Set the brightness of a device
- Set the color of a device
- Check a device current color
- Check a device brightness level
- Check if a device is online
- Check if a device is on or off
- Check if a device can be controlled
- Check if a device is retrievable
- Get all devices on your account
- Get all commands that can be done with a device
## Issues?
Create an [issue](https://github.com/5aVi0R/govee-wrapper/issues) and I will try my fastest to resolve it  
