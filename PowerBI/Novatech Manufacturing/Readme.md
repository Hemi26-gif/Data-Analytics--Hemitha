**Novatech Manufacturing Analytics | Power BI Project**
<img width="775" height="438" alt="01_EXECUTIVE OVERVIEW" src="https://github.com/user-attachments/assets/a8c91c90-80c9-4b53-bf48-05687b1e7474" />

**Project Overview**
Novatech Manufacturing Analytics is an end-to-end Business Intelligence
project developed using Microsoft Power BI. It brings together
manufacturing, quality, operational, finance, procurement, and
supply-chain analysis to help management understand operational
inefficiencies, financial cost exposure, and potential supply-chain
risks.

Novitech Manufacturing operates multiple plants and produces different
products using raw materials purchased from external suppliers. The
available data covers production runs, products, plants, operators, raw
materials, suppliers, bill of materials, and purchase orders.
Business Problem
Operational and procurement data is distributed across separate
datasets. Management therefore lacks a centralized view of how
production output, defective production, downtime, energy consumption,
product costs, procurement spending, supplier performance, and material
dependencies collectively affect manufacturing efficiency and financial
exposure.

Core business question: Where is Novitech Manufacturing losing
operational efficiency and carrying financial exposure, and what
production or supply-chain factors are contributing to those risks?
Project Objectives
- Analyze production output and trends by date, plant, product,
  operator, and shift.
- Compare plant performance using production, defects, downtime,
  energy, and cost exposure.
- Identify products and plants with high defective quantities and
  defect rates.
- Analyze downtime and energy consumption, including energy per unit
  produced.
- Compare operational outcomes across operators, shifts, and
  experience levels.
- Analyze product unit costs and potential unit margin context.
- Estimate defect-related cost exposure.
- Analyze procurement spending, purchase-order delays, and lead times.
- Compare supplier ratings with observed delivery performance.
- Identify critical raw-material dependencies and potential
  supply-chain risks.
- Provide evidence-based insights and recommendations for management.
Tools & Technologies
  Tool / Technology    Purpose
  Microsoft Excel      Initial dataset inspection
Power Query          Data cleaning and transformation
Microsoft Power BI   Interactive dashboard development
DAX                  KPI calculations and analytical measures
Data Modeling        Fact, dimension, and bridge-table relationships
Dataset Structure
Fact Tables
- fact_production_runs --- Production, quality, downtime, energy,
  and estimated cost-exposure analysis.
- fact_purchase_orders --- Procurement spending, purchase orders,
  lead times, and delivery delays.
Dimension Tables
- dim_plants --- Manufacturing plant information.
- dim_products --- Product, category, unit cost, and target price
  information.
- dim_operators --- Operator, shift, and experience information.
- dim_raw_materials --- Raw-material details and standard costs.
- dim_suppliers --- Supplier information and ratings.
Bridge Table
- bridge_bill_of_materials --- Product-to-material dependencies.
Power BI Dashboard Pages
The project requirements define seven interactive report pages.
1. Executive Overview
A consolidated view of key manufacturing and financial indicators:
- Total Production
- Total Defects
- Defect Rate
- Total Downtime
- Total Energy
- Total Procurement Spend
- Delayed Orders
- Estimated Defect Cost Exposure
2. Production & Plant Performance
- Production trends
- Plant comparison
- Production by product and category
- Plant operational KPIs
3. Quality & Operational Efficiency
- Defect analysis
- Downtime analysis
- Energy analysis
- Energy per unit
- Operational efficiency comparison
4. Finance & Cost Analysis
- Total procurement spend
- Spend by supplier and material
- Product unit cost
- Potential unit margin
- Estimated production cost context
- Estimated defect cost exposure
5. Procurement & Supplier Performance
- Purchase orders
- Delay rate
- Lead time
- Supplier rating
- Supplier performance
- Procurement spend
6. Raw Materials & Supply Chain Risk
- Material standard cost
- Product-material dependencies
- Materials per product
- Critical material dependencies
7. Operator & Shift Performance
- Operator output
- Shift comparison
- Defects
- Downtime
- Operator experience context
Key DAX Measures
  Measure                             Business Logic
  Total Production                    Total quantity produced

  Total Defects                       Total defective units

  Defect Rate                         Defects ÷ Production

  Total Production Runs               Count of production runs

  Total Downtime                      Total operational time loss

  Average Downtime per Run            Average downtime per production run

  Total Energy                        Total energy consumed

  Energy per Unit                     Total energy ÷ Total production

  Total Procurement Spend             Quantity ordered × Unit price

  Total Purchase Orders               Count of purchase orders

  Delayed Orders                      Count of delayed orders

  Delay Rate                          Delayed orders ÷ Total orders

  Average Lead Time                   Average procurement lead time

  Potential Unit Margin               Target price − Unit cost

  Estimated Defect Cost Exposure      Defective quantity × Unit cost

  Estimated Production Cost Context   Produced quantity × Unit cost
Potential Production Value Context  Produced quantity × Target price
The denominator and aggregation logic for each measure should be
validated against the dataset's actual field definitions and table
grain.
Project Workflow
1. Business understanding --- Review the Business Requirements
   Document and identify management questions.
2. Data exploration --- Inspect datasets, columns, data types, and
   available keys.
3. Data cleaning --- Investigate nulls, blanks, duplicates,
   inconsistent categories, and invalid values using Power Query.
4. Data transformation --- Validate quantities, costs, prices,
   downtime, energy, lead-time, ratings, and date fields.
5. Data modeling --- Build and validate relationships between fact,
   dimension, and bridge tables.
6. DAX development --- Create operational, quality, finance, and
   supply-chain measures.
7. Dashboard development --- Build the seven-page interactive Power
   BI report.
8. Analysis and recommendations --- Identify data-supported
   performance gaps, cost exposure, and potential supply-chain risks.
Business Questions
The dashboard is designed to help investigate questions such as:
- Which plants have the strongest and weakest production performance?
- Which products and plants have higher defective quantities or defect
  rates?
- Where is downtime concentrated?
- Which operations consume more energy per unit produced?
- Which products have the highest unit costs?
- Which products have the highest or lowest potential unit margin?
- Which products and plants have higher estimated defect cost
  exposure?
- Which suppliers receive the highest procurement spend?
- Which suppliers experience the greatest delivery delays?
- Which raw materials are shared across multiple products?
- Which suppliers combine high procurement spend with poor delay
  performance?
Financial Assumptions & Limitations
Financial measures must be interpreted according to the available data:
- Actual sales transactions are not available; actual revenue and
  profit cannot be calculated.
- Target Price is not actual selling price.
- Potential Unit Margin (Target Price − Unit Cost) is not actual
  profit.
- Estimated Defect Cost Exposure
  (Defective Quantity × Unit Cost) is an estimate, not confirmed
  scrap or rework cost.
- Estimated Production Cost Context
  (Produced Quantity × Unit Cost) is not a formal accounting Cost of
  Goods Sold (COGS) calculation.
- Potential Production Value Context
  (Produced Quantity × Target Price) is a target-price scenario, not
  actual revenue.
- Actual discounts, returns, tax, and customer-level sales information
  are unavailable.
- Material dependency and procurement delays can indicate potential
  supply-chain risk; direct causation should not be claimed without
  supporting evidence.
Expected Deliverables
- Cleaned and transformed data using Power Query
- Validated fact-dimension data model
- DAX measures for operational, quality, financial, and supply-chain
  KPIs
- Seven-page interactive Power BI report
- Evidence-based business insights
- Prioritized management recommendations
- Documentation of KPI definitions, assumptions, and limitations
Conclusion
Novatech Manufacturing Analytics demonstrates how Business Intelligence
can bring manufacturing and procurement information into a centralized
analytical solution. By examining production, quality, downtime, energy,
product cost, procurement, supplier performance, and material
dependencies together, the project supports management in identifying
operational inefficiencies, understanding financial exposure, and
investigating potential supply-chain risks.
Project: Novatech Manufacturing Analytics
Industry: Manufacturing
Domain: Manufacturing Analytics & Business Intelligence
Platform: Microsoft Power BI
BRD Version: 2.0 --- Finance Included
Project Type: End-to-End Data Analytics Project
