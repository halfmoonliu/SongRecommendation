[![Python Continuous Integration with Github Actions](https://github.com/halfmoonliu/SongRecommendation/actions/workflows/cicd.yml/badge.svg)](https://github.com/halfmoonliu/SongRecommendation/actions/workflows/cicd.yml)

# Using Voice Prompt for Song Recommendation

This repository contains codes for **deploying a voice-triggered song recommendation application** (App). Ｗhen using the App, the user can **talk** about their feelings or conditions at moment, such as "I am waiting for my plane" or " I am feeing down today", and a song will be recommended and played on spotify. The user can also use a **pull-down menu get a recommended song played based on their mood** (e.g. happy, sad, chill...etc).

Below is a **walkthrough** of the App.




Project structural diagram:


Files in the repo:

1. Main Functions associated libraries .
  <br>a. _main.py_: the main function for the
  <br>b. _./libraries_:
      <br>i.   _speech2text.py_: **tranforms user's input** voice into **text**. 
      <br>ii.  _GPR_prompt.py_: uses transfomed user input to **prompt chat GPT** and **returns song recommendations received**.
      <br>iii. _parser.py_: output **one song name** and the corresponding **artist name** by parsing chat GPT's response.
      <br>iv.  _spotifyFunc.py_: takes a **song name** and an **artist name** and feed them to **Spotify API** and output **spotify soundtrack playing URL**.
      <br>v.  _songDB.py_: contains functions for **building a song database** and **querying song names and artist names** based on **user input mood**.

3. **Github actions setup for continuous integration**
      <br>c. _.github/workflows/main.yml_: Quality control actions are triggered when pushed/ pulled to main branch. After setting up the environment, actions of **installing packages**, **linting**, **testing**, **formatting** would be executed in order (specified in Makefile). 

4. **Other files for development environment settings**
      <br>d. _.gitignore_: specify file names to ignore.
      <br>e. _requirements.txt_: list required packages for the project.

5. **Description of the project**
   <br>f. _README.md_: THIS FILE, explaining the purpose and structure of the directory, with example output and code snippets.

This is a collective project with the following contibutors: @afraa-n (Afraa Noureen), @BobZhang26 (Bob Zhang), @jiwonny29 (Jiwon Shin), and @halfmoonliu (Yun-Chung (Murphy) Liu).
