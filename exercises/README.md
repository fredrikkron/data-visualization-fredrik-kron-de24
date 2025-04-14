# Exercise 0 - Matplotlib fundamentals
In this exercise, you get to familiarize yourself with matplotlib to make simple graphings such as line and bar charts.

### Note

For each chart that you draw, make sure to have appropriate titles, xlabel, ylabel and other annotations that might be needed

## 0. Car sales in Norway - emissions and trends
From lecture 02 with car sales in Norway, we worked with one dataset, however there were some more that you downloaded from kaggle. In this exercise, work with this dataset norway_new_car_sales_by_month.csv

  a) Do some EDA with info, find out column names, shape of dataset, describe method to get summary descriptive statistics.

  b) Draw a line chart of quantity for each year. Is there a year that should be skipped?

  c) Draw a line chart of average CO2 emissions for same years that as in b)

  d) Draw a line chart of all years and months for import

  e) Draw a line chart of all years and months for average CO2 emissions

  f) Draw a line chart of all years and months for electric cars import

  g) Draw a line chart of average diesel share per year

  h) Discuss some findings with a friend based on this dataset, and do plot more graphs

## 1. Recreate graphs
The following graphs below are created from this dataset. Try to recreate them as close as possible

  a) Here we use subplots to get two axes in one figure

bar chart and line chart

  b) This one will require some data processing to be able to come to this point.

Hint: df.explode() and df.join()

bar chart and line chart

  c) A df has a hist() method for creating histogram

bar chart and line chart

## 2. Theory questions
  a) When can you make line charts and when can't you make line charts?

  b) Whats wrong with this chart?

bar chart and line chart

  c) Whats wrong with this chart?

bar chart and line chart

  d) What is the difference between OOP approach and plt approach in drawing graphs.

  e) How do you draw an arrow in matplotlib?

## Glossary
Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

terminology	| explanation
------------|------------
artist	
containers	
spine	
axes	
figure	
subplot	
patch	
annotation	
arrowprops	
marker	
ticks	
ticklabels	
layout	
grid	
legend