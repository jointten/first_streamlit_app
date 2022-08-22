# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 10:49:14 2022

@author: HannaHassinen
"""
###streamlit app

import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Blueberry oatmeal')
streamlit.text('Kale smoothie')
streamlit.text('Eggs')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_shown = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_shown)