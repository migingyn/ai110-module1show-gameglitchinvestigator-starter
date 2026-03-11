# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

The game was set on normal mode as a default, where you input a value and only a value, no other inputs would work. The game gives you a hint and you continue until you guess correctly. The hint was incorrect relative to the secret value, as I had a secret value of 13, yet my hint told me to go lower than 11, expected to say "Go higher". The new game button doesn't function properly, you have to reload in order to play a new game rather than it restarting all in one session. Also, when you first run the game, the "Attempts" text stays the same number rather than decreasing until you attempt a new value.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude for this project. I used Claude to help explain the parsing that happens in the try except block in app.py, and utilized its suggestion of parsing from str to int, so that the hints are accurate according to user input. I verified by running some manual tests on the localhost and they have been correct so far. One incorrect suggestion was for the proper decrement and resulting UI change for attempts left, where although the attempts left matched the attempts allowed, the attempts list would fill up before attempts left became 0. The suggestion was to add feedback and force the attempts to rerender, and I just did a couple manual tests in the localhost which all failed. Also, the pytests generated would result in wrong outcomes.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided when a bug was really fixed when it met the functionality that I proposed for it, so no weird code logic, aligned with the goals of the UI/UX so something shouldn't be difficult to set up or hard to understand, and logic that would pass through multiple tests (both pytest and manual checks). One test I ran manually was checking if the New Game button would work properly by implementing the newly adjusted code and checking on the localhost if the button interacts and resets the session states so a new game can work well. This manual test showed me that initially the button only reset attempts to 0 and generated a new secret number, while leaving the previous session state's score, status, history, and feedback unchanged, carrying over into the new/current game. AI helped me design the pytests by running through agent mode and check for comments I previously had bugs over and fixed, which it would then create different tests that would check for all use cases of the functions. Running those tests with pytest would confirm if each fix was done correctly or still had an issue.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

In my own experience, I found that the secret number never changed for me, it was consistent throughout all my runs in each difficulty, but the hints it gave were inconsistent. The parsing of the input number was the reason for the fluctuating hints as it would parse an even number into a string and compare that to the secret number lexicographically instead of numerically. Streamlit "reruns" are like refreshes that reruns the entire python script during each interaction and session state holds the memory of the elements during your current run. Again, since I didn't have issues with a changing secret number, I worked on correcting the logic of the parsing so I removed the condition for even numbers to become strings instead focusing on parsing only into ints so that they are compared correctly without fluctuation.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I would want to reuse the habit of looking through suggestions and editting in parts to be more specific, so that AI doesn't fully run autonomous. I think being the driver rather than the passenger is a great way to learn from AI as it helps debug your code. I would honestly take what I have learned from this project about debugging, understanding code with AI, and the prompt engineering to coding tasks next time. Intially, I thought AI generated code would super complex, working but not as intended, and kinda rough around the edges, but by continuously prompting and prompting more specific instructions as well manual checks through this project, it really proves the efficiency and power of AI generated code as I would've have taken longer to learn, understand, and then attempt at debugging each issue than for AI to interpret to me the structure of the code.