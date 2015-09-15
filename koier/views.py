from django.shortcuts import render
from django.http import *
from .forms import KoieForm
import MySQLdb


def home(request):
    db = MySQLdb.connect(user='naesheim', db='koier',passwd='1234', host='localhost')
    cursor = db.cursor()
    cursor.execute('select * from koier_koie')
    names = [row[1] for row in cursor.fetchall()]
    db.close()
    return render(request, 'koier/base.html',{'names':names})

def rapport(request):
    if request.method == 'POST':
        form = KoieForm(request.POST)
        if form.is_valid():
            koie_name = form.koie_name
            rapport = form.rapport
            vedstatus = form.vedstatus
            post = (koie_name,vedstatus,rapport)
            html = "<html><body> %s </body></html>" % post
            return HttpResponse(html)
    else:
        form = KoieForm()

    return render(request, 'koier/form.html',{'form':form})