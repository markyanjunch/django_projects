from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        result = request.session.get('result', None)
        if result: del(request.session['result'])
        tc = 4163
        ctx = {'TimeCode': tc, 'result': result}
        return render(request, 'solo/main.html', ctx)
        
    def post(self, request):
        Field1 = request.POST.get('field1','')
        Field2 = request.POST.get('field2','')
        Field1 = Field1.strip()
        Field2 = Field2.strip()
        result = Field1 + " " + Field2
        result = result.upper()
        request.session['result'] = result
        return redirect(reverse_lazy('solo:main'))
