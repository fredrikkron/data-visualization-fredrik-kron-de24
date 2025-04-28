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
------------|--------------
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

# Exercise 1 - Data storytelling

In this exercise, you get to use matplotlib and combine with data storytelling to make visuals that are targeted towards telling a suitable story for your target audience.

> [!NOTE]
> For each explanatory chart that you draw, make sure to use data storytelling principles to make your visualizations truly explanatory and not exploratory

## 0. Tell a story from immigration

This visualization comes from [03_matplotlib_annotations](https://github.com/AIgineerAB/data_visualization_course/tree/main/03_matplotlib_annotations).

<img src="https://github.com/kokchun/assets/blob/main/data_visualization/annotate_arrow.png?raw=true" alt="bar chart and line chart" width="300">

Lets improve upon this visualization.

&nbsp; a) Remove clutter from this visualization such as top spine and right spine. Also change the unit to thousands with a prefix K.

&nbsp; b) Left align the xlabel, top align the ylabel and left align the title

&nbsp; c) Use contrast to focus the attention to what you want the audience to see

&nbsp; d) Choose a story to tell and change the labels and title accordingly

&nbsp; e) You can choose several different stories to tell and depending on which one you choose, the visualization might look differently in terms of what parts are annotated, what parts are highlighted etc.

## 1. Makeover

The given code

```py
import pandas as pd
import duckdb

df = pd.read_csv("data/norway_new_car_sales_by_month.csv")
df = duckdb.query(
    """
    SELECT avg_CO2, import,quantity, year, month
    FROM df

"""
).df()

df["date"] = pd.to_datetime(
    df["Year"].astype(str) + "-" + df["Month"].astype(str).str.zfill(2), format="%Y-%m"
)

df = df.set_index("date")

ax = df["Avg_CO2"].plot()
```

creates a graph that looks like this

<img src="https://github.com/kokchun/assets/blob/main/data_visualization/avg_co2.png?raw=true" alt="bar chart and line chart" width="300">

<br/>

Your task is to do a `data storytelling makeover` of this visual.


## 2. CO2 data storytelling

Based on the dataset `co2_annmean_mlo.csv` create this visualization as closely as you can 

<img src="https://github.com/kokchun/assets/blob/main/data_visualization/CO2_emissions_annual_mean.png?raw=true" alt="bar chart and line chart" width="300">



## 3. Exploring and explaining happiness

In the data happiness.xlsx from [here](https://data.world/makeovermonday/2025-week-4-world-happiness-report-2024) you can find happiness scores as well as a visualization of all the countries happiness along with different variables to explain the happiness to various levels. Do exploratory data analysis on this dataset, then pick out a few visualizations that you turn into explanatory data analysis using the principles of data storytelling. 

## 4. Theory questions

&nbsp; a) Why is it good to use the proximity principle when designing visuals? 

&nbsp; b) What is clutter and why is it undesirable?

&nbsp; c) Why should you spend time on data storytelling when there is a lot of things that needs to be explored and cleaned in the data? 

&nbsp; d) Data storytelling is very subjective in terms of which story to tell. How could you or your team craft a compelling story to tell? 


## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology               | explanation |
| ------------------------- | ----------- |
| exploratory data analysis |             |
| explanatory data analysis |             |
| clutter                   |             |
| proximity principle       |             |
| attention                 |             |
| contrast                  |             |
| colors sparingly          |             |
| data storytelling         |             |
| grid                      |             |
| axis                      |             |
| insight                   |             |
| context                   |             |
| call to action            |             |
| annotation                |             |
| KPI                       |             |
| story arc                 |             |
| data literacy             |             |
| dashboard fatigue         |             |

# Exercise 2 - Interactive charting with plotly

In this exercise, you learn how to do interactive charting with plotly express and with plotly graph objects.

> [!NOTE]
> all data for the exercises is found in this repo under exercises/data

## 0. Internet usage

This visualization comes from [ourworldindata](https://ourworldindata.org/technological-change).

<img src="https://github.com/kokchun/assets/blob/main/data_visualization/share-of-individuals-using-the-internet.png?raw=true" alt="bar chart and line chart" width="300">

&nbsp; a) Recreate this visualization using plotly, make it as close as possible to the image.

&nbsp; b) Apply storytelling principles to improve this visualization. You can make several variations if you want to tell different stories.

## 1. Internet usage historical

This visualization comes from [ourworldindata](https://ourworldindata.org/technological-change).

<img src="https://github.com/kokchun/assets/blob/main/data_visualization/share-of-individuals-using-the-internet-historical.png?raw=true" alt="bar chart and line chart" width="300">

&nbsp; a) Recreate this visualization using plotly, make it as close as possible to the image.

&nbsp; b) Apply storytelling principles to improve this visualization. You can make several variations if you want to tell different stories.

## 2. Price on memory

This visualization comes from [ourworldindata](https://ourworldindata.org/technological-change).

<img src="https://github.com/kokchun/assets/blob/main/data_visualization/historical-cost-of-computer-memory-and-storage.png?raw=true" alt="bar chart and line chart" width="300">

&nbsp; a) Recreate this visualization using plotly, make it as close as possible to the image.

&nbsp; b) Apply storytelling principles to improve this visualization. You can make several variations if you want to tell different stories.

## 3. Spider chart

Create a spider chart for different set of skills that you think are relevant for a job. Assess your own skill levels as of today and plot it out on the spider chart. Make a guess of 1 year from now where you think your skills will be within these fields and plot another spider chart upon the one you have. For simplicity you could pick out a few core skills that your education covers e.g. python, sql, cloud, ...

## 4. Internet map

This visualization comes from [ourworldindata](https://ourworldindata.org/technological-change).

<img src="https://github.com/kokchun/assets/blob/main/data_visualization/landline-internet-subscriptions-map.png?raw=true" alt="internet map" width="300">

&nbsp; a) Recreate this visualization using plotly, make it as close as possible to the image.

&nbsp; b) Now make it start with zooming in to display Europe.

## 4. Theory questions

&nbsp; a) What is the difference between plotly graph objects and plotly express

&nbsp; b) How do customize the hover in your visualizations?

&nbsp; c) When should you use plotly vs matplotlib?

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology       | explanation |
| ----------------- | ----------- |
| choropleth        |             |
| fig.update_layout |             |
| radar chart       |             |
| spider chart      |             |
| mapbox            |             |
| geojson           |             |
| bubble chart      |             |
| pie chart         |             |
| hovertemplate     |             |
| trace             |             |