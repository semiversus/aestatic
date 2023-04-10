# ÆStatic

There are still too few static website building tools out there. Here's mine.

## How to build the website
### Using `venv` and `pip`
* (Optionally) create a virtual environment (eg. `python3 -m venv .venv; source .venv/bin/activate`)
* install via `pip install .` (or `pip install -e .` if you want to work on the source code)
* run `aestatic` - result is in folder ./output

### Using `poetry`
* run `poetry shell` and then `poetry install`
* run `aestatic` - result is in folder ./output
* optionally install jupyter notebooks with tensorflow and others using `poetry install --with jupyter`