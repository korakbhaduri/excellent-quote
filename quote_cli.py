#!/usr/bin/env python3
"""
Tiny CLI that prints one or more random quotes from Kevin Kelly's "Excellent Advice for Living".

Usage:
  python quote_cli.py               # prints 1 quote
  python quote_cli.py --count 3     # prints 3 quotes

Place the accompanying `quotes.csv` (one column named `quote`) in the same folder as this script,
or adjust the --csv option to point elsewhere.
"""

import csv
import pathlib
import random
import sys
from typing import List

import click

# --- Configuration ---------------------------------------------------------
DEFAULT_CSV = pathlib.Path(__file__).with_name("quotes.csv")

# --- Helpers ---------------------------------------------------------------

def load_quotes(csv_path: pathlib.Path = DEFAULT_CSV) -> List[str]:
    """Read the quotes from a CSV file (expects a `quote` column)."""
    if not csv_path.exists():
        sys.exit(f"Quotes file not found at {csv_path}. Download it and place alongside this script.")

    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row["quote"].strip() for row in reader if row.get("quote")]

# --- CLI -------------------------------------------------------------------

@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.option("-n", "--count", default=1, show_default=True, type=int, help="Number of random quotes to print.")
@click.option("--csv", "csv_path", type=click.Path(path_type=pathlib.Path), default=DEFAULT_CSV, show_default=False, help="Path to quotes.csv (one `quote` column).")
@click.version_option("0.1.0", prog_name="excellent-quote")
def main(count: int, csv_path: pathlib.Path) -> None:  # noqa: D401
    """Print **count** random quotes from *Excellent Advice for Living*."""
    if count < 1:
        click.echo("Count must be >= 1", err=True)
        raise SystemExit(1)

    quotes = load_quotes(csv_path)
    if not quotes:
        click.echo("No quotes found in CSV.", err=True)
        raise SystemExit(1)

    for i in range(count):
        click.echo(random.choice(quotes))
        if i < count - 1:
            click.echo()  # blank line between quotes


if __name__ == "__main__":  # pragma: no cover
    main()
