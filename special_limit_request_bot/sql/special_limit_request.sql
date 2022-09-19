SELECT a1.idxCorp, a2.resCompanyNm AS 법인명, FORMAT(a3.hopeLimit,0) AS 희망한도, DATE(a1.createdAt) AS 심사요청일, DATE(DATE_SUB(a1.createdAt, INTERVAL -5 DAY)) AS 마감예정일
FROM LimitReview a1
INNER JOIN Corp a2 ON a2.idx = a1.idxCorp
INNER JOIN CardIssuanceInfo a3 ON a3.idxCorp = a1.idxCorp
WHERE receiptStatus IN ('REQUESTED')
ORDER BY idxCorp ASC
