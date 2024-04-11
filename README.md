Database Tools | Edwin Sanchez
# Functional Dependencies
This program allows you to automatically find functional dependencies in a given set of data. This is a bottom-up approach to database design.

## Setup
* **Create an Anaconda Environment:** `conda create -n func-dep python=3.11`
* **Install Numpy:** `pip install -r requirements.txt`

That's it, you're all set!


## Future Work
Now that I have an auto-functional dependency tool, it would be nice if I could somehow automatically generate the relations for the SQL database from the known possible functional dependency lists. I can do this by training a model on given column names to determine whether two specific columns would be functionally dependent, based on their names. For training this model, I should take an existing database design and take out their primary keys and all the attributes dependent on those keys. Then I should label the those as positive pairs, while generating random negative pairs. This way I can make a robust model that given (1) a potential primary key attribute name, and (2) a potential depend key attribute name, tell me if one (2) is likely to be dependent on (1).

Then I can feed in the functional dependencies generated from this program. This will be a much easier task than what the model is trained on, as it will only be given pairs that have been proven likely to be functionally dependent based on the given data (Although the model may be able to pick them out without having this functional dependency program run on them - this would be something to investigate further, but it would be much safer to just check the dependencies first).

After this, it may be useful to add attribute descriptions to make the decision easier.

Try naive classifiers vs. fine-tuned LLMs.
