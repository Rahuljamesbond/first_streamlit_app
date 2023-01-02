
import streamlit
streamlit.title('My Parents New Healthy Diner')
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

