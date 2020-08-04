Project Files and Folders

I. Files

1. IMDB_Dataset_get_titles.ipynb

Explored the IMDB datasets to get the final list of the movies’unique identifiers. The list of the movies is divided by decades into a total of 8 csv files. Each one contains the IDs of movies from a certain decade and was placed in the folder named after that specific decade.

2. IMDB_web_scraper.ipynb

This notebook is a web scraper. Giving the collection of CSV files divided by decades and enclosing movies unique identifiers, the web scraper will be adjusted to call every csv file, loop through the unique identifier of the movies and extract and store their plots and genres. 
Please note that there are 8 copies of this web scraper. Every copy is placed in a folder with a decade’s name. Every web scraper was slightly tweaked and modified to adjust to the dataset that I wanted to loop over. Here I am showcasing the web scraper for movies from the nineties. It was adjusted to call a certain csv (in this case `df_nineties` ) and to return a corresponding output  (in this case `scraped_df_nineties.csv` )

Example:  in the folder “eighties”, you will find

* The input csv file about all the movies from the eighties
* The web scraper that will take the input df_eighties.csv and will output df_scraped_eighties.csv
* The output which is df_scraped_eighties.csv that includes the plots and the genres of some of the movies from the df_eighties.csv (those that their webpage exists and that have an actual synopsis to show)

This example is replicated for all the following folders:
'fifties', 'sixties', 'seventies', 'eighties', 'nineties', 'twothousands', 'twothousandstens’ and ‘twothousandstwenties'

PS: The web scrapers in all the others folders do not include markdowns. All the detailed steps are provided in IMDB_web_scraper.ipynb

3. IMDB_EDA.ipynb
Merged the data, cleaned the collected data, performed some EDA and encoded the genres

4. Preprocessing.ipynb
Preprocessed the text data using a customized tokenizer and applied CounVectorizer to transform the movie plots into vectors.

5. Modeling.ipynb
Chose the One-Vs-All model along with logistic Regression as a model to work with. Used a pipeline to scale the data and fit the model to the data. Incorporated a GridSearchCV to optimize the hyperparameters of the model. Returned the best parameters of the best model.

6. Model Evaluation.ipynb
Implemented the best model. Used total accuracy, accuracy per genre, confusion matrix, precision and recall to evaluate the model’s performance. Created a Plotly graph that displays the tokens that best describe a movie genre.

7. Is_spoiler.ipynb (This file can be found in the folder named 7_is_spoiler)
Cleaned and preprocessed the data. Implemented 3 methods to check the text similarity,optimized the threshold, checked the accuracy, the precision and recall for every statistical method that I used. Chose the one that gave me the best results.

8. My_app.py (This file can be found in the folder named 8_App)
This python script encloses the code for my Movie App.
Follow the steps to make the app work:

In your environment where the streamlit package is  installed run the following command line

streamlit run my_app.py

PS: All the other files from the 8_App folder should be present in your working directory.

II. Folders

* fifties
Contains df_fifties.csv, scraped_df_fifties.csv and web_scraper_fifties.ipynb

* sixties
Contains df_sixties.csv, scraped_df_sixties.csv and web_scraper_sixties.ipynb
 
* seventies
Contains df_seventies.csv, scraped_df_seventies.csv and web_scraper_seventies.ipynb

* eighties
Contains df_eighties.csv, scraped_df_eighties.csv and web_scraper_eighties.ipynb

* nineties
Contains df_nineties.csv, scraped_df_nineties.csv and web_scraper_nineties.ipynb

* twothousands
Contains df_twothousands.csv, scraped_df_twothousands.csv and web_scraper_twothousands.ipynb

* twothousandstens
Contains df_ twothousandstens.csv, scraped_df_twothousandstens.csv and web_scraper_twothousandstens.ipynb

* twothousandstwenties
Contains df_ twothousandstwenties.csv, scraped_df_twothousandstwenties.csv and web_scraper_twothousandstwenties.ipynb

* 7_is_spoiler
Contains the reviews dataset from Kaggle (a fraction of it to be precise)
And the 7_is_spoiler.ipynb

* 8_App
Contains bagofwords.pkl, the best model “my_model.pkl”, the python script file my_app.py and an image used in the App








