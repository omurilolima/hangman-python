## User Stories Testing
ID | Player stories | Requirement met |
| - | --------- | --------------- |
| 1 | As a player, I want to be able to input my name. | Yes | 
| 2 | As a player, I want to be able to see how many attempts I have to guess the word. | Yes | 
| 3 | As a player, I want to be able to see all the letters I guessed. | Yes |
| 4 | As a player, I want to be warned if I try to guess a letter I've already guessed. | Yes |
| 5 | As a player, I want to see my current score. | Yes |
| 6 | As a player, I want to be able to play again after the game has finished without exiting the program. | Yes |

## Program Validation Testing
Section Tested | Input To Validate | Expected Outcome | Pass/Fail
| - | --------- | --------------- | - | 
| Start Program	| N/A |	Load welcome message and prompt user to enter name |	PASS
| Enter Name	| Input "Murilo" |	Move on to the game + presents "Good luck, {username}!" | PASS
| Guess a letter |	Input a number	| Error message warning to enter a single letter. | PASS
| Guess a letter |	Input two letters	| Error message warning to enter a single letter. | PASS
| Guess a letter |	Press enter with no input	| Error message warning to enter a single letter. | PASS
| Guess a letter |	Correct letter	| Display the letter in the correct space of the dashed word | PASS
| Guess a letter |	Correct letter	| Display the letter in the "Guessed letters" list | PASS
| Guess a letter |	Correct letter	| Subtract 1 from "Attempts remaining" | PASS
| Guess a letter |	Incorrect letter	| Subtract 1 from "Attempts remaining" | PASS
| Guess a letter |	Incorrect letter | Display the letter in the "Guessed letters" list | PASS
| Guess a letter |	Letter already guessed	| Error message: "letter" was already guessed. Try another letter.| PASS
| Play Again after make a point | "Y" | Start a new game manteining the score | Pass
| Play Again after game over | "Y" | Start a new game with score = 0 | Pass
| Play Again | Input anything other than "Y" | Exit the program | Pass