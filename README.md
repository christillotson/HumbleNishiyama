# HumbleNishiyama
Monte Carlo simulations of the Humble-Nishiyama randomness game, a variation of Penney's game. Testing different versions / rules / programming approaches of Humble-Nishiyama to determine changes in win-rate and also runtime efficiency. First major project of Automation &amp; Workflows (Fall 2025) taught by Ron Smith at the College of William &amp; Mary. 

## Quick Start (PROFESSOR SMITH)
Navigate to the top-level directory (HumbleNishiyama folder) of this repo and run the following commands:

`uv sync`

(to get some required libraries)

then to DO DATA GENERATION:

`uv run run_tests.py`

This will create the data folder locally, containing the deck files (.npz) for each method, as well as a log file (.txt) and summary of results (.txt) in a table. These results will also be printed to the terminal.

See our explanations for methods 1 and 2 in DataGeneration.md

then to DO DECK SCORING:

`uv run run_scoring.py`

This will run on a pre-defined set of 1000 decks, print the results of that, add it to the database, print the database contents, and write them to **data/db_out/database_output.csv**.

You may also read more about our scoring logic in **Scoring.md**
