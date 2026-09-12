# Algorithms-and-Data-Structures-Assignment
Sales Sorting Demo

A Python console application demonstrating object-oriented sorting algorithm design, built for the Algorithms & Data Structures module.

Overview

Loads sales transaction data from a CSV file into model objects, then uses a custom-built sorting algorithm (implementing an abstract Sorter interface) to rank sales by total value and retrieve the top-performing transactions.

Project Structure
├── business/
│   └── company.py         # Company class - manages a collection of sales
├── data/
│   └── source/
│       └── sales.csv      # Sample sales dataset
├── data_loader/
│   └── data_loader.py     # Loads and parses CSV data into Sale objects
├── models/
│   └── sale.py            # Sale data model
├── sorter/
│   ├── sorter_adt.py      # Abstract Sorter interface (ADT)
│   └── bubble_sort.py     # Bubble Sort implementation of Sorter
└── main.py                # Entry point - runs the demo
How it works
SalesDataLoader reads sales.csv and converts each row into a Sale object.
A Company object holds the loaded sales and exposes methods to sort and query them.
BubbleSort implements the abstract Sorter interface, so other sorting algorithms could be swapped in without changing Company's code.
The demo sorts sales by total value and prints the top 10 highest-value transactions, along with the time taken to sort.
Running it
python main.py
Tech used

Python, object-oriented design (abstract base classes), CSV parsing
