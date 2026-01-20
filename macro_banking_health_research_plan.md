# Research Plan: Macroeconomic Indicators & Banking Sector Health in Bangladesh

**Topic:** The Impact of Macroeconomic Variables on Non-Performing Loans (NPLs) in the Bangladeshi Banking Sector.

## 1. Research Objectives
- To investigate the long-run and short-run relationship between macroeconomic indicators and NPLs in Bangladesh.
- To determine if factors like Inflation, GDP Growth, and Interest Rates significantly affect the credit quality of banks.
- To forecast future trends of NPLs based on macroeconomic projections.

## 2. Key Variables & Data Sources

### Dependent Variable
- **Non-Performing Loan (NPL) Ratio:** Gross NPL to Total Loans ratio.
  - *Source:* Bangladesh Bank (Quarterly Scheduled Banks Statistics), Annual Reports of Bangladesh Bank.

### Independent Variables (Macroeconomic)
1.  **GDP Growth Rate:** A proxy for economic activity. Higher growth typically leads to lower NPLs (borrowers have more income).
    - *Source:* World Bank Open Data, Bangladesh Bureau of Statistics (BBS).
2.  **Inflation Rate (CPI):** High inflation can erode real income, making loan repayment difficult.
    - *Source:* Bangladesh Bank Economic Data, World Bank.
3.  **Interest Rate (Lending Rate):** Higher interest rates increase the cost of borrowing, potentially leading to defaults.
    - *Source:* Bangladesh Bank (Monthly Economic Trends).
4.  **Exchange Rate (BDT/USD):** Fluctuations can affect importers/exporters, impacting their ability to repay loans.
    - *Source:* Bangladesh Bank.
5.  **Broad Money Supply (M2):** Liquidity in the economy.
    - *Source:* Bangladesh Bank.

## 3. Data Frequency
- Ideally **Quarterly** data (since NPLs are often reported quarterly).
- If quarterly GDP is unavailable, you might need to use interpolation methods or stick to Annual data (though annual data requires a very long time horizon, e.g., 1980-2023, to have enough data points).

## 4. Methodology (Econometric Approach)

Since you are dealing with time-series data, standard regression (OLS) might give spurious results if data is non-stationary.

1.  **Unit Root Test:**
    - Use **Augmented Dickey-Fuller (ADF)** or **Phillips-Perron (PP)** tests to check if variables are stationary.
2.  **Cointegration Test:**
    - If variables are non-stationary but integrated of the same order, use **Johansen Cointegration Test** to check for a long-run relationship.
3.  **Model Selection:**
    - **Vector Autoregression (VAR):** If there is no cointegration.
    - **Vector Error Correction Model (VECM):** If cointegration exists (captures both short-run and long-run dynamics).
    - **ARDL (Autoregressive Distributed Lag):** Useful if you have a mix of stationary (I(0)) and non-stationary (I(1)) variables.
4.  **Granger Causality:**
    - To check the direction of causality (e.g., Does GDP cause NPL changes, or vice-versa?).

## 5. Tools & Software
- **Python:** `pandas`, `statsmodels` (for ADF, OLS, VAR/VECM).
- **R:** `urca`, `vars`, `tseries` packages.
- **EViews / STATA:** Very popular for this specific type of econometric analysis in finance.

## 6. Structure of the Thesis
1.  **Introduction:** Background of Banking in Bangladesh, Definition of NPL, Problem Statement.
2.  **Literature Review:** Previous studies on Macro factors vs. NPLs (Global vs. Bangladesh context).
3.  **Methodology:** Explanation of ADF, Cointegration, VECM/ARDL.
4.  **Data Analysis:** Descriptive statistics, graphs of trends, test results.
5.  **Discussion:** Interpret coefficients (e.g., "A 1% increase in Lending Rate leads to a 0.5% increase in NPLs").
6.  **Conclusion & Policy Implications:** What should the Central Bank do?

## 7. Next Immediate Steps
1.  **Visit Bangladesh Bank Website:** Go to the "Research & Publications" or "Economic Data" section.
2.  **Download "Monthly Economic Trends":** This is a goldmine for monthly/quarterly data.
3.  **Compile Excel Sheet:** Create a master CSV with columns: `Date`, `NPL_Ratio`, `GDP`, `Inflation`, `Lending_Rate`.
