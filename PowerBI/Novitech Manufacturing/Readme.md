# 🏭 AeroHome Manufacturing Analytics – Power BI Project
<img width="775" height="438" alt="01_EXECUTIVE OVERVIEW" src="https://github.com/user-attachments/assets/4d7fe2e5-681b-4054-9a88-4321eb38d146" />

## 📌 Project Overview

**AeroHome Manufacturing Analytics** is an end-to-end Business Intelligence project developed using Microsoft Power BI to analyze manufacturing operations and identify performance gaps across multiple manufacturing plants.

AeroHome Manufacturing produces home appliances such as washing machines, air conditioners, refrigerators, microwave ovens, and dishwashers.

The project focuses on analyzing production performance, product quality, machine downtime, operational efficiency, financial exposure, procurement spending, supplier performance, and raw-material dependencies.

The main objective is to transform raw manufacturing data into meaningful business insights through interactive dashboards that support management decision-making.

## 🎯 Business Problem

AeroHome Manufacturing records large amounts of operational data across different departments. However, management lacks a centralized analytical solution to understand:

- Why production targets are not achieved.
- Which plants and machines experience performance issues.
- What causes production downtime.
- Which products have higher defect rates.
- How much financial exposure is associated with defective products.
- Which suppliers experience delivery delays.
- Which raw materials create supply-chain dependencies.

This project addresses these challenges by developing a centralized Power BI analytical solution.

## 🎯 Project Objectives

- Analyze planned versus actual production performance.
- Identify production shortfalls across plants and products.
- Evaluate machine performance and downtime causes.
- Monitor product quality and defect patterns.
- Analyze operator and shift performance.
- Measure energy consumption and operational efficiency.
- Estimate defect-related cost exposure.
- Analyze procurement spending and supplier reliability.
- Identify critical raw-material dependencies.
- Provide data-driven insights and recommendations.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Microsoft Excel | Initial dataset inspection |
| Power Query | Data cleaning and transformation |
| Power BI | Interactive dashboard development |
| DAX | KPI calculations and business measures |
| Data Modeling | Fact and dimension relationships |

## 📂 Dataset Description

The project uses multiple datasets organized into dimension, fact, and bridge tables.

### Dimension Tables
- `dim_plants` – Plant locations and production capacity.
- `dim_products` – Product details, categories, unit costs, and target prices.
- `dim_machines` – Machine types and plant assignments.
- `dim_operators` – Operator details, experience, and shift information.
- `dim_suppliers` – Supplier information, country, and ratings.
- `dim_materials` – Raw-material details and standard costs.

### Fact Tables
- `fact_production` – Planned production, actual production, defects, downtime, and energy consumption.
- `fact_quality` – Quality inspections, defective units, and inspection outcomes.
- `fact_downtime` – Downtime duration, reasons, and categories.
- `fact_purchase_orders` – Procurement quantities, prices, suppliers, and delivery information.

### Bridge Table
- `bridge_bill_of_materials` – Product-to-material dependencies and required quantities.

## 📊 Dashboard Pages

The Power BI solution contains nine analytical dashboard pages.

### 1. Executive Overview
Provides a centralized view of overall manufacturing performance.

Key metrics:
- Total Planned Units
- Total Produced Units
- Production Achievement %
- Total Defects
- Defect Rate
- Total Downtime
- Total Energy Consumption
- Total Procurement Spend
- Estimated Defect Cost Exposure

### 2. Production & Plant Performance
Analyzes production performance across manufacturing plants.

Key analysis:
- Planned vs Actual Production
- Production Achievement by Plant
- Production Shortfall
- Production Trends
- Production by Product
- Production by Machine

### 3. Machine & Downtime Analysis
Identifies machine-related operational interruptions.

Key analysis:
- Total Downtime
- Downtime by Machine
- Downtime by Machine Type
- Downtime Reasons
- Downtime Categories
- Downtime Trends
- Machine and Plant Comparison

### 4. Quality Analysis
Evaluates manufacturing quality and inspection performance.

Key analysis:
- Units Inspected
- Defective Units
- Defect Rate
- Defect Type Analysis
- Inspection Status
- Pass, Fail, and Rework Analysis
- Product and Plant Quality Comparison

### 5. Operational Efficiency
Combines production, quality, downtime, and energy indicators.

Key analysis:
- Production Achievement
- Defect Rate
- Machine Downtime
- Energy Consumption
- Energy per Unit Produced
- Plant Efficiency Comparison

### 6. Finance & Cost Analysis
Provides financial and product cost exposure insights.

Key analysis:
- Procurement Spending
- Spending by Supplier
- Spending by Material
- Product Unit Cost
- Potential Unit Margin
- Estimated Production Cost Context
- Estimated Defect Cost Exposure

### 7. Procurement & Supplier Performance
Evaluates purchasing activities and supplier delivery reliability.

Key analysis:
- Purchase Order Volume
- Procurement Spend
- Expected vs Actual Lead Time
- Delivery Status
- Supplier Rating
- Supplier Delivery Comparison

### 8. Materials & Supply Chain Risk
Analyzes raw-material dependencies and potential supply-chain risks.

Key analysis:
- Material Standard Cost
- Product-Material Dependency
- Materials Used Across Products
- Materials per Product
- High-Cost Material Dependency
- Material Shortage Downtime Context

### 9. Operator & Shift Performance
Evaluates workforce-related production and quality patterns.

Key analysis:
- Production by Operator
- Production by Shift
- Defects by Operator and Shift
- Downtime Context
- Operator Experience Analysis

## 📈 Key DAX Measures

The following business measures are developed for manufacturing performance analysis.

| KPI | Calculation |
|---|---|
| Production Achievement % | Produced Units / Planned Units |
| Production Shortfall | Planned Units - Produced Units |
| Defect Rate | Defective Units / Relevant Production or Inspection Denominator |
| Total Downtime | SUM(Downtime Minutes) |
| Energy per Unit | Total Energy / Total Produced Units |
| Quality Pass Rate | Passed Inspections / Total Inspections |
| Quality Fail Rate | Failed Inspections / Total Inspections |
| Rework Rate | Rework Inspections / Total Inspections |
| Procurement Spend | Quantity Ordered × Unit Price |
| Delivery Delay Difference | Actual Lead Days - Expected Lead Days |
| Potential Unit Margin | Target Price - Unit Cost |
| Estimated Defect Cost Exposure | Defective Units × Product Unit Cost |

## 🔄 Project Workflow

1. **Data Understanding:** Explore the manufacturing datasets and understand the business requirements.
2. **Data Cleaning:** Use Power Query to handle null values, duplicates, data types, and inconsistent text values.
3. **Data Transformation:** Prepare datasets and create derived columns wherever required.
4. **Data Modeling:** Establish appropriate relationships between fact, dimension, and bridge tables.
5. **DAX Development:** Create calculated measures for production, quality, downtime, finance, and procurement.
6. **Dashboard Development:** Build nine interactive Power BI dashboard pages.
7. **Business Analysis:** Identify operational performance gaps and important business patterns.
8. **Recommendations:** Provide actionable recommendations based on data-supported findings.

## 💡 Expected Business Insights

The analytical solution helps management investigate:

- Plants with lower production achievement.
- Products contributing to production shortfalls.
- Machines associated with higher downtime.
- Major manufacturing defect categories.
- Quality inspection failures and rework patterns.
- Energy consumption relative to production output.
- Products with higher estimated defect cost exposure.
- Suppliers with longer actual delivery lead times.
- High-cost materials with broad product dependencies.
- Operator and shift-level production patterns.

## ⚠️ Assumptions & Limitations

- Actual sales transactions and revenue data are not available.
- Target Price is not considered actual selling price.
- Potential Unit Margin is not considered actual profit.
- Estimated Defect Cost Exposure is not confirmed scrap or rework cost.
- Material shortages and supplier delays are analyzed as potential risk indicators; direct causation is not assumed.
- Different fact tables have different levels of detail, so calculations must respect their respective data grains.


## 🏁 Conclusion

The AeroHome Manufacturing Analytics project demonstrates how Business Intelligence can transform manufacturing data into actionable insights.

By integrating production, quality, machine, operational, financial, and supply-chain analysis into a centralized Power BI solution, the project helps management identify performance gaps, investigate operational risks, and make informed business decisions.

---

**Project Name:** AeroHome Manufacturing Analytics  
**Industry:** Home Appliance Manufacturing  
**Domain:** Manufacturing Analytics / Business Intelligence  
**Tool:** Microsoft Power BI  
**Project Type:** End-to-End Data Analytics Project
