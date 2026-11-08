# PLP Capstone Project: Multi-Tool CLI Toolkit

An interactive, menu-driven toolkit program that provides three useful tools within a resilient terminal dashboard.

## Included Tools
1. **Simple Calculator**: Handles basic mathematical calculations via conditional branch routing.
2. **Number Guessing Game**: A game logic implementation utilizing execution guess-tracking loops.
3. **Task Organizer**: Tracks temporary user directives inside an operations-responsive system list.

## How to Run
Run the toolkit from your project root directory with:
```bash
python toolkit.py
```

## Reflective Analysis
Building this capstone toolkit brought together basic controls, error isolation, and operational structures. The hardest element of the project design was maintaining list data safely between sequential iterations of the menu looping logic without letting subroutines reset data states accidentally. The trickiest bug happened when non-integer string data crashed the calculator routing engine, which required isolating the logic blocks inside protective try/except structural buffers. Given an additional week for modification, I would incorporate external JSON stream components to write lists permanently onto storage objects rather than keeping them temporarily inside running memory blocks.
