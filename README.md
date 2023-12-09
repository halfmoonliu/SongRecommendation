[![Python Continuous Integration with Github Actions](https://github.com/halfmoonliu/SongRecommendation/actions/workflows/cicd.yml/badge.svg)](https://github.com/halfmoonliu/SongRecommendation/actions/workflows/cicd.yml)

# Using Voice Prompt for Song Recommendation

## Objectives

This repository is dedicated to the development of a **voice-triggered song recommendation application** (App). Our primary aim with this project is to empower users to effortlessly convey their current emotions or situations using **voice** commands, such as "I am waiting for my plane" or "I am feeling down today." Subsequently, the App will intelligently recommend and play a suitable song from Spotify that aligns with the user's mood. Furthermore, users have the option to choose a specific mood from a predefined set of six moods, including happy, sad, energetic, calm, anxious, and chill, via a **user-friendly pull-down menu**.

A crucial aspect of this project involves leveraging a cloud-based environment, specifically **Azure Databricks**, to deploy our functional web microservice. This approach ensures that our service can operate seamlessly, regardless of the number of concurrent users, and guarantees a high level of reliability. To enhance song recommendations, we have integrated the **OpenAI API**, enabling us to curate a list of recommended songs based on users' voice inputs.

In order to provide users with a diverse selection of songs for each mood category, we have meticulously generated a song dataset. This dataset encompasses six distinct sentiment categories: Happy, Sad, Energetic, Calm, Anxious, and Chill. Each sentiment category contains a curated list of 50 songs, complete with song titles, artist names, and mood labels. To ensure efficient storage and reliability, we initially created a CSV file and then stored it in a **Delta Lake** table within Databricks. This storage approach not only guarantees high performance but also offers scalability and flexibility to accommodate future needs.

The following sections provide a detailed **walkthrough** of the App's functionality and usage.

## Demo Video Link 



## Project Structural Diagram
![Final-26](https://github.com/halfmoonliu/SongRecommendation/assets/141781876/8546444e-f752-4a4f-95f5-9b3b9fe69561)




Files in the repo:

1. Main Functions associated libraries .
  <br>a. _main.py_: the main function for the
  <br>b. _./libraries_:
      <br>i.   _speech2text.py_: **tranforms user's input** voice into **text**. 
      <br>ii.  _GPT_prompt.py_: uses transfomed user input to **prompt chat GPT** and **returns song recommendations received**.
      <br>iii. _parser.py_: output **one song name** and the corresponding **artist name** by parsing chat GPT's response.
      <br>iv.  _spotifyFunc.py_: takes a **song name** and an **artist name** and feed them to **Spotify API** and output **spotify soundtrack playing URL**.
      <br>v.  _songDB.py_: contains functions for **building a song database**.
      <br>vi. _query.py__: **querying song names and artist names** based on **user input mood**.

3. **Github actions setup for continuous integration**
      <br>c. _.github/workflows/main.yml_: Quality control actions are triggered when pushed/ pulled to main branch. After setting up the environment, actions of **installing packages**, **linting**, **testing**, **formatting** would be executed in order (specified in Makefile). 

4. **Other files for development environment settings**
      <br>d. _.gitignore_: specify file names to ignore.
      <br>e. _requirements.txt_: list required packages for the project.

5. **Description of the project**
   <br>f. _README.md_: THIS FILE, explaining the purpose and structure of the directory, with example output and code snippets.

This is a collective project with the following contibutors: Afraa Noureen(@afraa-n), Bob Zhang(@BobZhang26), Jiwon Shin(@jiwonny29),Yun-Chung (Murphy) Liu (@halfmoonliu).
