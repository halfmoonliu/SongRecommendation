[![Python Continuous Integration with Github Actions](https://github.com/halfmoonliu/SongRecommendation/actions/workflows/cicd.yml/badge.svg)](https://github.com/halfmoonliu/SongRecommendation/actions/workflows/cicd.yml)

# Using Voice Prompt for Song Recommendation

This repository contains codes for deploying a voice-triggered song recommendation application (app). Ｗhen using the app, the user can **talk** about their feelings or conditions at moment, such as "I am waiting for my plane" or " I am feeing down today", and a song will be recommended and played on spotify. The user can also use the pull down

This is a collective project with the following contibutors: Jiwon Shin, halfmoonliu

The Following are an over view of the project:

1. Building the app locally.
  <br>a. main.py: taking the response of **chat GPT as input** and output **name of the song and artist**.

3. **Github actions setup for continuous integration**
  <br>b. _.github/workflows/main.yml_: Quality control actions are triggered when pushed/ pulled to main branch. After setting up the environment, actions of **installing packages**, **linting**, **testing**, **formatting** would be executed in order (specified in Makefile). 

4. **Other files for development environment settings**
  
  <br>c. _.gitignore_: specify file names to ignore.
  <br>d. _requirements.txt_: list required packages for the project.

5. **Description of the project**
   <br>e. _README.md_: THIS FILE, explaining the purpose and structure of the directory, with example output and code snippets.
