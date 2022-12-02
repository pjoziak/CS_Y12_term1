## Tasks

### Tasks 1
Write a program that would allow the user to enter a sequence of numbers of arbitrary length, and then:
1. compute (and output) the sum of the above sequence
2. find (and output) one longest increasing subsequence
3. find (and output) one longest monotone subsequence

Hint: use `any` structure, e.g.: 
```python
increasing_subsequences = [[0, 2, 4], [1, 2, 4]]
if any(2 in subsequence for subsequence in increasing_subsequences):
    # do not construct this subsequence
else:
    # do look for subsequence using 2.
```

### Task 2
Write a program that allows `n` players to join the participate a game. The rules of the game are as follows:
- the player states a number, and a dice is thrown;
- if he guessed the right number, he is awarded 3 points
- otherwise, if the parity of the numbers agree, he is awarded 1 point
- otherwise, he looses 2 points
- and then the next player's turn starts.
At certain moment of the game, a player may wish to resign. The program should then summarize the points of each of the player.

### Task 3
Write a random sentence generator, by concatenating components from the lists as in the following example:

```json
[
	["Application", "System", "Feature", "Mobile App", "Website"],
	["yields", "shows", "displays", "throws", "renders"],
	["invalid response", "error", "warning", "exception"],
	["when button was", "when page was", "when the window was", "then page link was"],
	["clicked", "visited", "opened", "showed", "refreshed"]
]
```

### Task 4
Write a tic-tac-toe game that's controlled with a text input. 