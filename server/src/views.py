from aiohttp import web
from settings import config

import cx_Oracle
import json

# Connect string format: [username]/[password]@//[hostname]:[port]/[DB service name]
DSN = "{user}/{password}@//{host}:{port}/{database}"

async def dbquery(statement):
    try:
        db_url = DSN.format(**config['oracle'])
        conn = cx_Oracle.connect(db_url)
        cursor = conn.cursor()
        row = cursor.execute(statement)
        result = None
        if row:
            result = [dict(zip([desc[0] for desc in row.description], col)) for col in row.fetchall()]
    finally:
        cursor.close()
    return result

async def main(request):
    sortby_type = request.message.url.query['sortby']
    #print(sortby_type)
    if (sortby_type=='class'):
        static_path = 'static/final_class.json'
    elif(sortby_type=='group'):
        static_path = 'static/final_group.json'
    else:
        static_path = 'static/test.json'
    jobj = json.loads(open(static_path).read())
    headers = {'Access-Control-Allow-Origin': '*'}
    return web.json_response(jobj,headers=headers)

async def replace_classes(result):
    str = json.dumps(result)
    str = str.replace("DEVICE_CLASS_ID","id")
    str = str.replace("NAME","name")
    final = json.loads(str)
    return  final


async def object_classes(request):
    sql = """select dc.device_class_id, dc.name
             from device_classes dc
             where dc.root_device = '1'"""
    result = dbquery(sql)
    for obj in result:
        obj.setdefault("children",[])
    result = adddevices(result)
    return web.json_response(data=replace_classes(result), headers=[('Access-Control-Allow-Origin', '*')],
                            content_type='application/json', dumps=json.dumps)

async def adddevices(jsonobj):


async def object_types(request):
    sql = '''select dt.device_class,
                    dt.device_type_id, 
                    dt.name, 
                    dt.remark
             from os_eqm.device_types dt
          '''
    try:
        db_url = DSN.format(**config['oracle'])
        conn = cx_Oracle.connect(db_url)
        cursor = conn.cursor()
        row = cursor.execute(sql)
        result = None
        if row:
            result = [dict(zip([desc[0] for desc in row.description], col)) for col in row.fetchall()]
    finally:
        cursor.close()
    return web.json_response(data=result, headers=[('Access-Control-Allow-Origin', '*')],
                            content_type='application/json', dumps=json.dumps)

async def representation(request):
    sql = '''select g.device_group_id,
                    g.par_group_id,
                    g.group_name,
                    g.group_remark,
                    g.group_type_id
             from os_eqm.device_groups g
             where g.group_type_id = 1
          '''
    try:
        db_url = DSN.format(**config['oracle'])
        conn = cx_Oracle.connect(db_url)
        cursor = conn.cursor()
        row = cursor.execute(sql)
        result = None
        if row:
            result = [dict(zip([desc[0] for desc in row.description], col)) for col in row.fetchall()]
    finally:
        cursor.close()
    return web.json_response(data=result, headers=[('Access-Control-Allow-Origin', '*')],
                            content_type='application/json', dumps=json.dumps)

async def replace_groups(result):
    str = json.dumps(result)
    str = str.replace("DEVICE_GROUP_ID","id")
    str = str.replace("GROUP_NAME","name")
    str = str.replace("GROUP_REMARK","remark")
    str = str.replace("GROUP_TYPE_ID","type")
    final = json.loads(str)
    return  final


async def group_representation_old(request):
    sql = '''select dg.device_group_id,
                    dg.par_group_id,
                    dg.group_name,
                    dg.group_remark,
                    dg.group_type_id
             from os_eqm.device_groups dg
             connect by prior dg.device_group_id = dg.par_group_id
          '''
    groups = dbquery(sql)
    groups = replace_groups(groups)
    for group in groups:
        group.setdefault("children",[])
    devices = get_all_devices()
    for device in devices:
        for group in groups:
            if device["grid"]==group["id"]:
                group["children"].append(device)
                break

    return web.json_response(data=groups, headers=[('Access-Control-Allow-Origin', '*')],
                            content_type='application/json', dumps=json.dumps)

async def get_all_devices():
    sql = '''SELECT d.DEVICE_ID,
                    d.DEVICE_TYPE,
                    d.GROUP_ID,
                    d."remark",
                    d."device_name"
            from OS_EQM.DEVICES d
          '''
    result = dbquery(sql)
    return replace_devices(result)


async def replace_devices(result):
    str = json.dumps(result)
    str = str.replace("DEVICE_ID","id")
    str = str.replace("DEVICE_TYPE","type")
    str = str.replace("NAME","name")
    str = str.replace("GROUP_ID","grid")
    final = json.loads(str)
    return  final


async def group_representation(request):
    sql = '''select dg.device_group_id,
                    dg.par_group_id,
                    dg.group_name,
                    dg.group_remark,
                    dg.group_type_id
             from os_eqm.device_groups dg
             connect by prior dg.device_group_id = dg.par_group_id
          '''
    try:
        db_url = DSN.format(**config['oracle'])
        conn = cx_Oracle.connect(db_url)
        cursor = conn.cursor()
        row = cursor.execute(sql)
        result = None
        if row:
            result = [dict(zip([desc[0] for desc in row.description], col)) for col in row.fetchall()]
    finally:
        cursor.close()

    str = json.dumps(result)
    str = str.replace("DEVICE_GROUP_ID","id")
    str = str.replace("GROUP_NAME","name")
    str = str.replace("GROUP_REMARK","remark")
    str = str.replace("GROUP_TYPE_ID","type")
    groups = json.loads(str)

    for group in groups:
        group.setdefault("children",[])
    sql = '''SELECT d.DEVICE_ID,
                    d.DEVICE_TYPE,
                    d.GROUP_ID,
                    d."remark",
                    d."device_name"
            from OS_EQM.DEVICES d
          '''
    try:
        db_url = DSN.format(**config['oracle'])
        conn = cx_Oracle.connect(db_url)
        cursor = conn.cursor()
        row = cursor.execute(sql)
        resultd = None
        if row:
            resultd = [dict(zip([desc[0] for desc in row.description], col)) for col in row.fetchall()]
    finally:
        cursor.close()

    str = json.dumps(resultd)
    str = str.replace("DEVICE_ID","id")
    str = str.replace("DEVICE_TYPE","type")
    str = str.replace("NAME","name")
    str = str.replace("GROUP_ID","grid")
    devices = json.loads(str)

    for device in devices:
        for group in groups:
            if device["grid"]==group["id"]:
                group["children"].append(device)
                break

    return web.json_response(data=groups, headers=[('Access-Control-Allow-Origin', '*')],
                            content_type='application/json', dumps=json.dumps)

