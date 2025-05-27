# excellent-quote

Tiny Python **CLI** that spits out random wisdom from Kevin Kelly’s  
*Excellent Advice for Living*.

> ```bash
> pip install excellent-quote && excellent_quote
> ```
>
> ```bash
> ➜  ~  excellent_quote
> Being enthusiastic is worth 25 IQ points.
> ```

---

<div align="center">

[![PyPI](https://img.shields.io/pypi/v/excellent-quote?color=%2334D058)](https://pypi.org/project/excellent-quote)
[![License](https://img.shields.io/github/license/korakbhaduri/excellent-quote?color=%23FFC107)](LICENSE)

</div>

## Table of Contents

1. [Features](#features)  
2. [Installation](#installation)  
3. [Usage](#usage)  
4. [Embedding in Your Own Code](#embedding-in-your-own-code)  
5. [Customising Quotes](#customising-quotes)  
6. [Development Setup](#development-setup)  
7. [Releasing](#releasing)  
8. [Contributing](#contributing)  
9. [License](#license)  
10. [Acknowledgements](#acknowledgements)

---

## Features

* **One-liner install** – available on PyPI.  
* **Zero configuration** – ships with `quotes.csv` (≈460 aphorisms).  
* **Battle-tested CLI** built with [Click](https://palletsprojects.com/click/).  
* **Shell-friendly** – plain text to `stdout`, easy to pipe anywhere:
  * `excellent_quote | cowsay | lolcat`
  * `excellent_quote | say` (macOS TTS → “audio fortune-cookie”)  
* **Importable helper** – reuse the loader in notebooks, bots, or web apps.

---

## Installation

### 1 • PyPI (recommended)

```bash
pip install excellent-quote
```

Requires Python ≥ 3.8.


### From source (dev mode)
```bash
git clone https://github.com/korakbhaduri/excellent-quote.git
cd excellent-quote
python -m venv venv && source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e .
``` 

## Usage

```bash
# one random quote
excellent_quote

# three quotes
excellent_quote -n 3

# see all options
excellent_quote --help
```

### Fun pipes

```bash
excellent_quote | cowsay | lolcat          # rainbow ASCII cow 🐄
excellent_quote | say                      # macOS text-to-speech
# cron example: every day at 09:00
0 9 * * *  excellent_quote >> ~/kk_daily.log
```

### Module invocation

```bash
python -m excellent_quote.cli -n 2
```

## Embedding in Your Own Code

```python
import random
from excellent_quote.loader import load_quotes

quote = random.choice(load_quotes())
print(f"<blockquote>{quote}</blockquote>")
```

## Customising Quotes

1. Fork this repo.

2. Replace excellent_quote/quotes.csv with your own single-column CSV (quote).

3. Update pyproject.toml (name, version) if you plan to publish.

4. Build & upload your variant to PyPI — instant wisdom generator!

Tip: add a topic column, then extend cli.py with --topic creativity.

## Development Setup

```bash
python -m venv venv && source venv/bin/activate
pip install -e .[dev]      # once you add test / lint extras

# run tests (to be added)
pytest -q
```
Lint with ruff / black and enforce via pre-commit hooks.

## Releasing

```bash
# 1  Bump version in pyproject.toml
# 2  Tag & push
git tag v0.1.1 && git push --tags

# 3  Build & upload
python -m build
python -m twine upload dist/*
```

A GitHub Actions workflow (if added) can automate release creation.

## Contributing

PRs welcome – especially:

* New flags (--json, --topic, --format md/html)

* Additional quote sets or loaders

* Docs & typo fixes

Open an issue or ping @korakbhaduri.

## License

[MIT](LICENSE.txt) © 2025 Korak Bhaduri

## Acknowledgements

* Kevin Kelly for Excellent Advice for Living. All quotes © Kevin Kelly, excerpted from Excellent Advice for Living. Used here for educational/demo purposes.

* The Click maintainers for a stellar CLI framework.

* Everyone encouraging “ship tiny tools” culture on Twitter, Product Hunt, and Hacker News.