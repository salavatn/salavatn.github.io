
SELECT
  company.name AS "Company",
  company.city AS "City",
  COUNT(job.TITLE) AS JobCount
FROM company

INNER JOIN job
  ON company.ID = job.COMPANY_ID

-- WHERE company.city = 'Cupertino'
GROUP BY company.name, company.city

HAVING JobCount > 10
ORDER BY JobCount DESC

-- SELECT HAVING 
SELECT
  company.name AS "Company",
  company.city AS "City",
  COUNT(job.TITLE) AS JobCount
FROM company
INNER JOIN job
  ON company.ID = job.COMPANY_ID
HAVING JobCount > 10
ORDER BY JobCount DESC
