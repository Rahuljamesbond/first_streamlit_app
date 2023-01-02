
import streamlit
streamlit.title('My Parents New Healthy Diner')
import snowflake.connector
streamlit.text("Hello from Snowflake:")
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
