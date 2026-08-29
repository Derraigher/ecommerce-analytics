# E-Commerce Analytics Project

## Tech Stack

- Python
- Pandas
- MySQL
- SQL
- Power BI
- PyCharm

## Project Overview

This project analyzes an e-commerce dataset with the goal of understanding customer behavior, product performance, sales trends, reviews, and conversion metrics.

The project combines **Python (Pandas)** for Exploratory Data Analysis, **MySQL** for business-oriented SQL analysis, and **Power BI** for data visualization.

The analysis is based on six related datasets:

- Users
- Products
- Purchases
- Reviews
- Sessions
- Interactions

## 1. Exploratory Data Analysis (Python / Pandas)

Each dataset was independently explored using Pandas.

The EDA focused on:

- Data structure and data types
- Missing values
- Duplicate detection
- Descriptive statistics
- Dataset dimensions
- Business KPI exploration

The analysis was used to understand the available data and identify the most relevant metrics for the subsequent business analysis.

## 2. Business Analysis

The business analysis focused on four main areas.

### Customer Analysis

- Which loyalty tier generates the most revenue?
- Which income level spends the most?
- Which countries generate the highest revenue?

### Product Analysis

- Which product categories generate the most revenue?
- Which brands generate the most revenue?
- Which products sell the most?

### Reviews Analysis

- Which categories have the highest ratings?
- Which brands receive the best reviews?

### Conversion Analysis

- Which device has the highest conversion rate?
- Which traffic source has the highest conversion rate?

## 3. SQL Analysis

The datasets were imported into MySQL and analyzed using SQL queries.

The analysis required combining information from the different tables using joins and aggregations.

The main SQL concepts demonstrated in the project include:

- `SELECT`
- `JOIN`
- `GROUP BY`
- `SUM()`
- `AVG()`
- `COUNT()`
- `ORDER BY`
- `LIMIT`

These queries were used to answer the main business questions related to customers, products, reviews, sales, and conversion.

## 4. Power BI Dashboard

The results of the SQL business analysis were visualized in Power BI through interactive dashboards.

The dashboard was designed to provide an overview of the main e-commerce KPIs and allow the data to be explored across different customer, product, review, and conversion dimensions.

The main areas of analysis include:

- Customer performance
- Product performance
- Sales performance
- Review analysis
- Conversion analysis

Interactive filters and visualizations were used to explore the relationships between the different dimensions of the e-commerce dataset.

## 5. Key Findings

The analysis produced several relevant findings:

- Electronics generated the highest revenue.
- Bronze customers generated the highest total revenue.
- Conversion rates were similar across device types.
- Product ratings showed a very weak correlation with sales volume.