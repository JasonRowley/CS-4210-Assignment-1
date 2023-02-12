#-------------------------------------------------------------------------
# AUTHOR: Jason Rowley
# FILENAME: decision_tree.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
feature_vals = [
  ['Young', 'Myope', 'Yes', 'Reduced'],
  ['Prepresbyopic', 'Hypermetrope', 'No', 'Normal'],
  ['Presbyopic']
] # the row index is the number for the feature value - 1

for row in db:
  new_row = []
  for j, fv in enumerate(row):
    if j == len(row) - 1:
      # Skip class values column
      continue
    for i, fvs in enumerate(feature_vals):
      if fv in fvs:
        new_row.append(i + 1)
  X.append(new_row)
# X =

#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
class_vals = ['Yes', 'No']
for row in db:
  for i, cv in enumerate(class_vals):
    if row[-1] == cv:
      Y.append(i + 1)
# Y =

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()