# How to Start
``` bash
> pip install bleak
```
### Debug on MAC 
- no module of "_ctype"
https://github.com/pypa/pipenv/issues/4901

``` bash
# Get the device address and UUID by
python BLE_DiscoverDevice.py 

# Make the connection by 
python BLE_ConnectToArduino