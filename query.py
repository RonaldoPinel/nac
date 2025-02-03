import cx_Oracle
import pandas as pd

def get_data():
    dsn = cx_Oracle.makedsn("10.15.7.2", 1521, service_name="sankhya.privatesubnet.natvcn.oraclevcn.com")
    user = "SANKHYA"
    senha = "nNO9S5#eHMN93hprod"

    conn = cx_Oracle.connect(user=user, password=senha, dsn=dsn)

    query = '''
    SELECT
	IPI.CODEMP
   ,IPI.CODVEND
   ,VEN.APELIDO
   ,NVL(SUM(CASE WHEN PRO.MARCA = 'IPIRANGA' THEN ((IPI.QTDNEG * PRO.AD_LITROS) * TOP.GOLDEV) END),0) AS LITROS_IPIRANGA
   ,NVL(SUM(CASE WHEN PRO.MARCA = 'TEXACO' THEN ((IPI.QTDNEG * PRO.AD_LITROS) * TOP.GOLDEV) END),0) AS LITROS_TEXACO
   ,NVL(SUM(CASE WHEN PRO.MARCA = 'TECFIL' THEN ((IPI.QTDNEG * PRO.AD_LITROS) * TOP.GOLDEV) END),0) AS TECFIL
   ,NVL(SUM((IPI.QTDNEG * PRO.AD_LITROS) * TOP.GOLDEV),0)  AS LITROS_TOTAL
 
FROM
	AD_TGFITEPOSTOIPI IPI
INNER JOIN 
		TGFPAR PAR ON IPI.CODPARC = PAR.CODPARC
INNER JOIN 
		TSICID CID ON PAR.CODCID = CID.CODCID
INNER JOIN 
		TGFVEN VEN ON IPI.CODVEND = VEN.CODVEND
INNER JOIN	
		TGFPRO PRO ON IPI.CODPROD = PRO.CODPROD
INNER JOIN 
		TGFTOP TOP ON IPI.CODTIPOPER = TOP.CODTIPOPER AND IPI.DHTIPOPER = TOP.DHALTER
	
   WHERE
   IPI.CODEMP IN (1,2,4,7,8,16,20)
GROUP BY IPI.CODEMP
 	  ,IPI.CODVEND
   ,VEN.APELIDO
   
    '''

    df = pd.read_sql(query, conn)
    print(df)
    conn.close()

    return df