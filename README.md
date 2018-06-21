
# Window Functions Lab

In this lab we will use window functions to write queries over certain segments, or "windows", of a larger table.  We will use the `OVER()` keyword in conjunction with `PARTITION BY` to perform aggregate functions on specific rows of the table.

## Objectives

1.  Understand window functions and how they simplify queries that operate on segments of a table
2.  Become comfortable declaring windows with the `OVER()` clause
3.  Practice operating on different segments of the table with the `PARTITION BY` clause
4.  Differentiate between using `ORDER BY` inside and outside the window function
5.  Use the `DISTINCT` keyword to remove duplicate results

## Record Store Sales

Records-R-Sweet is a startup retail company aiming to repopularize record collecting despite the ubiquity of digital music and smartphones.  Records-R-Sweet has opened retail stores in several cities, including Manhattan, Brooklyn, Washington, D.C., Houston, and London.  We have been hired to track various aspects of the company's sales data across all its locations.  The company has provided us with a table of information, as seen below:

|date_of_sale|location  |amount|
|------------|----------|------|
|2018-04-21  |New York  |50    |
|2018-04-21  |New York  |40    |
|2018-04-22  |New York  |60    |
|2018-04-22  |New York  |30    |
|2018-04-22  |New York  |30    |
|2018-04-23  |New York  |30    |
|2018-04-23  |New York  |80    |
|2018-04-21  |Brooklyn  |90    |
|2018-04-22  |Brooklyn  |80    |
|2018-04-22  |Brooklyn  |80    |
|2018-04-22  |Brooklyn  |70    |
|2018-04-23  |Brooklyn  |90    |
|2018-04-23  |Brooklyn  |80    |
|2018-04-21  |Washington|20    |
|2018-04-21  |Washington|30    |
|2018-04-21  |Washington|20    |
|2018-04-22  |Washington|30    |
|2018-04-22  |Washington|40    |
|2018-04-23  |Washington|20    |
|2018-04-21  |Houston   |25    |
|2018-04-22  |Houston   |30    |
|2018-04-23  |Houston   |35    |
|2018-04-23  |Houston   |25    |
|2018-04-21  |London    |100   |
|2018-04-22  |London    |50    |
|2018-04-22  |London    |75    |
|2018-04-23  |London    |45    |

The table tracks sales across all Records-R-Sweet for three days, April 21-23.  Each store registered at least one sale per day.  Our task is to write window functions to make comparisons across stores to see which stores do the most business.  We also will determine how Records-R-Sweet's business fluctuates day-to-day.

## Queries

Write your queries in the `window_function.py` file to get the tests to pass.  As always, each query should be wrapped in a string inside each function.

#### 1. select_distinct_total_location_sales_on_april_23

For all locations, select the location and its total sales for the day April 23, 2018.

#### 2.  select_distinct_location_and_avg_amount_partitioned_by_location

For all locations, select the location and its average sales over the three day period.

#### 3.  select_distinct_date_and_total_company_wide_sales_split_by_date_ordered_by_date

Select the date and the company-wide sales for that day.  The resulting dataset should appear in chronological order from April 21 to April 23.

#### 4.  select_rank_the_sales_of_each_location_from_highest_to_lowest


Rank each store's individual sales (that is, not the store's daily total) from lowest to highest.  The query should select the location, the amount of the sale, and the sale's ranking.  The rankings should be ordered from highest to lowest, and make sure they rank each location's sales and not the overall company's sales.
