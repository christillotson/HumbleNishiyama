Project Penney 2 Million Deck Generation: Chris Tillotson and Katy Lenshin

Method 1: Generates a numpy array of numpy arrays of 'decks of cards.' The decks of cards are actually represented by the integers 0 and 1 and encoded into np.uint8, and these 'decks of cards' are saved in the (incredibly compressive) .npz file-types with a specified maximum of 500,000 decks per file.

Method 2: Generates a numpy array of strings, each string being '0' or '1', representing the deck. Then, a '1' is appended to a version of this array as a list, then all the strings are joined into one long string, then that string is turned into an integer (but a regular integer type, not np.uint8). All of these integers are stored in a very large numpy array, in a similar manner to the smaller 52 individual integer long numpy arrays are stored in a very large numpy array. They are then saved into npz file-types with a specified maximum of 500,000 decks per file.

Which method we prefer, and why:
These two methods to have an interesting tradeoff: Method 1 has better storage efficiency, likely due to the np.uint8 (Long Integer) type, while Method 2 is faster and more memory efficient. However, we value storage, especially at the scale of 2 million decks, over memory usage and speed, so we think Method 1 is superior.
