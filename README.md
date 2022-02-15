# midi-controller



## Installing
```
poetry shell
poetry update
pip install cryptography
pip install Cython
sudo apt-get install libjack-dev

```

## Running
```
export CONFIG_FOLDER=/home/pi/midi-controller/config/
```

## Pytest from console
```
export PYTHONPATH=$PYTHONPATH:src/
pytest tests/
```