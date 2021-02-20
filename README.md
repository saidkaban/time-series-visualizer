### Assignment

Pandas, Matplotlib, and Seaborn is used to visualize a dataset containing the number of page views each day on the freeCodeCamp.org forum from 2016-05-09 to 2019-12-03.

Data is used to complete the following tasks:
* Used Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the "date" column.
* Cleaned the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
* Created a `draw_line_plot` function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png".
* Created a `draw_bar_plot` function that draws a bar chart similar to "examples/Figure_2.png". It shows the average daily page views for each month grouped by year.
* Created a `draw_box_plot` function that uses Searborn to draw two adjacent box plots similar to "examples/Figure_3.png". 
