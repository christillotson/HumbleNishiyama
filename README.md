## Overview

### Authors

We are Katy Lenshin and Christopher Tillotson, students in Dr. Ron Smith’s Automation & Workflows class during the Fall 2025 semester. 

### Description

Penney’s Game is a game played with two players named after its creator, Walter Penney, wherein Player One chooses a 3-long sequence of coin faces (for example, heads-heads-tails, tails-heads-tails, etc). After seeing Player One’s decision, Player Two chooses their own 3-long sequence of coin faces. A coin is tossed over and over, and its order is recorded. A player wins when the coin falls in their order.

The Humble-Nishiyama variant of the game is played with a fair deck of 52 cards, and instead of generating sequences based on coin faces, they are chosen based on card color: Black or Red. The cards in the deck are dealt out one by one, and the game does not end after only one win, but after all 52 cards have been exhausted. For each time a player’s sequence occurs in the cards, the player scores a ‘trick’, and each time a player scores a trick, the player earns the number of cards placed down since the last trick was scored — these are the two methods of ‘winning’ in the game.

Penney’s Game and the Humble-Nishiyama variant are not games of chance, however — Player Two can greatly increase their chances of winning by selecting a sequence based on the choice made by Player One. The best option for Player Two is to choose a sequence whose first object is the opposite of the middle object of Player One’s sequence, which should then be followed by the first two options made by Player One (EX: P1: THT, P2: TTH).

In this repository, we have performed a mass number of Monte-Carlo simulations in order to see each player’s chances of winning, both by tricks and by cards, for each valid combination of the Humble-Nishiyama game. We first generated millions of randomized decks of 52 cards, and then simulated all valid Humble-Nishiyama games on these decks of cards. We tracked the number of wins and draws each player made in each game, in both their number of cards and number of tricks won. Finally we generated two heatmaps (one for tricks and one for cards), depicting the percentage of wins and draws for Player Two in each valid game combination.

We see in these heatmaps that the top winning sequence, when scoring by cards, differs in some places, and overall the sequence win probabilities differ. This is obviously attributed to the difference in scoring method, but the reasons behind these differences are unclear and are worth investigating in the future.


A "Quickstart" guide, telling a new user what they need to do to run your code and reproduce your results. Assume they already know what Python is, but link to the UV documentation in case the user does not know what UV is.

## Quickstart

This project utilizes UV for library management. UV is a tool that is faster than pip and is our preferred way of preserving packages and versioning to ensure that this project can work on any machine. You can read more about it here:

https://docs.astral.sh/uv/

Once UV is installed,

Navigate to the top-level directory (HumbleNishiyama folder) of this repo and run the following command in your terminal to get required libraries:

`uv sync`

then to GENERATE + SCORE NEW DECKS and SEE Win(Draw) PROBABILITIES HEATMAP:

run the command 

`uv run augment_data.py` 

and enter in the input as prompted.

This will score x number of new decks. The scores of each combination are stored in the database file in ./src/db_code/database/HN_DB. These can be viewed in the generated plots in ./plots, as heatmap_cards and heatmap_tricks.
