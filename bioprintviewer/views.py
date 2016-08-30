from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader
from django.shortcuts import render
from mydbutils import dbConnect, extractUserId
from numpy import unique
import pymongo
from forms import UserForm


'''
def index(request):
    context = {}
    return render(request, 'bioprintviewer/index.html', context)
'''

def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            return HttpResponseRedirect('/bioprintviewer/'+user_id+'/')

    else:
        form = UserForm()

    return render(request, 'bioprintviewer/index.html', {'form': form})

def manager(request):
    # DB Hook
    db = dbConnect()
    # Query
    cursor = db.bioprints.find({}, {"user_info":1, "_id":0})
    user_ids = unique([ extractUserId(document["user_info"]["email"]) for document in cursor ])
    context = { 'user_ids': user_ids}
    return render(request, 'bioprintviewer/manager.html', context)

def user(request, user_id):
    # DB Hook
    db = dbConnect()
    # Query
    user_email = user_id+'@gmail.com'
    cursor = (db.bioprints.find({"user_info.email": user_email})
                          .sort([("print_info.files.input", pymongo.ASCENDING)])
             )

    prints = []
    serials = []
    for document in cursor:
        serials.append(document['user_info']['serial'])
        prints.append({'file': document['print_info']['files']['input']})

    context = {
        'user_id': user_id,
        'serials': unique(serials),
        'prints': prints,
    }
    return render(request, 'bioprintviewer/user.html', context)


def bioprint(request, user_id, serial, input_file):
    db = dbConnect()
    # Query
    user_email = user_id+'@gmail.com'
    cursor = (db.bioprints.find({"user_info.email": user_email,
                                 "user_info.serial": int(serial),
                                 "print_info.files.input": input_file}
                                 )
             )
    prints = []
    for document in cursor:
        prints.append(document)
    context = {
        'user_id': user_id,
        'print': prints[0],
    }
    return render(request, 'bioprintviewer/bioprint.html', context)
