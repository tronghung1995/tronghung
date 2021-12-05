import json
import sys
import configparser
import psycopg2
import uvicorn
from fastapi import FastAPI
from con_database import engineDB_BRVT, session
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
import requests

app = FastAPI()

# Connect tới database BRVT
engine = engineDB_BRVT

@app.get("/")
async def first_module():
    table_name = "import_data.ktts_tonghop_tinh"
    with engine.connect() as connection:
        #sql_select = ("""SELECT nhom,chuyenmuc,soluong_tau,tau_khaithac_6m_12m,tau_khaithac_12m_15m,tau_khaithac_15m_trolen,loai_khaithac,sanluong_theo_thang,mota2,mahuyen,ngaybaocao,thang_baocao,nam_baocao,fromfile,id, sum(soluong_tau) as total FROM import_data.ktts_tonghop_tinh GROUP BY nhom,chuyenmuc,soluong_tau,tau_khaithac_6m_12m,tau_khaithac_12m_15m,tau_khaithac_15m_trolen,loai_khaithac,sanluong_theo_thang,mota2,mahuyen,ngaybaocao,thang_baocao,nam_baocao,fromfile,id;""")
        sql_sum_soluongtau_theo_nhom = ("""select nhom, sum(soluong_tau) as total FROM import_data.ktts_tonghop_tinh GROUP BY nhom;""")
        result = connection.execute(sql_sum_soluongtau_theo_nhom)
        for i in result:
            pass
        print_ = i["total"]
        # abc = {"total": print_}
        # sorted_string = json.dumps(abc, indent=4, sort_keys=True)
    return print_

# uvicorn main:app --reload --host 0.0.0.0