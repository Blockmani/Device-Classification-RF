# Device Classification with Random Forest

## Task
Using Machine Learning to identify devices (sensors) based on the specifications provided.

## The Machine Learning Approach
In the realm of Machine Learning, this is an elegant **supervised classification** problem. 
Now, when it comes to classifying something, there are tons of algorithms to choose from. 
But, for this task, we need a robust, dynamic and an algorithm which can work really well
with large datasets and variations. These algorithmic requirements lands us right on top of
one well-known machine learning algorithm called, **_Random Forest_**

## What is Random Forest?
Random Forest is an advanced algorithmic upgrade of an existing supervised model called, **_Decision Trees_**. It is considered one of the most precise machine learning models created so far for
supervised classification purposes.

Decision Trees are classifiers which makes implicit decisions (binary or multi-variant) to reach 
the target. The only problem with Decision Trees is that its very basic and cannot be extended to 
data which might have imbalance. Decision Trees tend to overfit very fast. _(**Reason:** How is it even 
possible to generalize decisions? At some point, Decision Trees have to abstract out many decisions just
to improve the accuracy)_.

![Decision Trees](https://i.imgur.com/3Yn0P0w.png)

Random Forest algorithm, as the name suggests, employs many decision trees at its core. Its an **ensembling** technique (where multiple algorithms are used to decide on a final fate). The individual
Decision Tree predicts out a class. Then, a majority voting scheme is conducted to finally decide the 
model's prediction.

![Random Forest](https://i.imgur.com/Xdff4tc.png)
In the above case, in a forest of **nine** decision trees, there are **six** decision trees which spat out **_1_** and **three** decision trees spat out **_0_**. Upon voting, the clear winner comes out to be **_1_**.

The random forest sometime, also employs the **bagging method** to generate the required prediction.
Bagging involves using different samples of data (training data) rather than just one sample. A training dataset comprises observations and features that are used for making predictions. The decision trees produce different outputs, depending on the training data fed to the random forest algorithm. These outputs will be ranked, and the highest will be selected as the final output.

## Why Random Forest?
Random Forest is known to produce highest number of accuracies among all the models. Reason? It capitalizes on the number of weak learners to give a very strong prediction. This is called as the **_"wisdom of the crowd_**.

A large number of incorrect to accurately related models work together to give a very consistent model.
Some other known advantages of this model are:
- Never allows decision trees to overfit
- Variable Importance measure
- Works extremely well with large datasets
- Imabalance data is handled pretty well 
- Individual tree's error(s) are almost cancelled out by each other.

<<<<<<< HEAD
The device classification model demands a model which is **error free to a great extent**. Typically, there will be a very **huge dataset** including many attributes.
