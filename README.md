#cwrap-(py)thon

``` shell
# ____ _ _ _ ____ ____ ___     ___  _   _ 
# |    | | | |__/ |__| |__] __ |__]  \_/  
# |___ |_|_| |  \ |  | |       |      |   
#                                         
```

`cwrap(py)`, written in `(py)`thon. Nothing more than a handy file comment header utility that helps easily me see (with my old eyes) what file I am working on.  

# Install

Clone the `repo`:

``` shell
git clone https://github.com/TylerDurham/cwrap-python
```

I like to use `uv` to build and install:

``` shell
uv build
```

``` shell
uv tool install dist/cwrap*.whl  
```

**Note:** Shell completions can be added by running `cwrap --install-completion`

To remove, run `uv tool uninstall cwrap`.

# Usage

## Commands

### Help

Get help:

``` shell
cwrap --help
```

### Programming Languages

List supported languages:

``` shell
cwrap list-languages
```

### Figlets

#### Basic Usage

Generate a simple comment wrapped figlet header:

``` shell
cwrap figlet "Hello World"
```
This will output:

``` python
# _  _ ____ _    _    ____    _ _ _ ____ ____ _    ___  
# |__| |___ |    |    |  |    | | | |  | |__/ |    |  \ 
# |  | |___ |___ |___ |__|    |_|_| |__| |  \ |___ |__/ 
#                                                       
```

**Note:** The default figlet font is `cybermedium`. The default language is `python`.

#### Specifying a Figlet Font

To generate a simple comment wrapped figlet header with a *specific figlet font*, use the `-f` or `--font` option:

``` shell
cwrap figlet -f avatar "Hello World"
```
This will output:

``` python
#  _     _____ _     _     ____    _      ____  ____  _     ____ 
# / \ /|/  __// \   / \   /  _ \  / \  /|/  _ \/  __\/ \   /  _ \
# | |_|||  \  | |   | |   | / \|  | |  ||| / \||  \/|| |   | | \|
# | | |||  /_ | |_/\| |_/\| \_/|  | |/\||| \_/||    /| |_/\| |_/|
# \_/ \|\____\\____/\____/\____/  \_/  \|\____/\_/\_\\____/\____/
#                                                                
```

#### Specifying a Programming Language

You can also wrap with different programming languages:

``` shell
cwrap figlet -l lua "UPDATE TABLE"
```

This will output:

``` lua
-- _  _ ___  ___  ____ ___ ____    ___ ____ ___  _    ____ 
-- |  | |__] |  \ |__|  |  |___     |  |__| |__] |    |___ 
-- |__| |    |__/ |  |  |  |___     |  |  | |__] |___ |___ 
--                                                         
```

**Note:** You can run `cwrap list-languages` to get a list of supported programming languages.

#### Multiline Comments

If the programming language supports it, you can specify the `-m` or `--multiline` option to wrap the figlet text in a multiline comment:

``` shell
cwrap figlet -f avatar -l javascript -m "Hello World"
```
This will output:

``` javascript
/*
  _     _____ _     _     ____    _      ____  ____  _     ____ 
 / \ /|/  __// \   / \   /  _ \  / \  /|/  _ \/  __\/ \   /  _ \
 | |_|||  \  | |   | |   | / \|  | |  ||| / \||  \/|| |   | | \|
 | | |||  /_ | |_/\| |_/\| \_/|  | |/\||| \_/||    /| |_/\| |_/|
 \_/ \|\____\\____/\____/\____/  \_/  \|\____/\_/\_\\____/\____/
                                                                
*/
```
#### Horizontal Rules

You can add a horizontal rule at the top and bottom of the comment by specifying the `--hr-width` option:

``` shell
cwrap figlet "Hello, HR" -l javascript --hr-width
```

This will output:

``` javascript
/*
 ======================================
 _  _ ____ _    _    ____    _  _ ____ 
 |__| |___ |    |    |  |    |__| |__/ 
 |  | |___ |___ |___ |__|    |  | |  \ 
                                       
 ======================================
*/

```

#### Clipboard Support 

You can place the generated text on the clipboard by specifying the `-c` option:

``` shell
cwrap figlet "Hello, Clipboard" -c
```

# Local Development

## Using UV

Clone the `repo`:

``` shell
git clone https://github.com/TylerDurham/cwrap-python && cd cwrap-python
```

Create venv:

``` shell
uv venv
```

Run tests:

``` shell
uv run pytest
```

Run the project locally:

``` shell
uv run cwrap figlet "Hello"
```

## Using Pip

Clone the `repo`:

``` shell
git clone https://github.com/TylerDurham/cwrap-python && cd cwrap-python
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
