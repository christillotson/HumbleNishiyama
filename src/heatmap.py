import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

GAME_ORDER = ['BBB', 'BBR', 'BRB', 'BRR', 'RBB', 'RBR', 'RRB', 'RRR']
PLOTS_PATH = "./plots"

## This function written iteratively with ChatGPT
def make_heatmap(scoring_method, input_df, GAME_ORDER=GAME_ORDER, PLOTS_PATH=PLOTS_PATH):
    # Ensure output directory exists
    os.makedirs(PLOTS_PATH, exist_ok=True)

    # Scoring method should be "cards" or "tricks"

    card_df = input_df.copy()

    # Compute ratios
    card_df["p2_win_ratio"] = card_df[f"p2_win_{scoring_method}"] / card_df["times_run"]
    card_df["draw_ratio"] = card_df[f"draw_{scoring_method}"] / card_df["times_run"]

    # Pivot tables for heatmap and annotation
    win_data = card_df.pivot(index="p1choice", columns="p2choice", values="p2_win_ratio").reindex(index=GAME_ORDER, columns=GAME_ORDER)
    draw_data = card_df.pivot(index="p1choice", columns="p2choice", values="draw_ratio").reindex(index=GAME_ORDER, columns=GAME_ORDER)

    # Annotation text: "% wins (% draws)"
    annotations = win_data.copy().astype(str)
    for i in range(len(win_data)):
        for j in range(len(win_data.columns)):
            win_pct = float(win_data.iloc[i, j]) * 100
            draw_pct = float(draw_data.iloc[i, j]) * 100
            annotations.iloc[i, j] = f"{win_pct:.0f}({draw_pct:.0f})"

    # Plot heatmap
    plt.figure(figsize=(8, 8))
    ax = sns.heatmap(
        win_data,
        annot=annotations,
        fmt="",
        cmap="RdBu",
        center=0.5,
        cbar = False, # turns off the colorbar
        # cbar_kws={'label': 'P2 (Me) Win Probability'},
        linewidths=0.5,      # white gridlines
        linecolor='white'
    )

    # Add black box around highest win cell in each row
    for i, row in enumerate(win_data.index):
        j = win_data.loc[row].idxmax()  # column of max
        col_idx = win_data.columns.get_loc(j)
        ax.add_patch(plt.Rectangle((col_idx, i), 1, 1, fill=False, edgecolor='black', lw=2.5))

    # Sample size from first row
    sample_size = int(card_df["times_run"].iloc[0])

    # Labels and title
    plt.title(f"My Win % ({sample_size:,} simulations) \n by {scoring_method} \n Wins(Draws)")
    plt.xlabel("My Choice")
    plt.ylabel("Opponent Choice")

    # Save and show
    output_path = os.path.join(PLOTS_PATH, f"heatmap_{scoring_method}.png")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    # plt.show() # I think this makes it run infinitely

    print(f"✅ Heatmap saved to {output_path}") # eyecatching emoji
