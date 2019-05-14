# Exploring Las Vegas Restaurants from the Yelp Dataset
Lufeng Lin, Zixuan Wang, Jonathan Yuan

MUSA 620 Data Wrangling
May 13, 2019

Launch the app here:
[![](https://img.shields.io/badge/launch-binder%20app-F5A252.svg)](https://mybinder.org/v2/gh/MUSA-620-Spring-2019/final-project-lin-wang-yuan/master?urlpath=final.ipynb)

### ABSTRACT

Yelp is a crowd-sourced business directory service, which compiles and publishes location information, user reviews, and photos on restaurants, shops, offices, and other businesses. As part of the Yelp Dataset Challenge, Yelp has published a subset of its dataset for students and researchers to analyze and explore their data.

Our final project is a dashboard which may be used to examine cross-sections of Las Vegas restaurants. Written in Python and using using Pyviz’s `panel` library, it allows users to filter (with `param`) these restaurants and their user reviews and dynamically create visualizations backed by `altair` and Leaflet’s `folium`. Users can select the type and category of Las Vegas restaurants to analyze, and the dashboard will display a text summary, as well as:
1. a heatmap of their locations,
1. a bivariate bar plot showing the number of restaurants in each category and the number with each rating, and 
1. a histogram of the usefulness of Yelp reviews.

### THE DATA

We used two primary components of the Yelp dataset, one of which has 1M+ rows.

First, the provided `business.json` contains 192,609 rows, one for each business included in the dataset. This contains business information, such as name, location, categories, number of reviews, and average rating (out of five stars), as well as a 22-character `business_id`.

Second, `review.json` contains 5,261,668 user reviews, each associated with a `business_id`. The text value of each review is included, as well as other users' feedback for these reviews, or a count of the number of "funny", "cool", and "useful" responses.

### THE CODE

#### Filtering using `param` callbacks

One of the primary features of the dashboard is the ability to examine only a selection of Las Vegas restaurants in our selected categories. With the `param` library, a new object of class `ourapp()` is created containing two filters which may be used to select restaurants and any visualizations that depend on them.

On a `param.integer()` slider titled "Star", users may select restaurants that have between 0 and 5 stars in integer increments. (Partial star ratings are rounded.) And with a `param.ObjectSelector()` drop-down named "Foodselector", the specific category of restaurant ("Burgers", "Mexican", "Chinese", "Italian", "Pizza", etc.) may be chosen.

Because the `categories` column is in `string` format that sometimes contains multiple categories, some data frame operations are necessary to separate out the categories. A new column was created containing only one of the categories in the drop-down, and a new dataset was created ignoring all restaurants not having those categories. One issue with this approach is that restaurants with two of those categories (e.g. "Italian" and "Pizza"), only the result of the last operation is kept.

Dataframe operations on the output of the filter allows the compilation of a text summary, e.g. for 2-star Chinese restaurants: "There are 20 restaurant(s) and 1759 reviews, including 1687 useful reviews, 665 cool reviews, and 835 funny reviews." Each of the below visualizations is updated according to the selection of filters and is implemented as callback functions within the `ourapp()` object.

#### 1. Heatmap

The Python wrapper of mapping tool Leaflet.js is called `folium`, which works with the Leaflet.heat plugin. This library and plug-in was used to generate a dynamic heatmap showing where selected restaurants tend to be clustered. 2-star Chinese restaurants, for example, appear throughout the city, but are especially clustered along a section of Las Vegas Boulevard known as "the Strip".

#### 2. Barplot by category and rating

This `altair` stacked bar plot shows, for each category, the number of restaurants in each rating. The `altair` package is used to aggregate, for each bar, the number of Las Vegas restaurants in each category, and, for each color, the number of restaurants that have each rating in half-star increments. 

#### 3. Histogram of "useful", "funny", and "cool" feedback per restaurant

These `altair` histogram (actually a bar plot; `altair` histograms would not appear with `panel`) shows the distribution of the amount of "useful" feedback for the reviews of restuarant. The value for each restaurant is the sum of the "useful", "funny", or "cool" count of all of its reviews. This may be interpreted as the overall usefulness of reviews for each Yelp listing.

In order to prepare this data, a join was performed between the `business.json` and `review.json` datasets. Then, grouping by each business, a sum of all counts of "useful" responses is created. If a restaurant has 5 reviews, and each review has 3 "useful" responses, The restaurant will have a "useful" count of 15.

Most Yelp listings of 2-star Chinese restaurants have a "useful" count less than 100. Reviews for one particular Sandwich restaurant, however, have over 11000 "useful" responses.
