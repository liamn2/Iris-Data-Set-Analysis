# analysis.py
# Author: Liam Nutley
# Program using Iris Data set to output a summary of each variable to a single text file, save a histogram of each variable to png files, and output a scatter plot of each pair of variables. 

# Variable summaries output as text file.
import pandas as pd   
import numpy as np
pd.set_option("display.max_rows", None, "display.max_columns", None) # Option edit to display all rows
data = pd.read_csv('iris.csv', delimiter= None) # Reads our CSV file
n = 150 # Number of Data entries
f = open('output.txt', 'w') # opens/creates file we write to
f.write(str(data.head(n = n))) # Writes data to new text file
data.head(150) # Number of data entries
f.close() # Closes file

# Histograms of each variable.
import numpy
data=numpy.genfromtxt('iris.csv',delimiter=',') 
import matplotlib.pyplot as pl
pl.hist(data[:,0]) #Column Entries
pl.title('Histogram of sepal length') # Title
pl.xlabel('Sepal length in cm') # X axis title
pl.ylabel('Frequency / Number of flowers') # Y axis title
pl.savefig('sepal_length_hist.png') # saves graph
pl.show() # Shows graph

pl.hist(data[:,1])  #Column Entries
pl.title('Histogram of sepal width')  # Title
pl.xlabel('Sepal width in cm')  # X axis title
pl.ylabel('Frequency / Number of flowers') # Y axis title
pl.savefig('sepal_width_hist.png') # saves graph
pl.show() # Shows graph

pl.hist(data[:,2])  #Column Entries
pl.title('Histogram of petal length')  # Title
pl.xlabel('Petal length in cm')  # X axis title
pl.ylabel('Frequency / Number of flowers')  # Y axis title
pl.savefig('petal_length_hist).png')  # saves graph
pl.show() # Shows graph

pl.hist(data[:,3])  #Column Entries
pl.title('Histogram of petal width') # Title
pl.xlabel('Petal width in cm')  # X axis title
pl.ylabel('Frequency / Number of flowers')  # Y axis title
pl.savefig('petal_width_hist.png') # saves graph
pl.show() # Shows graph

# Scatter plots of paired variables.
import matplotlib.pyplot as plt
x=[data[:,0][range(150)]] # Taking Data from Column 0 over 0 - 149

y=[data[:,1][range(150)]] # Taking Data from Column 1 over 0 - 149

plt.scatter(x,y,label='flow',s=25,marker='*')
plt.xlabel('Sepal length in cm') # X-axis plot
plt.ylabel('Sepal width in cm') # Y-axis plot
plt.title('Plot of Sepals') # Title of Scatter Plot
plt.show() # Shows scatter plot

x=[data[:,2][range(150)]] # Taking Data from Column 2 over 0 - 149
y=[data[:,3][range(150)]] # Taking Data from Column 3 over 0 - 149

plt.scatter(x,y,label='flow',s=25,marker='*')
plt.xlabel('Petal length in cm') # X-axis plot
plt.ylabel('Petal width in cm') # Y-axis plot
plt.title('Plot of Petal') # Title of Scatter Plot
plt.show() # Shows scatter plot