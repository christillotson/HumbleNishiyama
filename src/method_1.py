import sys
import os
import numpy as np
import random

# class that generates a numpy array of numpy arrays of decks.

class DecksInt:
  def __init__(self, num_decks, random_seed = 440, write_decks_to_file = True, base_path = "../data/method_1/"):
    self.num_decks = num_decks
    self.random_seed = random_seed
    self.rng = np.random.default_rng(random_seed)
    self.decks = self.make_many_decks(self.num_decks)
    self.base_path = base_path

    if write_decks_to_file:
            self.save_decks()

  def make_one_deck(self):
    deck = np.repeat([0, 1], 26).astype(np.uint8)
    self.rng.shuffle(deck)
    return deck

  def make_many_decks(self, num_decks):
    deck_list = np.array([self.make_one_deck() for i in range(num_decks)])
    return deck_list

  def save_decks(self, max_decks_per_file = 500_000):
      num_decks = self.decks.shape[0]
      
      subdir = os.path.join(self.base_path, f"{num_decks}_decks_seed_{self.random_seed}")
      os.makedirs(subdir, exist_ok=True) 
            
      for i in range(0, num_decks, max_decks_per_file):
          # chunk = self.decks[i : i + max_decks_per_file]
          # filename = f"{base_filepath}decks_{i}-{i + chunk.shape[0]}.npz"
          chunk = self.decks[i : i + max_decks_per_file]
          start, end = i, i + chunk.shape[0] - 1
          filename = os.path.join(subdir, f"decks_{start+1}-{end+1}.npz")
          np.savez_compressed(filename, decks=chunk)
          print(f"Saved {filename} with {chunk.shape[0]} decks")
      return None