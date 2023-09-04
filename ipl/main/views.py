import pickle,numpy as np
from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'POST':
        overs = float(request.POST['overs'])
        runs = int(request.POST['runs'])
        wickets = int(request.POST['wickets'])
        runs_in_prev_5 = int(request.POST['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.POST['wickets_in_prev_5'])
        batting_team = request.POST['batting-team']
        bolwing_team = request.POST['bowling-team']
        with open(r"C:\Users\user\Documents\aimlp\ipl\main\model.pkl",'rb') as f:
            md,enc = pickle.load(f).values()
            data = np.array([list(enc.transform([[batting_team, bolwing_team]]).toarray()[0])+[overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]])
            final = int(md.predict(data))
            return render(request,'result.html',{'score':final})


    return render(request,'index.html')