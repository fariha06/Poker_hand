# Poker_hand
This Python program implements an algorithm to rank two poker hands and determine the winner.

## Description
The program takes two poker hands as input and ranks them based on the following hand types, from best to worst:

- Four of a Kind
- Full House
- Triples
- Two Pairs
- Pair
- Highest Card

If two hands have the same hand type, the program compares the highest card value to determine the winner. If the highest card values are also the same, it's a tie.
The program is implemented in Python and can be run from the command line.

## Usage
To use the program, below steps are followed:

1. Ensure to have Python installed on your machine.

2. Clone this repository or download the `poker.py` file.

3. Open a terminal or command prompt and navigate to the directory containing the `poker.py` file.

4. Run the program by executing the following command:
Replace `[hand1]` and `[hand2]` with the poker hands you want to compare, represented as strings. Each card in the hand should be represented by its rank and suit. For example, "A" for Ace, "K" for King, "Q" for Queen, "J" for Jack, "T" for Ten, and "2" to "9" for the corresponding numbered cards. The cards should be provided in the order they were dealt.

5. The program will output the result indicating which hand wins or if it's a tie.

## Examples
Here are some example poker hands and their outcomes:

- `KQ23Q` vs. `TA3J7` => First hand wins!
- `KTQTT` vs. `AAQQT` => First hand wins!
- `AKKAA` vs. `222T2` => Second hand wins!
- `A3A46` vs. `K32KT` => First hand wins!
- `A3A46` vs. `258AA` => Second hand wins!
- `TA982` vs. `98TA2` => It's a tie!
- `32233` vs. `A4A5A` => First hand wins!

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

