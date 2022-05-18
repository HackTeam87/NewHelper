import os
import sys
sys.path.insert(0, './schemas')
sys.path.insert(0, './modules')
sys.path.insert(0, './db')
from typing import List
from schemas import Device
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from modules.Api import Mikrotik
from db.base import database
from db.device import devices

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://185.190.150.5:8080",
    "http://185.190.150.5:8080/detail/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

 
@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


       

@app.get("/api/device/list", response_model=List[Device])
async def list_device():
    
    query = 'SELECT * FROM devices'
    query2 = '''SELECT id, ip, created, up, down,
                api_login,api_pass,api_port,
                community_r, community_rw, desc,
                status,  modules_id,
                group_id, sort_id FROM devices'''
    return await database.fetch_all(query)

#Mikrotik 
@app.get("/api/device/mikrotik/interface/{id}")
async def api_mikrotik_interface(id: int):
    # id = {"id": id}
    query = '''SELECT * FROM devices WHERE id=''' + str(id)
    rdb = await database.fetch_one(query)
    res = Mikrotik().interface_info(rdb.ip, rdb.api_port, rdb.api_login, rdb.api_pass)
    # d = {'data': res}
    return res

@app.get("/api/device/mikrotik/arp/{id}")
async def api_mikrotik_arp(id: int):
    # id = {"id": id}
    query = '''SELECT * FROM devices WHERE id=''' + str(id)
    rdb = await database.fetch_one(query)
    res = Mikrotik().ip_arp_info(rdb.ip, rdb.api_port, rdb.api_login, rdb.api_pass)
    # d = {'data': res}
    return res 

@app.get("/api/device/mikrotik/dhcp-server/{id}")
async def api_mikrotik_dhcp_server(id: int):
    # id = {"id": id}
    query = '''SELECT * FROM devices WHERE id=''' + str(id)
    rdb = await database.fetch_one(query)
    res = Mikrotik().ip_dhcp_server_info(rdb.ip, rdb.api_port, rdb.api_login, rdb.api_pass)
    return res     


@app.get("/api/device/mikrotik/lease/mac-or-ip/{mac_or_ip}/id/{id}")
async def api_mikrotik_lease(id: int, mac_or_ip: str):
    # id = {"id": id}
    query = '''SELECT * FROM devices WHERE id=''' + str(id)
    rdb = await database.fetch_one(query)
    res = Mikrotik().ip_dhcp_server_lease_info(rdb.ip, rdb.api_port, rdb.api_login, rdb.api_pass, mac_or_ip)
    return res

  
@app.get("/api/device/mikrotik/bgp/peer/{id}")
async def api_mikrotik_bgp_peer(id: int):
    # id = {"id": id}
    query = '''SELECT * FROM devices WHERE id=''' + str(id)
    rdb = await database.fetch_one(query)
    res = Mikrotik().routing_bgp_peer_info(rdb.ip, rdb.api_port, rdb.api_login, rdb.api_pass)
    # d = {'data': res}
    return res  

 

@app.get("/api/device/mikrotik/routing/filter/{id}")
async def api_mikrotik_routing_filter(id: int):
    # id = {"id": id}
    query = '''SELECT * FROM devices WHERE id=''' + str(id)
    rdb = await database.fetch_one(query)
    res = Mikrotik().routing_filter_info(rdb.ip, rdb.api_port, rdb.api_login, rdb.api_pass)
    return res


@app.get("/api/device/mikrotik/firewall/filter/{id}")
async def api_mikrotik_firewall_filter(id: int):
    # id = {"id": id}
    query = '''SELECT * FROM devices WHERE id=''' + str(id)
    rdb = await database.fetch_one(query)
    res = Mikrotik().ip_firewall_filter_info(rdb.ip, rdb.api_port, rdb.api_login, rdb.api_pass)
    return res

@app.get("/api/device/mikrotik/firewall/address-list/{id}")
async def api_mikrotik_firewall_address_list(id: int):
    # id = {"id": id}
    query = '''SELECT * FROM devices WHERE id=''' + str(id)
    rdb = await database.fetch_one(query)
    res = Mikrotik().ip_firewall_address_list_info(rdb.ip, rdb.api_port, rdb.api_login, rdb.api_pass)
    return res    

@app.get("/api/device/mikrotik/ip/route/{id}")
async def api_mikrotik_route(id: int):
    query = '''SELECT * FROM devices WHERE id=''' + str(id)
    rdb = await database.fetch_one(query)
    res = Mikrotik().ip_route_info(rdb.ip, rdb.api_port, rdb.api_login, rdb.api_pass)
    return res

# ip firewall connection print where src-address~"185.253.216.196"
@app.get("/api/device/mikrotik/firewall/connection/src-address/{ip}/id/{id}")
async def api_mikrotik_firewall_connection_src_address(id: int, ip: str):
    query = '''SELECT * FROM devices WHERE id=''' + str(id)
    rdb = await database.fetch_one(query)
    res = Mikrotik().connection_info(rdb.ip, rdb.api_port, rdb.api_login, rdb.api_pass, ip)
    return res

@app.get("/api/device/mikrotik/arp-ping/address/{address}/interface/{interface}/id/{id}")
async def api_mikrotik_arp_ping(id: int, address: str, interface: str ):
    query = '''SELECT * FROM devices WHERE id=''' + str(id)
    rdb = await database.fetch_one(query)
    res = Mikrotik().arp_ping_info(rdb.ip, rdb.api_port, rdb.api_login, rdb.api_pass, address, interface)
    return res    





    

       

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
