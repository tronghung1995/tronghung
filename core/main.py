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
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional

app = FastAPI()

origins = [
    "http://tronghung.cf",
    "http://tronghung.cf/*",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect tới database BRVT
engine = engineDB_BRVT


# -------------- Bệnh viêm da nỗi cục -----------------
# ------ Lấy thuộc tính -------
# def channuoi_benhviemdanoicuc():
#     with engine.connect() as connection:
#         sql = "select  tenhuyen, sum(sothon) as sothon, sum(soho) as soho, sum(sobenh) as sobenh, sum(sochet) as sochet, sum(tongchet_huy) as tongchet_huy, sum(tongdan) as tongdan, sum(kl_tieuhuy) as kl_tieuhuy from import_data.vw_channuoi_dichbenhtonghop where chuyenmuc='Bệnh Viêm da nổi cục' group by  tenhuyen, chuyenmuc;"
#         result = connection.execute(sql)
#         ketqua = result.fetchall()
#         ketqua_encoder = jsonable_encoder(ketqua)
#         ketqua_json = JSONResponse(content=ketqua_encoder)
#         result.close()
#         return ketqua_json


# @app.get("/api_channuoi_benhviemdanoicuc")
# async def channuoi_benhviemdanoicuc_render():
#     return channuoi_benhviemdanoicuc()


# ------ Lấy thuộc tính -------


# ----------------------Biểu đồ-----------------------
# def channuoi_benhviemdanoicuc_bieudo():
#     with engine.connect() as connection:
#         sql = "select  tenhuyen as name, sum(sothon) as y, sum(soho) as y1, sum(sobenh) as y2, sum(sochet) as y3, sum(tongchet_huy) as y4, sum(tongdan) as y5, sum(kl_tieuhuy) as y6 from import_data.vw_channuoi_dichbenhtonghop where chuyenmuc='Bệnh Viêm da nổi cục' group by  tenhuyen, chuyenmuc;"
#         result = connection.execute(sql)
#         ketqua = result.fetchall()
#         ketqua_encoder = jsonable_encoder(ketqua)
#         ketqua_json = JSONResponse(content=ketqua_encoder)
#         result.close()
#         return ketqua_json


# @app.get("/api_channuoi_benhviemdanoicuc_bieudo")
# async def channuoi_benhviemdanoicuc_bieudo_render():
#     return channuoi_benhviemdanoicuc_bieudo()


# ----------------------Biểu đồ-----------------------


# -------------- Bệnh viêm da nỗi cục -----------------


# -------------- Bệnh tả heo Châu Phi -----------------
# ------ Lấy thuộc tính -------
# def channuoi_benhtalonchauphi():
#     with engine.connect() as connection:
#         sql = "select tenhuyen, sum(sothon) as sothon, sum(soho) as soho, sum(sobenh) as sobenh, sum(sochet) as sochet, sum(tongchet_huy) as tongchet_huy, sum(tongdan) as tongdan, sum(kl_tieuhuy) as kl_tieuhuy from import_data.vw_channuoi_dichbenhtonghop where chuyenmuc = 'Bệnh Dịch tả lợn Châu Phi' group by tenhuyen;"
#         result = connection.execute(sql)
#         ketqua = result.fetchall()
#         ketqua_encoder = jsonable_encoder(ketqua)
#         ketqua_json = JSONResponse(content=ketqua_encoder)
#         result.close()
#         return ketqua_json


# @app.get("/api_channuoi_benhtalonchauphi")
# async def channuoi_channuoi_benhtalonchauphi_render():
#     return channuoi_benhtalonchauphi()


# ------ Lấy thuộc tính -------

# ----------------------Biểu đồ-----------------------
# def channuoi_benhtalonchauphi_bieudo():
#     with engine.connect() as connection:
#         sql = "select tenhuyen as name, sum(sothon) as y, sum(soho) as y1, sum(sobenh) as y2, sum(sochet) as y3, sum(tongchet_huy) as y4, sum(tongdan) as y5, sum(kl_tieuhuy) as y6 from import_data.vw_channuoi_dichbenhtonghop where chuyenmuc = 'Bệnh Dịch tả lợn Châu Phi' group by tenhuyen;"
#         result = connection.execute(sql)
#         ketqua = result.fetchall()
#         ketqua_encoder = jsonable_encoder(ketqua)
#         ketqua_json = JSONResponse(content=ketqua_encoder)
#         result.close()
#         return ketqua_json


# @app.get("/api_channuoi_benhtalonchauphi_bieudo")
# async def channuoi_benhtalonchauphi_bieudo_render():
#     return channuoi_benhtalonchauphi_bieudo()


# ----------------------Biểu đồ-----------------------
# -------------- Bệnh tả heo Châu Phi -----------------


# Query parameters dichbenh_channuoi
@app.get("/api_channuoi/dichbenh")
def channuoi_dichbenh_solieu(benhdich: Optional[str]):
    tendichbenh = f"'{benhdich}'"
    with engine.connect() as connection:
        sql = "select tenhuyen, sum(sothon) as sothon, sum(soho) as soho, sum(sobenh) as sobenh, sum(sochet) as sochet, sum(tongchet_huy) as tongchet_huy, sum(tongdan) as tongdan, sum(kl_tieuhuy) as kl_tieuhuy from import_data.vw_channuoi_dichbenhtonghop where chuyenmuc = %s group by tenhuyen;" % (tendichbenh)
        result = connection.execute(sql)
        ketqua = result.fetchall()
        ketqua_encoder = jsonable_encoder(ketqua)
        ketqua_json = JSONResponse(content=ketqua_encoder)
        result.close()
        return ketqua_json


# ----------------------Biểu đồ-----------------------
@app.get("/api_channuoi/bieudo/dichbenh")
def channuoi_bieudo_dichbenh(loaitk: Optional[str], benhdich: Optional[str]):
    loai_tk = f"{loaitk}"
    # tendichbenh có 2 dấu nháy vì select thuộc tính bên trong cần có thêm 1 dấu nháy
    tendichbenh = f"'{benhdich}'"
    with engine.connect() as connection:
        sql = "select tenhuyen as name, sum(%s) as y from import_data.vw_channuoi_dichbenhtonghop where chuyenmuc = %s group by tenhuyen;" % (
            loai_tk, tendichbenh)
        result = connection.execute(sql)
        ketqua = result.fetchall()
        ketqua_encoder = jsonable_encoder(ketqua)
        ketqua_json = JSONResponse(content=ketqua_encoder)
        result.close()
        return ketqua_json


# ----------------------Biểu đồ-----------------------
@app.get("/api_channuoi/bando/dichbenh")
def channuoi_bando_dichbenh():
    # loai_tk = f"{loaitk}"
    # tendichbenh có 2 dấu nháy vì select thuộc tính bên trong cần có thêm 1 dấu nháy
    # tendichbenh = f"'{benhdich}'"
    with engine.connect() as connection:
        # sql = "SELECT st_asgeojson(t2.geom) AS extgeo FROM donvihanhchinh.hanhchinh_huyen t1 JOIN donvihanhchinh.hanhchinh_huyen_geo t2 ON t2.mahuyen = t1.mahuyen;"
        sql = "SELECT tenhc as name, st_asgeojson(geom) AS extgeo FROM donvihanhchinh.hanhchinh_huyen_view;"
        # % (tendichbenh)
        result = connection.execute(sql)
        ketqua = result.fetchall()
        ketqua_encoder = jsonable_encoder(ketqua)
        ketqua_json = JSONResponse(content=ketqua_encoder)
        result.close()
        return ketqua_json

    # uvicorn main:app --reload --host 127.0.0.1
