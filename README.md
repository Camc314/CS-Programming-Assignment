# CS Programming Assignment - Snakes and Ladders Game

This project is writen in [Python](https://www.python.org/) and uses the [Turtle Graphics](https://docs.python.org/3/library/turtle.html) module.

## Getting started

1. Clone or download this repository.

   ```sh
   $ git clone https://github.com/Camc314/cs-programming-assignment
   $ cd cs-programming-assignment
   ```

2. Run the program.

   ```sh
   $ python3 main.py
   ```

## Requirements

```
Python Version > 3.9
```

This program may work on versions of Python earlier than 3.9, but has not been tested on them. If using on prior Python versions proceed with caution.

## Other

### To run the program with debug mode enabled:

```sh
$ python3 main.py --debug
```

This mode has increased logging.

### To run the tests

```sh
$ python3 test_utils.py
```

### Limitations

This program contains a customizable board size, however, due to the limitations of the Turtle module, the Snakes/Ladders sizes cannot be adjusted, this means that on some board sizes, the snake and ladders will not appear to be going to the correct locations. One possible resolution to this problem is to use a module to resize the Gifs as they are imported into the screen, however since no external libraries are allowed, this is not possible

### Features

- Fully adjustable board size
- Dark mode
- Debug mode
- Randomly placed snakes and ladders
- Restart game
- Track the number of wins or losses for each player
- Impossible gamemode

**Dark Mode 🌙**

Strained eyes? Play in dark mode and reduce the strain!

**Debug Mode 👨‍💻**

To use the debug mode simply run the program with the `--debug` flag. This mode shows traces for turtle pens, as well as outputing data such as the location of snakes and ladders

```sh
$ python3 main.py --debug
```

**Randomly placed snakes and ladders 🎲**

Every time the game is played, the location of the snakes and ladders are randomly generated based on the difficulty and board size to make the game more interesting and exciting to play

**Impossible gamemode**

Normal mode too... normal? Play the impossible mode, which is... impossible to win!
