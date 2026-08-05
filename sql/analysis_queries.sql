-- =====================================
-- BREWERIES ETL SQL ANALYSIS
-- =====================================

-- 1. View brewery data
SELECT * FROM breweries LIMIT 10;

-- 2. View population data
SELECT * FROM state_population LIMIT 10;

-- 3. Total breweries
SELECT COUNT(*) AS total_breweries
FROM breweries;

-- 4. Total states in population table
SELECT COUNT(*) AS total_states
FROM state_population;

-- 5. Brewery count by state
SELECT
    state,
    COUNT(*) AS brewery_count
FROM breweries
GROUP BY state
ORDER BY brewery_count DESC;

-- 6. Brewery count by type
SELECT
    brewery_type,
    COUNT(*) AS total
FROM breweries
GROUP BY brewery_type
ORDER BY total DESC;

-- 7. Top cities by breweries
SELECT
    city,
    COUNT(*) AS brewery_count
FROM breweries
GROUP BY city
ORDER BY brewery_count DESC
LIMIT 10;

-- 8. Join breweries with population
SELECT
    b.state,
    COUNT(*) AS brewery_count,
    sp.population
FROM breweries b
JOIN state_population sp
ON b.state = sp.state
GROUP BY b.state, sp.population
ORDER BY brewery_count DESC;

-- 9. Breweries per 100,000 population
SELECT
    b.state,
    COUNT(*) AS brewery_count,
    sp.population,
    ROUND(
        COUNT(*) * 100000.0 / sp.population,
        2
    ) AS breweries_per_100k
FROM breweries b
JOIN state_population sp
ON b.state = sp.state
GROUP BY b.state, sp.population
ORDER BY breweries_per_100k DESC;

-- 10. States with highest population
SELECT
    state,
    population
FROM state_population
ORDER BY population DESC
LIMIT 10;

-- 11. States with lowest population
SELECT
    state,
    population
FROM state_population
ORDER BY population ASC
LIMIT 10;

-- 12. Missing state values
SELECT *
FROM breweries
WHERE state IS NULL;

-- 13. Create index
CREATE INDEX idx_breweries_state
ON breweries(state);

CREATE INDEX idx_population_state
ON state_population(state);

-- 14. Query optimization check
EXPLAIN ANALYZE
SELECT
    b.state,
    COUNT(*),
    sp.population
FROM breweries b
JOIN state_population sp
ON b.state = sp.state
GROUP BY b.state, sp.population;