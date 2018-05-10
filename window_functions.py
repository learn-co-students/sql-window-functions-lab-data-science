def select_distinct_total_location_sales_on_april_23():
    return "SELECT DISTINCT location, SUM(amount) OVER(PARTITION BY location) FROM sales WHERE date_of_sale = '2018-04-23';"

def select_distinct_location_and_avg_amount_partitioned_by_location():
    return "SELECT DISTINCT location, AVG(amount) OVER(PARTITION BY location) FROM sales;"

def select_distinct_date_and_total_company_wide_sales_split_by_date_ordered_by_date():
    return "SELECT DISTINCT date_of_sale, SUM(amount) OVER(PARTITION BY date_of_sale) FROM sales ORDER BY date_of_sale;"

def select_rank_the_sales_of_each_location_from_highest_to_lowest():
    return "SELECT location, amount, rank() OVER(PARTITION BY location ORDER BY amount DESC) FROM sales;"
