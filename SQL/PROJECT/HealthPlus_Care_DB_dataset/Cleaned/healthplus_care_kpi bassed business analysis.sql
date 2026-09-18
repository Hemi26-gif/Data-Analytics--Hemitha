# Total revenue
SELECT SUM(total_amount) AS total_revenue
FROM billing;

# Consultation mix
SELECT consultation_mode, COUNT(*) AS total
FROM consultations
GROUP BY consultation_mode;

# Payment status breakdown
SELECT payment_status, COUNT(*) AS total
FROM payments
GROUP BY payment_status;
SELECT payment_status, COUNT(*) AS total
FROM payments GROUP BY payment_status;

# Top specializations
SELECT specialization,
       COUNT(*) AS total_specialists
FROM specialists
GROUP BY specialization
ORDER BY total_specialists DESC;

# Average feedback rating
SELECT AVG(rating) AS average_rating
FROM feedback;

# Validated revenue (excl. bad rows)
SELECT SUM(total_amount) AS validated_revenue
FROM billing
WHERE total_amount > 0;

# Leakage rate by clinic
SELECT clinic_id,
  ROUND(100.0*SUM(CASE WHEN status IN
  ('cancelled','no_show') THEN 1 ELSE 0 END)
  /COUNT(*),2) AS leakage_rate_pct
FROM consultations
GROUP BY clinic_id
ORDER BY leakage_rate_pct DESC;

# Telemedicine vs in-clinic completion
SELECT consultation_mode,
  ROUND(100.0*SUM(CASE WHEN status='completed'
  THEN 1 ELSE 0 END)/COUNT(*),2) AS
  completion_rate_pct
FROM consultations
GROUP BY consultation_mode;

# Claims aging by provider
SELECT insurance_provider,
  COUNT(*) AS pending_claims,
  ROUND(AVG(DATEDIFF(CURRENT_DATE,
  claim_date)),1) AS avg_days_pending
FROM claims
WHERE claim_status='pending'
GROUP BY insurance_provider
ORDER BY pending_claims DESC;

# Segment & subscription retention
SELECT m.membership_type,
  COUNT(DISTINCT m.member_id) AS members,
  SUM(CASE WHEN s.subscription_status='active'
  THEN 1 ELSE 0 END) AS active_subscriptions
FROM members m JOIN subscriptions s
  ON m.member_id = s.member_id
GROUP BY m.membership_type;

# Low-rating feedback hotspots
SELECT clinic_id, specialist_id,
  ROUND(AVG(rating),2) AS avg_rating,
  COUNT(*) AS feedback_count
FROM feedback
WHERE rating <= 2
GROUP BY clinic_id, specialist_id
ORDER BY feedback_count DESC
LIMIT 10;
 



