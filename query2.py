import cx_Oracle
import pandas as pd

def get_data():
    dsn = cx_Oracle.makedsn("10.15.7.2", 1521, service_name="sankhya.privatesubnet.natvcn.oraclevcn.com")
    user = "SANKHYA"
    senha = "nNO9S5#eHMN93hprod"

    conn = cx_Oracle.connect(user=user, password=senha, dsn=dsn)

    query = '''
    SELECT
    CASE WHEN PRO.MARCA = 'TECFIL' THEN ((ITE.QTDNEG * PRO.AD_LITROS)) END AS FILTROS,
    CASE WHEN PRO.MARCA = 'IPIRANGA' THEN ((ITE.QTDNEG * PRO.AD_LITROS)) END AS IPIRANGA,
    CASE WHEN PRO.MARCA = 'TEXACO' THEN ((ITE.QTDNEG * PRO.AD_LITROS)) END AS TEXACO
FROM
    TGFCAB CAB
INNER JOIN TGFITE ITE ON CAB.NUNOTA = ITE.NUNOTA
INNER JOIN TGFPRO PRO ON ITE.CODPROD = PRO.CODPROD
INNER JOIN TGFTOP TOP ON CAB.CODTIPOPER = TOP.CODTIPOPER AND CAB.DHTIPOPER = TOP.DHALTER
WHERE
    CAB.CODEMP = 2
AND CAB.DTMOV BETWEEN TO_DATE('01/01/2025', 'DD/MM/YYYY') AND TO_DATE('31/01/2025', 'DD/MM/YYYY')
AND GOLSINAL = -1
AND CAB.STATUSNOTA = 'L'

   
    '''

    df = pd.read_sql(query, conn)
    print(df)
    conn.close()

    return df