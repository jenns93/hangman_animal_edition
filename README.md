# Hangman Animal edition
![](/assests/images/all-devices-mockup.png)
- [Live Website](https://hangman-animal-edition.herokuapp.com/)
- [Github Repository](https://github.com/jenns93/hangman_animal_edition)
 # About
Classic Hangman game, running in the Code Institute mock terminal on Heroku.

Players need to guess the correct word before the hangman picture is complete.
## Table of Contents

- [How To Play](#How-To-Play)

- [User Experience UX](#User-Experience-UX)

- [Features](#Features)

- [Technologies Used](#Technologies-Used)

- [Testing](#Testing)

- [Deployment](#Deployment)

- [Bugs](#Bugs)

- [Credits](#Credits)

## How To Play
Players can select between three difficulties, easy, medium, and hard.
Players will then have nine attempts to guess a letter in the animal word before the hangman picture is complete and the game is over.

## User Experience UX
### User Stories
i. As a user, I am looking to play a classic version of Hangman.
1. I want the layout of the game to be simple to navigate through.
2. I want the game to have a retro design.
3. I want to be able to see the results as I play.
4. I want to be able to see what stage of the Hangman I ‘am at.

ii. As a user who has never played this game before.
1. I don't want it to be too difficult.
2. I want the game to tell me what the word was if I lose.
3. I want to be able to see what correct letters I have guessed.
4. I want to be informed if I have already guessed a letter before.


iii. As a user who is well versed in the game.
1. I want to be able to play on a higher difficulty.
2. I want the game to tell me if I have guessed correctly or not.
3. I want the game to have a retro/arcade feel.

## Features
![Title-screen](/assests/images/hangman-title-screenshot.png)
- Users are welcomed to the game with the title screen displaying the game title and prompting the to initiate the game.
- Players will then need to select between three difficulties, easy, medium, and hard. As difficulty increases animal words that are more obscure and or longer words are selected from the word dictionary.
- Players are then asked to provide their letter guess.
- When guess is submitted the program will give feedback on whether the input was valid then whether the letter guessed was in the word.
- If players guess was correct the word is displayed with the correct letter visible, and the letters still not guessed hidden with an underscore.

![](/assests/images/hangman-game-screenshot.png)
- If input is not in the word the hangman picture is displayed along with a wrong answer counter.
- The hangman picture is iterated through as users get wrong answers until the last stage of the picture is displayed.
- Game over is displayed when the player reaches nine wrong answers without completing the word, the word they were attempting to guess is also displayed.
![Title-screen](assests/images/hangman-gameover-screenshot.png)
- If the player guesses all of the letters in the word, then WINNER is displayed.
![](/assests/images/hangman-winner-screenshot.png)
- Win or Lose when the game is complete the player is asked whether they want to play again, yes or no.
- If yes is selected the player is brought back to the difficulty menu.
- If no is selected the player is returned to the title screen.  

### Future Features
- An expansion of the word dictionary.
- Additional difficulty levels.
- Addition text graphics.
## Technologies Used

### Languages Used

- Python

### Frameworks, libraries, and programs used

-[Heroku](https://dashboard.heroku.com/apps) Heroku was used to host the files and to publish the finished program.

-[Gitpod](https://www.gitpod.io/) Gitpod was used to code the website and commit changes throughout the development to Github.

## Testing

### Functionality Testing
Invalid inputs have been entered into all options and navigational inputs throughout the game such as:
- Strings too long.
- Strings too short.
- Integers.
- Valid word plus space.
Game inputs for letter guesses have also been tested such as:
- integers.
- Strings too long.
- Strings too short.
- Valid word plus space.
- Already guessed letters.
- All input testing returns correct and expected responses.
### Validator Testing 
- PEP8. No errors were returned from PEP8online.com

### Usability Testing

-

### Testing User Stories

i. As a user, I am looking to play a classic version of Hangman.
1. I want the layout of the game to be simple to navigate through.
- The game has clear prompts to navigate through with ease.
2. I want to be able to see the results as I play.
- The player is provided with feedback on wrong guesses / correct guesses.
3. I want to be able to see what stage of the Hangman I ‘am at.
- The Hangman picture is displayed in corresponds with how many wrong guesses the player has submitted.

ii. As a user who has never played this game before.
1. I do not want it to be too difficult.
- The player is provided with an easy difficulty.
2. I want the game to tell me what the word was if I lose.
- Win or lose the game will display what the word was at the end of play.
3. I want to be able to see what correct letters I have guessed.
- The game displays each letter of the word as underscores unless correct letter has been submitted. e.g., "_","o","_".  
4. I want to be informed if I have already guessed a letter before.
- Right or wrong the player will be informed if they have already guessed the letter. 

iii. As a user who is well versed in the game.
1. I want to be able to play on a higher difficulty.
- The player has the choice of three levels of difficulty: easy/med/hard.
2. I want the game to tell me if I have guessed correctly or not.
- The player is always informed whether the letter they have guessed is right or wrong.
3. I want the game to have a retro/arcade feel.
- As the game is run in the Code Institute mock terminal it lends to an arcade/retro design.

## Deployment
### Heroku
The program has been deployed using Code Institute mock terminal for Heroku.
#### Steps for deployment:
- Fork or clone the repository.
- Create a new Heroku app.
- Set the build backs to Python and Nodejs in this order.
- Link the Heroku app to the repository.
- Click Deploy. 

### Forking the GitHub Repository
To contribute you can Fork without affecting the main branch. Follow the instructions outlined below.

1. Go to GitHub and log in.
2. Find the Repository that was used for this project.
3. To the right of the Repository name you will see the 'Fork' button. This is located next to the 'Start' and 'Watch' buttons.
4. Doing this will place a copy in your own repository.
5. When you are finished locating the 'New Pull Request' button above the file list on the original repository.

### Cloning
- To clone or download the repository to your own device follow the instructions listed below.

1. Head to Github and log in.
2. Find the Repository for this site.
3. Below the name of the repository find the 'Clone or Download' green button.
4. To clone the repo using HTTPS click the link below "Clone with HTTPS".
5. Open your Terminal and go to the directory you want the cloned directory to be copied to.
6. Enter "Git Clone" and paste the URL copied from GitHub.
7. Create your local clone by pressing "Enter".

## Bugs
### Solved Bugs
- Each time correct letter was submitted to correct list it would print for example "_","i","_","p","i","_","p","i","g".
- This was resolved by clearing the list at the end for the for loop which was latter made into a function to reduce length of program code.
### Remaining Bugs
- No known bugs remaining at time of writing.

## Credits

#### Code

- Code institute walkthrough “love Sandwiches” for Python structure layout 
- Code institute Python essentials. 
- Stackoverflow for tips, examples concepts for further understanding of language definitions.
- w3schools for tips, examples concepts for further understanding of language definitions.
- GeeksforGeeks for examples for understanding language better.

#### Content

- All code written by the author - Jack Jenns

- To create the README file inspiration was taken from:

- Code Institute [SampleREADME](https://github.com/Code-Institute-Solutions/SampleREADME)
- Code Institute [README Template](https://github.com/Code-Institute-Solutions/readme-template)
- [Markdown cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

### Acknowledgements
- Stackoverflow.
- Fellow students on slack.
- My mentor for his guidance.
- W3schools. 
- GeeksforGeeks

