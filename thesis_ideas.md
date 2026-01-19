# Thesis Research Ideas in Finance and Banking

Here are several research ideas for a thesis in finance and banking, paired with publicly available datasets.

## 1. Credit Risk Assessment & Default Prediction
**Objective:** Develop machine learning models to predict the probability of a borrower defaulting on a loan. compare traditional statistical methods (Logistic Regression) with advanced ML techniques (XGBoost, Neural Networks).

**Datasets:**
- **German Credit Data (UCI Machine Learning Repository):** A classic dataset classifying people by good or bad credit risks.
- **LendingClub Loan Data (Kaggle):** Contains complete loan data for all loans issued through 2007-2015, including current loan status (Current, Late, Fully Paid, etc.) and latest payment information.
- **Home Credit Default Risk (Kaggle):** Predict how capable each applicant is of repaying a loan.

## 2. Financial Fraud Detection
**Objective:** Build a system to detect fraudulent credit card transactions. This often involves handling highly imbalanced datasets (very few fraud cases vs. legitimate ones).

**Datasets:**
- **Credit Card Fraud Detection (Kaggle):** Transactions made by credit cards in September 2013 by European cardholders. It contains only numerical input variables which are the result of a PCA transformation.
- **PaySim Mobile Money Simulator (Kaggle):** Synthetic dataset for fraud detection in mobile money transfer.

## 3. Customer Churn Prediction in Banking
**Objective:** Analyze factors contributing to customer attrition and build a predictive model to identify customers likely to leave the bank.

**Datasets:**
- **Bank Customer Churn Modeling (Kaggle):** Contains details of a bank's customers and the target variable is a binary variable reflecting the fact whether the customer left the bank (closed his account) or he continues to be a customer.

## 4. Stock Market Volatility & Price Prediction
**Objective:** Use Time Series analysis (ARIMA, LSTM) to predict stock prices or volatility. Another angle is to study the correlation between different sectors.

**Datasets:**
- **Yahoo Finance:** You can access historical market data using the `yfinance` Python library.
- **S&P 500 Stock Data (Kaggle):** Historical stock data for S&P 500 companies.

## 5. Sentiment Analysis for Financial Markets (Behavioral Finance)
**Objective:** Investigate the impact of news headlines or social media sentiment on stock prices or market trends.

**Datasets:**
- **Financial PhraseBank (Hugging Face / Research):** Sentences from financial news suitable for sentiment classification.
- **Daily News for Stock Market Prediction (Kaggle):** News headlines from Reddit WorldNews Channel and DJIA stock prices.

## 6. Cryptocurrency Analysis
**Objective:** Analyze the price dynamics of cryptocurrencies, study the correlation between Bitcoin and altcoins, or predict price movements using deep learning.

**Datasets:**
- **Cryptocurrency Historical Prices (Kaggle/CoinGecko):** Historical data for Bitcoin, Ethereum, etc.

## 7. Portfolio Optimization with Robo-Advising
**Objective:** Create an algorithm for automated portfolio construction based on user risk tolerance and historical asset returns (Markowitz Efficient Frontier).

**Datasets:**
- Use **Yahoo Finance (`yfinance`)** to pull historical data for a basket of assets (Stocks, Bonds, ETFs).

## Next Steps
1. **Select a Topic:** Choose the one that interests you most.
2. **Exploratory Data Analysis (EDA):** Download the dataset and perform initial analysis.
3. **Literature Review:** Read existing papers on the chosen topic.
4. **Methodology:** Decide on the algorithms/models you will use.
