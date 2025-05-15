#cwrap-python

``` shell
# ____ _ _ _ ____ ____ ___  ___  _   _ 
# |    | | | |__/ |__| |__] |__]  \_/  
# |___ |_|_| |  \ |  | |    |      |   
#                                      
```

`cwrap(py)`, written in `(py)`thon. Nothing more than a handy file comment header utility that helps easily me see (with my old eyes) what file I am working on.  

# Install

Clone the `repo`:

``` shell
git clone https://github.com/TylerDurham/cwrap-python
```

I like to use `pipx`:

``` shell
pipx install .  
```

To remove, run `pipx uninstall cwrappy`.

# Local Development

Clone the `repo`:

``` shell
git clone https://github.com/TylerDurham/cwrap-python
```

Create the `python` virtual environment:

``` shell
python3 -m venv .venv
```

Source the `python` environment:

``` shell
source .venv/bin/activate
```

Install `required packages`:

``` shell
pip install -r requirements.txt
```

Install to the `virtual environment` for testing:

``` shell
pip install -e .
```
