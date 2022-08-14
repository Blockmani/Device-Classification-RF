# Device Classification with Random Forest

## Task
Using Machine Learning to identify devices (sensors) based on the specifications provided.

## The Machine Learning Approach
In the realm of Machine Learning, this is an elegant **supervised classification** problem. 
Now, when it comes to classifying something, there are tons of algorithms to choose from. 
But, for this task, we need a robust, dynamic and an algorithm which can work really well
with large datasets and variations. These algorithmic requirements lands us right on top of
one well-known machine learning algorithm called, **_Random Forest_**

## What is Random Forest? Why Random Forest?
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
<center> <b>Predicts 1</b> </center>