# Math Game!

Math Game is a simple command-line arithmetic game that allows players to test and improve their mathematical abilities. Depending on the selected difficulty, players will face different arithmetic operations including addition, subtraction, multiplication, and division

![app_Screenshot](./assets/readme_media/website_Screenshot.jpg)

## Features:

- **Multiple Difficulty Levels:**

  - Players can choose from three difficulty levels - Easy, Medium, and Hard

    ![Multiple_Difficulty](./assets/readme_media/Start_Game_Overlay_image.jpg)

- **Varied Operations:**

  - Depending on the level, players will be tested on addition, subtraction, multiplication, and even division

    ![Varied_Operations](./assets/readme_media/Footer_image.jpg)

- **Score Tracking:**

  - The game keeps track of your score as you progress. Each correct answer increases your score

    ![Score_Tracking](./assets/readme_media/Game_Board_image.jpg)

- **Retry Mechanism:**

  - If you get an answer wrong, don't worry! The game allows for three wrong attempts before it's game over

    ![Retry_Mechanism](./assets/readme_media/Flipping_Animation_image.jpg)

## Features Left to Implement:

- Timer and Time's Up Message
  - Introduce a countdown timer that starts when the player begins the game.
    Display a "Time's Up" message when the timer reaches zero, indicating that the game is over.
    This feature would add a sense of urgency and challenge to the game
## Testing:

- During the development of Math Game, we used systematic testing to ensure that the game functions as intended and offers a seamless experience to users

 ### Manual Testing:
    - Name Input: Ensured that the game asks for the player's name and uses it during the gameplay
    -  Difficulty Levels: Tested whether all difficulty levels work as intended and increase in complexity
    - Score Tracking: Made sure that the game correctly tracks and displays the score
    - Retry Mechanism: Tested the mechanism that counts the number of wrong attempts and observed the game's response after three wrong answers

### Bugs:

#### Solved Bugs:

- Input Acceptance Bug
  - Earlier versions did not handle non-integer inputs for answers, leading to crashes. This was fixed using input validation
- Game Loop Issue:
  - Initially, when a player chose to not continue after game over, the game would unintentionally restart. This has been resolved.

#### Unsolved Bugs:

- No unsolved bugs

### Validator Testing:

- PEP 8 Online Validator:

  - Initially, there were a few line length violations, which have since been resolved [PEP8 herokuapp](https://pep8ci.herokuapp.com/)

## Deployment:

### Deployment
* From the Heroku dashboard, select dropdown menu “New” and “Create new app”.
* Name the app
* Set the region to “Europe”.
* Select “Create app”.
* Add Config Config Vars
    * Enter “PORT” in the KEY field.
    * Enter 8000 in the VALUES field.
* Add buildpacks
    * Select “Add buildpack”
    * Select “python”, “Add buildpack”
    * Select “nodejs“, Add buildpack”
    * Ensure the buildpacks are added in this order (python folowed by nodejs)
* Deploy the project 
    * Select “Deploy”
    * Select “Connect to GitHub”.
    * Search for the GitHub repository
    * Select “Connect”
    * Under “Manual Deploy”, select “Enable Manual Deploy”
