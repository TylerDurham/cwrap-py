
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

**Important**: Source the venv

``` shell
source .venv/bin/activate
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

## Maintenance

### Bump the version

``` shell
uv run bumpver update --patch
uv run bumpver update --minor
uv run bumpver update --major
```
