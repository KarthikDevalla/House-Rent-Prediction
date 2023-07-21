# House-Rent-Prediction in the Major States of India

## Introduction

This repository contains a machine learning project for predicting house rents in major states of India. The goal is to build a robust and accurate predictive model that can estimate house rents based on various features like __Location, Property Type, Layout Type, Furnish Type, Number of Bedrooms and Bathrooms, and Area__. In addition to the predictive model, it is integrated with FastAPI to create a RESTful API that allows users to make real-time rent predictions using HTTP requests. The goal is to build a user-friendly web API that can serve predictions based on various house features, making it convenient for users and real estate agents to access rental estimates.

## Real-time Prediction using FastAPI

The `main.py` file contains the FastAPI code for the prediction API. This API allows users to make rent predictions by sending a POST request with relevant house features as input. The API will respond with the predicted rent for the provided feature set.
