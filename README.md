# Analytical Exploration of Boston Crime Statistics

This repository contains an exploratory data analysis (EDA) of Boston crime statistics, aiming to uncover trends and insights from crime data, weather data, and (soon) map data.

 The goal is to investigate if there is any correlation between various weather factors (such as temperature, humidity, and precipitation) and the occurrence of different types of crimes in Boston over a specific time frame.

## Data Sources

The dataset contains crime records from the city of Boston, including details about the crime type, district, location, date, and time. Additionally, weather data (temperature, humidity, etc.) for the same period is incorporated to analyze how environmental factors may influence crime rates.

### Crime Data
- Source: [Boston Crime Data 2012-2015](https://data.boston.gov/dataset/crime-incident-reports-july-2012-august-2015-source-legacy-system)
- Source: [Boston Crime Data 2015](https://data.boston.gov/dataset/crime-incident-reports-august-2015-to-date-source-new-system)
- Includes: Crime type, district, location, shooting status, date and time of crime, etc.

### Weather Data
- Source: [Boston Weather 2013-2023](https://www.kaggle.com/datasets/swaroopmeher/boston-weather-2013-2023?resource=download)
- Includes: Date, temperature (high, average, low), humidity, precipitation, and other weather variables.

## Objective

This analysis seeks to answer the following questions:
- Is there a relationship between crime rates and average temperature in Boston?
- Do certain types of crimes occur more frequently during particular weather conditions?
- How do temperature, humidity, and other weather factors impact crime trends across time?

## Installation

### Requirements
- Python 3.7+
- pandas 
- matplotlib 
- seaborn
- numpy
- geopandas (in the future once I get map shape data)
- scikit-learn (optional for advanced analysis in the future)

You can install the required packages using `pip`:

```bash
pip install -r requirements.txt
