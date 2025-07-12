CREATE TABLE invoices (
    id SERIAL PRIMARY KEY,
    vendor TEXT,
    amount NUMERIC,
    status TEXT,
    created_at DATE
);

INSERT INTO invoices (vendor, amount, status, created_at) VALUES
('Tech Solutions Ltd', 25000, 'Approved', '2025-01-15'),
('Global Supply Co', 32000, NULL, '2025-01-17'),
('Innovation Corp', NULL, 'Approved', '2025-01-18'),
('Smart Systems', 0, 'Rejected', NULL),
('Data Bridge Inc', 41500, 'Approved', '2025-01-20'),
('Future Tech', NULL, NULL, '2025-01-22'),
('Cloud Services', -500, 'Error', '2025-01-23');
