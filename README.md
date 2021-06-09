# SQLAlchemy 
In this project, Python and SQLAlchemy were used for climate analysis and data exploration of a climate database for Hawaii weather. Python connection using SQLAlchemy was made to the SQLite database to reflect the tables for reference. Queries were then questioned of the data and summary statistics were made of of the precipitation data. A Flask API was then made to allow easy modifying of the queries to allow easy visualistation of the resulting data. Further analysis of temperature and precipitation were then analysed in SQLAlchemy/Pandas where Matplotlib was used to visualise the analysis and exploration of the data.


## Technologies uesed:
* SQLAlchemy
* Python
* Pandas
* Matplotlib
* ORM Queries
* Flask 


## Step 1 - Climate Analysis and Exploration

### Precipitation Analysis

* Design a query to retrieve the last 12 months of precipitation data.

* Select only the `date` and `prcp` values.

* Load the query results into a Pandas DataFrame and set the index to the date column.

* Sort the DataFrame values by `date`.

* Plot the results using the DataFrame `plot` method.

* Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Design a query to calculate the total number of stations.

* Design a query to find the most active stations.

  * List the stations and observation counts in descending order.

* Design a query to retrieve the last 12 months of temperature observation data (TOBS).

  * Filter by the station with the highest number of observations.

  * Plot the results as a histogram with `bins=12`

## Step 2 - Climate App

* Use Flask to create your routes.

### Flask Routes

* `/`

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`

  * Query the dates and temperature observations of the most active station for the last year of data.
  
  * Return a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.


## Other Analyses

### Temperature Analysis I

* Identify average temperature in June at all stations across all available years in the dataset. Same for December temperature.

* Use t-test to determine whether the difference in the means, if any, is statistically significant. 

### Temperature Analysis II

* Using `calc_temps` function calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year 

* Plot min, avg, and max temperature from your previous query as a bar chart.

  * Use the average temperature as the bar height.

  * Use the peak-to-peak (TMAX-TMIN) value as the y error bar.

### Daily Rainfall Average

* Calculate rainfall per weather station using the previous year's matching dates.

* Calculate daily normals.

* Create a list of dates for a trip in the format `%m-%d` and calculate the normals for each date.

* Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.

* Use Pandas to plot an area plot for the daily normals.
