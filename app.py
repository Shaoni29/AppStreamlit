import numpy as np
import pandas as pd
import streamlit as st

def welcome():
    return "Welcome All"

def main():
  st.title("Multiplication")
  num_1 = st.number_input("Number 1")
  num_2 = st.number_input("Number 2")
  result = num_1 * num_2
  st.success('The output is {}'.format(result))
  if st.button("Made By"):
      st.text("Shaoni Samanta")
      

if __name__=='__main__':
  main()