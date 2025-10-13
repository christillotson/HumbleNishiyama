# code to generate a heatmap based on our scored game data

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

GAME_ORDER = ['BBB', 'BBR', 'BRB', 'BRR', 'RBB', 'RBR', 'RRB', 'RRR']

def make_heatmap(scoring_method, card_df, GAME_ORDER = GAME_ORDER):
    heatmap_data = card_df.pivot(index='p1choice', columns='p2choice', values='p1_win_cards')

    # Create the heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap='viridis')

    # Labels and title
    plt.title("P1 Win Cards Heatmap")
    plt.xlabel("P2 Choice")
    plt.ylabel("P1 Choice")

    plt.show()
    return