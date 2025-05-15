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

# Usage

## Commands

### Help

Get help:

``` shell
cwrappy --help
```

### Programming Languages

List supported languages:

``` shell
cwrappy list-languages
```

### Figlets

Generate a simple comment wrapped figlet header:

``` shell
cwrappy figlet "Hello World"
```

The default figlet font is `cybermedium`.

To generate a simple comment wrapped figlet header with a *specific figlet font*, use the `-f` or `--font` option:

``` shell
cwrappy figlet -f avatar "Hello World"
```

If the programming language supports it, you can specify the `-m` or `--multiline` option to wrap the figlet text in a multiline comment:

``` shell
cwrappy figlet -f avatar -m "Hello World"
```


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
