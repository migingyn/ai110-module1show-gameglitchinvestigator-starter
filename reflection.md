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

I used Claude for this project. I used Claude to help explain the parsing that happens in the try except block in app.py, and utilized its suggestion of parsing from str to int, so that the hints are accurate according to user input. I verified by running some manual tests on the localhost and they have been correct so far. One incorrect suggestion was for the proper decrement and resulting UI change for attempts left, where although the attempts left matched the attempts allowed, the attempts list would fill up before attempts left became 0. The suggestion was to add feedback and force the attempts to rerender, and I just did a couple tests which all failed.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
