# MovieApp
Prediction of movie genres and detection of spoilers in reviews

Author: Sana Krichen    
https://www.linkedin.com/in/sanakrichen/    
https://github.com/skrichen
    

# Goals of the Project
Deciding what movie to watch with your significant other or with your friends can be the most difficult part
of movie night! It is not only time consuming but a real source of struggle. Agreeing on a movie genre usually
speed up the decision towards a common ground. Another way to help you decide which movie to pick is
to check out the reviews to find out if a movie is worth watching. However, many times people come across
spoilers that take away all the intrigue and ruin all the big moments!! As a movie lover, I have encountered
these situations several times and that is what motivated me into designing an app that predicts movie genres
and detects spoilers.

<img src="https://drive.google.com/uc?export=view&id=1ZgwemPW66Jgmp3OiHV9lowKCQ41gjdt5" width="640" height="480">



# Background
Predicting movie genres falls into the so called multilabel classification. In machine learning, this refers to a
problem where multiple labels may be assigned to each instance. Unlike the traditional two-class and multiclass
classification problems where classes are mutually exclusive, in the multilabel problem the classes are not
mutually exclusive. Thus there is no constraint on how many of the classes the instance can be assigned to. To
better understand the difference, please refer to fig. 2 There are different models that can handle the multilabel
classification. The One-Vs-All model is one of them. As its name suggests, it is a strategy where you train
multiple independent binary classifiers with one class at a time and leaving rest out. For instance, this can be
translated to the following set of questions: Is this movie a Comedy or not? Is this movie a Drama or not? Is
this movie a Thriller or not?... The main assumption here is that the labels are completely independent and we
do not consider any correlation between the classes.
Determining if a review is a spoiler or not requires an analysis based on text similarity. The way to implement
the latter is to use particular techniques to find the closeness between two chunks of text. Among the most
popular statistical methods we can find Cosine similarity, Jaccard Similarity and Word Mover's Distance. All
of them require preprocessing of the text before proceeding with the comparison.
