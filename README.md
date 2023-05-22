# Poker_hand

## Description
This is a Python program that ranks two poker hands and determines which hand wins based on the standard poker hand rankings. The program implements the ranking algorithm according to the specified rules, considering different hand types such as Four of a kind, Full House, Triples, Two pairs, Pair, and Highest card.

## How to Use

1. Clone the repository to your local machine or download the source code files.
2. Make sure you have Python installed on your system.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the program using the following command:

    ```
    python poker.py [hand1] [hand2]
    ```

    Replace `[hand1]` and `[hand2]` with the poker hands you want to compare, using the following format:

    - Use uppercase letters for cards: A (Ace), K (King), Q (Queen), J (Jack), T (Ten), and numbers 2-9.
    - Each hand should consist of exactly 5 cards, separated by no spaces.

5. The program will display the result, indicating which hand wins or if it's a tie.

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

