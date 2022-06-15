from django.http import HttpResponse
import sqlite3
from django.db import connections

from sqlite3 import Error

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def error(request):
    raise NotImplementedError
    return HttpResponse("Hello, world. You're at the polls index.")

def sql_select(request):
    conn = connections['default']
    name = "fdsfds"
    sql_query = "UPDATE student SET weight = 80 WHERE name = %s " % (name)
    with conn.cursor() as cur:
        cur.execute(sql_query)
    return HttpResponse("Hello, world. You're at the polls index.")
