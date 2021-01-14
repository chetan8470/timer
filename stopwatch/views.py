from django.shortcuts import render, redirect

# Create your views here.
def form(request):
    if request.method == 'POST':
        laps = request.POST['laps']
        reps = request.POST['reps']
        time = request.POST['time']
        print('----------------->', laps, reps, time)
        request.session['laps'] = str(request.POST['laps'])
        request.session['reps'] = str(request.POST['reps'])
        request.session['time'] = str(request.POST['time'])
        request.session['form'] = True
        return redirect('/watch')
    return render(request, 'stopwatch/form.html')

def watch(request):
    if request.session.get('form', None):
        print('------------------------------------------------> post', request.session.keys())
        laps = request.session['laps']
        reps = request.session['reps']
        time = request.session['time']
        return render(request, 'stopwatch/watch.html', {'laps':laps, 'reps':reps, 'time':time})
    return redirect('/form')