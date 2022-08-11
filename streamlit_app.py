# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 10:49:14 2022

@author: HannaHassinen
"""
###streamlit app

import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Blueberry oatmeal')
streamlit.text('Kale smoothie')
streamlit.text('Eggs')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.dataframe(my_fruit_list)