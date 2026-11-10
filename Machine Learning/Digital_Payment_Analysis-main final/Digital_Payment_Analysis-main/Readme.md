# 💳 Digital Payment Failure Analysis & Revenue Recovery Dashboard

### An Interactive Analytics Dashboard for Payment Failure Monitoring, Revenue Recovery, Refund Reconciliation & ML-Based Risk Prediction
<img width="1357" height="632" alt="image" src="https://github.com/user-attachments/assets/a3039ce4-e21b-4474-b938-24b8bb8d1154" />

## 📌 Project Overview

Digital payments have become an essential part of everyday transactions. However, payment failures, technical timeouts, pending transactions, delayed refunds, and settlement mismatches can lead to revenue loss and poor customer experiences.

This project focuses on analyzing digital payment transactions to identify failure patterns, monitor pending payments, recover lost revenue through retry attempts, and investigate refund and settlement discrepancies.

The project provides an interactive dashboard that helps business stakeholders understand payment performance, identify operational issues, monitor financial risks, and make data-driven decisions.

## 🎯 Business Objectives

- Analyze overall digital payment performance and transaction success rates.
- Identify the major reasons behind payment failures.
- Measure revenue recovered through successful retry attempts.
- Monitor long-pending transactions and potential double-debit risks.
- Track refund completion and gateway settlement discrepancies.
- Apply Machine Learning to estimate payment failure risk.

## 📊 Dashboard Modules

### 1. Executive Overview
Provides a high-level view of payment performance and financial metrics.

**Key Metrics:**
- Gross Transaction Volume
- Payment Success Rate
- Payment Failure Rate
- Retry Recovered Revenue
- Net Revenue Leakage

**Analysis:**
- Transaction volume and outcome trends.
- Revenue leakage analysis.
- Payment gateway performance comparison.
- Payment method distribution and efficiency.

### 2. Payment Failure Analysis
Identifies the major reasons behind failed digital payment transactions.

**Key Metrics:**
- Total Failed Transactions
- Technical Timeouts
- Bank Declines
- Customer-Related Errors

**Analysis:**
- Error code analysis using Pareto charts.
- Root cause responsibility analysis.
- Gateway vs Payment Method failure heatmap.
- Hourly failure trends.
- Failure rate by transaction amount.
- Payment processing latency analysis.

### 3. Retry Recovery Analysis
Analyzes how retry attempts help recover failed transactions and reduce revenue leakage.

**Key Metrics:**
- Recovered Transaction Volume
- Retry Recovery Success Rate
- Overall Success Rate Improvement
- Unretried Revenue Opportunity

**Analysis:**
- Conversion rate before and after retries.
- Recovery rate by failure reason.
- Monthly recovered revenue trends.
- Retry time-to-resolution.
- Identification of high-value failed transactions that were never retried.

### 4. Pending Payment Monitoring
Monitors transactions that remain in pending status beyond expected processing times.

**Key Metrics:**
- Total Stuck Pending Transactions
- Transactions Pending More Than 15 Minutes
- Transactions Pending More Than 30 Minutes
- Double-Debit Risk Exposure

**Analysis:**
- Pending transaction severity by gateway.
- Pending transaction inflow by hour.
- SLA-based monitoring.
- Identification of potential duplicate debit risks.
- Pending transaction escalation worklist.

### 5. Refund & Settlement Reconciliation
Focuses on identifying refund delays, settlement gaps, and financial reconciliation exceptions.

**Key Metrics:**
- Total Refund Volume
- Completed Refund Amount
- Unsettled Refund Amount
- Gateway Settlement Gap
- Audit Exceptions

**Analysis:**
- Refund aging and SLA monitoring.
- Expected vs actual gateway payout comparison.
- Refund and settlement exception tracking.
- Priority-based audit investigation (P1, P2, P3).

### 6. Machine Learning Risk Analysis
Uses Machine Learning to estimate the probability of payment failure based on transaction characteristics.

**Models Implemented:**
- Logistic Regression
- Random Forest Classifier

**Features Considered:**
- Transaction Amount
- Payment Method
- Payment Gateway
- Transaction Time
- Customer Historical Failure Rate
- Day of the Week

**Key Features:**
- Model performance comparison.
- Confusion matrix visualization.
- Failure recall and ROC-AUC evaluation.
- Interactive failure risk simulator.
- Transaction risk classification.

*Note: The ML evaluation currently uses a limited cleaned sample of 374 records, with 299 training records and 75 test records. The model results are experimental and require further validation before production use.*

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| HTML5 | Dashboard structure |
| CSS3 | Dashboard styling and responsive layout |
| JavaScript | Interactive functionality and data processing |
| Chart.js | Data visualization |
| Python | Machine Learning model development |
| Scikit-learn | Model training and evaluation |
| Pandas | Data preprocessing and manipulation |

## 📈 Key Project Insights

Based on the current dashboard dataset:

| Metric | Result |
|---|---:|
| Total Transactions | 5,000 |
| Gross Transaction Volume | ₹62.21M |
| Successful Transactions | 3,488 |
| Payment Success Rate | 69.76% |
| Failed Transactions | 977 |
| Payment Failure Rate | 19.54% |
| Recovered Transactions | 441 |
| Retry Recovered Revenue | ₹5.57M |
| Stuck Pending Transactions | 535 |
| Unsettled Refund Amount | ₹2.39M |

These metrics help identify payment performance issues, revenue recovery opportunities, and areas requiring operational attention.

## 💡 Business Recommendations

1. **Improve Payment Gateway Performance:** Investigate gateways with higher failure rates and technical timeout issues.
2. **Implement Smart Retry Mechanisms:** Encourage retry attempts for recoverable payment failures.
3. **Monitor Pending Transactions:** Introduce automated alerts for transactions exceeding defined SLA thresholds.
4. **Prevent Double Debits:** Prioritize investigation of customers who initiate another payment while an earlier transaction remains pending.
5. **Improve Refund Processing:** Monitor delayed refunds and investigate unsettled amounts.
6. **Strengthen Failure Prediction:** Improve model performance with more representative transaction data and further validation.

## 📂 Project Structure

```text
Digital-Payment-Analysis/
│
├── index.html          # Main dashboard structure
├── style.css           # Dashboard styling
├── app.js              # Dashboard interactions and logic
├── data.js             # Embedded transaction dataset
├── chart.min.js        # Chart.js local library
│
└── README.md           # Project documentation
```

## 🚀 How to Run the Project

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Open the project folder:

```bash
cd Digital-Payment-Analysis
```

3. Ensure all project files are available in the same directory.

4. Open `index.html` in your browser.

5. Explore the dashboard using the navigation menu, filters, charts, and interactive features.

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Understanding real-world digital payment business problems.
- Identifying business KPIs and analytical requirements.
- Analyzing transaction failures and revenue leakage.
- Building interactive dashboards.
- Performing financial reconciliation analysis.
- Understanding Machine Learning model evaluation.
- Converting analytical findings into actionable business recommendations.

## 👩‍💻 Author

**Hemitha Ilangovan**

B.E. Computer Science and Engineering | 2026

**Areas of Interest:** Data Analytics | Business Intelligence | Machine Learning

---

⭐ If you find this project useful, feel free to explore the repository and share your feedback.
