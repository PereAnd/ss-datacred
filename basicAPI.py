from flask import Flask, request, jsonify
from faker import Faker
import random, hashlib, datetime, random


app = Flask(__name__)
faker = Faker()
TASA_REPORT_DATACRED = 0
TASA_REPORT_CLINTON = 0
API_KEY = 'ESTAESMIAPIKEY'

@app.route('/api/ping', methods=['GET'])
def health():
    response = {"mssg": "pong"}
    return response, 200

@app.route('/api/datacredito', methods=['POST'])
def getDatacredRequestID():
    #if not Authorization(request.headers, 'datacred'): return {"mssg": "No autorizado"}, 403
    if ('last_name' not in request.json or 'document_type' not in request.json or 'document_number' not in request.json):
        return {"mssg": "Los datos de entrada no están completos"}, 400
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    hash = hashlib.sha256(date.encode()).hexdigest()[:20]
    response = {
        "message": "Request processed successfully",
        "url": f"/api/datacredito/{hash}/",
        "request_id": hash
    }
    return response, 200

@app.route('/api/datacredito/<request_id>', methods=['GET'])
def responseDatacred(request_id):
    #if not Authorization(request.headers, 'datacred'): return {"mssg": "No autorizado"}, 403
    if not Reportado(TASA_REPORT_DATACRED): return {"mssg": "Cliente no encontrado"}, 404
    
    response = {
        "result": {
            "data": {
                "warning": "",
                "informes": {
                    "informe": {
                    "score": {
                        "tipo": "67",
                        "fecha": "2020-05-26",
                        "razon": [
                            {
                                "codigo": "00099"
                            },
                            {
                                "codigo": "00000"
                            }
                        ],
                        "puntaje": "815.0",
                        "poblacion": "95"
                    },
                    "alerta": [
                        {
                            "llave": "100888888885990003001",
                            "texto": "MAS DE 3 CONSULTAS DE DIFERENTES ENTIDADES EN LOS ULTIMOS 60 DIAS",
                            "codigo": "012",
                            "fuente": {
                                "codigo": "990001",
                                "nombre": "B.D DATACREDIT"
                            },
                            "colocacion": "2020-05-26",
                            "vencimiento": "2020-05-26",
                            "modificacion": "2020-05-26"
                        },
                        {
                            "llave": "100888888885990003001",
                            "texto": "NO SE ENCUENTRA COINCIDENCIA CON LISTAS RESTRICTIVAS DE ID CONSULTADO AL 20200526",
                            "codigo": "304",
                            "fuente": {
                                "codigo": "000003",
                                "nombre": "LISTAS RESTRICTIVAS"
                            },
                            "cod_lista": "00",
                            "colocacion": "2020-05-26",
                            "vencimiento": "2020-05-26",
                            "modificacion": "2020-05-26"
                        }
                    ],
                    "reclamo": [
                        {
                            "tipo": "02",
                            "fecha": "2020-03-13",
                            "texto": "TERRE",
                            "estado": "1",
                            "numero": "2692382",
                            "entidad": "MOVISTAR",
                            "subtipo": {
                                "codigo": "01",
                                "nombre": "NO ACTUALIZACION DE LA INFORMACION"
                            },
                            "ratificado": "TRUE",
                            "tipo_leyenda": "1",
                            "numero_cuenta": "000000000032788629"
                        },
                        {
                            "tipo": "02",
                            "fecha": "2020-03-13",
                            "texto": "TEST",
                            "estado": "1",
                            "numero": "2692376",
                            "entidad": "MOVISTAR",
                            "subtipo": {
                                "codigo": "01",
                                "nombre": "NO ACTUALIZACION DE LA INFORMACION"
                            },
                            "ratificado": "TRUE",
                            "tipo_leyenda": "1",
                            "numero_cuenta": "000000000032788562"
                        },
                        {
                            "tipo": "02",
                            "fecha": "2020-03-13",
                            "texto": "567567",
                            "estado": "1",
                            "numero": "2692374",
                            "entidad": "MOVISTAR",
                            "subtipo": {
                                "codigo": "02",
                                "nombre": "NO REPORTE INFORMACION OPORTUNO"
                            },
                            "ratificado": "TRUE",
                            "tipo_leyenda": "1",
                            "numero_cuenta": "000000000031827442"
                        },
                        {
                            "tipo": "02",
                            "fecha": "2020-03-13",
                            "texto": "TEST",
                            "estado": "1",
                            "numero": "2692373",
                            "entidad": "MOVISTAR",
                            "subtipo": {
                                "codigo": "02",
                                "nombre": "NO REPORTE INFORMACION OPORTUNO"
                            },
                            "ratificado": "TRUE",
                            "tipo_leyenda": "1",
                            "numero_cuenta": "000000000031579364"
                        },
                        {
                            "tipo": "02",
                            "fecha": "2020-03-13",
                            "texto": "P. FRANDO",
                            "estado": "1",
                            "numero": "2692372",
                            "entidad": "MOVISTAR",
                            "subtipo": {
                                "codigo": "01",
                                "nombre": "NO ACTUALIZACION DE LA INFORMACION"
                            },
                            "ratificado": "FALSE",
                            "tipo_leyenda": "5",
                            "numero_cuenta": "000000000031394664"
                        },
                        {
                            "tipo": "02",
                            "fecha": "2020-03-12",
                            "texto": "PRUEBA",
                            "estado": "1",
                            "numero": "2692370",
                            "entidad": "MOVISTAR",
                            "subtipo": {
                                "codigo": "02",
                                "nombre": "NO REPORTE INFORMACION OPORTUNO"
                            },
                            "ratificado": "TRUE",
                            "tipo_leyenda": "1",
                            "numero_cuenta": "000000000032067200"
                        },
                        {
                            "tipo": "02",
                            "fecha": "2020-03-12",
                            "texto": "PRUEBAS MARZO 12 DE 2020",
                            "estado": "1",
                            "numero": "2692369",
                            "entidad": "MOVISTAR",
                            "subtipo": {
                                "codigo": "01",
                                "nombre": "NO ACTUALIZACION DE LA INFORMACION"
                            },
                            "ratificado": "TRUE",
                            "tipo_leyenda": "1",
                            "numero_cuenta": "00034455954-603806"
                        },
                        {
                            "tipo": "02",
                            "fecha": "2020-03-12",
                            "texto": "PRUEBA MARZO 12 DE 2020",
                            "estado": "1",
                            "numero": "2692368",
                            "entidad": "MOVISTAR",
                            "subtipo": {
                                "codigo": "01",
                                "nombre": "NO ACTUALIZACION DE LA INFORMACION"
                            },
                            "ratificado": "TRUE",
                            "tipo_leyenda": "1",
                            "numero_cuenta": "000000000030158493"
                        }
                    ],
                    "consulta": [
                        {
                            "fecha": "2020-05-26",
                            "llave": "10088888888145",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "APITUDE SAS",
                            "oficina": "------------------",
                            "cantidad": "02",
                            "tipo_cuenta": "COC",
                            "nit_suscriptor": "00901353791"
                        },
                        {
                            "fecha": "2020-05-26",
                            "llave": "10088888888150",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "SUPERAVAL SAS",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "TRT",
                            "nit_suscriptor": "00901369750"
                        },
                        {
                            "fecha": "2020-05-22",
                            "llave": "10088888888146",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "2 TRANSFAIR",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "COM",
                            "nit_suscriptor": "00900926817"
                        },
                        {
                            "fecha": "2020-05-12",
                            "llave": "10088888888149",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "DATACREDITO",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "TDC",
                            "nit_suscriptor": "00900422614"
                        },
                        {
                            "fecha": "2020-05-12",
                            "llave": "10088888888144",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "FIE SAS",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "CCL",
                            "nit_suscriptor": "00901273824"
                        },
                        {
                            "fecha": "2020-05-06",
                            "llave": "10088888888148",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "ACR PLUS SAS",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "COC",
                            "nit_suscriptor": "00901184516"
                        },
                        {
                            "fecha": "2020-05-06",
                            "llave": "10088888888147",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "UNIPILOTO",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "EDU",
                            "nit_suscriptor": "00860022382"
                        },
                        {
                            "fecha": "2020-04-29",
                            "llave": "10088888888142",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "2 TRANSFAIR",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "COM",
                            "nit_suscriptor": "00900926817"
                        },
                        {
                            "fecha": "2020-04-27",
                            "llave": "10088888888140",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "PROMOSUMMA SAS",
                            "oficina": "------------------",
                            "cantidad": "02",
                            "tipo_cuenta": "COC",
                            "nit_suscriptor": "00900475865"
                        },
                        {
                            "fecha": "2020-04-23",
                            "llave": "10088888888139",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "DATACREDITO",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "TDC",
                            "nit_suscriptor": "00900422614"
                        },
                        {
                            "fecha": "2020-04-18",
                            "llave": "10088888888133",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "APITUDE SAS",
                            "oficina": "------------------",
                            "cantidad": "02",
                            "tipo_cuenta": "COC",
                            "nit_suscriptor": "00901353791"
                        },
                        {
                            "fecha": "2020-04-17",
                            "llave": "10088888888137",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "ACR PLUS SAS",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "COC",
                            "nit_suscriptor": "00901184516"
                        },
                        {
                            "fecha": "2020-04-08",
                            "llave": "10088888888136",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "C3 BROKER",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "CCS",
                            "nit_suscriptor": "00900871733"
                        },
                        {
                            "fecha": "2020-04-08",
                            "llave": "10088888888135",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "CHIPER SAS",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "COC",
                            "nit_suscriptor": "00901145411"
                        },
                        {
                            "fecha": "2020-04-07",
                            "llave": "10088888888134",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "IMPORTADORA  CELESTE",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "CAU",
                            "nit_suscriptor": "00800004800"
                        },
                        {
                            "fecha": "2020-04-03",
                            "llave": "10088888888132",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "ASDEM",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "COC",
                            "nit_suscriptor": "00901276338"
                        },
                        {
                            "fecha": "2020-04-02",
                            "llave": "10088888888131",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "DENARIO    CAPITAL SAS",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "COM",
                            "nit_suscriptor": "00901317239"
                        },
                        {
                            "fecha": "2020-03-30",
                            "llave": "10088888888125",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "APITUDE SAS",
                            "oficina": "------------------",
                            "cantidad": "06",
                            "tipo_cuenta": "COC",
                            "nit_suscriptor": "00901353791"
                        },
                        {
                            "fecha": "2020-03-27",
                            "llave": "10088888888124",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "CHIPER SAS",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "COC",
                            "nit_suscriptor": "00901145411"
                        },
                        {
                            "fecha": "2020-03-27",
                            "llave": "10088888888123",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "MULTIRED    GLOBAL",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "COM",
                            "nit_suscriptor": "00901287335"
                        },
                        {
                            "fecha": "2020-03-25",
                            "llave": "10088888888117",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "GRUMA HERPO",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "CVE",
                            "nit_suscriptor": "00900091175"
                        },
                        {
                            "fecha": "2020-03-05",
                            "llave": "10088888888120",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "AGRICAPITAL  SAS",
                            "oficina": "------------------",
                            "cantidad": "02",
                            "tipo_cuenta": "CMZ",
                            "nit_suscriptor": "00900962538"
                        },
                        {
                            "fecha": "2020-03-04",
                            "llave": "10088888888119",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "COSVICENTE",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "CFE",
                            "nit_suscriptor": "00890981497"
                        },
                        {
                            "fecha": "2020-03-04",
                            "llave": "10088888888118",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "UNIPILOTO",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "EDU",
                            "nit_suscriptor": "00860022382"
                        },
                        {
                            "fecha": "2020-03-04",
                            "llave": "10088888888116",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "VERFOND",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "COC",
                            "nit_suscriptor": "00901292638"
                        },
                        {
                            "fecha": "2020-02-28",
                            "llave": "10088888888115",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "ASDEM",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "COC",
                            "nit_suscriptor": "00901276338"
                        },
                        {
                            "fecha": "2020-02-28",
                            "llave": "10088888888114",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "1",
                            "entidad": "BBVA      COLOMBIA",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "TDC",
                            "nit_suscriptor": "00860003020"
                        },
                        {
                            "fecha": "2020-02-28",
                            "llave": "10088888888113",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "VERFOND",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "COC",
                            "nit_suscriptor": "00901292638"
                        },
                        {
                            "fecha": "2020-02-21",
                            "llave": "10088888888111",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "CHIPER SAS",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "COC",
                            "nit_suscriptor": "00901145411"
                        },
                        {
                            "fecha": "2020-02-20",
                            "llave": "10088888888112",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "C3 BROKER",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "CCS",
                            "nit_suscriptor": "00900871733"
                        },
                        {
                            "fecha": "2020-02-19",
                            "llave": "10088888888110",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "2 TRANSFAIR",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "COM",
                            "nit_suscriptor": "00900926817"
                        },
                        {
                            "fecha": "2020-02-19",
                            "llave": "10088888888109",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "ACR PLUS SAS",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "COC",
                            "nit_suscriptor": "00901184516"
                        },
                        {
                            "fecha": "2020-02-03",
                            "llave": "10088888888108",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "CUEROS VELEZ  S.A.S.",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "CMZ",
                            "nit_suscriptor": "00800191700"
                        },
                        {
                            "fecha": "2019-10-30",
                            "llave": "10088888888107",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "1",
                            "entidad": "BBVA COLOMBIA",
                            "oficina": "------------------",
                            "cantidad": "02",
                            "tipo_cuenta": "CCB",
                            "nit_suscriptor": "00860003020"
                        },
                        {
                            "fecha": "2019-10-29",
                            "llave": "10088888888105",
                            "razon": "01",
                            "ciudad": "------------",
                            "sector": "3",
                            "entidad": "DATACREDITO",
                            "oficina": "------------------",
                            "cantidad": "02",
                            "tipo_cuenta": "TDC",
                            "nit_suscriptor": "00900422614"
                        },
                        {
                            "fecha": "2019-02-05",
                            "llave": "10088888888103",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "1",
                            "entidad": "BC CAJA SOCIAL BCSC DEMO",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "CAB",
                            "nit_suscriptor": "00860007335"
                        },
                        {
                            "fecha": "2018-12-21",
                            "llave": "10088888888102",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "1",
                            "entidad": "SERFINANSA S.A",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "CCL",
                            "nit_suscriptor": "00860043186"
                        },
                        {
                            "fecha": "2018-11-30",
                            "llave": "10088888888101",
                            "razon": "00",
                            "ciudad": "------------",
                            "sector": "1",
                            "entidad": "BC CAJA SOCIAL BCSC DEMO",
                            "oficina": "------------------",
                            "cantidad": "01",
                            "tipo_cuenta": "CAB",
                            "nit_suscriptor": "00860007335"
                        }
                    ],
                    "respuesta": "13",
                    "cod_seguridad": "4AG774C",
                    "info_agregada": {
                        "cheques": None,
                        "resumen": {
                            "saldos": {
                                "mes": [
                                {
                                    "fecha": "2019-02-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2019-01-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2018-12-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2018-11-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2018-10-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2018-09-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2018-08-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2018-07-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2018-06-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2018-05-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2018-04-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2018-03-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2018-02-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2018-01-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2017-12-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2017-11-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2017-10-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2017-09-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2017-08-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2017-07-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2017-06-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2017-05-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2017-04-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                },
                                {
                                    "fecha": "2017-03-28",
                                    "saldo_total": "0",
                                    "saldo_total_mora": "0"
                                }
                                ],
                                "sector": [
                                {
                                    "saldo": "0.0",
                                    "sector": "1",
                                    "participacion": "0.0"
                                },
                                {
                                    "saldo": "0.0",
                                    "sector": "2",
                                    "participacion": "0.0"
                                },
                                {
                                    "saldo": "0.0",
                                    "sector": "3",
                                    "participacion": "0.0"
                                },
                                {
                                    "saldo": "0.0",
                                    "sector": "4",
                                    "participacion": "0.0"
                                }
                                ],
                                "saldom30": "0.0",
                                "saldom60": "0.0",
                                "saldom90": "0.0",
                                "saldo_total": "0.0",
                                "cuota_mensual": "81.0",
                                "saldo_total_en_mora": "0.0",
                                "saldo_credito_mas_alto": "0.0"
                            },
                            "principales": {
                                "antiguedad_desde": "2006-08-01",
                                "credito_vigentes": "3",
                                "creditos_cerrados": "34",
                                "reclamos_vigentes": "8",
                                "hist_neg_ult12_meses": "0",
                                "consultadas_ult6meses": "42",
                                "desacuerdos_a_la_fecha": "8",
                                "cuentas_abiertas_ahoccb": "0",
                                "cuentas_cerradas_ahoccb": "0",
                                "creditos_actuales_negativos": "0"
                            },
                            "comportamiento": {
                                "mes": [
                                {
                                    "fecha": "2019-02-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2019-01-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2018-12-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2018-11-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2018-10-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2018-09-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2018-08-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2018-07-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2018-06-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2018-05-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2018-04-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2018-03-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2018-02-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2018-01-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2017-12-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2017-11-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2017-10-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2017-09-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2017-08-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2017-07-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2017-06-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2017-05-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2017-04-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                },
                                {
                                    "fecha": "2017-03-28",
                                    "cantidad": "0",
                                    "comportamiento": "N"
                                }
                                ]
                            }
                        },
                        "totales": {
                            "total": [
                                {
                                "cupo": "0.0",
                                "cuota": "81.0",
                                "saldo": "0.0",
                                "saldo_mora": "0.0",
                                "participacion": "0.0",
                                "calidad_deudor": "PRINCIPAL"
                                },
                                {
                                "cupo": "0.0",
                                "cuota": "0.0",
                                "saldo": "0.0",
                                "saldo_mora": "0.0",
                                "participacion": "0.0",
                                "calidad_deudor": "CODEUDOR"
                                }
                            ],
                            "tipo_cuenta": [
                                {
                                "cupo": "0.0",
                                "tipo": "CARTERA TELEFONIA CELULAR",
                                "cuota": "81.0",
                                "saldo": "0.0",
                                "saldo_mora": "0.0",
                                "codigo_tipo": "CTC",
                                "calidad_deudor": "PRINCIPAL"
                                },
                                {
                                "cupo": "0.0",
                                "tipo": "CARTERA COMPUTADORES",
                                "cuota": "0.0",
                                "saldo": "0.0",
                                "saldo_mora": "0.0",
                                "codigo_tipo": "COM",
                                "calidad_deudor": "PRINCIPAL"
                                }
                            ]
                        },
                        "evolucion_deuda": {
                            "trimestre": [
                                {
                                "cuota": "81000",
                                "fecha": "2018-12-01",
                                "saldo": "0",
                                "score": "0.0",
                                "cupo_total": "0",
                                "mora_maxima": "M 0",
                                "calificacion": "D",
                                "cierre_cuentas": "0",
                                "porcentaje_uso": "0.0",
                                "total_abiertas": "3",
                                "total_cerradas": "34",
                                "apertura_cuentas": "0",
                                "meses_mora_maxima": "0"
                                },
                                {
                                "cuota": "81000",
                                "fecha": "2018-09-01",
                                "saldo": "0",
                                "score": "0.0",
                                "cupo_total": "0",
                                "mora_maxima": "M 0",
                                "calificacion": "D",
                                "cierre_cuentas": "0",
                                "porcentaje_uso": "0.0",
                                "total_abiertas": "3",
                                "total_cerradas": "34",
                                "apertura_cuentas": "0",
                                "meses_mora_maxima": "0"
                                },
                                {
                                "cuota": "84000",
                                "fecha": "2018-06-01",
                                "saldo": "0",
                                "score": "0.0",
                                "cupo_total": "0",
                                "mora_maxima": "M 0",
                                "calificacion": "D",
                                "cierre_cuentas": "0",
                                "porcentaje_uso": "0.0",
                                "total_abiertas": "3",
                                "total_cerradas": "34",
                                "apertura_cuentas": "0",
                                "meses_mora_maxima": "0"
                                }
                            ],
                            "analisis_promedio": {
                                "cuota": "-3.6",
                                "saldo": "0.0",
                                "score": "0.0",
                                "cupo_total": "0.0",
                                "mora_maxima": "0",
                                "calificacion": "0",
                                "cierre_cuentas": "0.0",
                                "porcentaje_uso": "0.0",
                                "total_abiertas": "0.0",
                                "total_cerradas": "0.0",
                                "apertura_cuentas": "0.0"
                            }
                        },
                        "historico_saldos": {
                            "totales": [
                                {
                                "fecha": "2018-12-01",
                                "saldo": "0.0",
                                "total_cuentas": "3",
                                "cuentas_consideradas": "0"
                                },
                                {
                                "fecha": "2018-09-01",
                                "saldo": "0.0",
                                "total_cuentas": "3",
                                "cuentas_consideradas": "0"
                                },
                                {
                                "fecha": "2018-06-01",
                                "saldo": "0.0",
                                "total_cuentas": "4",
                                "cuentas_consideradas": "0"
                                },
                                {
                                "fecha": "2018-03-01",
                                "saldo": "0.0",
                                "total_cuentas": "6",
                                "cuentas_consideradas": "0"
                                },
                                {
                                "fecha": "2017-12-01",
                                "saldo": "0.0",
                                "total_cuentas": "5",
                                "cuentas_consideradas": "0"
                                },
                                {
                                "fecha": "2017-09-01",
                                "saldo": "0.0",
                                "total_cuentas": "8",
                                "cuentas_consideradas": "0"
                                },
                                {
                                "fecha": "2017-06-01",
                                "saldo": "0.0",
                                "total_cuentas": "6",
                                "cuentas_consideradas": "0"
                                },
                                {
                                "fecha": "2017-03-01",
                                "saldo": "0.0",
                                "total_cuentas": "6",
                                "cuentas_consideradas": "0"
                                }
                            ],
                            "tipo_cuenta": [
                                {
                                "tipo": "CAB",
                                "trimestre": [
                                    {
                                        "fecha": "2018-12-01",
                                        "saldo": "0",
                                        "total_cuentas": "0",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2018-09-01",
                                        "saldo": "0",
                                        "total_cuentas": "0",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2018-06-01",
                                        "saldo": "0",
                                        "total_cuentas": "0",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2018-03-01",
                                        "saldo": "0",
                                        "total_cuentas": "0",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2017-12-01",
                                        "saldo": "0",
                                        "total_cuentas": "0",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2017-09-01",
                                        "saldo": "0",
                                        "total_cuentas": "0",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2017-06-01",
                                        "saldo": "0",
                                        "total_cuentas": "0",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2017-03-01",
                                        "saldo": "0",
                                        "total_cuentas": "0",
                                        "cuentas_consideradas": "0"
                                    }
                                ]
                                },
                                {
                                "tipo": "CCF",
                                "trimestre": [
                                    {
                                        "fecha": "2018-12-01",
                                        "saldo": "0",
                                        "total_cuentas": "0",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2018-09-01",
                                        "saldo": "0",
                                        "total_cuentas": "0",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2018-06-01",
                                        "saldo": "0",
                                        "total_cuentas": "0",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2018-03-01",
                                        "saldo": "0",
                                        "total_cuentas": "0",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2017-12-01",
                                        "saldo": "0",
                                        "total_cuentas": "0",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2017-09-01",
                                        "saldo": "0",
                                        "total_cuentas": "0",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2017-06-01",
                                        "saldo": "0",
                                        "total_cuentas": "0",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2017-03-01",
                                        "saldo": "0",
                                        "total_cuentas": "0",
                                        "cuentas_consideradas": "0"
                                    }
                                ]
                                },
                                {
                                "tipo": "COM",
                                "trimestre": [
                                    {
                                        "fecha": "2018-12-01",
                                        "saldo": "0",
                                        "total_cuentas": "1",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2018-09-01",
                                        "saldo": "0",
                                        "total_cuentas": "1",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2018-06-01",
                                        "saldo": "0",
                                        "total_cuentas": "1",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2018-03-01",
                                        "saldo": "0",
                                        "total_cuentas": "1",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2017-12-01",
                                        "saldo": "0",
                                        "total_cuentas": "1",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2017-09-01",
                                        "saldo": "0",
                                        "total_cuentas": "1",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2017-06-01",
                                        "saldo": "0",
                                        "total_cuentas": "1",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2017-03-01",
                                        "saldo": "0",
                                        "total_cuentas": "1",
                                        "cuentas_consideradas": "0"
                                    }
                                ]
                                },
                                {
                                "tipo": "CTC",
                                "trimestre": [
                                    {
                                        "fecha": "2018-12-01",
                                        "saldo": "0",
                                        "total_cuentas": "2",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2018-09-01",
                                        "saldo": "0",
                                        "total_cuentas": "2",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2018-06-01",
                                        "saldo": "0",
                                        "total_cuentas": "3",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2018-03-01",
                                        "saldo": "0",
                                        "total_cuentas": "5",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2017-12-01",
                                        "saldo": "0",
                                        "total_cuentas": "4",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2017-09-01",
                                        "saldo": "0",
                                        "total_cuentas": "7",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2017-06-01",
                                        "saldo": "0",
                                        "total_cuentas": "5",
                                        "cuentas_consideradas": "0"
                                    },
                                    {
                                        "fecha": "2017-03-01",
                                        "saldo": "0",
                                        "total_cuentas": "5",
                                        "cuentas_consideradas": "0"
                                    }
                                ]
                                }
                            ]
                        },
                        "resumen_endeudamiento": None,
                        "composicion_portafolio": {
                            "tipo_cuenta": [
                                {
                                "tipo": "COM",
                                "estado": {
                                    "codigo": "EN RECLAMACION",
                                    "cantidad": "1"
                                },
                                "cantidad": "1",
                                "porcentaje": "1.0",
                                "calidad_deudor": "PRINCIPAL"
                                },
                                {
                                "tipo": "CTC",
                                "estado": {
                                    "codigo": "AL DIA",
                                    "cantidad": "2"
                                },
                                "cantidad": "2",
                                "porcentaje": "1.0",
                                "calidad_deudor": "PRINCIPAL"
                                }
                            ]
                        }
                    },
                    "cuenta_cartera": [
                        {
                            "llave": "10088888888105009805001234567000000000",
                            "ciudad": "",
                            "numero": "001234567",
                            "sector": "REAL",
                            "entidad": "EXPERIAN    COLOMBIA SA",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2012-09-11",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2012-09-11",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2006-08-01",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "NO INFORMO",
                            "valores": None,
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "cod_suscriptor": "050098",
                            "comportamiento": "NNN-------------------N------N-----------------",
                            "fecha_apertura": "2006-08-01",
                            "identificacion": "00900422614",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA BANCARIA",
                                "tipo_contrato": "0",
                                "calidad_deudor": "05",
                                "tipo_obligacion": "COMERCIALES",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "1"
                            },
                            "fecha_vencimiento": "2012-08-01",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888118001718000CLJ524000000000",
                            "ciudad": "",
                            "numero": "000CLJ524",
                            "sector": "REAL",
                            "entidad": "EXPERIAN    COLOMBIA SA",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2012-09-12",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2012-09-12",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2012-01-31",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "NO INFORMO",
                            "valores": None,
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "cod_suscriptor": "180017",
                            "comportamiento": "NNNNN----NNNNNNNNNNNNNN------------------------",
                            "fecha_apertura": "2010-06-12",
                            "identificacion": "00900422614",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA COMPA\u00d1IAS DE FINANCIAMIENTO COMERCIAL",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "CONSUMO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "2"
                            },
                            "fecha_vencimiento": "2014-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123031297116000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "031297116",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2019-02-28",
                                "meses": "48",
                                "codigo": "AL DIA"
                                },
                                "estado_cuenta": {
                                "fecha": "2019-02-28",
                                "codigo": "AL DIA"
                                },
                                "estado_origen": {
                                "fecha": "2015-07-05",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA BOGOTA       00",
                            "valores": {
                                "valor": {
                                "cuota": "51000.0",
                                "fecha": "2019-02-28",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2016-02-16",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "0",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN-NN--------",
                            "fecha_apertura": "2015-07-05",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123031931295000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "031931295",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2019-02-28",
                                "meses": "48",
                                "codigo": "AL DIA"
                                },
                                "estado_cuenta": {
                                "fecha": "2019-02-28",
                                "codigo": "AL DIA"
                                },
                                "estado_origen": {
                                "fecha": "2015-09-02",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA BOGOTA       00",
                            "valores": {
                                "valor": {
                                "cuota": "30000.0",
                                "fecha": "2019-02-28",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2016-02-26",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "0",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN--------",
                            "fecha_apertura": "2015-09-02",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123030692467000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "030692467",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2015-10-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2015-10-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2015-05-06",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA BOGOTA       00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2015-10-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2015-09-02",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "N----------------------------------------------",
                            "fecha_apertura": "2015-05-06",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123030697456000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "030697456",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2015-10-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2015-10-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2015-05-06",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA BOGOTA       00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2015-10-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2015-05-14",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "N----------------------------------------------",
                            "fecha_apertura": "2015-05-06",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123031394664000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "031394664",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2015-10-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2015-10-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2015-07-14",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA BOGOTA       00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2015-10-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2015-07-27",
                                "cuotas_canceladas": "-1",
                                "fecha_limite_pago": "2015-08-11"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "N----------------------------------------------",
                            "fecha_apertura": "2015-07-14",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123031551192000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "031551192",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2015-10-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2015-10-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2015-07-29",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA BOGOTA       00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2015-10-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2015-08-04",
                                "cuotas_canceladas": "-1",
                                "fecha_limite_pago": "2015-08-19"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "N----------------------------------------------",
                            "fecha_apertura": "2015-07-29",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123031685596000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "031685596",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2015-10-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2015-10-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2015-08-11",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA BOGOTA       00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2015-10-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2015-08-31",
                                "cuotas_canceladas": "-1",
                                "fecha_limite_pago": "2015-09-09"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "N----------------------------------------------",
                            "fecha_apertura": "2015-08-11",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123032071475000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "032071475",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2015-10-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2015-10-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2015-09-15",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA AGUA DE DIOS    00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2015-10-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2015-09-24",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "N----------------------------------------------",
                            "fecha_apertura": "2015-09-15",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123032788610000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "032788610",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2015-12-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2015-12-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2015-11-20",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA AGUA DE DIOS    00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2015-12-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2015-12-23",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "N----------------------------------------------",
                            "fecha_apertura": "2015-11-20",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123032792985000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "032792985",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2016-01-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2016-01-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2015-11-20",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA AGUA DE DIOS    00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2016-01-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2016-01-27",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "NN---------------------------------------------",
                            "fecha_apertura": "2015-11-20",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123033472679000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "033472679",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2016-01-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2016-01-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2016-01-22",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA AGUA DE DIOS    00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2016-01-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2016-01-27",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "-----------------------------------------------",
                            "fecha_apertura": "2016-01-22",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123033472876000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "033472876",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2016-01-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2016-01-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2016-01-22",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA AGUA DE DIOS    00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2016-01-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2016-01-27",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "-----------------------------------------------",
                            "fecha_apertura": "2016-01-22",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123034777732000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "034777732",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2016-08-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2016-08-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2016-05-22",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA BOGOTA       00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2016-08-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2016-08-04",
                                "cuotas_canceladas": "-1",
                                "fecha_limite_pago": "2016-06-07"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "NNN--------------------------------------------",
                            "fecha_apertura": "2016-05-22",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123035350722000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "035350722",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2016-07-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2016-07-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2016-07-17",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA BOGOTA       00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2016-07-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2016-07-28",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "-----------------------------------------------",
                            "fecha_apertura": "2016-07-17",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123036504378000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "036504378",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2016-11-30",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2016-11-30",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2016-10-26",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA BOGOTA       00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2016-11-30",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2016-11-02",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "N----------------------------------------------",
                            "fecha_apertura": "2016-10-26",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123036675948000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "036675948",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2016-11-30",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2016-11-30",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2016-11-11",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA AGUA DE DIOS    00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2016-11-30",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2016-11-21",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "-----------------------------------------------",
                            "fecha_apertura": "2016-11-11",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123036675949000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "036675949",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2016-12-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2016-12-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2016-11-11",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA AGUA DE DIOS    00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2016-12-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2016-11-21",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "N----------------------------------------------",
                            "fecha_apertura": "2016-11-11",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123036675954000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "036675954",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2016-12-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2016-12-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2016-11-11",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA AGUA DE DIOS    00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2016-12-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2016-11-21",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "N----------------------------------------------",
                            "fecha_apertura": "2016-11-11",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123036675959000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "036675959",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2016-12-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2016-12-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2016-11-11",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA AGUA DE DIOS    00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2016-12-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2016-11-21",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "N----------------------------------------------",
                            "fecha_apertura": "2016-11-11",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123036675988000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "036675988",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2016-11-30",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2016-11-30",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2016-11-11",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA AGUA DE DIOS    00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2016-11-30",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2016-11-21",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "-----------------------------------------------",
                            "fecha_apertura": "2016-11-11",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123036676194000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "036676194",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2016-12-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2016-12-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2016-11-11",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA AGUA DE DIOS    00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2016-12-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2016-11-21",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "N----------------------------------------------",
                            "fecha_apertura": "2016-11-11",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123036975591000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "036975591",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2016-12-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2016-12-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2016-12-04",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA BOGOTA       00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2016-12-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2016-12-16",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "-----------------------------------------------",
                            "fecha_apertura": "2016-12-04",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123037558978000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "037558978",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2017-07-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2017-07-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2017-01-19",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA AGUA DE DIOS    00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2017-07-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2017-05-25",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "NNNNNN-----------------------------------------",
                            "fecha_apertura": "2017-01-19",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123037740598000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "037740598",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2017-07-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2017-07-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2017-02-01",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA BOGOTA       00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2017-07-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2017-05-25",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "NNNNN------------------------------------------",
                            "fecha_apertura": "2017-02-01",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123037740614000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "037740614",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2017-07-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2017-07-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2017-02-01",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA BOGOTA       00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2017-07-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2017-04-22",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "NNNNN------------------------------------------",
                            "fecha_apertura": "2017-02-01",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123040456047000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "040456047",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2018-01-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2018-01-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2017-08-07",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA BOGOTA       00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2018-01-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2017-11-24",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "NNNN-------------------------------------------",
                            "fecha_apertura": "2017-08-07",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123040535347000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "040535347",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2018-01-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2018-01-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2017-08-12",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA BOGOTA       00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2018-01-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2017-11-24",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "NNNN-------------------------------------------",
                            "fecha_apertura": "2017-08-12",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        },
                        {
                            "llave": "10088888888123000123042004372000000000",
                            "ciudad": "000000BOGOTA",
                            "numero": "042004372",
                            "sector": "TELECOMUNICACIONES",
                            "entidad": "MOVISTAR",
                            "estados": {
                                "estado_pago": {
                                "fecha": "2018-05-31",
                                "meses": "48",
                                "codigo": "PAGO VOLUNTARIO"
                                },
                                "estado_cuenta": {
                                "fecha": "2018-05-31",
                                "codigo": "PAGO TOTAL"
                                },
                                "estado_origen": {
                                "fecha": "2018-02-15",
                                "codigo": "NORMAL. CREACION POR APERTURA"
                                }
                            },
                            "oficina": "BOGOTA BOGOTA       00",
                            "valores": {
                                "valor": {
                                "cuota": "0.0",
                                "fecha": "2018-05-31",
                                "moneda": "MONEDA LEGAL",
                                "dias_mora": "0",
                                "disponible": "0.0",
                                "saldo_mora": "0.0",
                                "cuotas_mora": "0",
                                "calificacion": "1",
                                "periodicidad": "1",
                                "saldo_actual": "0.0",
                                "total_cuotas": "-1",
                                "valor_inicial": "-1",
                                "fecha_pago_cuota": "2018-02-28",
                                "cuotas_canceladas": "-1"
                                }
                            },
                            "bloqueada": "FALSE",
                            "forma_pago": "1",
                            "calificacion": "1",
                            "cod_suscriptor": "230001",
                            "comportamiento": "NN---------------------------------------------",
                            "fecha_apertura": "2018-02-15",
                            "identificacion": "00830037330",
                            "calificacion_hd": "TRUE",
                            "caracteristicas": {
                                "garantia": "2",
                                "tipo_cuenta": "CARTERA DE TELEFONIA CELULAR",
                                "tipo_contrato": "2",
                                "calidad_deudor": "00",
                                "tipo_obligacion": "OTRO",
                                "meses_permanencia": "0",
                                "ejecucion_contrato": "4"
                            },
                            "fecha_vencimiento": "2030-12-31",
                            "situacion_titular": "NORMAL",
                            "codigo_dane_ciudad": "00000000",
                            "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
                            "probabilidad_incumplimiento": "0.0"
                        }
                    ],
                    "fecha_consulta": "2020-05-26T12:59:48",
                    "natural_nacional": {
                        "rut": "FALSE",
                        "edad": {
                            "max": "55",
                            "min": "46"
                        },
                        "genero": "4",
                        "nombres": "JUAN",
                        "validada": "TRUE",
                        "identificacion": {
                            "ciudad": "BOGOTA DC",
                            "estado": "00",
                            "genero": "4",
                            "numero": "00888888881",
                            "departamento": "CUNDINAMAR",
                            "fecha_expedicion": "1988-10-05"
                        },
                        "nombre_completo": "PRUEBAS PEREZ JUAN",
                        "primer_apellido": "PRUEBAS",
                        "info_demografica": None,
                        "segundo_apellido": "PEREZ"
                    },
                    "tipo_id_digitado": "CEDULA DE CIUDADANIA",
                    "apellido_digitado": "PRUEBAS",
                    "productos_valores": {
                        "razon1": "0099",
                        "razon2": "00000",
                        "razon3": "00000",
                        "razon4": "00000",
                        "razon5": "00000",
                        "razon6": "00000",
                        "razon7": "00000",
                        "razon8": "00000",
                        "razon9": "00000",
                        "valor1": "1422",
                        "valor2": "995",
                        "valor3": "1848",
                        "valor4": "0",
                        "valor5": "0",
                        "valor6": "0",
                        "valor7": "0",
                        "valor8": "0",
                        "valor9": "0",
                        "razon10": "00000",
                        "valor10": "0",
                        "producto": "62",
                        "valor1smlv": "1.62",
                        "valor2smlv": "1.134",
                        "valor3smlv": "2.106",
                        "valor4smlv": "0.0",
                        "valor5smlv": "0.0",
                        "valor6smlv": "0.0",
                        "valor7smlv": "0.0",
                        "valor8smlv": "0.0",
                        "valor9smlv": "0.0",
                        "valor10smlv": "0.0"
                    },
                    "identificacion_digitada": "888888881",
                    "info_agregada_microcredito": {
                        "resumen": {
                            "perfil_general": {
                                "desacuerdos": {
                                "sector_real": "0",
                                "sector_telcos": "0",
                                "sector_financiero": "0",
                                "sector_cooperativo": "0",
                                "total_como_principal": "0",
                                "total_como_codeudor_y_otros": "0"
                                },
                                "antiguedad_desde": {
                                "sector_real": "2006-08-01",
                                "sector_telcos": "2015-03-09"
                                },
                                "creditos_cerrados": {
                                "sector_real": "2",
                                "sector_telcos": "32",
                                "sector_financiero": "0",
                                "sector_cooperativo": "0",
                                "total_como_principal": "33",
                                "total_como_codeudor_y_otros": "1"
                                },
                                "creditos_vigentes": {
                                "sector_real": "0",
                                "sector_telcos": "3",
                                "sector_financiero": "0",
                                "sector_cooperativo": "0",
                                "total_como_principal": "3",
                                "total_como_codeudor_y_otros": "0"
                                },
                                "consulta_ult6_meses": {
                                "sector_real": "43",
                                "sector_telcos": "0",
                                "sector_financiero": "6",
                                "sector_cooperativo": "0",
                                "total_como_principal": "0",
                                "total_como_codeudor_y_otros": "0"
                                },
                                "creditos_refinanciados": {
                                "sector_real": "0",
                                "sector_telcos": "0",
                                "sector_financiero": "0",
                                "sector_cooperativo": "0",
                                "total_como_principal": "0",
                                "total_como_codeudor_y_otros": "0"
                                },
                                "creditos_reestructurados": {
                                "sector_real": "0",
                                "sector_telcos": "0",
                                "sector_financiero": "0",
                                "sector_cooperativo": "0",
                                "total_como_principal": "0",
                                "total_como_codeudor_y_otros": "0"
                                }
                            },
                            "endeudamiento_actual": {
                                "sector": {
                                "cod_sector": "4",
                                "tipo_cuenta": [
                                    {
                                        "usuario": {
                                            "cuenta": {
                                            "cuota_mes": "0.0",
                                            "saldo_mora": "0.0",
                                            "calificacion": "D",
                                            "saldo_actual": "0.0",
                                            "estado_actual": "EN RECLAMACION",
                                            "valor_inicial": "0.0",
                                            "total_deuda_carteras": "0.0",
                                            "comportamiento_negativo": "FALSE"
                                            },
                                            "tipo_usuario": "PRINCIPAL"
                                        },
                                        "tipo_cuenta": "COM"
                                    },
                                    {
                                        "usuario": {
                                            "cuenta": [
                                            {
                                                "cuota_mes": "51.0",
                                                "saldo_mora": "0.0",
                                                "calificacion": "A",
                                                "saldo_actual": "0.0",
                                                "estado_actual": "AL DIA",
                                                "valor_inicial": "0.0",
                                                "total_deuda_carteras": "0.0",
                                                "comportamiento_negativo": "FALSE"
                                            },
                                            {
                                                "cuota_mes": "30.0",
                                                "saldo_mora": "0.0",
                                                "calificacion": "A",
                                                "saldo_actual": "0.0",
                                                "estado_actual": "AL DIA",
                                                "valor_inicial": "0.0",
                                                "total_deuda_carteras": "0.0",
                                                "comportamiento_negativo": "FALSE"
                                            }
                                            ],
                                            "tipo_usuario": "PRINCIPAL"
                                        },
                                        "tipo_cuenta": "CTC"
                                    }
                                ]
                                }
                            },
                            "vector_saldos_y_moras": {
                                "saldos_y_moras": [
                                {
                                    "fecha": "2019-02-28",
                                    "moras_maximas": "N",
                                    "num_creditos30": "0",
                                    "saldo_deuda_total": "0.0",
                                    "total_cuentas_mora": "0",
                                    "saldo_deuda_total_mora": "0.0",
                                    "moras_max_sector_telcos": "N",
                                    "num_creditos_mayor_igual60": "0"
                                },
                                {
                                    "fecha": "2019-01-28",
                                    "moras_maximas": "N",
                                    "num_creditos30": "0",
                                    "saldo_deuda_total": "0.0",
                                    "total_cuentas_mora": "0",
                                    "saldo_deuda_total_mora": "0.0",
                                    "moras_max_sector_telcos": "N",
                                    "num_creditos_mayor_igual60": "0"
                                },
                                {
                                    "fecha": "2018-12-28",
                                    "moras_maximas": "N",
                                    "num_creditos30": "0",
                                    "saldo_deuda_total": "0.0",
                                    "total_cuentas_mora": "0",
                                    "saldo_deuda_total_mora": "0.0",
                                    "moras_max_sector_telcos": "N",
                                    "num_creditos_mayor_igual60": "0"
                                },
                                {
                                    "fecha": "2018-11-28",
                                    "moras_maximas": "N",
                                    "num_creditos30": "0",
                                    "saldo_deuda_total": "0.0",
                                    "total_cuentas_mora": "0",
                                    "saldo_deuda_total_mora": "0.0",
                                    "moras_max_sector_telcos": "N",
                                    "num_creditos_mayor_igual60": "0"
                                },
                                {
                                    "fecha": "2018-10-28",
                                    "moras_maximas": "N",
                                    "num_creditos30": "0",
                                    "saldo_deuda_total": "0.0",
                                    "total_cuentas_mora": "0",
                                    "saldo_deuda_total_mora": "0.0",
                                    "moras_max_sector_telcos": "N",
                                    "num_creditos_mayor_igual60": "0"
                                },
                                {
                                    "fecha": "2018-09-28",
                                    "moras_maximas": "N",
                                    "num_creditos30": "0",
                                    "saldo_deuda_total": "0.0",
                                    "total_cuentas_mora": "0",
                                    "saldo_deuda_total_mora": "0.0",
                                    "moras_max_sector_telcos": "N",
                                    "num_creditos_mayor_igual60": "0"
                                },
                                {
                                    "fecha": "2018-08-28",
                                    "moras_maximas": "N",
                                    "num_creditos30": "0",
                                    "saldo_deuda_total": "0.0",
                                    "total_cuentas_mora": "0",
                                    "saldo_deuda_total_mora": "0.0",
                                    "moras_max_sector_telcos": "N",
                                    "num_creditos_mayor_igual60": "0"
                                },
                                {
                                    "fecha": "2018-07-28",
                                    "moras_maximas": "N",
                                    "num_creditos30": "0",
                                    "saldo_deuda_total": "0.0",
                                    "total_cuentas_mora": "0",
                                    "saldo_deuda_total_mora": "0.0",
                                    "moras_max_sector_telcos": "N",
                                    "num_creditos_mayor_igual60": "0"
                                },
                                {
                                    "fecha": "2018-06-28",
                                    "moras_maximas": "N",
                                    "num_creditos30": "0",
                                    "saldo_deuda_total": "0.0",
                                    "total_cuentas_mora": "0",
                                    "saldo_deuda_total_mora": "0.0",
                                    "moras_max_sector_telcos": "N",
                                    "num_creditos_mayor_igual60": "0"
                                },
                                {
                                    "fecha": "2018-05-28",
                                    "moras_maximas": "N",
                                    "num_creditos30": "0",
                                    "saldo_deuda_total": "0.0",
                                    "total_cuentas_mora": "0",
                                    "saldo_deuda_total_mora": "0.0",
                                    "moras_max_sector_telcos": "N",
                                    "num_creditos_mayor_igual60": "0"
                                },
                                {
                                    "fecha": "2018-04-28",
                                    "moras_maximas": "N",
                                    "num_creditos30": "0",
                                    "saldo_deuda_total": "0.0",
                                    "total_cuentas_mora": "0",
                                    "saldo_deuda_total_mora": "0.0",
                                    "moras_max_sector_telcos": "N",
                                    "num_creditos_mayor_igual60": "0"
                                },
                                {
                                    "fecha": "2018-03-28",
                                    "moras_maximas": "N",
                                    "num_creditos30": "0",
                                    "saldo_deuda_total": "0.0",
                                    "total_cuentas_mora": "0",
                                    "saldo_deuda_total_mora": "0.0",
                                    "moras_max_sector_telcos": "N",
                                    "num_creditos_mayor_igual60": "0"
                                }
                                ],
                                "posee_sector_real": "FALSE",
                                "posee_sector_telcos": "TRUE",
                                "posee_sector_financiero": "FALSE",
                                "posee_sector_cooperativo": "FALSE"
                            },
                            "imagen_tendencia_endeudamiento": None
                        },
                        "evolucion_deuda": {
                            "trimestres": {
                                "trimestre": [
                                "2019/03",
                                "2018/12",
                                "2018/09",
                                "2018/06",
                                "2018/03",
                                "2017/12"
                                ]
                            },
                            "evolucion_deuda_sector": {
                                "cod_sector": "4",
                                "nombre_sector": "TELCOS",
                                "evolucion_deuda_tipo_cuenta": [
                                {
                                    "tipo_cuenta": "COM",
                                    "evolucion_deuda_valor_trimestre": [
                                        {
                                            "num": "1",
                                            "cuota": "0.0",
                                            "saldo": "0.0",
                                            "trimestre": "2019/03",
                                            "saldo_mora": "0.0",
                                            "tipo_cuenta": "COM",
                                            "cupo_inicial": "0.0",
                                            "porcentaje_deuda": "0.0",
                                            "cod_menor_calificacion": "4",
                                            "texto_menor_calificacion": "D"
                                        },
                                        {
                                            "num": "1",
                                            "cuota": "0.0",
                                            "saldo": "0.0",
                                            "trimestre": "2018/12",
                                            "saldo_mora": "0.0",
                                            "tipo_cuenta": "COM",
                                            "cupo_inicial": "0.0",
                                            "porcentaje_deuda": "0.0",
                                            "cod_menor_calificacion": "0",
                                            "texto_menor_calificacion": "-"
                                        },
                                        {
                                            "num": "1",
                                            "cuota": "0.0",
                                            "saldo": "0.0",
                                            "trimestre": "2018/09",
                                            "saldo_mora": "0.0",
                                            "tipo_cuenta": "COM",
                                            "cupo_inicial": "0.0",
                                            "porcentaje_deuda": "0.0",
                                            "cod_menor_calificacion": "0",
                                            "texto_menor_calificacion": "-"
                                        },
                                        {
                                            "num": "1",
                                            "cuota": "0.0",
                                            "saldo": "0.0",
                                            "trimestre": "2018/06",
                                            "saldo_mora": "0.0",
                                            "tipo_cuenta": "COM",
                                            "cupo_inicial": "0.0",
                                            "porcentaje_deuda": "0.0",
                                            "cod_menor_calificacion": "0",
                                            "texto_menor_calificacion": "-"
                                        },
                                        {
                                            "num": "1",
                                            "cuota": "0.0",
                                            "saldo": "0.0",
                                            "trimestre": "2018/03",
                                            "saldo_mora": "0.0",
                                            "tipo_cuenta": "COM",
                                            "cupo_inicial": "0.0",
                                            "porcentaje_deuda": "0.0",
                                            "cod_menor_calificacion": "0",
                                            "texto_menor_calificacion": "-"
                                        },
                                        {
                                            "num": "1",
                                            "cuota": "0.0",
                                            "saldo": "0.0",
                                            "trimestre": "2017/12",
                                            "saldo_mora": "0.0",
                                            "tipo_cuenta": "COM",
                                            "cupo_inicial": "0.0",
                                            "porcentaje_deuda": "0.0",
                                            "cod_menor_calificacion": "0",
                                            "texto_menor_calificacion": "-"
                                        }
                                    ]
                                },
                                {
                                    "tipo_cuenta": "CTC",
                                    "evolucion_deuda_valor_trimestre": [
                                        {
                                            "num": "2",
                                            "cuota": "81.0",
                                            "saldo": "0.0",
                                            "trimestre": "2019/03",
                                            "saldo_mora": "0.0",
                                            "tipo_cuenta": "CTC",
                                            "cupo_inicial": "0.0",
                                            "porcentaje_deuda": "0.0",
                                            "cod_menor_calificacion": "1",
                                            "texto_menor_calificacion": "A"
                                        },
                                        {
                                            "num": "2",
                                            "cuota": "81.0",
                                            "saldo": "0.0",
                                            "trimestre": "2018/12",
                                            "saldo_mora": "0.0",
                                            "tipo_cuenta": "CTC",
                                            "cupo_inicial": "0.0",
                                            "porcentaje_deuda": "0.0",
                                            "cod_menor_calificacion": "1",
                                            "texto_menor_calificacion": "A"
                                        },
                                        {
                                            "num": "2",
                                            "cuota": "81.0",
                                            "saldo": "0.0",
                                            "trimestre": "2018/09",
                                            "saldo_mora": "0.0",
                                            "tipo_cuenta": "CTC",
                                            "cupo_inicial": "0.0",
                                            "porcentaje_deuda": "0.0",
                                            "cod_menor_calificacion": "1",
                                            "texto_menor_calificacion": "A"
                                        },
                                        {
                                            "num": "2",
                                            "cuota": "81.0",
                                            "saldo": "0.0",
                                            "trimestre": "2018/06",
                                            "saldo_mora": "0.0",
                                            "tipo_cuenta": "CTC",
                                            "cupo_inicial": "0.0",
                                            "porcentaje_deuda": "0.0",
                                            "cod_menor_calificacion": "1",
                                            "texto_menor_calificacion": "A"
                                        },
                                        {
                                            "num": "3",
                                            "cuota": "87.0",
                                            "saldo": "0.0",
                                            "trimestre": "2018/03",
                                            "saldo_mora": "0.0",
                                            "tipo_cuenta": "CTC",
                                            "cupo_inicial": "0.0",
                                            "porcentaje_deuda": "0.0",
                                            "cod_menor_calificacion": "1",
                                            "texto_menor_calificacion": "A"
                                        },
                                        {
                                            "num": "4",
                                            "cuota": "82.0",
                                            "saldo": "0.0",
                                            "trimestre": "2017/12",
                                            "saldo_mora": "0.0",
                                            "tipo_cuenta": "CTC",
                                            "cupo_inicial": "0.0",
                                            "porcentaje_deuda": "0.0",
                                            "cod_menor_calificacion": "1",
                                            "texto_menor_calificacion": "A"
                                        }
                                    ]
                                }
                                ]
                            }
                        },
                        "analisis_vectores": {
                            "sector": {
                                "cuenta": [
                                {
                                    "estado": "EN RECLAMACION",
                                    "entidad": "MOVISTAR",
                                    "tipo_cuenta": "COM",
                                    "numero_cuenta": "54-603806",
                                    "caracter_fecha": [
                                        {
                                            "fecha": "2019-02-28"
                                        },
                                        {
                                            "fecha": "2019-01-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2018-12-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2018-11-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2018-10-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2018-09-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2018-08-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2018-07-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2018-06-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2018-05-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2018-04-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2018-03-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2018-02-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2018-01-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2017-12-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2017-11-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2017-10-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2017-09-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2017-08-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2017-07-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2017-06-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2017-05-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2017-04-28",
                                            "saldo_deuda_total_mora": ""
                                        },
                                        {
                                            "fecha": "2017-03-28",
                                            "saldo_deuda_total_mora": ""
                                        }
                                    ],
                                    "contiene_datos": "TRUE"
                                },
                                {
                                    "estado": "AL DIA",
                                    "entidad": "MOVISTAR",
                                    "tipo_cuenta": "CTC",
                                    "numero_cuenta": "031297116",
                                    "caracter_fecha": [
                                        {
                                            "fecha": "2019-02-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2019-01-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-12-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-11-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-10-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-09-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-08-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-07-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-06-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-05-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-04-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-03-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-02-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-01-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-12-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-11-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-10-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-09-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-08-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-07-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-06-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-05-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-04-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-03-28",
                                            "saldo_deuda_total_mora": "N"
                                        }
                                    ],
                                    "contiene_datos": "TRUE"
                                },
                                {
                                    "estado": "AL DIA",
                                    "entidad": "MOVISTAR",
                                    "tipo_cuenta": "CTC",
                                    "numero_cuenta": "031931295",
                                    "caracter_fecha": [
                                        {
                                            "fecha": "2019-02-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2019-01-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-12-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-11-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-10-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-09-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-08-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-07-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-06-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-05-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-04-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-03-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-02-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-01-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-12-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-11-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-10-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-09-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-08-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-07-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-06-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-05-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-04-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-03-28",
                                            "saldo_deuda_total_mora": "N"
                                        }
                                    ],
                                    "contiene_datos": "TRUE"
                                },
                                {
                                    "estado": "PAGO VOL",
                                    "entidad": "MOVISTAR",
                                    "tipo_cuenta": "CTC",
                                    "numero_cuenta": "037558978",
                                    "caracter_fecha": [
                                        {
                                            "fecha": "2019-02-28"
                                        },
                                        {
                                            "fecha": "2019-01-28"
                                        },
                                        {
                                            "fecha": "2018-12-28"
                                        },
                                        {
                                            "fecha": "2018-11-28"
                                        },
                                        {
                                            "fecha": "2018-10-28"
                                        },
                                        {
                                            "fecha": "2018-09-28"
                                        },
                                        {
                                            "fecha": "2018-08-28"
                                        },
                                        {
                                            "fecha": "2018-07-28"
                                        },
                                        {
                                            "fecha": "2018-06-28"
                                        },
                                        {
                                            "fecha": "2018-05-28"
                                        },
                                        {
                                            "fecha": "2018-04-28"
                                        },
                                        {
                                            "fecha": "2018-03-28"
                                        },
                                        {
                                            "fecha": "2018-02-28"
                                        },
                                        {
                                            "fecha": "2018-01-28"
                                        },
                                        {
                                            "fecha": "2017-12-28"
                                        },
                                        {
                                            "fecha": "2017-11-28"
                                        },
                                        {
                                            "fecha": "2017-10-28"
                                        },
                                        {
                                            "fecha": "2017-09-28"
                                        },
                                        {
                                            "fecha": "2017-08-28"
                                        },
                                        {
                                            "fecha": "2017-07-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-06-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-05-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-04-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-03-28",
                                            "saldo_deuda_total_mora": "N"
                                        }
                                    ],
                                    "contiene_datos": "TRUE"
                                },
                                {
                                    "estado": "PAGO VOL",
                                    "entidad": "MOVISTAR",
                                    "tipo_cuenta": "CTC",
                                    "numero_cuenta": "037740598",
                                    "caracter_fecha": [
                                        {
                                            "fecha": "2019-02-28"
                                        },
                                        {
                                            "fecha": "2019-01-28"
                                        },
                                        {
                                            "fecha": "2018-12-28"
                                        },
                                        {
                                            "fecha": "2018-11-28"
                                        },
                                        {
                                            "fecha": "2018-10-28"
                                        },
                                        {
                                            "fecha": "2018-09-28"
                                        },
                                        {
                                            "fecha": "2018-08-28"
                                        },
                                        {
                                            "fecha": "2018-07-28"
                                        },
                                        {
                                            "fecha": "2018-06-28"
                                        },
                                        {
                                            "fecha": "2018-05-28"
                                        },
                                        {
                                            "fecha": "2018-04-28"
                                        },
                                        {
                                            "fecha": "2018-03-28"
                                        },
                                        {
                                            "fecha": "2018-02-28"
                                        },
                                        {
                                            "fecha": "2018-01-28"
                                        },
                                        {
                                            "fecha": "2017-12-28"
                                        },
                                        {
                                            "fecha": "2017-11-28"
                                        },
                                        {
                                            "fecha": "2017-10-28"
                                        },
                                        {
                                            "fecha": "2017-09-28"
                                        },
                                        {
                                            "fecha": "2017-08-28"
                                        },
                                        {
                                            "fecha": "2017-07-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-06-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-05-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-04-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-03-28",
                                            "saldo_deuda_total_mora": "N"
                                        }
                                    ],
                                    "contiene_datos": "TRUE"
                                },
                                {
                                    "estado": "PAGO VOL",
                                    "entidad": "MOVISTAR",
                                    "tipo_cuenta": "CTC",
                                    "numero_cuenta": "037740614",
                                    "caracter_fecha": [
                                        {
                                            "fecha": "2019-02-28"
                                        },
                                        {
                                            "fecha": "2019-01-28"
                                        },
                                        {
                                            "fecha": "2018-12-28"
                                        },
                                        {
                                            "fecha": "2018-11-28"
                                        },
                                        {
                                            "fecha": "2018-10-28"
                                        },
                                        {
                                            "fecha": "2018-09-28"
                                        },
                                        {
                                            "fecha": "2018-08-28"
                                        },
                                        {
                                            "fecha": "2018-07-28"
                                        },
                                        {
                                            "fecha": "2018-06-28"
                                        },
                                        {
                                            "fecha": "2018-05-28"
                                        },
                                        {
                                            "fecha": "2018-04-28"
                                        },
                                        {
                                            "fecha": "2018-03-28"
                                        },
                                        {
                                            "fecha": "2018-02-28"
                                        },
                                        {
                                            "fecha": "2018-01-28"
                                        },
                                        {
                                            "fecha": "2017-12-28"
                                        },
                                        {
                                            "fecha": "2017-11-28"
                                        },
                                        {
                                            "fecha": "2017-10-28"
                                        },
                                        {
                                            "fecha": "2017-09-28"
                                        },
                                        {
                                            "fecha": "2017-08-28"
                                        },
                                        {
                                            "fecha": "2017-07-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-06-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-05-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-04-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-03-28",
                                            "saldo_deuda_total_mora": "N"
                                        }
                                    ],
                                    "contiene_datos": "TRUE"
                                },
                                {
                                    "estado": "PAGO VOL",
                                    "entidad": "MOVISTAR",
                                    "tipo_cuenta": "CTC",
                                    "numero_cuenta": "040456047",
                                    "caracter_fecha": [
                                        {
                                            "fecha": "2019-02-28"
                                        },
                                        {
                                            "fecha": "2019-01-28"
                                        },
                                        {
                                            "fecha": "2018-12-28"
                                        },
                                        {
                                            "fecha": "2018-11-28"
                                        },
                                        {
                                            "fecha": "2018-10-28"
                                        },
                                        {
                                            "fecha": "2018-09-28"
                                        },
                                        {
                                            "fecha": "2018-08-28"
                                        },
                                        {
                                            "fecha": "2018-07-28"
                                        },
                                        {
                                            "fecha": "2018-06-28"
                                        },
                                        {
                                            "fecha": "2018-05-28"
                                        },
                                        {
                                            "fecha": "2018-04-28"
                                        },
                                        {
                                            "fecha": "2018-03-28"
                                        },
                                        {
                                            "fecha": "2018-02-28"
                                        },
                                        {
                                            "fecha": "2018-01-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-12-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-11-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-10-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-09-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-08-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2017-07-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2017-06-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2017-05-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2017-04-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2017-03-28",
                                            "saldo_deuda_total_mora": "-"
                                        }
                                    ],
                                    "contiene_datos": "TRUE"
                                },
                                {
                                    "estado": "PAGO VOL",
                                    "entidad": "MOVISTAR",
                                    "tipo_cuenta": "CTC",
                                    "numero_cuenta": "040535347",
                                    "caracter_fecha": [
                                        {
                                            "fecha": "2019-02-28"
                                        },
                                        {
                                            "fecha": "2019-01-28"
                                        },
                                        {
                                            "fecha": "2018-12-28"
                                        },
                                        {
                                            "fecha": "2018-11-28"
                                        },
                                        {
                                            "fecha": "2018-10-28"
                                        },
                                        {
                                            "fecha": "2018-09-28"
                                        },
                                        {
                                            "fecha": "2018-08-28"
                                        },
                                        {
                                            "fecha": "2018-07-28"
                                        },
                                        {
                                            "fecha": "2018-06-28"
                                        },
                                        {
                                            "fecha": "2018-05-28"
                                        },
                                        {
                                            "fecha": "2018-04-28"
                                        },
                                        {
                                            "fecha": "2018-03-28"
                                        },
                                        {
                                            "fecha": "2018-02-28"
                                        },
                                        {
                                            "fecha": "2018-01-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-12-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-11-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-10-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-09-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2017-08-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2017-07-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2017-06-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2017-05-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2017-04-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2017-03-28",
                                            "saldo_deuda_total_mora": "-"
                                        }
                                    ],
                                    "contiene_datos": "TRUE"
                                },
                                {
                                    "estado": "PAGO VOL",
                                    "entidad": "MOVISTAR",
                                    "tipo_cuenta": "CTC",
                                    "numero_cuenta": "042004372",
                                    "caracter_fecha": [
                                        {
                                            "fecha": "2019-02-28"
                                        },
                                        {
                                            "fecha": "2019-01-28"
                                        },
                                        {
                                            "fecha": "2018-12-28"
                                        },
                                        {
                                            "fecha": "2018-11-28"
                                        },
                                        {
                                            "fecha": "2018-10-28"
                                        },
                                        {
                                            "fecha": "2018-09-28"
                                        },
                                        {
                                            "fecha": "2018-08-28"
                                        },
                                        {
                                            "fecha": "2018-07-28"
                                        },
                                        {
                                            "fecha": "2018-06-28"
                                        },
                                        {
                                            "fecha": "2018-05-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-04-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-03-28",
                                            "saldo_deuda_total_mora": "N"
                                        },
                                        {
                                            "fecha": "2018-02-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2018-01-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2017-12-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2017-11-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2017-10-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2017-09-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2017-08-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2017-07-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2017-06-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2017-05-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2017-04-28",
                                            "saldo_deuda_total_mora": "-"
                                        },
                                        {
                                            "fecha": "2017-03-28",
                                            "saldo_deuda_total_mora": "-"
                                        }
                                    ],
                                    "contiene_datos": "TRUE"
                                }
                                ],
                                "moras_maximas": {
                                "caracter_fecha": [
                                    {
                                        "fecha": "2017-03-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2017-04-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2017-05-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2017-06-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2017-07-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2017-08-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2017-09-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2017-10-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2017-11-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2017-12-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2018-01-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2018-02-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2018-03-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2018-04-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2018-05-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2018-06-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2018-07-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2018-08-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2018-09-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2018-10-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2018-11-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2018-12-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2019-01-28",
                                        "saldo_deuda_total_mora": "N"
                                    },
                                    {
                                        "fecha": "2019-02-28",
                                        "saldo_deuda_total_mora": "N"
                                    }
                                ]
                                },
                                "nombre_sector": "SECTOR TELCOS"
                            }
                        },
                        "comportamiento_entidades": None
                    }
                    }
                },
                "experian_score": 815.0
            },
            "error": "",
            "end_at": "2020-05-26 17:59:48.984936",
            "status": 200,
            "message": "successful",
            "queried_by": "YOUR-USER",
            "service_name": "experian-hcpn-co"
        },
        "message": "Request completed"
    }
    
    # MESSAGE
    message = 'Request completed'
    response['message'] = message

    # SCORE
    score = Datacred_Score()
    response['result']['data']['informes']['informe']['score'] = score
    # ALERTA
    alerta = Datacred_Alerta(random.randint(1, 10))
    response['result']['data']['informes']['informe']['alerta'] = alerta
    # CUENTAS
    cuenta_cartera = Datacred_CuentaCartera(random.randint(1, 20))
    response['result']['data']['informes']['informe']['cuenta_cartera'] = cuenta_cartera

    experian_score = str(random.randint(500, 900))
    response['result']['data']['experian_score'] = experian_score

    status = 200
    response['result']['status'] = status

    return jsonify(response), 200

@app.route('/api/clinton', methods=['POST'])
def responseOfac():
    data = request.json
    if not Authorization(data, 'clinton'): return {"mssg": "No autorizado"}, 401
    if 'name' not in data: return {"mssg": "Los datos de entrada no están completos"}, 400
    response = {
        "error": False,
        "sourcesUsed": [{
            "source": "SDN",
            "publishDate": str(faker.date_between(start_date='-2y', end_date='-1y'))
        }],
        "matches": {
            data['name']: []
        }
    }

    if Reportado(TASA_REPORT_CLINTON):
        response['matches'][data['name']] = ClintonMatches(random.randint(1, 4), data=data)
    return jsonify(response), 200

def Authorization(json, service):
    if service == 'datacred':
        api_key = json.get('x-api-key')
        if not api_key or api_key != API_KEY:
            return False
        return True
    elif service == 'clinton':
        api_key = json.get('apiKey')
        if not api_key or api_key != API_KEY:
            return False
        return True

def Datacred_Score():
    score = {
            "tipo": random.randint(1, 100),
            "fecha": str(faker.date_between(start_date='-10y', end_date='-1y')),
            "razon": [
              {
                "codigo": "00099"
              },
              {
                "codigo": "00000"
              }
            ],
            "puntaje": str(random.randint(15, 900)) + '.0',
            "poblacion": str(random.randint(1, 100))
          }
    print('Score datacred:', score['puntaje'])
    return score

def Datacred_Alerta(cantAlertas):
    alertas = []
    for i in range(cantAlertas):
        alerta = {
              "llave": str(random.randint(10**15, 10**16-1)),
              "texto": faker.sentence(),
              "codigo": str(random.randint(1, 200)),
              "fuente": {
                "codigo": "990001",
                "nombre": "B.D DATACREDIT"
              },
              "cod_lista": str(random.randint(1, 20)),
              "colocacion": str(faker.date_between(start_date='-10y', end_date='-1y')),
              "vencimiento": str(faker.date_between(start_date='-10y', end_date='-1y')),
              "modificacion": str(faker.date_between(start_date='-10y', end_date='-1y'))
            }
        alertas.append(alerta)
    return alertas

def Datacred_CuentaCartera(cantCuentas):
    cuentas = []
    
    for i in range(cantCuentas):
        cuenta = {
              "llave": str(random.randint(10**15, 10**16-1)),
              "ciudad": faker.city(),
              "numero": str(random.randint(10**10, 10**11-1)),
              "sector": "REAL",
              "entidad": faker.company(),
              "estados": {
                "estado_pago": {
                  "fecha": str(faker.date_between(start_date='-10y', end_date='-1y')),
                  "meses": str(random.randint(1, 10) * 6),
                  "codigo": "PAGO VOLUNTARIO"
                },
                "estado_cuenta": {
                  "fecha": str(faker.date_between(start_date='-10y', end_date='-1y')),
                  "codigo": "PAGO TOTAL"
                },
                "estado_origen": {
                  "fecha": str(faker.date_between(start_date='-10y', end_date='-1y')),
                  "codigo": "NORMAL. CREACION POR APERTURA"
                }
              },
              "oficina": "NO INFORMO",
              "valores": None,
              "bloqueada": random.choice(['TRUE', 'FALSE']),
              "forma_pago": str(random.randint(1, 5)),
              "cod_suscriptor": "050098",
              "comportamiento": Datacred_Comportamiento(),
              "fecha_apertura": str(faker.date_between(start_date='-10y', end_date='-1y')),
              "identificacion": str(random.randint(10**10, 10**11-1)),
              "calificacion_hd": random.choice(['TRUE', 'FALSE']),
              "caracteristicas": {
                "garantia": "2",
                "tipo_cuenta": "CARTERA BANCARIA",
                "tipo_contrato": "0",
                "calidad_deudor": "05",
                "tipo_obligacion": "COMERCIALES",
                "meses_permanencia": "0",
                "ejecucion_contrato": "1"
              },
              "fecha_vencimiento": str(faker.date_between(start_date='-10y', end_date='-1y')),
              "situacion_titular": "NORMAL",
              "codigo_dane_ciudad": "00000000",
              "tipo_identificacion": "NUMERO DE IDENTIFICACION TRIBUTARIA",
              "probabilidad_incumplimiento": "0.0"
            }
        cuentas.append(cuenta)
    return cuentas

def Datacred_Comportamiento():
    comportamiento = ''
    for i in range(40): comportamiento += random.choice(['-', 'N'])
    comportamiento += '--------'
    return comportamiento

def Reportado(probabilidad):
    num = random.randint(1, 100)
    print('Reportado:', num, True if num <= probabilidad else False)
    return True if num <= probabilidad else False

def ClintonMatches(cantCoincidencias, data):
    coincidencias = []
    programs = ["561-RELATED", "BALKANS", "BALKANS-EO14033", "BELARUS", "BELARUS-EO14038", "BPI-PA", "BPI-SDNTK", "BURMA-EO14014", "CAATSA - IRAN", "CAATSA - RUSSIA", "CAR", "CMIC-EO13959", "CUBA", "CYBER2", "DARFUR", "DPRK", "DPRK2", "DPRK3", "DPRK4", "DPRK-NKSPEA", "DRCONGO", "ELECTION-EO13848", "ETHIOPIA-EO14046", "FSE-SY", "FSE-IR", "FSE-WMD", "FSE-SDGT", "FTO", "GLOMAG", "HIFPAA", "HK-EO13936", "HRIT-SY", "HRIT-IR", "IFCA", "IFSR", "ILLICIT-DRUGS-EO14059", "IRAN", "IRAN-CON-ARMS-EO", "IRAN-EO13846", "IRAN-EO13876", "IRAN-EO13871", "IRAN-EO13902", "IRAN-HR", "IRAN-TRA", "IRAQ2", "IRAQ3", "IRGC", "ISA", "LEBANON", "LIBYA2", "LIBYA3", "MAGNIT", "MALI-EO13882", "NDAA", "NICARAGUA", "NICARAGUA-NHRAA", "NPWMD", "NS-ISA", "NS-PLC", "PEESA", "PEESA-EO14039", "RUSSIA-EO14024", "SDGT", "SDNT", "SDNTK", "SOMALIA", "SSIDES", "SUDAN", "SOUTH SUDAN", "SYRIA", "SYRIA-CAESAR", "SYRIA-EO13894", "TCO", "UKRAINE-EO13660", "UKRAINE-EO13661", "UKRAINE-EO13662", "UKRAINE-EO13685", "VENEZUELA", "VENEZUELA-EO13850", "VENEZUELA-EO13884", "YEMEN", "ZIMBABWE"]
    for i in range(cantCoincidencias):
        firstName = faker.first_name()
        lastName = data['name'].split()[-1]

        coincidencia = coincidencia = {
                "source": "SDN",
                "firstName": firstName,
                "lastName": lastName,
                "fullName": f"{firstName} {lastName}",
                "dob": "30 Jan 1969",
                "addresses": [{
					"uid": 35667,
					"city": "Donetsk",
					"stateOrProvince": "Donetsk Oblast",
					"country": "Ukraine"
				}],
                "citizenship": [],
                "title": "Minister of State Security of the so-called Donetsk People's Republic",
                "uid": random.randint(10**5, 10**6-1),
                "sdnType": "Individual",
                "remarks": "(Linked To: DONETSK PEOPLE'S REPUBLIC)",
                "gender": random.choice(['Male', 'Female']),
                "programs": [
                    random.choice(programs)
                ],
                "additionalSanctions": [],
                "passports": [],
                "score": random.randint(1, 100),
                "akas": [{
						"score": 57,
						"uid": 37195,
						"category": "strong",
						"lastName": "PAVLENKO",
						"firstName": "Volodymyr Mykolaiovych"
					}],
                "ids": [{
                    "type": "Secondary sanctions risk:",
                    "id": "Ukraine-/Russia-Related Sanctions Regulations, 31 CFR 589.201 and/or 589.209"
                }]
            }
        coincidencias.append(coincidencia)
    return coincidencias

if __name__ == '__main__':
    app.run(debug=True, port=5000)
