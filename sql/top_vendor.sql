SELECT vendor, SUM(amount) AS total_amount
FROM invoices
WHERE created_at >= CURRENT_DATE - INTERVAL '30 days'
    AND status IN ('Approved')
GROUP BY vendor
ORDER BY total_amount DESC
LIMIT 5;