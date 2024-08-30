from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
import folium
import pymongo
import sys
import pandas as pd
from dotenv import load_dotenv
from langchain_groq.chat_models import ChatGroq
import os
from pandasai import SmartDataframe
import logging
import ast
import plotly.graph_objects as go
import pickle
import difflib
from flask import jsonify, request
import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename



app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

grping_formatt2 = {
            'DEREBAIL NAIRUTHYA': {
                'EmploymentStatus': {
                    'S': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'W': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'O': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'T': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    }
                },

                'EconomicStatus': {
                    'S': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'W': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'O': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'T': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    }
                },

                'HealthStatus': {
                    'S': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },

                    'W': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },

                    'O': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'T': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    }
                },

                'HomeType': {
                    'S': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'W': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'O': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'T': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    }
                },

                'Education': {
                    'S': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'W': {

                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'O': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'T': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    }
                }
            },

            'BEJAI': {
                'EmploymentStatus': {
                    'S': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'W': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'O': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'T': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    }
                },

                'EconomicStatus': {
                    'S': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'W': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'O': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'T': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    }
                },

                'HealthStatus': {
                    'S': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },

                    'W': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },

                    'O': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'T': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    }
                },

                'HomeType': {
                    'S': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'W': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'O': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'T': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    }
                },

                'Education': {
                    'S': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'W': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'O': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'T': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    }
                }
            }
        }



def check_integer1(num, count, lb, per):
    if num > 0:
        return ("Positive", num, count, lb, per)
    elif num < 0:
        return ("Negative", num, count, lb, per)
    else:
        return ("Zero", num, count, lb, per)



def check_integer2(num, count):
    if num > 0:
        return ("Positive", num, count)
    elif num < 0:
        return ("Negative", num, count)
    else:
        return ("Zero", num, count)


def check_integer(num, count, lb):
    if num > 0:
        return ("Positive", num, count, lb)
    elif num < 0:
        return ("Negative", num, count, lb)
    else:
        return ("Zero", num, count, lb)


def comparison(a, b):
    if a > b:
        data1 = {a: 'High'}
        data2 = {b: 'Low'}
    elif a < b:
        data1 = {a: 'Low'}
        data2 = {b: 'High'}
    return data1, data2


def SelectedWardAnalytics(ward):
    Client_Cloud = pymongo.MongoClient('mongodb+srv://ravindraacharya0512:Iwilltakeovertheworld123@cluster0.ynaiaut.mongodb.net/')
    MainDB = Client_Cloud['MainB']
    MainDB_Coll = MainDB['CollDB']
    total_documents = MainDB_Coll.count_documents({})

    data_ref = {
        'BEJAI': {
            'Emp': 6025,
            'Unemp': 4321,
            'Ed': 4963,
            'Uned': 5421,
            'Hea': 9986,
            'Dis': 1752,
            'Rent': 5975,
            'Own': 5696,
            'Ap': 6286,
            'Bp': 5696
        },
        'DEREBAIL NAIRUTHYA': {
            'Emp': 3569,
            'Unemp': 1012,
            'Ed': 3059,
            'Uned': 3652,
            'Hea': 5863,
            'Dis': 1496,
            'Rent': 4793,
            'Own': 2689,
            'Ap': 5286,
            'Bp': 2256
        }
    }

    queries = [
        {'WARD': ward, 'EmploymentStatus': 'Employed'},
        {'WARD': ward, 'EmploymentStatus': 'UnEmployed'},
        {'WARD': ward, 'Education': 'Educated'},
        {'WARD': ward, 'Education': 'Uneducated'},
        {'WARD': ward, 'HealthStatus': 'Healthy'},
        {'WARD': ward, 'HealthStatus': 'Diseased'},
        {'WARD': ward, 'HomeType': 'Rent'},
        {'WARD': ward, 'HomeType': 'Own'},
        {'WARD': ward, 'EconomicStatus': 'APL'},
        {'WARD': ward, 'EconomicStatus': 'BPL'}
    ]
    print(queries)
    results = [MainDB_Coll.count_documents(q) for q in queries]
    print(results)
    get_emp, get_unemp, get_ed, get_uned, get_hea, get_unhea, get_rent, get_own, get_apl, get_bpl = results

    percentages = [count / total_documents * 100 for count in results]
    print(percentages)
    get_emp_per, get_unemp_per, get_ed_per, get_uned_per, get_hea_per, get_unhea_per, get_rent_per, get_own_per, get_apl_per, get_bpl_per = percentages
    print('----->', get_emp_per, get_unemp_per, get_ed_per)

    labels = [
        comparison(get_emp_per, get_unemp_per),
        comparison(get_ed_per, get_uned_per),
        comparison(get_hea_per, get_unhea_per),
        comparison(get_rent_per, get_own_per),
        comparison(get_apl_per, get_bpl_per)
    ]

    emp_LB, Unemp_LB = labels[0]
    ed_LB, Uned_LB = labels[1]
    hea_LB, unhea_LB = labels[2]
    rent_LB, own_LB = labels[3]
    apl_LB, bpl_LB = labels[4]

    increments = [
        (get_emp - data_ref[ward]['Emp']) / get_emp * 100,
        (get_unemp - data_ref[ward]['Unemp']) / get_unemp * 100,
        (get_ed - data_ref[ward]['Ed']) / get_ed * 100,
        (get_uned - data_ref[ward]['Uned']) / get_uned * 100,
        (get_hea - data_ref[ward]['Hea']) / get_hea * 100,
        (get_unhea - data_ref[ward]['Dis']) / get_unhea * 100,
        (get_rent - data_ref[ward]['Rent']) / get_rent * 100,
        (get_own - data_ref[ward]['Own']) / get_own * 100,
        (get_apl - data_ref[ward]['Ap']) / get_apl * 100,
        (get_bpl - data_ref[ward]['Bp']) / get_bpl * 100
    ]

    results_sign = [
        check_integer(increments[0], get_emp, emp_LB),
        check_integer(increments[1], get_unemp, Unemp_LB),
        check_integer(increments[2], get_ed, ed_LB),
        check_integer(increments[3], get_uned, Uned_LB),
        check_integer(increments[4], get_hea, hea_LB),
        check_integer(increments[5], get_unhea, unhea_LB),
        check_integer(increments[6], get_rent, rent_LB),
        check_integer(increments[7], get_own, own_LB),
        check_integer(increments[8], get_apl, apl_LB),
        check_integer(increments[9], get_bpl, bpl_LB)
    ]

    data_to_display = {
        'EmploymentStatus': {
            'Employed': results_sign[0],
            'UnEmployed': results_sign[1]
        },
        'Education': {
            'Educated': results_sign[2],
            'Uneducated': results_sign[3]
        },
        'HealthStatus': {
            'Healthy': results_sign[4],
            'Diseased': results_sign[5]
        },
        'HomeType': {
            'Rent': results_sign[6],
            'Own': results_sign[7]
        },
        'EconomicStatus': {
            'APL': results_sign[8],
            'BPL': results_sign[9]
        }
    }
    print(data_to_display)
    return data_to_display


def comparison2(percentage):
    if 90 < percentage <= 100:
        return 'HA'
    elif 80 < percentage <= 90:
        return 'HB'
    elif 70 < percentage <= 80:
        return 'HC'
    elif 60 < percentage <= 70:
        return 'HD'
    elif 50 < percentage <= 60:
        return 'MA'
    elif 40 < percentage <= 50:
        return 'MB'
    elif 30 < percentage <= 40:
        return 'MC'
    elif 20 < percentage <= 30:
        return 'LA'
    elif 10 < percentage <= 20:
        return 'LB'
    elif 0 <= percentage <= 10:
        return 'LC'


def HMC_Analytics(location):
    Client_Cloud = pymongo.MongoClient('mongodb+srv://ravindraacharya0512:Iwilltakeovertheworld123@cluster0.ynaiaut.mongodb.net/')
    MainDB = Client_Cloud['MainB']
    MainDB_Coll = MainDB['CollDB']
    total_documents = MainDB_Coll.count_documents({})

    dic_data = {
        'BEJAI': {
            'H': 4589,
            'M': 3102,
            'C': 1863,
            'B': 596,
            'J': 623,
            'S': 264
        },

        'DEREBAIL NAIRUTHYA': {
            'H': 3056,
            'M': 1682,
            'C': 1502,
            'B': 482,
            'J': 341,
            'S': 141
        }
    }

    queriesHmC = [
        {'WARD': location, 'Religion': 'Hindu'},
        {'WARD': location, 'Religion': 'Muslim'},
        {'WARD': location, 'Religion': 'Christian'},
        {'WARD': location, 'Religion': 'Jain'},
        {'WARD': location, 'Religion': 'Buddhist'},
        {'WARD': location, 'Religion': 'Sikh'}
    ]

    results = [MainDB_Coll.count_documents(q) for q in queriesHmC]
    H, M, C, J, B, S = results

    percentages = [count / total_documents * 100 for count in results]
    H_per, M_per, C_per, J_per, B_per, S_per = percentages

    lb_H_per = comparison2(H_per)
    lb_M_per = comparison2(M_per)
    lb_C_per = comparison2(C_per)
    lb_J_per = comparison2(J_per)
    lb_B_per = comparison2(B_per)
    lb_S_per = comparison2(S_per)

    increments = [
        (H - dic_data[location]['H']) / H * 100,
        (M - dic_data[location]['M']) / M * 100,
        (C - dic_data[location]['C']) / C * 100,
        (J - dic_data[location]['J']) / J * 100,
        (B - dic_data[location]['B']) / B * 100,
        (S - dic_data[location]['S']) / S * 100
    ]

    results_sign = [
        check_integer(increments[0], H, lb_H_per),
        check_integer(increments[1], M, lb_M_per),
        check_integer(increments[2], C, lb_C_per),
        check_integer(increments[3], J, lb_J_per),
        check_integer(increments[4], B, lb_B_per),
        check_integer(increments[5], S, lb_S_per)
    ]

    data_to_prensent = {
        'Religion': {
            'Hindu ': results_sign[0],
            'Muslim': results_sign[1],

            'Christian': results_sign[2],
            'Jain': results_sign[3],

            'Buddhist': results_sign[4],
            'Sikh': results_sign[5]
        }
    }

    return data_to_prensent


def Women_EmploymentStatus(wrd):
    Client_Cloud = pymongo.MongoClient('mongodb+srv://ravindraacharya0512:Iwilltakeovertheworld123@cluster0.ynaiaut.mongodb.net/')
    MainDB = Client_Cloud['MainB']
    MainDB_Coll = MainDB['CollDB']
    total_documents = MainDB_Coll.count_documents({})

    data_ref = {
        'BEJAI': {
            'FE': 2789,
            'FU': 2398,
            'FM': 325
        },
        'DEREBAIL NAIRUTHYA': {
            'FE': 1875,
            'FU': 156,
            'FM': 123
        }
    }
    queries = [
        {'WARD': wrd, 'Gender': 'Female', 'EmploymentStatus': 'Employed'},
        {'WARD': wrd, 'Gender': 'Female', 'EmploymentStatus': 'UnEmployed'},
        {'WARD': wrd, 'Gender': 'Female', 'EmploymentStatus': 'Minor'}
    ]

    results = [MainDB_Coll.count_documents(q) for q in queries]
    Q1, Q2, Q3 = results
    sum_ = Q1 + Q2 + Q3
    D_percent = [count / sum_ * 100 for count in results]
    DQ1, DQ2, DQ3 = D_percent
    percentages = [count / total_documents * 100 for count in results]
    Q1_per, Q2_per, Q3_per = percentages

    lb_Q1_per = comparison2(Q1_per)
    lb_Q2_per = comparison2(Q2_per)
    lb_Q3_per = comparison2(Q3_per)

    increments = [
        (Q1 - data_ref[wrd]['FE']) / Q1 * 100,
        (Q2 - data_ref[wrd]['FU']) / Q2 * 100,
        (Q3 - data_ref[wrd]['FU']) / Q3 * 100
    ]

    results_sign = [
        check_integer1(increments[0], Q1, lb_Q1_per, DQ1),
        check_integer1(increments[1], Q2, lb_Q2_per, DQ2),
        check_integer1(increments[2], Q3, lb_Q3_per, DQ3)
    ]

    data_to_present = {
        'Female-Employed': results_sign[0],
        'Female-Unemployed': results_sign[1],
        'Female-Minor': results_sign[2]

    }
    pie_chart_data = {key: value[-1] for key, value in data_to_present.items()}

    return data_to_present, pie_chart_data


def MinorityStatus(ward_in):
    def MinorityEmploymentStatus(ward):
        Client_Cloud = pymongo.MongoClient('mongodb+srv://ravindraacharya0512:Iwilltakeovertheworld123@cluster0.ynaiaut.mongodb.net/')
        MainDB = Client_Cloud['MainB']
        MainDB_Coll = MainDB['CollDB']
        total_documents = MainDB_Coll.count_documents({})

        data_ref = {
            'BEJAI': {
                'MEmp': 1789,
                'MUnemp': 825,
                'CEmp': 799,
                'CUnemp': 1024
            },
            'DEREBAIL NAIRUTHYA': {
                'MEmp': 1589,
                'MUnemp': 203,
                'CEmp': 856,
                'CUnemp': 389
            }
        }

        queries = [
            {'WARD':ward_in, 'Religion': 'Muslim', 'EmploymentStatus': 'Employed'},
            {'WARD':ward_in, 'Religion': 'Muslim', 'EmploymentStatus': 'UnEmployed'},
            {'WARD':ward_in, 'Religion': 'Christian', 'EmploymentStatus': 'Employed'},
            {'WARD':ward_in, 'Religion': 'Christian', 'EmploymentStatus': 'UnEmployed'},
        ]

        results = [MainDB_Coll.count_documents(q) for q in queries]
        mus_emp, mus_unemp, chr_emp, chr_unemp = results
        Sun_emp = mus_emp + chr_emp
        Sum_unemp = mus_unemp + chr_unemp

        list_emp = [mus_emp, chr_emp]
        percentages_emp = [count / Sun_emp * 100 for count in list_emp]
        mus_emp_per, chr_emp_per = percentages_emp
        data_to_present2 = {
            'Muslim-Employed': mus_emp_per,
            'Christian-Employed': chr_emp_per,
        }


        list_unemp = [mus_unemp, chr_unemp]
        percentages_unemp = [count / Sum_unemp * 100 for count in list_unemp]
        mus_unemp_per, chr_unemp_per = percentages_unemp
        data_to_present3 = {
            'Muslim-Unemployed': mus_unemp_per,
            'Christian-Unemployed': chr_unemp_per
        }


        percentages = [count / total_documents * 100 for count in results]
        mus_emp_per, mus_unemp_per, chr_emp_per, chr_unemp_per = percentages

        sum_ = mus_emp + mus_unemp + chr_emp + chr_unemp
        D_percent = [count / sum_ * 100 for count in results]
        DQ1, DQ2, DQ3, DQ4 = D_percent
        labels = [
            comparison(mus_emp_per, mus_unemp_per),
            comparison(chr_emp_per, chr_unemp_per),
        ]

        mus_emp_LB, mus_unemp_LB = labels[0]
        chr_emp_LB, chr_unemp_LB = labels[1]

        increments = [
            (mus_emp - data_ref[ward]['MEmp']) / mus_emp * 100,
            (mus_unemp - data_ref[ward]['MUnemp']) / mus_unemp * 100,
            (chr_emp - data_ref[ward]['CEmp']) / chr_emp * 100,
            (chr_unemp - data_ref[ward]['CUnemp']) / chr_unemp * 100
        ]

        results_sign = [
            check_integer1(increments[0], mus_emp, mus_emp_LB, DQ1),
            check_integer1(increments[1], mus_unemp, mus_unemp_LB, DQ2),
            check_integer1(increments[2], chr_emp, chr_emp_LB, DQ3),
            check_integer1(increments[3], chr_unemp, chr_unemp_LB, DQ4)
        ]

        data_to_present1 = {
            'Muslim-Employed': results_sign[0],
            'Muslim-Unemployed': results_sign[1],
            'Christian-Employed': results_sign[2],
            'Christian-Unemployed': results_sign[3]
        }

        pie_chart_data_min_emp = data_to_present2
        pie_chart_data_min_unemp = data_to_present3
        return data_to_present1, pie_chart_data_min_emp, pie_chart_data_min_unemp


    def MinorityEconomicStatus(ward):
        Client_Cloud = pymongo.MongoClient('mongodb+srv://ravindraacharya0512:Iwilltakeovertheworld123@cluster0.ynaiaut.mongodb.net/')
        MainDB = Client_Cloud['MainB']
        MainDB_Coll = MainDB['CollDB']
        total_documents = MainDB_Coll.count_documents({})

        data_ref = {
            'BEJAI': {
                'Mapl': 1598,
                'Mbpl': 1623,
                'Capl': 956,
                'Cbpl': 1256
            },
            'DEREBAIL NAIRUTHYA': {
                'Mapl': 1325,
                'Mbpl': 411,
                'Capl': 969,
                'Cbpl': 325
            }
        }

        queries = [
            {'WARD':ward, 'Religion': 'Muslim', 'EconomicStatus': 'APL'},
            {'WARD':ward, 'Religion': 'Muslim', 'EconomicStatus': 'BPL'},
            {'WARD':ward, 'Religion': 'Christian', 'EconomicStatus': 'APL'},
            {'WARD':ward, 'Religion': 'Christian', 'EconomicStatus': 'BPL'},
        ]

        results = [MainDB_Coll.count_documents(q) for q in queries]
        mus_apl, mus_bpl, chr_apl, chr_bpl = results
        Sun_apl = mus_apl + chr_apl
        Sum_bpl = mus_bpl + chr_bpl

        list_apl = [mus_apl, chr_apl]
        percentages_apl = [count / Sun_apl * 100 for count in list_apl]
        mus_apl_per, chr_apl_per = percentages_apl
        data_to_present2_2 = {
            'Muslim-APL': mus_apl_per,
            'Christian-APL': chr_apl_per,
        }

        list_bpl = [mus_bpl, chr_bpl]
        percentages_bpl = [count / Sum_bpl * 100 for count in list_bpl]
        mus_bpl_per, chr_bpl_per = percentages_bpl

        data_to_present3_3 = {
            'Muslim-BPL': mus_bpl_per,
            'Christian-BPL': chr_bpl_per
        }

        percentages = [count / total_documents * 100 for count in results]
        mus_apl_per, mus_bpl_per, chr_apl_per, chr_bpl_per = percentages

        sum_ = mus_apl + mus_bpl + chr_apl + chr_bpl
        D_percent = [count / sum_ * 100 for count in results]
        DQ1, DQ2, DQ3, DQ4 = D_percent
        labels = [
            comparison(mus_apl_per, mus_bpl_per),
            comparison(chr_apl_per, chr_bpl_per),
        ]

        mus_apl_LB, mus_bpl_LB = labels[0]
        chr_apl_LB, chr_bpl_LB = labels[1]

        increments = [
            (mus_apl - data_ref[ward]['Mapl']) / mus_apl * 100,
            (mus_bpl - data_ref[ward]['Mbpl']) / mus_bpl * 100,
            (chr_apl - data_ref[ward]['Capl']) / chr_apl * 100,
            (chr_bpl - data_ref[ward]['Cbpl']) / chr_bpl * 100
        ]

        results_sign = [
            check_integer1(increments[0], mus_apl, mus_apl_LB, DQ1),
            check_integer1(increments[1], mus_bpl, mus_bpl_LB, DQ2),
            check_integer1(increments[2], chr_apl, chr_apl_LB, DQ3),
            check_integer1(increments[3], chr_bpl, chr_bpl_LB, DQ4)
        ]

        data_to_present1_1 = {
            'Muslim-APL': results_sign[0],
            'Muslim-BPL': results_sign[1],
            'Christian-APL': results_sign[2],
            'Christian-BPL': results_sign[3]
        }

        pie_chart_data_min_apl = data_to_present2_2
        pie_chart_data_min_bpl = data_to_present3_3
        return data_to_present1_1, pie_chart_data_min_apl, pie_chart_data_min_bpl



    def MinorityHealthStatus(LOC):
        Client_Cloud = pymongo.MongoClient('mongodb+srv://ravindraacharya0512:Iwilltakeovertheworld123@cluster0.ynaiaut.mongodb.net/')
        MainDB = Client_Cloud['MainB']
        MainDB_Coll = MainDB['CollDB']
        total_documents = MainDB_Coll.count_documents({})

        data_ref = {
            'BEJAI': {
                'Mhea': 2690,
                'Mdis': 589,
                'Chea': 1536,
                'Cdis': 326
            },
            'DEREBAIL NAIRUTHYA': {
                'Mhea': 1564,
                'Mdis': 562,
                'Chea': 1289,
                'Cdis': 203
            }
        }

        queries = [
            {'WARD':LOC, 'Religion': 'Muslim', 'HealthStatus': 'Healthy'},
            {'WARD':LOC, 'Religion': 'Muslim', 'HealthStatus': 'Diseased'},
            {'WARD':LOC, 'Religion': 'Christian', 'HealthStatus': 'Healthy'},
            {'WARD':LOC, 'Religion': 'Christian', 'HealthStatus': 'Diseased'},
        ]

        results = [MainDB_Coll.count_documents(q) for q in queries]
        mus_hea, mus_dis, chr_hea, chr_dis = results
        
        Sun_hea = mus_hea + chr_hea
        Sum_dis = mus_dis + chr_dis
        list_hea = [mus_hea, chr_hea]
        percentages_hea = [count / Sun_hea * 100 for count in list_hea]
        mus_hea_per, chr_hea_per = percentages_hea
        data_to_present2_3 = {
            'Muslim-Healthy': mus_hea_per,
            'Christian-Healthy': chr_hea_per,
        }

        list_dis = [mus_dis, chr_dis]
        percentages_dis = [count / Sum_dis * 100 for count in list_dis]
        mus_dis_per, chr_dis_per = percentages_dis
        data_to_present4_3 = {
            'Muslim-Diseased': mus_dis_per,
            'Christian-Diseased': chr_dis_per,
        }

        percentages = [count / total_documents * 100 for count in results]
        mus_hea_per, mus_dis_per, chr_hea_per, chr_dis_per = percentages

        sum_ = mus_hea + mus_dis + chr_hea + chr_dis
        D_percent = [count / sum_ * 100 for count in results]
        DQ1, DQ2, DQ3, DQ4 = D_percent

        labels = [
            comparison(mus_hea_per, mus_dis_per),
            comparison(chr_hea_per, chr_dis_per),
        ]

        mus_hea_LB, mus_dis_LB = labels[0]
        chr_hea_LB, chr_dis_LB = labels[1]

        increments = [
            (mus_hea - data_ref[LOC]['Mhea']) / mus_hea * 100,
            (mus_dis - data_ref[LOC]['Mdis']) / mus_dis * 100,
            (chr_hea - data_ref[LOC]['Chea']) / chr_hea * 100,
            (chr_dis - data_ref[LOC]['Cdis']) / chr_dis * 100
        ]

        results_sign = [
            check_integer1(increments[0], mus_hea, mus_hea_LB, DQ1),
            check_integer1(increments[1], mus_dis, mus_dis_LB, DQ2),
            check_integer1(increments[2], chr_hea, chr_hea_LB, DQ3),
            check_integer1(increments[3], chr_dis, chr_dis_LB, DQ4)
        ]

        data_to_present55 = {
            'Muslim-Healthy': results_sign[0],
            'Muslim-Diseased': results_sign[1],
            'Christian-Healthy': results_sign[2],
            'Christian-Diseased': results_sign[3]
        }
        pie_chart_data_min_hea = data_to_present2_3
        pie_chart_data_min_dis = data_to_present4_3
        return data_to_present55, pie_chart_data_min_hea, pie_chart_data_min_dis



    data_to_present1, pie_chart_data_min_emp, pie_chart_data_min_unemp = MinorityEmploymentStatus(ward_in)
    data_to_present1_1, pie_chart_data_min_apl, pie_chart_data_min_bpl = MinorityEconomicStatus(ward_in)
    data_to_present55, pie_chart_data_min_hea, pie_chart_data_min_dis = MinorityHealthStatus(ward_in)
    return data_to_present1, pie_chart_data_min_emp, pie_chart_data_min_unemp, data_to_present1_1, pie_chart_data_min_apl, pie_chart_data_min_bpl, data_to_present55, pie_chart_data_min_hea, pie_chart_data_min_dis




def StudentsUnderBPL(ward):
    Client_Cloud = pymongo.MongoClient('mongodb+srv://ravindraacharya0512:Iwilltakeovertheworld123@cluster0.ynaiaut.mongodb.net/')
    MainDB = Client_Cloud['MainB']
    MainDB_Coll = MainDB['CollDB']
    total_documents = MainDB_Coll.count_documents({})
    data_ref = {
        'BEJAI': {
            'apl': 4986,
            'bpl': 4852,
        },
        'DEREBAIL NAIRUTHYA': {
            'apl': 4699,
            'bpl': 1910,
        }
    }

    queries = [
        {'WARD':ward, 'AGE': {'$lt': 18}, 'EconomicStatus': 'APL'},
        {'WARD':ward, 'AGE': {'$lt': 18}, 'EconomicStatus': 'BPL'}
    ]

    results = [MainDB_Coll.count_documents(q) for q in queries]
    apl, bpl = results

    percentages = [count / total_documents * 100 for count in results]
    apl_per, bpl_per = percentages

    sum_ = apl + bpl 
    D_percent = [count / sum_ * 100 for count in results]
    DQ1, DQ2 = D_percent

    labels = [
        comparison(apl_per, bpl_per)
    ]
    apl_LB, bpl_LB = labels[0]

    increments = [
        (apl - data_ref[ward]['apl']) / apl * 100,
        (bpl - data_ref[ward]['bpl']) / bpl * 100,
    ]
    
    results_sign = [
        check_integer1(increments[0], apl, apl_LB, DQ1),
        check_integer1(increments[1], bpl, bpl_LB, DQ2),
    ]

    data_to_present = {
        'APL': results_sign[0],
        'BPL': results_sign[1]
    }

    return data_to_present



def BackwardClassStatus():
    Client_Cloud = pymongo.MongoClient('mongodb+srv://ravindraacharya0512:Iwilltakeovertheworld123@cluster0.ynaiaut.mongodb.net/')
    MainDB = Client_Cloud['MainB']
    MainDB_Coll = MainDB['CollDB']
    total_documents = MainDB_Coll.count_documents({})
    return


def NumberOfResidence():
    Client_Cloud = pymongo.MongoClient('mongodb+srv://ravindraacharya0512:Iwilltakeovertheworld123@cluster0.ynaiaut.mongodb.net/')
    MainDB = Client_Cloud['MainB']
    MainDB_Coll = MainDB['CollDB']
    total_documents = MainDB_Coll.count_documents({})
    return


def Diseases_Analytics():
    Client_Cloud = pymongo.MongoClient('mongodb+srv://ravindraacharya0512:Iwilltakeovertheworld123@cluster0.ynaiaut.mongodb.net/')
    MainDB = Client_Cloud['MainB']
    MainDB_Coll = MainDB['CollDB']
    total_documents = MainDB_Coll.count_documents({})
    return


def GroupByHML(To_grp):
    grping_formatt = {
        'DEREBAIL NAIRUTHYA': {
            'EmploymentStatus': {
                'S': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'W': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'O': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'T': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                }
            },

            'EconomicStatus': {
                'S': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'W': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'O': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'T': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                }
            },

            'HealthStatus': {
                'S': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },

                'W': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },

                'O': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'T': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                }
            },

            'HomeType': {
                'S': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'W': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'O': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'T': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                }
            },

            'Education': {
                'S': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'W': {

                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'O': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'T': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                }
            }
        },

        'BEJAI': {
            'EmploymentStatus': {
                'S': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'W': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'O': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'T': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                }
            },

            'EconomicStatus': {
                'S': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'W': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'O': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'T': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                }
            },

            'HealthStatus': {
                'S': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },

                'W': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },

                'O': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'T': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                }
            },

            'HomeType': {
                'S': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'W': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'O': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'T': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                }
            },

            'Education': {
                'S': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'W': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'O': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'T': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                }
            }
        }
    }

    for kk6, vv6 in To_grp.item():
        for k4, v4 in vv6.items():
            for k5, v5 in v4.items():
                for datas in v5:
                    for k6, v6 in datas.items():
                        getHML = v6.get('HML')
                        grping_formatt[kk6][k4][k5][getHML].append(datas)

    return grping_formatt


def GroupBySWOT(To_grp):
    grping_format = {
        'DEREBAIL NAIRUTHYA': {
            'EmploymentStatus': {
                'S': [],
                'W': [],
                'O': [],
                'T': []
            },

            'EconomicStatus': {
                'S': [],
                'W': [],
                'O': [],
                'T': []
            },

            'HealthStatus': {
                'S': [],
                'W': [],
                'O': [],
                'T': []
            },

            'HomeType': {
                'S': [],
                'W': [],
                'O': [],
                'T': []
            },

            'Education': {
                'S': [],
                'W': [],
                'O': [],
                'T': []
            }
        },

        'BEJAI': {
            'EmploymentStatus': {
                'S': [],
                'W': [],
                'O': [],
                'T': []
            },

            'EconomicStatus': {
                'S': [],
                'W': [],
                'O': [],
                'T': []
            },

            'HealthStatus': {
                'S': [],
                'W': [],
                'O': [],
                'T': []
            },

            'HomeType': {
                'S': [],
                'W': [],
                'O': [],
                'T': []
            },

            'Education': {
                'S': [],
                'W': [],
                'O': [],
                'T': []
            }
        }
    }

    for kk5, vv5 in To_grp.items():
        for k2, v2 in vv5.items():
            for values in v2:
                for k3, v3 in values.items():
                    if isinstance(v3.get('SWOT'), str):
                        get_value = v3.get('SWOT')
                        grping_format[kk5][k2][get_value].append(values)
                    elif isinstance(v3.get('SWOT'), tuple):
                        get_value1 = v3.get('SWOT')
                        for ele in get_value1:
                            grping_format[kk5][k2][ele].append(values)

    return grping_format


def Group_based_on_five_ele(To_Group):
    grping_format = {
        'DEREBAIL NAIRUTHYA': {
            'EmploymentStatus': [],
            'EconomicStatus': [],
            'HealthStatus': [],
            'HomeType': [],
            'Education': []
        },
        'BEJAI': {
            'EmploymentStatus': [],
            'EconomicStatus': [],
            'HealthStatus': [],
            'HomeType': [],
            'Education': []
        }
    }
    for kk1, vv1 in To_Group.items():
        for queries in vv1:
            for k3, v3 in queries.items():
                data_dict2 = ast.literal_eval(k3)
                if 'EmploymentStatus' in data_dict2:
                    data_dict3 = {str(data_dict2): v3}
                    grping_format[kk1]['EmploymentStatus'].append(data_dict3)
                elif 'EconomicStatus' in data_dict2:
                    data_dict3 = {str(data_dict2): v3}
                    grping_format[kk1]['EconomicStatus'].append(data_dict3)
                elif 'HealthStatus' in data_dict2:
                    data_dict3 = {str(data_dict2): v3}
                    grping_format[kk1]['HealthStatus'].append(data_dict3)
                elif 'HomeType' in data_dict2:
                    data_dict3 = {str(data_dict2): v3}
                    grping_format[kk1]['HomeType'].append(data_dict3)
                elif 'Education' in data_dict2:
                    data_dict3 = {str(data_dict2): v3}
                    grping_format[kk1]['Education'].append(data_dict3)
    return grping_format


def collect_SWOT_data():
    Client_Cloud = pymongo.MongoClient('mongodb+srv://ravindraacharya0512:Iwilltakeovertheworld123@cluster0.ynaiaut.mongodb.net/')
    MainDB = Client_Cloud['FrontendData']

    bejai_collection = MainDB['BEJAI']
    derebail_collection = MainDB['DEREBAIL NAIRUTHYA']

    bejai_data = list(bejai_collection.find())
    derebail_data = list(derebail_collection.find())

    data_format = {
        'BEJAI': bejai_data,
        'DEREBAIL NAIRUTHYA': derebail_data
    }

    getColl = data_format
    print('Data--------', getColl)
    return getColl


def HomePageAnalytics():
    Client_Cloud = pymongo.MongoClient('mongodb+srv://ravindraacharya0512:Iwilltakeovertheworld123@cluster0.ynaiaut.mongodb.net/')
    MainDB = Client_Cloud['MainB']
    MainDB_Coll = MainDB['CollDB']
    total_documents = MainDB_Coll.count_documents({})
    prev_emp = 9632
    prev_unemp = 4436
    prev_ed = 7966
    prev_uned = 9562
    prev_hea = 15855
    prev_dis = 3025
    prev_rent = 11565
    prev_own = 11015
    prev_ap = 10236
    prev_bp = 6827

    queries = [
        {'EmploymentStatus': 'Employed'},
        {'EmploymentStatus': 'UnEmployed'},
        {'Education': 'Educated'},
        {'Education': 'Uneducated'},
        {'HealthStatus': 'Healthy'},
        {'HealthStatus': 'Diseased'},
        {'HomeType': 'Rent'},
        {'HomeType': 'Own'},
        {'EconomicStatus': 'APL'},
        {'EconomicStatus': 'BPL'}
    ]
    results = [MainDB_Coll.count_documents(q) for q in queries]
    get_emp, get_unemp, get_ed, get_uned, get_hea, get_unhea, get_rent, get_own, get_apl, get_bpl = results

    percentages = [count / total_documents * 100 for count in results]
    get_emp_per, get_unemp_per, get_ed_per, get_uned_per, get_hea_per, get_unhea_per, get_rent_per, get_own_per, get_apl_per, get_bpl_per = percentages

    labels = [
        comparison(get_emp_per, get_unemp_per),
        comparison(get_ed_per, get_uned_per),
        comparison(get_hea_per, get_unhea_per),
        comparison(get_rent_per, get_own_per),
        comparison(get_apl_per, get_bpl_per)
    ]

    emp_LB, Unemp_LB = labels[0]
    ed_LB, Uned_LB = labels[1]
    hea_LB, unhea_LB = labels[2]
    rent_LB, own_LB = labels[3]
    apl_LB, bpl_LB = labels[4]

    increments = [
        (get_emp - prev_emp) / get_emp * 100,
        (get_unemp - prev_unemp) / get_unemp * 100,
        (get_ed - prev_ed) / get_ed * 100,
        (get_uned - prev_uned) / get_uned * 100,
        (get_hea - prev_hea) / get_hea * 100,
        (get_unhea - prev_dis) / get_unhea * 100,
        (get_rent - prev_rent) / get_rent * 100,
        (get_own - prev_own) / get_own * 100,
        (get_apl - prev_ap) / get_apl * 100,
        (get_bpl - prev_bp) / get_bpl * 100
    ]

    results_sign = [
        check_integer(increments[0], get_emp, emp_LB),
        check_integer(increments[1], get_unemp, Unemp_LB),
        check_integer(increments[2], get_ed, ed_LB),
        check_integer(increments[3], get_uned, Uned_LB),
        check_integer(increments[4], get_hea, hea_LB),
        check_integer(increments[5], get_unhea, unhea_LB),
        check_integer(increments[6], get_rent, rent_LB),
        check_integer(increments[7], get_own, own_LB),
        check_integer(increments[8], get_apl, apl_LB),
        check_integer(increments[9], get_bpl, bpl_LB)
    ]

    data_to_display = {
        'EmploymentStatus': {
            'Employed': results_sign[0],
            'UnEmployed': results_sign[1]
        },
        'Education': {
            'Educated': results_sign[2],
            'Uneducated': results_sign[3]
        },
        'HealthStatus': {
            'Healthy': results_sign[4],
            'Diseased': results_sign[5]
        },
        'HomeType': {
            'Rent': results_sign[6],
            'Own': results_sign[7]
        },
        'EconomicStatus': {
            'APL': results_sign[8],
            'BPL': results_sign[9]
        }
    }
    print(data_to_display)
    return data_to_display


def GroupByHML(To_grp):
    grping_formatt = {
        'DEREBAIL NAIRUTHYA': {
            'EmploymentStatus': {
                'S': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'W': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'O': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'T': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                }
            },

            'EconomicStatus': {
                'S': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'W': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'O': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'T': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                }
            },

            'HealthStatus': {
                'S': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },

                'W': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },

                'O': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'T': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                }
            },

            'HomeType': {
                'S': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'W': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'O': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'T': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                }
            },

            'Education': {
                'S': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'W': {

                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'O': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'T': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                }
            }
        },

        'BEJAI': {
            'EmploymentStatus': {
                'S': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'W': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'O': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'T': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                }
            },

            'EconomicStatus': {
                'S': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'W': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'O': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'T': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                }
            },

            'HealthStatus': {
                'S': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },

                'W': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },

                'O': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'T': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                }
            },

            'HomeType': {
                'S': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'W': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'O': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'T': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                }
            },

            'Education': {
                'S': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'W': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'O': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                },
                'T': {
                    'HA': [],
                    'HB': [],
                    'HC': [],
                    'HD': [],
                    'MA': [],
                    'MB': [],
                    'MC': [],
                    'LA': [],
                    'LB': [],
                    'LC': []
                }
            }
        }
    }

    for kk6, vv6 in To_grp.items():
        for k4, v4 in vv6.items():
            for k5, v5 in v4.items():
                for datas in v5:
                    for k6, v6 in datas.items():
                        getHML = v6.get('HML')
                        grping_formatt[kk6][k4][k5][getHML].append(datas)

    return grping_formatt


def GroupBySWOT(To_grp):
    grping_format = {
        'DEREBAIL NAIRUTHYA': {
            'EmploymentStatus': {
                'S': [],
                'W': [],
                'O': [],
                'T': []
            },

            'EconomicStatus': {
                'S': [],
                'W': [],
                'O': [],
                'T': []
            },

            'HealthStatus': {
                'S': [],
                'W': [],
                'O': [],
                'T': []
            },

            'HomeType': {
                'S': [],
                'W': [],
                'O': [],
                'T': []
            },

            'Education': {
                'S': [],
                'W': [],
                'O': [],
                'T': []
            }
        },

        'BEJAI': {
            'EmploymentStatus': {
                'S': [],
                'W': [],
                'O': [],
                'T': []
            },

            'EconomicStatus': {
                'S': [],
                'W': [],
                'O': [],
                'T': []
            },

            'HealthStatus': {
                'S': [],
                'W': [],
                'O': [],
                'T': []
            },

            'HomeType': {
                'S': [],
                'W': [],
                'O': [],
                'T': []
            },

            'Education': {
                'S': [],
                'W': [],
                'O': [],
                'T': []
            }
        }
    }

    for kk5, vv5 in To_grp.items():
        for k2, v2 in vv5.items():
            for values in v2:
                for k3, v3 in values.items():
                    if isinstance(v3.get('SWOT'), str):
                        get_value = v3.get('SWOT')
                        grping_format[kk5][k2][get_value].append(values)
                    elif isinstance(v3.get('SWOT'), tuple):
                        get_value1 = v3.get('SWOT')
                        for ele in get_value1:
                            grping_format[kk5][k2][ele].append(values)

    return grping_format


def reorder_dict(to_be_first, data):
    if to_be_first not in data:
        raise KeyError(f"The key '{to_be_first}' is not in the dictionary")

    ordered_data = {}

    for key in list(data.keys()):
        if key == to_be_first:
            ordered_data[to_be_first] = data[to_be_first]
            break

    for key in list(data.keys()):
        if key != to_be_first:
            ordered_data[key] = data[key]

    ordered_data = dict(ordered_data)

    return ordered_data


def Group_based_on_five_ele(To_Group):
    grping_format = {
        'DEREBAIL NAIRUTHYA': {
            'EmploymentStatus': [],
            'EconomicStatus': [],
            'HealthStatus': [],
            'HomeType': [],
            'Education': []
        },
        'BEJAI': {
            'EmploymentStatus': [],
            'EconomicStatus': [],
            'HealthStatus': [],
            'HomeType': [],
            'Education': []
        }
    }

    for kk1, vv1 in To_Group.items():
        for queries in vv1:
            for k3, v3 in queries.items():
                data_dict2 = ast.literal_eval(k3)
                if 'EmploymentStatus' in data_dict2:
                    data_dict2 = reorder_dict('EmploymentStatus', data_dict2)
                    data_dict3 = {str(data_dict2): v3}
                    grping_format[kk1]['EmploymentStatus'].append(data_dict3)
                if 'EconomicStatus' in data_dict2:
                    data_dict2 = reorder_dict('EconomicStatus', data_dict2)
                    data_dict3 = {str(data_dict2): v3}
                    grping_format[kk1]['EconomicStatus'].append(data_dict3)
                if 'HealthStatus' in data_dict2:
                    data_dict2 = reorder_dict('HealthStatus', data_dict2)
                    data_dict3 = {str(data_dict2): v3}
                    grping_format[kk1]['HealthStatus'].append(data_dict3)
                if 'HomeType' in data_dict2:
                    data_dict2 = reorder_dict('HomeType', data_dict2)
                    data_dict3 = {str(data_dict2): v3}
                    grping_format[kk1]['HomeType'].append(data_dict3)
                if 'Education' in data_dict2:
                    data_dict2 = reorder_dict('Education', data_dict2)
                    data_dict3 = {str(data_dict2): v3}
                    grping_format[kk1]['Education'].append(data_dict3)
    return grping_format


def CollectDataStore():
    Client_Cloud = pymongo.MongoClient('mongodb+srv://ravindraacharya0512:Iwilltakeovertheworld123@cluster0.ynaiaut.mongodb.net/')
    MainDB = Client_Cloud['FrontendEnd2']
    Client_Cloud1 = pymongo.MongoClient('mongodb+srv://ravindraacharya0512:Iwilltakeovertheworld123@cluster0.ynaiaut.mongodb.net/')
    MainDB1 = Client_Cloud1['MainB']
    DataCollection = MainDB1['CollDB']
    Bejai_collection = MainDB['BEJAI']
    bejai_data = list(Bejai_collection.find())
    derebail_collection = MainDB['DEREBAIL NAIRUTHYA']
    derebail_data = list(derebail_collection.find())

    def remove_id_key(data):
        for record in data:
            if '_id' in record:
                del record['_id']
        return data

    bejai_data = remove_id_key(bejai_data)
    derebail_data = remove_id_key(derebail_data)

    data_format = {
        'BEJAI': bejai_data,
        'DEREBAIL NAIRUTHYA': derebail_data
    }

    getColl = data_format
    return getColl


def totalVoters(ward):
    Client_Cloud1 = pymongo.MongoClient('mongodb+srv://ravindraacharya0512:Iwilltakeovertheworld123@cluster0.ynaiaut.mongodb.net/')
    MainDB = Client_Cloud1['MainB']
    DataCollection = MainDB['CollDB']
    data_ref1 = {
        'BEJAI' : 9365,
        'DEREBAIL NAIRUTHYA': 6145
    }

    data_ref2 = {
        'BEJAI' : 1025,
        'DEREBAIL NAIRUTHYA': 568
    }


    query1 = {'WARD':ward, 'AGE': {'$gte': 18}}
    query2 = {'WARD':ward, 'AGE': {'$lt': 18}}
    count1 = DataCollection.count_documents(query1)
    count2 = DataCollection.count_documents(query2)
    inc1 = (count1 - data_ref1[ward]) / count1 * 100
    inc2 = (count2 - data_ref2[ward]) / count2 * 100
    pos_neg1 = check_integer2(inc1, count1)
    pos_neg2= check_integer2(inc2, count2)
    data_to_present1 = {
        'Total voters' : pos_neg1
    }
    data_to_present2 = {
        'Total below 18 years' : pos_neg2
    }
    return data_to_present1, data_to_present2



def ChatAI_1(user_input, file):
    sys.stdout.reconfigure(encoding='utf-8')
    load_dotenv()
    data = pd.read_csv(file, encoding='ISO-8859-1')
    llm = ChatGroq(
        model_name="mixtral-8x7b-32768",
        api_key="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"
    )
    df = SmartDataframe(data, config={'llm': llm})
    modify_prom = user_input
    prompt_op = df.chat(modify_prom)
    if isinstance(prompt_op, pd.DataFrame):
        file_path = 'Download.xlsx'
        prompt_op.to_excel(file_path, index=False)
        return {'type': 'file', 'path': file_path}
    elif isinstance(prompt_op, (int, float)):
        prompt_op = str(prompt_op)
    return {'type': 'text', 'result': prompt_op}


def ChatAI(user_input):
    sys.stdout.reconfigure(encoding='utf-8')
    load_dotenv()
    data = pd.read_csv('\Data\MainB.csv', encoding='ISO-8859-1')
    llm = ChatGroq(
        model_name='mixtral-8x7b-32768',
        api_key="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"
    )

    df = SmartDataframe(data, config={'llm': llm})
    modify_prom = user_input
    prompt_op = df.chat(modify_prom)
    if isinstance(prompt_op, pd.DataFrame):
        file_path = 'Download.xlsx'
        prompt_op.to_excel(file_path, index=False)
        return {'type': 'file', 'path': file_path}
    elif isinstance(prompt_op, (int, float)):
        prompt_op = str(prompt_op)
    return {'type': 'text', 'result': prompt_op}



def is_sublist_in_list(main_list, sublist):
    for existing_sublist in main_list:
        if len(existing_sublist) == len(sublist) and all(item in existing_sublist for item in sublist):
            return True
    return False


def getCounts(list_queries):
    conn = pymongo.MongoClient('mongodb+srv://ravindraacharya0512:Iwilltakeovertheworld123@cluster0.ynaiaut.mongodb.net/')
    dbase = conn['MainB']
    count_collection = dbase['CollDB']
    first_stage = []
    for sqBrac1 in list_queries:
        sec_stage = []
        for sqBrac2 in sqBrac1:
            get_freq = count_collection.count_documents(sqBrac2)
            data_dic = {get_freq : sqBrac2}
            sec_stage.append(data_dic)
        first_stage.append(sec_stage)         
    return first_stage

def remove_queries(queries, removable_queries):
    filtered_queries = []
    for query_list in queries:
        filtered_query_list = []
        for query in query_list:
            remove = False
            for r in removable_queries:
                if list(r.items())[0] in list(query.items()):
                    remove = True
                    break
            if not remove:
                filtered_query_list.append(query)
        filtered_queries.append(filtered_query_list)
    return filtered_queries


exclusion_criteria = [
                ['Wstudent', 'Uneducated'],
                ['Wstudent', 'UnEmployed'],
                ['Educated', 'Kindergarten'],
                ['Educated', 'Bachelors', 'Minor'],
                ['Educated', 'Masters', 'Minor'],
                ['Educated', 'Higher Primary', 'Minor'],
                ['Educated', 'Lower Primary', 'Minor'],
                ['Educated', 'High School', 'Minor'],
                ['Educated', 'PUC', 'Minor'],
                ['Educated', 'SSLC', 'Minor'],
                ['Educated', 'College Diploma', 'Minor'],
                ['Wstudent', 'Employed'],
                ['Wstudent', 'Married'],
                ['Wstudent', 'Widow'],
                ['Wstudent', 'SelfEmp'],
                ['Wstudent', 'Private'],
                ['Wstudent', 'Government'],
                ['Employed', 'Minor'],
                ['UnEmployed', 'Minor'],
                ['UnEmployed', 'Private'],
                ['UnEmployed', 'Government'],
                ['UnEmployed', 'SelfEmp']
            ]



def label_percentage(percentage):
    if 90 < percentage <= 100:
        return 'HA'
    elif 80 < percentage <= 90:
        return 'HB'
    elif 70 < percentage <= 80:
        return 'HC'
    elif 60 < percentage <= 70:
        return 'HD'
    elif 50 < percentage <= 60:
        return 'MA'
    elif 40 < percentage <= 50:
        return 'MB'
    elif 30 < percentage <= 40:
        return 'MC'
    elif 20 < percentage <= 30:
        return 'LA'
    elif 10 < percentage <= 20:
        return 'LB'
    elif 0 <= percentage <= 10:
        return 'LC'
        

def find_key(query_value):
        dict_info = {'WARD':['BEJAI', 'DEREBAIL NAIRUTHYA'],
            'Gender': ['Male', 'Female'],
            'EconomicStatus': ['APL', 'BPL'],
            'EmploymentStatus': ['Employed', 'UnEmployed', 'Minor'],
            'EmploymentType': ['Private', 'Government', 'SelfEmp', 'Minor'],
            'Religion': ['Hindu', 'Muslim', 'Christian', 'Jain', 'Buddhist', 'Sikh'],
            'Community': ['GC', 'OBC', 'SC', 'ST'],
            'SubCategory': ['2A', '2B', '2C'],
            'HomeType': ['Rent', 'Own'],
            'HealthStatus': ['Healthy', 'Diseased'],
            'PhysicalStatus': ['Handicapped', 'NonHandicapped'],
            'MaritalStatus': ['Married', 'Single', 'Widow'],
            'Education': ['Educated', 'Uneducated', 'Wstudent'],
            'EducationType': [
				        'Kindergarten',
						'Higher Primary', 
						'Lower Primary', 
						'High School', 
						'PUC', 
						'SSLC', 
						'College Diploma', 
						'Bachelors', 
						'Masters'],
			'DiseaseType' : [
				       'Asthma',
					   'Bird flu virus',
					   'Dengue', 
					   'Rabies',
					   'Malaria',
					   'Diabetes', 
					   'Heart disease', 
					   'Lung disease', 
					   'Cancer', 
					   'Liver disease', 
					   'kidney disease',
					   'Nipha', 
					   'ZIKA', 
					   'Corona virus', 
					   'Respiratory infection', 
					   'Pneumonia', 
					   'Mental disorder', 
					   ]
        }


        for key_c, values in dict_info.items():
            for value_h in values:
                if difflib.SequenceMatcher(None, query_value, value_h).ratio() >= 0.7:
                    return key_c
        return None


def encode_str(data_, val):
        print(data_)
        print(val)
        layer_dict = {}
        Encoding_numbers = {
            'Male': 1,
            'Female': 11,
            'APL': 1,
            'BPL': 11,
            'Employed': 1,
            'UnEmployed': 11,
            'Minor':11001,
            'Private': 1,
            'Government': 11,
            'SelfEmp': 111,
            
            'Hindu': 1,
            'Muslim': 11,
            'Christian': 111,
            'Jain': 1111,
            'Sikh': 10000,
            'Buddhist': 11111,
            'OBC': 1111,
            'GC': 1,
            'SC': 11,
            'ST': 111,
            '2A': 1,
            '2B': 11,
            '2C': 111,
            'Rent': 1,
            'Own': 11,
            'Married': 1,
            'Single': 11,
            'Widow': 111,
            'Healthy': 1,
            'Diseased': 11,
            'Handicapped': 1,
            'NonHandicapped': 11,
            'Educated': 1,
            'Uneducated': 11,
            'Wstudent': 111,
            'Kindergarten': 11100,
            'Higher Primary': 11,
            'Lower Primary': 111,
            'High School': 1,
            'PUC': 1111,
            'SSLC': 11110,
            'College Diploma': 11111,
            'Bachelors': 10000,
            'Masters': 11000,
            'HA': 1,
            'HB': 11,
            'HC': 111,
            'HD': 1111,
            'MA': 11111,
            'MB': 10000,
            'MC': 11000,
            'LA': 11100,
            'LB': 11110,
            'LC': 10111
        }

        Classification_encode = {
            1: ('S'),
            11: ('S', 'O'),
            111: ('T'),
            1111: ('W'),
            11111: ('W', 'O'),
            10000: ('W', 'T')
        }

        columns = [
            'EmploymentStatus',
            'EmploymentType',
            'Gender',
            'EconomicStatus',
            'HomeType',
            'HealthStatus',
            'PhysicalStatus',
            'MaritalStatus',
            'Religion',
            'Community',
            'SubCategory',
            'Education',
            'EducationType',
            'HML'
        ]

        df = pd.DataFrame(columns=columns)
        main = []
        for x in data_:
            fetch_k = find_key(x)
            main.append(fetch_k)
        print(main)
        store_ = tuple(main)
        print(store_)
        data_dict = {store_[i]: Encoding_numbers[data_[i]] for i in range(len(store_))}
        df = df._append(data_dict, ignore_index=True)
        df['HML'] = Encoding_numbers[val]
        df = df.astype(float)

        with open('New_Model_decisionTree1.pkl', 'rb') as file:
            clf = pickle.load(file)

        predictions = clf.predict(df)
        get_pred = predictions[0]
        get_pred_val = Classification_encode[get_pred]

        return get_pred_val



def Calculate_percentage(list_queries):
    
    for sqbrac1 in list_queries:
        values_list = [list(d.values())[0] for d in sqbrac1]

        counts = [list(item.keys())[0] for item in sqbrac1]

        total_sum = sum(counts)
        
        percentages = [(count / total_sum) * 100 for count in counts]

        labels = [label_percentage(percentage) for percentage in percentages]

        return percentages, counts, values_list, labels


def remove_element_by_name(tup, element_name):
        return tuple(item for item in tup if item != element_name)

def GetDataFromDB(ListOfVar, connection):
    grping_formatt2 = {
            'DEREBAIL NAIRUTHYA': {
                'EmploymentStatus': {
                    'S': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'W': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'O': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'T': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    }
                },

                'EconomicStatus': {
                    'S': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'W': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'O': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'T': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    }
                },

                'HealthStatus': {
                    'S': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },

                    'W': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },

                    'O': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'T': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    }
                },

                'HomeType': {
                    'S': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'W': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'O': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'T': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    }
                },

                'Education': {
                    'S': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'W': {

                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'O': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'T': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    }
                }
            },

            'BEJAI': {
                'EmploymentStatus': {
                    'S': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'W': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'O': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'T': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    }
                },

                'EconomicStatus': {
                    'S': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'W': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'O': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'T': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    }
                },

                'HealthStatus': {
                    'S': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },

                    'W': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },

                    'O': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'T': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    }
                },

                'HomeType': {
                    'S': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'W': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'O': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'T': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    }
                },

                'Education': {
                    'S': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'W': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'O': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    },
                    'T': {
                        'HA': [],
                        'HB': [],
                        'HC': [],
                        'HD': [],
                        'MA': [],
                        'MB': [],
                        'MC': [],
                        'LA': [],
                        'LB': [],
                        'LC': []
                    }
                }
            }
        }


    for variables in ListOfVar:
        if variables == 'BEJAIy':
            ward = 'BEJAI'
            database = connection[variables]
            collection_names = database.list_collection_names()
            for collection_name in collection_names:
                collection = database[collection_name]
                cursor = collection.find()
            
                for Doc in cursor:
                    del Doc['_id']

                    for key, value in Doc.items():
                       
                        getHML = value['HML_Label']
                        getSWOT = value['SWOT']
                        if isinstance(getSWOT, list): 
                            for catg in getSWOT:
                                grping_formatt2[ward][collection_name][catg][getHML].append(Doc)
                        else:
                            grping_formatt2[ward][collection_name][getSWOT][getHML].append(Doc)

        else:
            ward = 'DEREBAIL NAIRUTHYA'
            database = connection[variables]
            collection_names = database.list_collection_names()
            for collection_name in collection_names:
                collection = database[collection_name]
                cursor = collection.find()
            
                for Doc in cursor:
                    del Doc['_id']
                    
                    for key, value in Doc.items():
                       
                        getHML = value['HML_Label']
                        getSWOT = value['SWOT']
                        if isinstance(getSWOT, list): 
                            for catg in getSWOT:
                                grping_formatt2[ward][collection_name][catg][getHML].append(Doc)
                        else:
                            grping_formatt2[ward][collection_name][getSWOT][getHML].append(Doc)
                    
                    

    return grping_formatt2


def is_invalid_combination(query):
    return (
        (query.get('Education') == 'Educated' and query.get('EducationType') == 'Kindergarten') or
        (query.get('Education') == 'Educated' and query.get('EducationType') == 'Bachelors' and query.get('EmploymentStatus') == 'Minor') or 
        (query.get('Education') == 'Educated' and query.get('EducationType') == 'Masters' and query.get('EmploymentStatus') == 'Minor') or
        (query.get('Education') == 'Wstudent' and query.get('EmploymentStatus') == 'Employed') 
    )

def Compar(conv_dict):
    dict_info = {'WARD':['BEJAI', 'DEREBAIL NAIRUTHYA'],
            'Gender': ['Male', 'Female'],
            'EconomicStatus': ['APL', 'BPL'],
            'EmploymentStatus': ['Employed', 'UnEmployed', 'Minor'],
            'EmploymentType': ['Private', 'Government', 'SelfEmp', 'Minor'],
            'Religion': ['Hindu', 'Muslim', 'Christian', 'Jain', 'Buddhist', 'Sikh'],
            'Community': ['GC', 'OBC', 'SC', 'ST'],
            'SubCategory': ['2A', '2B', '2C'],
            'HomeType': ['Rent', 'Own'],
            'HealthStatus': ['Healthy', 'Diseased'],
            'PhysicalStatus': ['Handicapped', 'NonHandicapped'],
            'MaritalStatus': ['Married', 'Single', 'Widow'],
            'Education': ['Educated', 'Uneducated', 'Wstudent'],
            'EducationType': [
				        'Kindergarten',
						'Higher Primary', 
						'Lower Primary', 
						'High School', 
						'PUC', 
						'SSLC', 
						'College Diploma', 
						'Bachelors', 
						'Masters']
        }
    
    last_key, last_value = list(conv_dict.items())[-1]
    possible_values = dict_info.get(last_key, [])
    
    result1 = [
        {**conv_dict, last_key: value}
        for value in possible_values if value != last_value
        if not is_invalid_combination({**conv_dict, last_key: value})
    ]
    
    if not is_invalid_combination(conv_dict):
        result1.append(conv_dict)
                
    return result1


def ComparAnalytics(getComparables, ward_name, MainDB_Coll):
    warddocum = {'WARD':ward_name}
    storewardcomb = []
    for quries in getComparables:
        combine2 = {**warddocum, **quries}
        getcount_ = MainDB_Coll.count_documents(combine2)
        data_to_push = {str(combine2) : getcount_}
        storewardcomb.append(data_to_push)


    Counts = []
    for Queries in storewardcomb:
        getVal = list(Queries.values())[0]
        Counts.append(getVal)
    sum_counts = sum(Counts)

    store_data_for_anal = []
    for Queries2 in storewardcomb:
        getQuery = list(Queries2.keys())[0]
        conv_dict = ast.literal_eval(getQuery)
        getVal = list(Queries2.values())[0]
        percent = getVal/sum_counts*100
        percent = round(percent, 2)
        getLabel = label_percentage(percent)
        GroupData = {'data': {'Query':conv_dict, 'Count':getVal, 'Percentage':percent, 'HML':getLabel}}
        store_data_for_anal.append(GroupData)
    return store_data_for_anal





def test(data):
    for k1, v1 in data.items():
        if k1=='EmploymentStatus':
            for k2, v2 in v1.items():
                print(k2)
                for k3, v3 in v2.items():
                    print(k3)
                    for data in v3[:10]:
                        print(data)



def mainFunc():
    GetHomePge_Analytics = HomePageAnalytics()
    return GetHomePge_Analytics


def OTH_pred(totalOTH, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': totalOTH
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_



def INC_pred(totalBJP, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': totalBJP
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_



def BJP_pred(totalBJP, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': totalBJP
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_


def margin_pred(totalMargin, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': totalMargin
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_


def Total_pollers_pred(totalP, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': totalP
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_

def Total_voters_pred(totalV, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': totalV
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_



def TVincrpred(totalV, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': totalV
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_



def TVincrPerpred(totalV, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': totalV
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_



def TPincrpred(totalV, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': totalV
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_


def TPincrPerpred(totalV, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': totalV
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_









def OTH_pred_mp(totalOTH, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': totalOTH
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2029, 2034)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2029, 'Forecasted_Polling']
  return pred_



def INC_pred_mp(totalBJP, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': totalBJP
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2029, 2034)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2029, 'Forecasted_Polling']
  return pred_



def BJP_pred_mp(totalBJP, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': totalBJP
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2029, 2034)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2029, 'Forecasted_Polling']
  return pred_


def margin_pred_mp(totalMargin, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': totalMargin
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2029, 2034)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2029, 'Forecasted_Polling']
  return pred_


def Total_pollers_pred_mp(totalP, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': totalP
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2029, 2034)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2029, 'Forecasted_Polling']
  return pred_

def Total_voters_pred_mp(totalV, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': totalV
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2029, 2034)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2029, 'Forecasted_Polling']
  return pred_



def TVincrpred_mp(totalV, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': totalV
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2029, 2034)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2029, 'Forecasted_Polling']
  return pred_



def TVincrPerpred_mp(totalV, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': totalV
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2029, 2034)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2029, 'Forecasted_Polling']
  return pred_



def TPincrpred_mp(totalV, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': totalV
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2029, 2034)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2029, 'Forecasted_Polling']
  return pred_


def TPincrPerpred_mp(totalV, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': totalV
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2029, 2034)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2029, 'Forecasted_Polling']
  return pred_



def prediction_process(data):
  get_years = data['Year'].tolist()
  get_TV = data['Total voters'].tolist()
  get_TP = data['Total polled'].tolist()
  get_TP_per = data['Total polling %'].tolist()
  get_MARGIN = data['MARGIN'].tolist()

  get_BJP = data['BJP POLL'].tolist()
  get_BJP_per = data['BJP POLL%'].tolist()
  get_BJP_incr = data['BJP INCR RATIO'].tolist()
  get_BJP_incr_per = data['BJP INCR RATIO%'].tolist()

  get_INC = data['INC POLL'].tolist()
  get_INC_per = data['INC POLL%'].tolist()
  get_INC_incr = data['INC INCR RATIO'].tolist()
  get_INC_incr_per = data['INC INCR RATIO%'].tolist()

  get_OTH = data['OTH POLL'].tolist()
  get_OTH_per = data['OTH POLL%'].tolist()
  get_OTH_incr = data['OTH INCR RATIO'].tolist()
  get_OTH_incr_per = data['OTH INCR RATIO%'].tolist()

  get_TVincr = data['Voting Increment Ratio'].tolist()
  get_TVincrPer = data['Voting Increment Ratio %'].tolist()
  get_TPincr = data['Polling Increment Ratio'].tolist()
  get_TPincrPer = data['Polling Increment Ratio %'].tolist()

  return get_TV,  get_TVincr, get_TVincrPer, get_TP, get_TP_per, get_TPincr, get_TPincrPer, get_MARGIN, get_BJP, get_BJP_per, get_BJP_incr, get_BJP_incr_per, get_INC, get_INC_per, get_INC_incr, get_INC_incr_per, get_OTH, get_OTH_per, get_OTH_incr, get_OTH_incr_per, get_years



def FuncTP_per_mla(tp_per, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': tp_per
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_



def FuncBJP_per_mla(BJP_per_mla, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': BJP_per_mla
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_


def FuncBJP_incr_mla(BJP_incr_mla, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': BJP_incr_mla
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_


def FuncBJP_incr_per_mla(BJP_incr_per_mla, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': BJP_incr_per_mla
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_


def FuncINC_per_mla(INC_per_mla, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': INC_per_mla
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_


def FuncINC_incr_mla(INC_incr_mla, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': INC_incr_mla
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_


def FuncINC_incr_per_mla(INC_incr_per_mla, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': INC_incr_per_mla
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_



def FuncOTH_per_mla(OTH_per_mla, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': OTH_per_mla
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_


def FuncOTH_incr_mla(OTH_per_mla, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': OTH_per_mla
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_


def FuncOTH_incr_per_mla(OTH_incr_per_mla, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': OTH_incr_per_mla
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_
















def FuncTP_per_mp(tp_per_ml, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': tp_per_ml
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_



def FuncBJP_per_mp(BJP_per_mp, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': BJP_per_mp
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_


def FuncBJP_incr_mp(BJP_incr_mp, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': BJP_incr_mp
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_


def FuncBJP_incr_per_mp(BJP_incr_per_mp, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': BJP_incr_per_mp
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_


def FuncINC_per_mp(INC_per_mp, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': INC_per_mp
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_


def FuncINC_incr_mp(INC_incr_mp, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': INC_incr_mp
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_


def FuncINC_incr_per_mp(INC_incr_per_mp, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': INC_incr_per_mp
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_



def FuncOTH_per_mp(OTH_per_mp, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': OTH_per_mp
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_


def FuncOTH_incr_mp(OTH_per_mp, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': OTH_per_mp
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_


def FuncOTH_incr_per_mp(OTH_incr_per_mp, years_list):
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': OTH_incr_per_mp
                     })
  df = pd.DataFrame(data)
  df.set_index('Year', inplace=True)
  polling_data = df['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(2028, 2033)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[2028, 'Forecasted_Polling']
  return pred_


def Main(category):
    if category == "mla":
        data1 = pd.read_csv('\Data\MLA_TV.csv')
        get_TV_mla,  get_TVincr_mla, get_TVincrPer_mla, get_TP_mla, get_TP_per_mla, get_TPincr_mla, get_TPincrPer_mla, get_MARGIN_mla, get_BJP_mla, get_BJP_per_mla, get_BJP_incr_mla, get_BJP_incr_per_mla, get_INC_mla, get_INC_per_mla, get_INC_incr_mla, get_INC_incr_per_mla, get_OTH_mla, get_OTH_per_mla, get_OTH_incr_mla, get_OTH_incr_per_mla, get_years_mla  = prediction_process(data1)
        Pred_TV_mla = Total_voters_pred(get_TV_mla, get_years_mla)
        Pred_TVincr_mla = TVincrpred(get_TVincr_mla, get_years_mla)
        Pred_TVincrPer_mla = TVincrPerpred(get_TVincrPer_mla, get_years_mla)


        Pred_TP_mla = Total_pollers_pred(get_TP_mla, get_years_mla)
        Pred_TP_per_mla = FuncTP_per_mla(get_TP_per_mla, get_years_mla)
        Pred_TPincr_mla = TPincrpred(get_TPincr_mla, get_years_mla)
        Pred_TPincrPer_mla = TPincrPerpred(get_TPincrPer_mla, get_years_mla)


        Pred_margin_mla = margin_pred(get_MARGIN_mla, get_years_mla)

        Pred_bjp_mla = BJP_pred(get_BJP_mla, get_years_mla)
        Pred_BJP_per_mla = FuncBJP_per_mla(get_BJP_per_mla, get_years_mla)
        Pred_BJP_incr_mla = FuncBJP_incr_mla(get_BJP_incr_mla, get_years_mla)
        Pred_BJP_incr_per_mla = FuncBJP_incr_per_mla(get_BJP_incr_per_mla, get_years_mla)

        Pred_inc_mla = INC_pred(get_INC_mla, get_years_mla)
        Pred_INC_per_mla = FuncINC_per_mla(get_INC_per_mla, get_years_mla)
        Pred_INC_incr_mla = FuncINC_incr_mla(get_INC_incr_mla, get_years_mla)
        Pred_INC_incr_per_mla = FuncINC_incr_per_mla(get_INC_incr_per_mla, get_years_mla)

        Pred_oth_mla = INC_pred(get_OTH_mla, get_years_mla)
        Pred_OTH_per_mla = FuncOTH_per_mla(get_OTH_per_mla, get_years_mla)
        Pred_OTH_incr_mla = FuncOTH_incr_mla(get_OTH_incr_mla, get_years_mla)
        Pred_OTH_incr_per_mla = FuncOTH_incr_per_mla(get_OTH_incr_per_mla, get_years_mla)

        data_dict_mla = {
            'Year': 2028,
            'Total voters': round(Pred_TV_mla),
            'Voting Increment Ratio': round(Pred_TVincr_mla),
            'Voting Increment Ratio %' : "{:.2f}".format(Pred_TVincrPer_mla),
            'Total polled': round(Pred_TP_mla),
            'Total polling %' : "{:.2f}".format(Pred_TP_per_mla),
            'Polling Increment Ratio' : round(Pred_TPincr_mla),
            'Polling Increment Ratio %' : "{:.2f}".format(Pred_TPincrPer_mla),
            'MARGIN': round(Pred_margin_mla),

            'BJP POLL': round(Pred_bjp_mla),
            'BJP POLL%' : "{:.2f}".format(Pred_BJP_per_mla),
            'BJP INCR RATIO' : round(Pred_BJP_incr_mla),
            'BJP INCR RATIO%':"{:.2f}".format(Pred_BJP_incr_per_mla),

            'INC POLL': round(Pred_inc_mla),
            'INC POLL%' : "{:.2f}".format(Pred_INC_per_mla),
            'INC INCR RATIO' :round(Pred_INC_incr_mla),
            'INC INCR RATIO%' : "{:.2f}".format(Pred_INC_incr_per_mla),

            'OTH POLL': round(Pred_oth_mla),
            'OTH POLL%' : "{:.2f}".format(Pred_OTH_per_mla),
            'OTH INCR RATIO' : round(Pred_OTH_incr_mla),
            'OTH INCR RATIO%' : "{:.2f}".format(Pred_OTH_incr_per_mla)

        }


        new_row_mla = pd.DataFrame([data_dict_mla])
        data1 = pd.concat([data1, new_row_mla], ignore_index=True)
        
        last_two_rows_mla1_voters = data1[['Year', 'Total voters', 'Voting Increment Ratio', 'Voting Increment Ratio %']]
       
        last_two_rows_mla2_polled = data1[['Year', 'Total polled', 'Polling Increment Ratio', 'Polling Increment Ratio %']]
       
        last_two_rows_mla3_bjp = data1[['Year', 'BJP POLL', 'BJP POLL%', 'BJP INCR RATIO', 'BJP INCR RATIO%']]
        
        last_two_rows_mla3_inc = data1[['Year', 'INC POLL', 'INC POLL%', 'INC INCR RATIO', 'INC INCR RATIO%']]
      
        last_two_rows_mla3_oth = data1[['Year', 'OTH POLL', 'OTH POLL%', 'OTH INCR RATIO', 'OTH INCR RATIO%']]
        

        Data_lineChart_mla_voters = data1[['Year', 'Total voters']]
        Data_lineChart_mla_polled = data1[['Year', 'Total polled']]
        Data_lineChart_mla_BJP = data1[['Year', 'BJP POLL']]
        Data_lineChart_mla_INC = data1[['Year', 'INC POLL']]
        Data_lineChart_mla_OTH = data1[['Year', 'OTH POLL']]
        
        getYaxis_mla_voters = Data_lineChart_mla_voters['Year'].tolist()
        getXaxis_mla_voters = Data_lineChart_mla_voters['Total voters'].tolist()

        getYaxis_mla_polled = Data_lineChart_mla_polled['Year'].tolist()
        getXaxis_mla_polled = Data_lineChart_mla_polled['Total polled'].tolist()

        getYaxis_mla_BJP = Data_lineChart_mla_BJP['Year'].tolist()
        getXaxis_mla_BJP = Data_lineChart_mla_BJP['BJP POLL'].tolist()
 
        getYaxis_mla_INC = Data_lineChart_mla_INC['Year'].tolist()
        getXaxis_mla_INC = Data_lineChart_mla_INC['INC POLL'].tolist()

        getYaxis_mla_OTH = Data_lineChart_mla_OTH['Year'].tolist()
        getXaxis_mla_OTH = Data_lineChart_mla_OTH['OTH POLL'].tolist()

        return last_two_rows_mla1_voters, last_two_rows_mla2_polled, last_two_rows_mla3_bjp, last_two_rows_mla3_inc, last_two_rows_mla3_oth, getYaxis_mla_voters, getXaxis_mla_voters, getYaxis_mla_polled, getXaxis_mla_polled, getYaxis_mla_BJP, getXaxis_mla_BJP, getYaxis_mla_INC, getXaxis_mla_INC, getYaxis_mla_OTH, getXaxis_mla_OTH
    


    else:
        data2 = pd.read_csv('\Data\MP_dataset.csv')
        get_TV_mp,  get_TVincr_mp, get_TVincrPer_mp, get_TP_mp, get_TP_per_mp, get_TPincr_mp, get_TPincrPer_mp, get_MARGIN_mp, get_BJP_mp, get_BJP_per_mp, get_BJP_incr_mp, get_BJP_incr_per_mp, get_INC_mp, get_INC_per_mp, get_INC_incr_mp, get_INC_incr_per_mp, get_OTH_mp, get_OTH_per_mp, get_OTH_incr_mp, get_OTH_incr_per_mp, get_years_mp  = prediction_process(data2)
        Pred_TV_mp = Total_voters_pred(get_TV_mp, get_years_mp)
        Pred_TVincr_mp = TVincrpred(get_TVincr_mp, get_years_mp)
        Pred_TVincrPer_mp = TVincrPerpred(get_TVincrPer_mp, get_years_mp)


        Pred_TP_mp = Total_pollers_pred(get_TP_mp, get_years_mp)
        Pred_TP_per_mp = FuncTP_per_mp(get_TP_per_mp, get_years_mp)
        Pred_TPincr_mp = TPincrpred(get_TPincr_mp, get_years_mp)
        Pred_TPincrPer_mp = TPincrPerpred(get_TPincrPer_mp, get_years_mp)

        Pred_margin_mp = margin_pred(get_MARGIN_mp, get_years_mp)

        Pred_bjp_mp = BJP_pred(get_BJP_mp, get_years_mp)
        Pred_BJP_per_mp = FuncBJP_per_mp(get_BJP_per_mp, get_years_mp)
        Pred_BJP_incr_mp = FuncBJP_incr_mp(get_BJP_incr_mp, get_years_mp)
        Pred_BJP_incr_per_mp = FuncBJP_incr_per_mp(get_BJP_incr_per_mp, get_years_mp)

        Pred_inc_mp = INC_pred(get_INC_mp, get_years_mp)
        Pred_INC_per_mp = FuncINC_per_mp(get_INC_per_mp, get_years_mp)
        Pred_INC_incr_mp = FuncINC_incr_mp(get_INC_incr_mp, get_years_mp)
        Pred_INC_incr_per_mp = FuncINC_incr_per_mp(get_INC_incr_per_mp, get_years_mp)

        Pred_oth_mp = INC_pred(get_OTH_mp, get_years_mp)
        Pred_OTH_per_mp = FuncOTH_per_mp(get_OTH_per_mp, get_years_mp)
        Pred_OTH_incr_mp = FuncOTH_incr_mp(get_OTH_incr_mp, get_years_mp)
        Pred_OTH_incr_per_mp = FuncOTH_incr_per_mp(get_OTH_incr_per_mp, get_years_mp)

        data_dict_mp = {
            'Year': 2029,
            'Total voters': round(Pred_TV_mp),
            'Voting Increment Ratio': round(Pred_TVincr_mp),
            'Voting Increment Ratio %' : "{:.2f}".format(Pred_TVincrPer_mp),
            'Total polled': round(Pred_TP_mp),
            'Total polling %' : "{:.2f}".format(Pred_TP_per_mp),
            'Polling Increment Ratio' : round(Pred_TPincr_mp),
            'Polling Increment Ratio %' : "{:.2f}".format(Pred_TPincrPer_mp),
            'MARGIN': round(Pred_margin_mp),

            'BJP POLL': round(Pred_bjp_mp),
            'BJP POLL%' : "{:.2f}".format(Pred_BJP_per_mp),
            'BJP INCR RATIO' : round(Pred_BJP_incr_mp),
            'BJP INCR RATIO%':"{:.2f}".format(Pred_BJP_incr_per_mp),

            'INC POLL': round(Pred_inc_mp),
            'INC POLL%' : "{:.2f}".format(Pred_INC_per_mp),
            'INC INCR RATIO' :round(Pred_INC_incr_mp),
            'INC INCR RATIO%' : "{:.2f}".format(Pred_INC_incr_per_mp),

            'OTH POLL': round(Pred_oth_mp),
            'OTH POLL%' : "{:.2f}".format(Pred_OTH_per_mp),
            'OTH INCR RATIO' : round(Pred_OTH_incr_mp),
            'OTH INCR RATIO%' : "{:.2f}".format(Pred_OTH_incr_per_mp)

        }

        new_row_mp = pd.DataFrame([data_dict_mp])
        data2 = pd.concat([data2, new_row_mp], ignore_index=True)
        last_two_rows_mp1_voters = data2[['Year', 'Total voters', 'Voting Increment Ratio', 'Voting Increment Ratio %']]
        last_two_rows_mp2_polled = data2[['Year', 'Total polled', 'Polling Increment Ratio', 'Polling Increment Ratio %']]
        last_two_rows_mp3_bjp = data2[['Year', 'BJP POLL', 'BJP POLL%', 'BJP INCR RATIO', 'BJP INCR RATIO%']]
        last_two_rows_mp3_inc = data2[['Year', 'INC POLL', 'INC POLL%', 'INC INCR RATIO', 'INC INCR RATIO%']]
        last_two_rows_mp3_oth = data2[['Year', 'OTH POLL', 'OTH POLL%', 'OTH INCR RATIO', 'OTH INCR RATIO%']]

        Data_lineChart_mp_voters = data2[['Year', 'Total voters']]
        Data_lineChart_mp_polled = data2[['Year', 'Total polled']]
        Data_lineChart_mp_BJP = data2[['Year', 'BJP POLL']]
        Data_lineChart_mp_INC = data2[['Year', 'INC POLL']]
        Data_lineChart_mp_OTH = data2[['Year', 'OTH POLL']]
        
        getYaxis_mp_voters = Data_lineChart_mp_voters['Year'].tolist()
        getXaxis_mp_voters = Data_lineChart_mp_voters['Total voters'].tolist()

        getYaxis_mp_polled = Data_lineChart_mp_polled['Year'].tolist()
        getXaxis_mp_polled = Data_lineChart_mp_polled['Total polled'].tolist()

        getYaxis_mp_BJP = Data_lineChart_mp_BJP['Year'].tolist()
        getXaxis_mp_BJP = Data_lineChart_mp_BJP['BJP POLL'].tolist()
 
        getYaxis_mp_INC = Data_lineChart_mp_INC['Year'].tolist()
        getXaxis_mp_INC = Data_lineChart_mp_INC['INC POLL'].tolist()

        getYaxis_mp_OTH = Data_lineChart_mp_OTH['Year'].tolist()
        getXaxis_mp_OTH = Data_lineChart_mp_OTH['OTH POLL'].tolist()

        return last_two_rows_mp1_voters, last_two_rows_mp2_polled, last_two_rows_mp3_bjp, last_two_rows_mp3_inc, last_two_rows_mp3_oth, getYaxis_mp_voters, getXaxis_mp_voters, getYaxis_mp_polled, getXaxis_mp_polled, getYaxis_mp_BJP, getXaxis_mp_BJP, getYaxis_mp_INC, getXaxis_mp_INC, getYaxis_mp_OTH, getXaxis_mp_OTH


@app.route('/ward_overview', methods=['POST'])
def ward_overview():
    if request.form.get('action1'):
        location_name = request.form.get('location_name')
        print('Ward Overview clicked for location:', location_name)
        return redirect(url_for('ward_overview_page', location_name=location_name))
    return redirect(url_for('index'))



@app.route('/ward_overview_page')
def ward_overview_page():
    location_name = request.args.get('location_name')

    if location_name:
        analytics_data = SelectedWardAnalytics(location_name)
        HMCAnalytics_data = HMC_Analytics(location_name)

        WomenAnalytics_data, pie_chart_data = Women_EmploymentStatus(location_name)
        data_to_present1, pie_chart_data_min_emp, pie_chart_data_min_unemp, data_to_present1_1, pie_chart_data_min_apl, pie_chart_data_min_bpl, data_to_present55, pie_chart_data_min_hea, pie_chart_data_min_dis = MinorityStatus(location_name)
        GetAnal_BPLStud = StudentsUnderBPL(location_name)

        return render_template('ward_overview.html',
                               WomenAnalytics_data=WomenAnalytics_data,
                               analytics_data=analytics_data,
                               HMCAnalytics_data=HMCAnalytics_data,
                               location_name=location_name,
                               pie_chart_data=pie_chart_data,

                               MinEmpStat=data_to_present1,
                               pie_chart_data_min_emp=pie_chart_data_min_emp,
                               pie_chart_data_min_unemp=pie_chart_data_min_unemp,

                               MinEconStat=data_to_present1_1,
                               pie_chart_data_min_apl=pie_chart_data_min_apl,
                               pie_chart_data_min_bpl=pie_chart_data_min_bpl,

                               MinHealthStat=data_to_present55,
                               pie_chart_data_min_hea=pie_chart_data_min_hea,
                               pie_chart_data_min_dis=pie_chart_data_min_dis
                               )
    
    return redirect(url_for('index'))



@app.route('/Predictions', methods=['POST'])
def Predictions():
    if request.form.get('action_Predictions') == 'clicked':
        print('Prediction clicked')
        return redirect(url_for('prediction_page'))
    return redirect(url_for('index'))



@app.route('/prediction_page')
def prediction_page():
    return render_template('prediction_page.html')


@app.route('/ai_chat', methods=['POST'])
def ai_chat():
    if request.form.get('action2') == 'clicked':
        print('AI Chat clicked')
        return redirect(url_for('ai_chat_page'))
    return redirect(url_for('index'))


@app.route('/ChatResp', methods=['POST'])
def ai_chat_resp():
    if request.form.get('chat_input'):
        user_input = request.form.get('chat_input')
        print('AI Chat Input:', user_input)

        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(file_path)

                get_res = ChatAI_1(user_input, file_path)
                if get_res['type'] == 'file':
                    return jsonify({'response': 'Download your file', 'file_url': url_for('download_file')})
                else:
                    return jsonify({'response': get_res['result']})
        else:
            get_res = ChatAI(user_input)
            if get_res['type'] == 'file':
                return jsonify({'response': 'Download your file', 'file_url': url_for('download_file')})
            else:
                return jsonify({'response': get_res['result']})

    return redirect(url_for('index'))


@app.route('/generate_chart', methods=['POST'])
def generate_chart():
    data = request.json['data']
    x_values = list(data.keys())
    y_values = [item[2] for item in data.values()]
    print(x_values)
    print(y_values)
    return jsonify({'X_values': x_values, 'Y_values': y_values})


@app.route('/generate_chart1', methods=['POST'])
def generate_chart1():
    ward = request.form.get('Ward')
    comp_queries = request.form.get('comparables')
    print(comp_queries)
    comparables = json.loads(comp_queries)
    print('Got-----', comparables)
    print(ward)
    return render_template()



   
@app.route('/generate_chart_for_anal', methods=['POST'])
def generate_chart_for_anal():
    data = request.json['data']
    X_val = []
    Y_val = []
    for k1, v1 in data.items():
        Y = v1[2]
        Y_val.append(Y)
        X_val.append(k1)
    fig = go.Figure(data=[go.Bar(x=X_val, y=Y_val)])
    fig.update_layout(title='Religion Distribution', xaxis_title='Religion', yaxis_title='Count')
    chart_html = fig.to_html(full_html=False)
    return jsonify({'chart': chart_html})



@app.route('/prediction_pg', methods=['POST'])
def prediction_pg():
    data = request.get_json()
    category = data.get('category')

    if category=="mp":
        tb1_mp, tb2_mp, tb3_mp, tb4_mp, tb5_mp, getYaxis1, getXaxis1, getYaxis2, getXaxis2, getYaxis3, getXaxis3, getYaxis4, getXaxis4, getYaxis5, getXaxis5 = Main(category)
        tb1_mp.columns = tb1_mp.columns.str.capitalize()
        tb2_mp.columns = tb2_mp.columns.str.capitalize()
        tb3_mp.columns = tb3_mp.columns.str.capitalize()
        tb4_mp.columns = tb4_mp.columns.str.capitalize()
        tb5_mp.columns = tb5_mp.columns.str.capitalize()

        voting_TableData_mp = tb1_mp.to_html(classes='table table-striped', index=False)
        polling_TableData_mp = tb2_mp.to_html(classes='table table-striped', index=False)
        bjp_TableData_mp = tb3_mp.to_html(classes='table table-striped', index=False)
        inc_TableData_mp = tb4_mp.to_html(classes='table table-striped', index=False)
        oth_TableData_mp = tb5_mp.to_html(classes='table table-striped', index=False)

        return jsonify({
                "voting_TableData_mp": voting_TableData_mp,
                "polling_TableData_mp": polling_TableData_mp,
                "bjp_TableData_mp" : bjp_TableData_mp,
                "inc_TableData_mp" : inc_TableData_mp,
                "oth_TableData_mp" : oth_TableData_mp,

                "voting_Yaxis_mp":getYaxis1,
                "voting_Xaxis_mp":getXaxis1,
                "polling_Yaxis_mp":getYaxis2,
                "polling_Xaxis_mp":getXaxis2,
                "BJP_Yaxis_mp":getYaxis3,
                "BJP_Xaxis_mp":getXaxis3,
                "INC_Yaxis_mp":getYaxis4,
                "INC_Xaxis_mp":getXaxis4,
                "OTH_Yaxis_mp":getYaxis5,
                "OTH_Xaxis_mp":getXaxis5
            })


    else:
        tb1_mla, tb2_mla, tb3_mla, tb4_mla, tb5_mla, getYaxis1, getXaxis1, getYaxis2, getXaxis2, getYaxis3, getXaxis3, getYaxis4, getXaxis4, getYaxis5, getXaxis5 = Main(category)
        tb1_mla.columns = tb1_mla.columns.str.capitalize()
        tb2_mla.columns = tb2_mla.columns.str.capitalize()
        tb3_mla.columns = tb3_mla.columns.str.capitalize()
        tb4_mla.columns = tb4_mla.columns.str.capitalize()
        tb5_mla.columns = tb5_mla.columns.str.capitalize()
        
        voting_TableData_mla = tb1_mla.to_html(classes='table table-striped', index=False)
        polling_TableData_mla = tb2_mla.to_html(classes='table table-striped', index=False)
        bjp_TableData_mla = tb3_mla.to_html(classes='table table-striped', index=False)
        inc_TableData_mla = tb4_mla.to_html(classes='table table-striped', index=False)
        oth_TableData_mla = tb5_mla.to_html(classes='table table-striped', index=False)

        return jsonify({
                "voting_TableData_mla": voting_TableData_mla,
                "polling_TableData_mla": polling_TableData_mla,
                "bjp_TableData_mla" : bjp_TableData_mla,
                "inc_TableData_mla" : inc_TableData_mla,
                "oth_TableData_mla" : oth_TableData_mla,

                "voting_Yaxis_mla":getYaxis1,
                "voting_Xaxis_mla":getXaxis1,
                "polling_Yaxis_mla":getYaxis2,
                "polling_Xaxis_mla":getXaxis2,
                "BJP_Yaxis_mla":getYaxis3,
                "BJP_Xaxis_mla":getXaxis3,
                "INC_Yaxis_mla":getYaxis4,
                "INC_Xaxis_mla":getXaxis4,
                "OTH_Yaxis_mla":getYaxis5,
                "OTH_Xaxis_mla":getXaxis5
            })



@app.route('/process', methods=['POST'])
def process_form():
    Client_Cloud = pymongo.MongoClient('mongodb+srv://ravindraacharya0512:Iwilltakeovertheworld123@cluster0.ynaiaut.mongodb.net/')
    MainDB = Client_Cloud['MainB']
    MainDB_Coll = MainDB['CollDB']
    if 'List' in request.form:
        getchartdata = request.form.get('option_val')
        ward_name = request.form.get('Ward')
        category = request.form.get('Category')
        getchartdata = eval(getchartdata)
        getComparable_q = getchartdata['ComparableQueries'][0]
        print(getComparable_q)
        x_values = [list(item.keys())[0] for item in getComparable_q]
        x_values = [int(x) for x in x_values]
        y_values = [list(item.values())[0] for item in getComparable_q]
        print(x_values)
        print(y_values)

        for record in y_values:
            if 'WARD' in record:
                del record['WARD']

        fig = go.Figure(data=[go.Bar(x=x_values, y=y_values)])
        fig.update_layout(title='Data graph Analysis', xaxis_title='Data', yaxis_title='Count')
        chartData = fig.to_html(full_html=False)
        Drop_value_swot = request.form.get('option_val')
        print('Query :',Drop_value_swot)
        Drop_value_swot = eval(Drop_value_swot)
        ward_name = request.form.get('Ward')
        print(ward_name)
        get_query = Drop_value_swot['Query']
        get_Count = Drop_value_swot['Count']
        get_HMC = Drop_value_swot['HML_Label']
        get_swot = Drop_value_swot['SWOT']
        getComparables = Compar(get_query)
        print(getComparables)
        getAnalData = ComparAnalytics(getComparables, ward_name, MainDB_Coll)
        print(getAnalData)
        warddoc = {'WARD':ward_name}
        combine = {**warddoc, **get_query}
        result = MainDB_Coll.find(combine)
        documents_list = list(result)
        df = pd.DataFrame(documents_list)
        if '_id' in df.columns:
            df = df.drop(columns=['_id'])

        return render_template('view.html',
                            analytic=getAnalData, 
                            df_list=df, 
                            QueryC=get_Count, 
                            Query=get_query,
                            HML=get_HMC,
                            SWOT=get_swot,
                            x_values=x_values,
                            y_values=y_values,
                            category=category
                            )
    


@app.route('/download_file')
def download_file():
    return send_file('Download.xlsx',
                     as_attachment=True)



@app.route('/swot_overview', methods=['POST'])
def swot_overview():
    if request.form.get('action_swot') == 'clicked':
        print('SWOT Analysis clicked')
        location_name = request.form.get('location_name')
        return redirect(url_for('swot_file', location_name=location_name))
    return redirect(url_for('index'))



@app.route('/swot_file')
def swot_file():
    location_name = request.args.get('location_name')
    if location_name:
        conn = pymongo.MongoClient('mongodb+srv://ravindraacharya0512:Iwilltakeovertheworld123@cluster0.ynaiaut.mongodb.net/')
        dbase_bejai = conn['BEJAIy']
        dbase_dn = conn['DEREBAIL_NAIRUTHYAy']
        store_dbnames_in_list = ['BEJAIy', 'DEREBAIL_NAIRUTHYAy']
        GetResult = GetDataFromDB(store_dbnames_in_list, conn)
        GetResult = GetResult[location_name]
        TV_anal1, T_anal2 = totalVoters(location_name)
        
        return render_template('SWOT_file.html',
                               ward=location_name,
                               SWOT_data=GetResult,
                               totalvoters=TV_anal1,
                               totalMinors=T_anal2
                               )
    
    else:
        return redirect(url_for('index'))



def Predict_res(df, time_period_column, data_column, prediction_year):
  df1 = df[[time_period_column, data_column]]
  years_list = df[time_period_column].tolist()
  Data_list = df[data_column].tolist()
  data = pd.DataFrame({
                      'Year': years_list,
                      'Data': Data_list
                     })
  df2 = pd.DataFrame(data)
  df2.set_index('Year', inplace=True)
  polling_data = df2['Data']
  model = ARIMA(polling_data, order=(1, 1, 1))
  model_fit = model.fit()
  print(model_fit.summary())
  forecast = model_fit.forecast(steps=5)
  forecast_years = np.arange(prediction_year, prediction_year + 5)
  forecast_df = pd.DataFrame({'Year': forecast_years, 'Forecasted_Polling': forecast})
  forecast_df.set_index('Year', inplace=True)
  pred_ = forecast_df.loc[prediction_year, 'Forecasted_Polling']
  data_dict = {
      time_period_column : prediction_year,
      data_column : round(pred_)
  }
  new_row = pd.DataFrame([data_dict])
  data1 = pd.concat([df1, new_row], ignore_index=True)
  getYears = data1[time_period_column].tolist()
  getData = data1[data_column].tolist()
  return pred_, data1, getYears, getData



@app.route('/Predict_for_data', methods=['POST'])
def predict_for_data():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    
    time_period_column = request.form['timePeriodColumn']
    data_column = request.form['dataColumn']
    prediction_year = int(request.form['predictionYear'])
    
    df = pd.read_csv(file_path)
    
    print(df)
    print(time_period_column)
    predicted_value, pred_Df, YearsList, DataList = Predict_res(df, time_period_column, data_column, prediction_year)
    predicted_value = float("{:.2f}".format(predicted_value))
    predicted_value = round(predicted_value)
    pred_Df = pred_Df.to_html(classes='table table-striped', index=False)
    print('Predicted Output', predicted_value)
    return jsonify({'predictedValue': predicted_value, 'pred_Df':pred_Df, 'YearsList':YearsList, 'DataList':DataList})



@app.route('/ai_chat_page')
def ai_chat_page():
    response = request.args.get('response', '')
    return render_template('Ai_Chat.html',
                           response=response)



@app.route('/')
def index():
    mangalore_coords = [12.9141, 74.8560]
    map = folium.Map(location=mangalore_coords, zoom_start=13)
    bounds = [
        [12.865, 74.787],
        [12.865, 74.925],
        [12.955, 74.925],
        [12.955, 74.787]
    ]
    folium.Polygon(bounds, color='darkblue', weight=3).add_to(map)
    folium.Marker([12.9230, 74.8422], popup='BEJAI').add_to(map)
    folium.Marker([12.9055, 74.8550], popup='DEREBAIL NAIRUTHYA').add_to(map)
    map.save('templates/map.html')
    BringHomePage = mainFunc()
    return render_template('index.html',
                           BringHomePage=BringHomePage)


@app.route('/location/<name>')
def location(name):
    return render_template('location.html',
                           location_name=name)
