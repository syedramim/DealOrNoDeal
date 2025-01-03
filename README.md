# DealOrNoDeal

DealOrNoDeal is a Python-based simulation of the popular game show "Deal or No Deal." This project was developed by four students at Boston College to provide a statistical representation of the game, utilizing Python and various libraries to analyze decision-making under risk.

## Table of Contents
* [Project Structure](#project-structure)
* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)


## Project Structure
* **DealOrNoDeal.py**: Main script to run the game simulation without a GUI.
* **Calculation.py**: Calculates the offer based on the current round using data from `Dealorno.xlsx`.
* **Dealorno.xlsx**: Excel sheet used for data processing in `Calculation.py`.
* **Differentcases.py**: Demonstrates that the initial case choice does not affect the final outcome.
* **Montehall.py**: Simulates the Monty Hall problem to determine the impact of switching cases on winning probabilities.

## Features
* **Random Case Assignment**: Shuffles case values to ensure randomness in each game session.
* **User Interaction**: Allows players to pick cases, remove cases, and decide whether to take the deal or continue.
* **Statistical Analysis**: Provides expected value calculations and probability assessments for offers.
* **Monte Hall Simulation**: Analyzes the probability of winning when switching cases versus staying with the initial choice.

## Installation
1. **Clone the Repository:**  
   `git clone https://github.com/yourusername/DealOrNoDeal.git`

2. **Navigate to the Project Directory:**  
   `cd DealOrNoDeal`

3. **Install Required Libraries:**  
   Make sure you have Python installed, then run:  
   `pip install numpy openpyxl`

## Usage
1. **Run the Game Simulation:**  
   `python DealOrNoDeal.py`  
   Follow the on-screen prompts to pick cases and make decisions.

2. **Run Statistical Calculations:**  
   `python Calculation.py`  
   Processes data from `Dealorno.xlsx` to provide offer calculations based on the current round.

3. **Run Different Cases Analysis:**  
   `python Differentcases.py`  
   Demonstrates that your initial case choice does not affect the final outcome.

4. **Run Monty Hall Simulation:**  
   `python Montehall.py`  
   Simulates the Monty Hall problem to analyze the benefits of switching cases.

## Contributing
Contributions are welcome! To contribute:
1. **Fork the Repository**
2. **Create a New Branch:**  
   `git checkout -b feature/YourFeature`
3. **Commit Your Changes:**  
   `git commit -m "Describe your changes"`
4. **Push to the Branch:**  
   `git push origin feature/YourFeature`
5. **Open a Pull Request**
