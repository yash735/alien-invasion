# Alien Invasion: Shoot em down!!
In Alien Invasion, the player controls a spaceship that appears at the bottom center of the screen. Use the arrow keys to move the ship right and left, and press the spacebar to shoot bullets. When the game begins, a fleet of aliens fills the sky and moves across and down the screen. Your goal is to shoot and destroy all the aliens. After clearing a fleet, a new, faster fleet appears. If an alien hits your ship or reaches the bottom of the screen, you lose a ship. The game ends when you lose three ships. Enjoy battling increasingly challenging alien fleets!

### Dependencies:
1. pygame
- I have a requirement.txt file where you can do this: pip install -r requirements.txt
- You could also create a virtual environment and install this, so that your device is clean.

### Running the game locally:
- Make sure to have a virtual environment (optional).
- cd into project folder.
- pip install -r requirements.txt.
- If you have a virtual environment, I already made a run.sh script to make it easier to run the program.
- The program should work as expected.

# Iterations:

### Iteration - 1
In the first iteration, the core game mechanics are established. The player can move the spaceship using the arrow keys and shoot bullets. The game runs smoothly, ensuring that the fundamental movement and shooting mechanics work as intended.

### Iteration - 2
This iteration introduces enemy elements to the game. A swarm of alien UFOs now moves toward the spaceship in a left-right-down pattern. The player can shoot the aliens, and when all are eliminated, a new swarm appears. If an alien UFO touches the spaceship or reaches the bottom of the screen, the game resets with a new swarm, and the spaceship returns to its starting position. However, if this happens three times, the game freezes, preventing further gameplay.

### Iteration - 3

The game now includes a play button to initiate gameplay. Instead of freezing upon game over, the player is presented with an option to restart and play again. Sound effects are introduced to enhance the experience, including effects for shooting, alien destruction, and game over. A scoring system is implemented, displaying both the current score and the highest score achieved. Additionally, levels are introduced, increasing the game's difficulty as the player progresses.

### Iteration - 4

Implementing AI to make it learn and play the game on it's own.


# COPYRIGHT:
This code was inspired and taken from: Python Crash Course, 3rd Edition: A Hands-On, Project-Based Introduction to Programming by Eric Matthes.


