# midi-controller



## Installing
```

sudo apt install liblo-dev
sudo apt-get install libasound2-dev
sudo apt-get install libjack-jackd2-dev

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