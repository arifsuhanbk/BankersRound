# BankersRound

A minimal Python module demonstrating **Banker's Rounding (Round Half to Even)**.
This project is designed to showcase pytest test scripting ability and CI automation with GitHub Actions.

## What is Banker's Rounding?
Banker's rounding is "round-half-to-even":
- .5 values round to the nearest **even** digit
- Used in financial systems to reduce rounding bias

## Example
bankers_round(1.005) → 1.00  
bankers_round(1.015) → 1.02

## Running Tests
pytest -q
