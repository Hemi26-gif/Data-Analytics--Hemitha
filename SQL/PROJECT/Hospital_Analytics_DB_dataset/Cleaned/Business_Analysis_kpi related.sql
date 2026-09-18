-- KPI Related Question

-- 1. Executive Revenue KPI
-- How much value has the hospital billed, and what is the average bill?
SELECT
    COUNT(*) AS total_bills,
    ROUND(SUM(total_amount), 2) AS total_billed,
    ROUND(AVG(total_amount), 2) AS avg_bill,
    ROUND(MAX(total_amount), 2) AS highest_bill
FROM Billing;

-- 2. Revenue by Department
-- Which departments generate the most billing value?
SELECT
    d.department_name,
    COUNT(DISTINCT b.bill_id) AS bills,
    ROUND(SUM(b.total_amount), 2) AS revenue
FROM Billing b
JOIN Admissions a ON b.admission_id = a.admission_id
JOIN Departments d ON a.department_id = d.department_id
GROUP BY d.department_name
ORDER BY revenue DESC;

-- 3. Patient & Admission Flow
-- How many appointments convert into admissions?
SELECT
    COUNT(DISTINCT a.appointment_id) AS appointments,
    COUNT(DISTINCT ad.admission_id) AS admissions,
    ROUND(100.0 * COUNT(DISTINCT ad.admission_id)
        / NULLIF(COUNT(DISTINCT a.appointment_id), 0), 2) AS admission_rate_pct
FROM Appointments a
LEFT JOIN Admissions ad ON a.patient_id = ad.patient_id;

-- 4. Payment Collection
-- How much of the billed value has actually been collected?
SELECT
    ROUND(SUM(b.total_amount), 2) AS billed_value,
    ROUND(SUM(COALESCE(p.amount_paid, 0)), 2) AS collected_value,
    ROUND(100.0 * SUM(COALESCE(p.amount_paid, 0))
        / NULLIF(SUM(b.total_amount), 0), 2) AS collection_rate_pct
FROM Billing b
LEFT JOIN Payments p ON b.bill_id = p.bill_id;

-- 5. Data Quality Validation
-- Can management trust the patient and transaction data?
-- Missing / invalid values
SELECT COUNT(*) AS missing_phone FROM Patients
WHERE phone IS NULL OR TRIM(phone) = '';

-- Duplicate business keys
SELECT patient_id, COUNT(*) AS duplicate_count
FROM Patients GROUP BY patient_id HAVING COUNT(*) > 1;

-- Orphan records
SELECT COUNT(*) AS orphan_admissions
FROM Admissions a
LEFT JOIN Patients p ON a.patient_id = p.patient_id
WHERE p.patient_id IS NULL;

-- 6 Cost vs Revenue
-- Which service areas should management investigate for profitability?
SELECT
    d.department_name,
    ROUND(SUM(t.treatment_cost), 2) AS treatment_cost,
    ROUND(SUM(b.total_amount), 2) AS billed_revenue,
    ROUND(SUM(b.total_amount) - SUM(t.treatment_cost), 2) AS contribution_gap
FROM Treatments t
JOIN Admissions a ON t.admission_id = a.admission_id
JOIN Departments d ON a.department_id = d.department_id
LEFT JOIN Billing b ON a.admission_id = b.admission_id
GROUP BY d.department_name
ORDER BY contribution_gap DESC;




