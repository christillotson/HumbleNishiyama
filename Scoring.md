How scoring logic works:
- We first have written a function that imports some amount of generated decks as a numpy array of numpy arrays
    (ex: [[0,1,1,0,1, ...],[1,0,0,1,0,...]])
- We then wrote a function that scores one deck which is inputted as a numpy array. For this deck we
    1. Iterate through the entire deck starting at index 0, and append each 'card' (0 or 1) to a list called running_sequence.
    2. As soon as len(running_sequence) > 3, we check its final 3 items.
    3. If those three final items are identical to a player's input combination of cards, we add +1 to the counter signifying the number of tricks they have won, and we add the length of the running sequence to the counter signifying the number of cards they have one. We then reset the running_sequence to an empty list, and continue the process.
    4. At this point we have 

Other approaches we tried: