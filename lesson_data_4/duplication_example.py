from IPython.display import display
import pandas as pd

listings_df = pd.read_csv('https://pynoon.github.io/data/inside_airbnb_listings_nz_2023_09.csv')

akl_listings_df = listings_df[listings_df['region_parent_name'] == 'Auckland']
akl_average_price = akl_listings_df['price_nzd'].median()
akl_above_average_price_df = akl_listings_df[akl_listings_df['price_nzd'] > akl_median_price]
display(akl_above_average_price_df)

wlg_listings_df = listings_df[listings_df['region_parent_name'] == 'Wellington City']
wlg_average_rating = wlg_listings_df['review_scores_rating'].median()
wlg_above_average_rating_df = wlg_listings_df[wlg_listings_df['review_scores_rating'] > wlg_average_rating]
display(wlg_above_average_rating_df)
