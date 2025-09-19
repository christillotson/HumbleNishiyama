import sys
import os
import numpy as np
import random

class DecksInt:
  """
  class that generates a numpy array of numpy arrays of 'decks of cards.'
  The decks of cards are actually represented by the integers 0 and 1,
  and these 'decks of cards' are saved in .npz files with a specified maximum of 500,000 decks per file.
  """
  def __init__(self, num_decks, random_seed = 440, write_decks_to_file = True, base_path = "./data/method_1/"):
    self.num_decks = num_decks
    self.random_seed = random_seed
    self.rng = np.random.default_rng(random_seed)
    self.decks = self.make_many_decks(self.num_decks)
    self.base_path = base_path

    if write_decks_to_file:
            self.save_decks()

  def make_one_deck(self) -> np.array:
    """
    Function that makes a numpy array of 26 0s and 1s (in integer format), 
    then shuffles it based on the prior defined random seed.
    """
    deck = np.repeat([0, 1], 26).astype(np.uint8)
    self.rng.shuffle(deck)
    return deck

  def make_many_decks(self, num_decks: int) -> np.array:
    """
    Function that makes a numpy array *of* numpy arrays, each containing a randomized deck of 'cards' (0 and 1 integers).
    num_decks (int): the number of decks to be generated.
    """
    deck_list = np.array([self.make_one_deck() for i in range(num_decks)])
    return deck_list

  def save_decks(self, max_decks_per_file = 500_000) -> None:
      """
      Function that, if specified, will save the generated decks as .npy files in the data/method_1 directory into subfolders identifying 
      1. the number of decks generated
      2. the random seed of those generated decks.
      The function will generate the subfolder if it doesn't exist, 
      and tests run with the same num_decks and random seed will overwrite existing files.
      max_decks_per_file specifies how many decks of cards will exist in one file, for example 
      2,000,000 decks will be divided into 4 files. This is in order to respect GitHub file size limits.
      """
      num_decks = self.decks.shape[0]
      
      os.makedirs(self.base_path, exist_ok=True)
      subdir = os.path.join(self.base_path, f"{num_decks}_decks_seed_{self.random_seed}")
      os.makedirs(subdir, exist_ok=True) 

      for i in range(0, num_decks, max_decks_per_file):
          
          chunk = self.decks[i : i + max_decks_per_file]
          start, end = i, i + chunk.shape[0] - 1
          filename = os.path.join(subdir, f"decks_{start+1}-{end+1}.npz")
          np.savez_compressed(filename, decks=chunk)
          
      return None