# Quizz Game

[View deployed game here](https://python-hangman.herokuapp.com/)

## Introduction

This project is a command-line application, build in Python and is deployed on Heroku using Code Institute's [mock terminal template](https://github.com/Code-Institute-Org/python-essentials-template).

### Game mechanics
The player informs his name before starting the game. After this, the first word is presented (in a dashed format) and the user begins to guess letters until either the word is completely found or they run out of attempts. The guess should be a single roman letter. If not, print an error message and give them another chance to enter a letter. The number of attempts is determined by the length of the word plus 3.

If the player guesses all the correct letters they gain 1 point. After the game is finished the player is given the choice to either play again or exit the game and the player can play the game until they found all 32 words.


![Game in different screen sizes](/documentation/images/python-hangman.png)

### Business goals addressed with this site:

- Build brand awareness;
- Catch customers' attention and entertain them;

### Customer needs:

- To have some fun with a hangman game.
- Challenge your knowledge about technology keywords.

## UX

### Ideal client:

- English speaking;
- Has interest about technology.;
- Likes hangman game kind of games;

### Player stories:
1. As a player, I want to be able to input my name.
2. As a player, I want to be able to see how many attempts I have to guess the word.
3. As a player, I want to be able to see all the letters I guessed.
4. As a player, I want to be warned if I try to guess a letter I've already guessed.
5. As a player, I want to see my current score.
6. As a player, I want to be able to play again after the game has finished without exiting the program.

### Features

1. Welcome Screen: 
    - The player is welcomed to the game and asked to input their name.
2. Main game:
    - The screen features an array of underscores ( _ ) to let the player knows how many letters are in the word.
    - The player can enter letters until they either guess all the letters correctly or run out of attempts.
3. Letters Guessed
  - As the game runs, the letters that the player has already guessed will be displayed on the screen so they know which ones they haven't tried yet. If they enter a letter that they have guessed before, they will be warned of this and have the chance to try again without losing an attempt.
4. Attempts remaining:
    - The number of attempts the player has left is displayed to let them know exactly how many attempts they have remaining.
5. Play again
    - Once the game is over and the player has either won or lost, they will be asked if they want to play again. If they choose Y, they will be brought back to a new game. If they choose anything else, the game finishes and a ‘thanks’ message is displayed.

### Features Left to Implement
- Features a hangman drawing that is completed little by little with every wrong guess. 
- Choose level of difficulty.
- Leaderboard. 

## Technologies Used
- <strong>Python</strong> programming language.
- <strong>Git hub</strong> for version control and host: https://omurilolima.github.io/quizz-game/  
- <strong>Gitpod</strong> for coding: https://gitpod.io/ 
- <strong>Google Sheets</strong> to store the list of words
- <strong>Google cloud</strong> was used to enable the APIs needed for this project.
- <strong>Google Drive</strong> and <strong>Notion</strong> for documenting.
- <strong>Pomodoro Tracker</strong> for measure my effort: https://pomodoro-tracker.com/

### Imported Libraries and Packages
- <strong>os</strong>: Create the clear_screen function to enhance user experience and achieve a cleaner look.
- <strong>Colorama</strong>: Add colour to the Python terminal.
- <strong>gspread</strong>: Link the program to Google Sheets to read words.

## Testing

Testing information can be found in separate [TEST.md file](/documentation/TEST.md)

### Code Validator Testing

- Code Institute Python Linter
    - No errors were found when passing through the Python Linter: https://pep8ci.herokuapp.com/
    
![Python Linter](/documentation/images/python-linter.png).

## Deployment

### Local Deployment
This project was developed using the [Gitpod IDE](https://gitpod.io/), committed to git and pushed to [GitHub](https://github.com).

If you are using another IDE, you can make a local copy of this repository by typing the following command in your terminal:
- `git clone https://github.com/omurilolima/hangman-python.git`

### How to run this project locally using Gitpod
To clone this project into Gitpod you will need:

1. Create a Github account at https://github.com/
2. Use the Chrome browser

Then follow these steps:
1. Install the [Gitpod Browser Extentions for Chrome](https://www.gitpod.io/docs/browser-extension/)
2. After installation, restart the browser
3. Log into [Gitpod](https://gitpod.com/) with your gitpod account.
4. Navigate to the Project GitHub repository
5. Click the green "Gitpod" button in the top right corner of the respository
6. This will trigger a new gitpod workspace to be created from the code in github where you can work locally.

Alternatively, you can create your own workspace using this repository clicking the button below:

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/omurilolima/hangman-python)

The live project can be found here - https://python-hangman.herokuapp.com/ 

### How to commit and push changes

To commit and push changes you need to follow these steps:
1. Run the "git add ." command on the terminal to add a change in the working directory to the staging area.
2. Run the "git commit" command on the terminal and add a message to help indentifing what this commit is about.
3. Run the "git push" command on the terminal to upload local repository content to a remote repository. Note that any new commits to the main branch will automatically update the site.

### Heroku Deployment
This project uses Heroku, a platform as a service (PaaS) that enables developers to build, run, and operate backend applications on cloud.

Deployment steps are as follows, after account setup:

- Select 'create new app" in the Heroku Dashboard.
- Your app name must be unique. Choose a region closest to you (EU or USA) and select Create App.
- In the Settings section, click 'Reveal Config Vars', set the value of KEY to PORT, set the value to 8000 and select add.
- Further down, to support dependencies, select Add Buildpack.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs an additional file in order to deploy properly.

- `requirements.txt`
    - You can find the requirements your file needs using the following command: 
    `pip3 freeze --local > requirements.txt`

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:

- In the Terminal/CLI, connect to Heroku using this command: heroku login -i
- Set the remote for Heroku: heroku git:remote -a <app_name> (replace app_name with your app, without the angle-brackets)
- After performing the standard Git add, commit, and push to GitHub, you can now type: git push heroku main
- The frontend terminal should now be connected and deployed to Heroku.

## Credits

### Code

In addition to the knowledge acquired in the [Professional Academy Diploma in Full Stack Software Development](https://www.ucd.ie/professionalacademy/findyourcourse/professional_diploma_in_software_development/) by [University College Dublin](https://www.ucd.ie/) and [Code Institute](https://codeinstitute.net/ie/), I also used the following sources to deal with specific points of this project:

- How to Print Colors in Python terminal: [Tutorial by GeekForGeeks](https://www.geeksforgeeks.org/print-colors-python-terminal/)

- Custom alert by [sweetalert2](https://sweetalert2.github.io/#configuration)
- How to [Shuffle an array](https://javascript.info/task/shuffle)
- How to [Perform Page Reload/Refresh in JavaScript When a Button is Clicked](https://www.freecodecamp.org/news/refresh-the-page-in-javascript-js-reload-window-tutorial/)

### Content

- Content by Murilo Lima

### Acknowledgments

- This project was inspired by my own experience of building digital products for tech companies as a Product Owner for the past 12 years.
- Python Hangman by <strong>Adam Gilroy</strong> was used as a benchmark: https://github.com/adamgilroy22/python-hangman
- Special thanks to my menthor <strong>Brian Macharia<strong>.

## Disclaimer

The content of this Website is for educational purposes only.