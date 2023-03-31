
import streamlit as st
from newsapi import NewsApiClient
import pycountry

# you have to get your api key from newapi.com and then paste it below
newsapi = NewsApiClient(api_key='c2c7588f9b744961a7be2cf85d2f4f9a')

# now we will take name of country from user as input
try:
    input_country = st.text_input("Country: ")
except:
    pass
input_countries = [f'{input_country.strip()}']
countries = {}

# iterate over all the countries in
# the world using pycountry module
for country in pycountry.countries:

	# and store the unique code of each country
	# in the dictionary along with it's full name
	countries[country.name] = country.alpha_2

# now we will check that the entered country name is
# valid or invalid using the unique code
codes = [countries.get(country.title(), 'Unknown code')
		for country in input_countries]

# now we have to display all the categories from which user will
# decide and enter the name of that category
option = st.selectbox("Which category are you interested in?",
                      ["Business", "Entertainment", "General", "Health", "Science", "Technology"])
try:
# now we will fetch the new according to the choice of the user
    top_headlines = newsapi.get_top_headlines(

        # getting top headlines from all the news channels
        category=f'{option.lower()}', language='en', country=f'{codes[0].lower()}')


    # fetch the top news under that category
    headlines = top_headlines['articles']

    # now we will display the that news with a good readability for user
    if headlines:
        # create a list of headline titles for the selectbox
        options = [article['title'] for article in headlines]
        # allow the user to select a headline
        selected_title = st.selectbox("Select an article", options)

        # Display selected article in iframe
        selected_article = [article for article in headlines if article['title'] == selected_title][0]
        # st.components.v1.iframe(f"<iframe src={selected_article['url']}></iframe>", height=800, width=1000, scrolling=True, )
        st.markdown(f"<iframe src={selected_article['url']} height='1200' width='1000'></iframe>", unsafe_allow_html=True)
    else:
        st.write(f"Sorry no articles found for {input_country} in the {option} category.")
except:
    pass