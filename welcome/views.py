import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from sqlalchemy import *
from project import database as pdb

from . import database
from .models import PageView

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    # check database connectivity
    db = create_engine(pdb.url())
    connection = engine.connect()
    result = connection.execute("select 1")
    connection.close()
    
    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count(),
        'result': result
    })

def health(request):
    return HttpResponse(PageView.objects.count())
