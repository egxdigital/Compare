# compare

## Requirements
- Assumes you have Python 3.10 installed and associated with the alias `python3` on your Linux system.

## Install
### 1. Clone repository 
Reccommended: Use `git clone` WITHOUT option `<directory>`
### 2. Run installation script

```bash
cd Compare/
./install
```
## Develop and Test
To test, install `compare` using instructions above then run tests using `pytest` in a virtual environment:

```
python3 -m virtualenv env
source env/bin/activate
pip install requirements.txt

pytest tests/
```

## Acknowledgements
- Thanks to StackOverflow user [fralau](https://stackoverflow.com/users/4334041/fralau) for solution to ['Create key/value pairs with argpase (python)'](https://stackoverflow.com/a/52014520)
