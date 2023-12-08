[![Python Continuous Integration with Github Actions](https://github.com/halfmoonliu/SongRecommendation/actions/workflows/cicd.yml/badge.svg)](https://github.com/halfmoonliu/SongRecommendation/actions/workflows/cicd.yml)

# Using Voice Prompt for Song Recommendation

This repository contains codes for **deploying a voice-triggered song recommendation application** (App). Ｗhen using the App, the user can **talk** about their feelings or conditions at moment, such as "I am waiting for my plane" or " I am feeing down today", and a song will be recommended and played on spotify. The user can also use a **pull-down menu get a recommended song played based on their mood** (e.g. happ, sad, chill...etc).

Below is a **walkthrough** of the App.




Project structural diagram:


Files:

1. Main Functions associated libraries .
  <br>a. _main.py_: the main function for the
  <br>b. _./libraries_:
      <br> i._
  

3. **Github actions setup for continuous integration**
  <br>b. _.github/workflows/main.yml_: Quality control actions are triggered when pushed/ pulled to main branch. After setting up the environment, actions of **installing packages**, **linting**, **testing**, **formatting** would be executed in order (specified in Makefile). 

4. **Other files for development environment settings**
  
  <br>c. _.gitignore_: specify file names to ignore.
  <br>d. _requirements.txt_: list required packages for the project.

5. **Description of the project**
   <br>e. _README.md_: THIS FILE, explaining the purpose and structure of the directory, with example output and code snippets.

This is a collective project with the following contibutors: @jiwonny29 (Jiwon Shin), @halfmoonliu (Yun-Chung Liu)
