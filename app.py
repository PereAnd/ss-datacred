from flask import Flask, request, jsonify
from faker import Faker
import random
import hashlib
import datetime
import random


app = Flask(__name__)
faker = Faker()
TASA_REPORT_DATACRED = 50
TASA_REPORT_CLINTON = 0
API_KEY = 'ESTAESMIAPIKEY'

global_data = {
    "last_name": '',
    "document_type": '',
    "document_number": ''
}


@app.route('/api/ping', methods=['GET'])
def health():
    response = {"mssg": "pong"}
    return response, 200


@app.route('/api/datacredito', methods=['POST'])
def getDatacredRequestID():
    # if not Authorization(request.headers, 'datacred'): return {"mssg": "No autorizado"}, 403
    if ('last_name' not in request.json or 'document_type' not in request.json or 'document_number' not in request.json):
        return {"mssg": "Los datos de entrada no están completos"}, 400
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    hash = hashlib.sha256(date.encode()).hexdigest()[:20]

    global_data['last_name'] = request.json['last_name']
    global_data['document_type'] = request.json['document_type']
    global_data['document_number'] = request.json['document_number']

    response = {
        "message": "Request processed successfully",
        "url": f"/api/datacredito/{hash}/",
        "request_id": hash
    }
    return response, 200


@app.route('/api/datacredito/<request_id>', methods=['GET'])
def responseDatacred(request_id):
    # if not Authorization(request.headers, 'datacred'): return {"mssg": "No autorizado"}, 403
    if not Reportado(TASA_REPORT_DATACRED):
        return {"mssg": "Cliente no encontrado"}, 404

    score = Datacred_Score()
    alerta = Datacred_Alerta(random.randint(1, 10))
    reclamo = Datacred_Reclamo(random.randint(1, 10))
    consulta = Datacred_Consulta(random.randint(1, 10))
    cuenta_cartera = Datacred_CuentaCartera(random.randint(1, 20))
    message = 'Request completed'
    experian_score = score["puntaje"]
    status = 200

    response = {
        "result": {
            "data": {
                "warning": "",
                "informes": {
                    "informe": {
                        "score": score,
                        "alerta": alerta,
                        "reclamo": reclamo,
                        "consulta": consulta,
                        "respuesta": str(random.randint(1, 20)),
                        "cod_seguridad": faker.md5(),
                        "info_agregada": {
                            "cheques": None,
                            "resumen": {
                                "saldos": {
                                    "mes": [
                                        {
                                            "fecha": "2019-02-28",
                                            "saldo_total": "0",
                                            "saldo_total_mora": "0"
                                        }
                                    ],
                                    "sector": [
                                        {
                                            "saldo": "0.0",
                                            "sector": "1",
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
                                        }
                                    }
                                ]
                            }
                        },
                        "cuenta_cartera": cuenta_cartera,
                        "fecha_consulta": faker.date_this_year(),
                        "natural_nacional": {},
                        "tipo_id_digitado": global_data['document_type'],
                        "apellido_digitado": global_data['last_name'],
                        "productos_valores": {},
                        "identificacion_digitada": global_data['document_number'],
                        "info_agregada_microcredito": {},
                    }
                },
                "experian_score": experian_score
            },
            "error": "",
            "end_at": "2020-05-26 17:59:48.984936",
            "status": status,
            "message": "successful",
            "queried_by": "YOUR-USER",
            "service_name": "experian-hcpn-co"
        },
        "message": message
    }

    return jsonify(response), 200


@app.route('/api/clinton', methods=['POST'])
def responseOfac():
    data = request.json
    if not Authorization(data, 'clinton'):
        return {"mssg": "No autorizado"}, 401
    if 'name' not in data:
        return {"mssg": "Los datos de entrada no están completos"}, 400
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
        response['matches'][data['name']] = ClintonMatches(
            random.randint(1, 4), data=data)
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


def Datacred_Reclamo(cantReclamos):
    reclamos = []
    for i in range(cantReclamos):
        reclamo = {
            "tipo": "0" + str(random.randint(1, 5)),
                    "fecha": str(faker.date_between(start_date='-10y', end_date='-1y')),
                    "texto": faker.word(),
                    "estado": str(random.randint(1, 5)),
                    "numero": random.randint(10**6, 10**7),
                    "entidad": faker.company(),
                    "subtipo": {
                        "codigo": "0" + str(random.randint(1, 5)),
                        "nombre": faker.sentence()
            },
            "ratificado": random.choice(['TRUE', 'FALSE']),
            "tipo_leyenda": "0" + str(random.randint(1, 5)),
            "numero_cuenta": "00000" + str(random.randint(10**10, 10**11-1))
        }
        reclamos.append(reclamo)
    return reclamos


def Datacred_Consulta(cantConsultas):
    consultas = []
    for i in range(cantConsultas):
        consulta = {
            "fecha": faker.date_between(start_date='-10y', end_date='-1y'),
            "llave": str(random.randint(10**15, 10**16-1)),
            "razon": random.choice(['00099', '00000']),
            "ciudad": "------------",
            "sector": random.randint(1, 5),
            "entidad": faker.company(),
            "oficina": "------------------",
            "cantidad": "0" + str(random.randint(1, 5)),
            "tipo_cuenta": "COC",
            "nit_suscriptor": faker.random_number(digits=10),
        }
        consultas.append(consulta)
    return consultas


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
    for i in range(40):
        comportamiento += random.choice(['-', 'N'])
    comportamiento += '--------'
    return comportamiento


def Reportado(probabilidad):
    num = random.randint(1, 100)
    print('Reportado:', num, True if num <= probabilidad else False)
    return True if num <= probabilidad else False


def ClintonMatches(cantCoincidencias, data):
    coincidencias = []
    programs = ["561-RELATED", "BALKANS", "BALKANS-EO14033", "BELARUS", "BELARUS-EO14038", "BPI-PA", "BPI-SDNTK", "BURMA-EO14014", "CAATSA - IRAN", "CAATSA - RUSSIA", "CAR", "CMIC-EO13959", "CUBA", "CYBER2", "DARFUR", "DPRK", "DPRK2", "DPRK3", "DPRK4", "DPRK-NKSPEA", "DRCONGO", "ELECTION-EO13848", "ETHIOPIA-EO14046", "FSE-SY", "FSE-IR", "FSE-WMD", "FSE-SDGT", "FTO", "GLOMAG", "HIFPAA", "HK-EO13936", "HRIT-SY", "HRIT-IR", "IFCA", "IFSR", "ILLICIT-DRUGS-EO14059", "IRAN", "IRAN-CON-ARMS-EO", "IRAN-EO13846", "IRAN-EO13876",
                "IRAN-EO13871", "IRAN-EO13902", "IRAN-HR", "IRAN-TRA", "IRAQ2", "IRAQ3", "IRGC", "ISA", "LEBANON", "LIBYA2", "LIBYA3", "MAGNIT", "MALI-EO13882", "NDAA", "NICARAGUA", "NICARAGUA-NHRAA", "NPWMD", "NS-ISA", "NS-PLC", "PEESA", "PEESA-EO14039", "RUSSIA-EO14024", "SDGT", "SDNT", "SDNTK", "SOMALIA", "SSIDES", "SUDAN", "SOUTH SUDAN", "SYRIA", "SYRIA-CAESAR", "SYRIA-EO13894", "TCO", "UKRAINE-EO13660", "UKRAINE-EO13661", "UKRAINE-EO13662", "UKRAINE-EO13685", "VENEZUELA", "VENEZUELA-EO13850", "VENEZUELA-EO13884", "YEMEN", "ZIMBABWE"]
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
    app.run(debug=True, port=4002)
