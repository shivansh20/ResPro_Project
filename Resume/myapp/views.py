from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from .forms import ResumeForm, ResumeForm2, ResumeForm3
from django.views.generic import View
from .models import Resume
import os
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
# from .utils import render_to_pdf

# Create your views here.


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username Already Taken!')
            return redirect('/')
        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.save()
            messages.success(request, 'Your Account Has Been Successfully Created!')
            return redirect('/')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        username1 = request.POST['username']
        password1 = request.POST['password']

        user = authenticate(username=username1, password=password1)

        if user is None:
            messages.error(request, "Invalid Credentials, Please Try Again")
            return redirect('login')
        else:
            return render(request, 'home.html', {'user': user})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("login")


class FormView(View):
    def get(self, request):
        form2 = ResumeForm()
        candidates = Resume.objects.all()
        return render(request, 'formCS.html', {'candidates': candidates, 'form2': form2})

    def post(self, request):
        form2 = ResumeForm(request.POST, request.FILES)
        if form2.is_valid():
            abc = form2.save()
            return redirect('candidate', pk=abc.pk)


class CandidateView(View):
    def get(self, request, pk, *args, **kwargs):
        candidate = Resume.objects.get(pk=pk)
        template_path = 'resume1.html'
        context = {
            "candidate": candidate,
        }
        response = HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        response['Content-Disposition'] = "filename=RESUME.pdf"

        template = get_template(template_path)
        html = template.render(context)

        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html + '</pre>')
        return response

        # pdf = render_to_pdf('myapp/candidate.html', context)
        # return HttpResponse(pdf, content_type='application/pdf')
        # return render(request, 'myapp/candidate.html', {'candidate': candidate})



def about(request):
    return HttpResponse("<h1>ABOUT PAGE!!!</h1>")

def home(request):
    return render(request, 'home.html')


def engineering(request):
    return render(request, 'engineering.html')


def csetemplates(request):
    return render(request, 'csetemplates.html')


def cetemplates(request):
    return render(request, 'cetemplates.html')


def metemplates(request):
    return render(request, 'metemplates.html')


def eetemplates(request):
    return render(request, 'eetemplates.html')


def ecetemplates(request):
    return render(request, 'ecetemplates.html')


def bankingtemplates(request):
    return render(request, 'BankingTemplates.html')


def marketingtemplates(request):
    return render(request, 'MarketingTemplates.html')


def teachingtemplates(request):
    return render(request, 'TeachingTemplates.html')


class Form1(View):
    def get(self, request):
        form2 = ResumeForm()
        candidates1 = Resume.objects.all()
        return render(request, 'formCS.html', {'candidates1': candidates1, 'form2': form2})

    def post(self, request):
        form2 = ResumeForm(request.POST, request.FILES)
        if form2.is_valid():
            abc1 = form2.save()
            return redirect('xyz1', pk=abc1.pk)


class xyz1(View):
    def get(self, request, pk, *args, **kwargs):
        candidate1 = Resume.objects.get(pk=pk)
        template_path1 = 'resume2.html'
        context1 = {
            "candidate1": candidate1,
        }
        response1 = HttpResponse(content_type='application1/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        response1['Content-Disposition'] = "filename=abc.pdf"
        template1 = get_template(template_path1)
        html1 = template1.render(context1)
        pisa_status = pisa.CreatePDF(html1, dest=response1)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return response1


class Form2(View):
    def get(self, request):
        form2 = ResumeForm()
        candidates2 = Resume.objects.all()
        return render(request, 'formCS.html', {'candidates2': candidates2, 'form2': form2})

    def post(self, request):
        form2 = ResumeForm(request.POST, request.FILES)
        if form2.is_valid():
            bcd1 = form2.save()
            return redirect('xyz2', pk=bcd1.pk)


class xyz2(View):
    def get(self, request, pk, *args, **kwargs):
        candidate2 = Resume.objects.get(pk=pk)
        template_path2 = 'resume3.html'
        context2 = {
            "candidate2": candidate2,
        }
        response2 = HttpResponse(content_type='application2/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        response2['Content-Disposition'] = "filename=CS_RESUME3.pdf"
        template2 = get_template(template_path2)
        html1 = template2.render(context2)
        pisa_status = pisa.CreatePDF(html1, dest=response2)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return response2


class Form3(View):
    def get(self, request):
        form2 = ResumeForm()
        candidates3 = Resume.objects.all()
        return render(request, 'formCS.html', {'candidates3': candidates3, 'form2': form2})

    def post(self, request):
        form2 = ResumeForm(request.POST, request.FILES)
        if form2.is_valid():
            cde1 = form2.save()
            return redirect('xyz3', pk=cde1.pk)


class xyz3(View):
    def get(self, request, pk, *args, **kwargs):
        candidate3 = Resume.objects.get(pk=pk)
        template_path3 = 'resume4.html'
        context3 = {
            "candidate3": candidate3,
        }
        response3 = HttpResponse(content_type='application3/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        response3['Content-Disposition'] = "filename=CS_RESUME4.pdf"
        template3 = get_template(template_path3)
        html1 = template3.render(context3)
        pisa_status = pisa.CreatePDF(html1, dest=response3)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return response3


class Form4(View):
    def get(self, request):
        form2 = ResumeForm()
        candidates4 = Resume.objects.all()
        return render(request, 'formCS.html', {'candidates4': candidates4, 'form2': form2})

    def post(self, request):
        form2 = ResumeForm(request.POST, request.FILES)
        if form2.is_valid():
            def1 = form2.save()
            return redirect('xyz4', pk=def1.pk)


class xyz4(View):
    def get(self, request, pk, *args, **kwargs):
        candidate4 = Resume.objects.get(pk=pk)
        template_path4 = 'resume5.html'
        context4 = {
            "candidate4": candidate4,
        }
        response4 = HttpResponse(content_type='application4/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        response4['Content-Disposition'] = "filename=CS_RESUME5.pdf"
        template4 = get_template(template_path4)
        html1 = template4.render(context4)
        pisa_status = pisa.CreatePDF(html1, dest=response4)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return response4


class FormCE1(View):
    def get(self, request):
        formme1 = ResumeForm2()
        candidates5 = Resume.objects.all()
        return render(request, 'form1ME.html', {'candidates5': candidates5, 'formme1': formme1})

    def post(self, request):
        formme1 = ResumeForm2(request.POST, request.FILES)
        if formme1.is_valid():
            efg1 = formme1.save()
            return redirect('xyz5', pk=efg1.pk)


class xyz5(View):
    def get(self, request, pk, *args, **kwargs):
        candidate5 = Resume.objects.get(pk=pk)
        template_path5 = 'resume6.html'
        context5 = {
            "candidate5": candidate5,
        }
        response5 = HttpResponse(content_type='application5/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        response5['Content-Disposition'] = "filename=CS_RESUME5.pdf"
        template4 = get_template(template_path5)
        html1 = template4.render(context5)
        pisa_status = pisa.CreatePDF(html1, dest=response5)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return response5


class FormCE2(View):
    def get(self, request):
        formme1 = ResumeForm2()
        candidates6 = Resume.objects.all()
        return render(request, 'form1ME.html', {'candidates6': candidates6, 'formme1': formme1})

    def post(self, request):
        formme1 = ResumeForm2(request.POST, request.FILES)
        if formme1.is_valid():
            fgh1 = formme1.save()
            return redirect('xyz6', pk=fgh1.pk)


class xyz6(View):
    def get(self, request, pk, *args, **kwargs):
        candidate6 = Resume.objects.get(pk=pk)
        template_path6 = 'resume7.html'
        context6 = {
            "candidate6": candidate6,
        }
        response6 = HttpResponse(content_type='application6/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        response6['Content-Disposition'] = "filename=CS_RESUME6.pdf"
        template6 = get_template(template_path6)
        html1 = template6.render(context6)
        pisa_status = pisa.CreatePDF(html1, dest=response6)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return response6


class FormCE3(View):
    def get(self, request):
        formme1 = ResumeForm2()
        candidates7 = Resume.objects.all()
        return render(request, 'form1ME.html', {'candidates7': candidates7, 'formme1': formme1})

    def post(self, request):
        formme1 = ResumeForm2(request.POST, request.FILES)
        if formme1.is_valid():
            ghi1 = formme1.save()
            return redirect('xyz7', pk=ghi1.pk)


class xyz7(View):
    def get(self, request, pk, *args, **kwargs):
        candidate7 = Resume.objects.get(pk=pk)
        template_path7 = 'resume8.html'
        context7 = {
            "candidate7": candidate7,
        }
        response7 = HttpResponse(content_type='application7/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        response7['Content-Disposition'] = "filename=CS_RESUME7.pdf"
        template7 = get_template(template_path7)
        html1 = template7.render(context7)
        pisa_status = pisa.CreatePDF(html1, dest=response7)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return response7

class FormCE4(View):
    def get(self, request):
        formme1 = ResumeForm2()
        candidates8 = Resume.objects.all()
        return render(request, 'form1ME.html', {'candidates8': candidates8, 'formme1': formme1})

    def post(self, request):
        formme1 = ResumeForm2(request.POST, request.FILES)
        if formme1.is_valid():
            hij1 = formme1.save()
            return redirect('xyz8', pk=hij1.pk)


class xyz8(View):
    def get(self, request, pk, *args, **kwargs):
        candidate8 = Resume.objects.get(pk=pk)
        template_path8 = 'resume9.html'
        context8 = {
            "candidate8": candidate8,
        }
        response8 = HttpResponse(content_type='application8/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        response8['Content-Disposition'] = "filename=CS_RESUME8.pdf"
        template8 = get_template(template_path8)
        html1 = template8.render(context8)
        pisa_status = pisa.CreatePDF(html1, dest=response8)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return response8


class FormCE5(View):
    def get(self, request):
        formme1 = ResumeForm2()
        candidates9 = Resume.objects.all()
        return render(request, 'form1ME.html', {'candidates9': candidates9, 'formme1': formme1})

    def post(self, request):
        formme1 = ResumeForm2(request.POST, request.FILES)
        if formme1.is_valid():
            ijk1 = formme1.save()
            return redirect('xyz9', pk=ijk1.pk)


class xyz9(View):
    def get(self, request, pk, *args, **kwargs):
        candidate9 = Resume.objects.get(pk=pk)
        template_path9 = 'resume10.html'
        context9 = {
            "candidate9": candidate9,
        }
        response9 = HttpResponse(content_type='application9/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        response9['Content-Disposition'] = "filename=CS_RESUME9.pdf"
        template9 = get_template(template_path9)
        html1 = template9.render(context9)
        pisa_status = pisa.CreatePDF(html1, dest=response9)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return response9


class FormME1(View):
    def get(self, request):
        formme1 = ResumeForm2()
        candidatesme1 = Resume.objects.all()
        return render(request, 'form1ME.html', {'candidatesme1': candidatesme1, 'formme1': formme1})

    def post(self, request):
        formme1 = ResumeForm2(request.POST, request.FILES)
        if formme1.is_valid():
            fgh1 = formme1.save()
            return redirect('pdfME1', pk=fgh1.pk)


class pdfME1(View):
    def get(self, request, pk, *args, **kwargs):
        candidateme1 = Resume.objects.get(pk=pk)
        template_pathme1 = 'resume1ME.html'
        contextme1 = {
            "candidateme1": candidateme1,
        }
        responseme1 = HttpResponse(content_type='applicationme1/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        responseme1['Content-Disposition'] = "filename=ME_RESUME1.pdf"
        templateme1 = get_template(template_pathme1)
        html1 = templateme1.render(contextme1)
        pisa_status = pisa.CreatePDF(html1, dest=responseme1)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return responseme1


class FormME2(View):
    def get(self, request):
        formme1 = ResumeForm2()
        candidatesme2 = Resume.objects.all()
        return render(request, 'form1ME.html', {'candidatesme2': candidatesme2, 'formme1': formme1})

    def post(self, request):
        formme1 = ResumeForm2(request.POST, request.FILES)
        if formme1.is_valid():
            fgh1 = formme1.save()
            return redirect('pdfME2', pk=fgh1.pk)


class pdfME2(View):
    def get(self, request, pk, *args, **kwargs):
        candidateme2 = Resume.objects.get(pk=pk)
        template_pathme2 = 'resume2ME.html'
        contextme2 = {
            "candidateme2": candidateme2,
        }
        responseme2 = HttpResponse(content_type='applicationme2/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        responseme2['Content-Disposition'] = "filename=ME_RESUME2.pdf"
        templateme2 = get_template(template_pathme2)
        html1 = templateme2.render(contextme2)
        pisa_status = pisa.CreatePDF(html1, dest=responseme2)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return responseme2


class FormME3(View):
    def get(self, request):
        formme1 = ResumeForm2()
        candidatesme3 = Resume.objects.all()
        return render(request, 'form1ME.html', {'candidatesme3': candidatesme3, 'formme1': formme1})

    def post(self, request):
        formme1 = ResumeForm2(request.POST, request.FILES)
        if formme1.is_valid():
            fgh1 = formme1.save()
            return redirect('pdfME3', pk=fgh1.pk)


class pdfME3(View):
    def get(self, request, pk, *args, **kwargs):
        candidateme3 = Resume.objects.get(pk=pk)
        template_pathme3 = 'resume3ME.html'
        contextme3 = {
            "candidateme3": candidateme3,
        }
        responseme3 = HttpResponse(content_type='applicationme3/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        responseme3['Content-Disposition'] = "filename=ME_RESUME3.pdf"
        templateme3 = get_template(template_pathme3)
        html1 = templateme3.render(contextme3)
        pisa_status = pisa.CreatePDF(html1, dest=responseme3)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return responseme3


class FormME4(View):
    def get(self, request):
        formme1 = ResumeForm2()
        candidatesme4 = Resume.objects.all()
        return render(request, 'form1ME.html', {'candidatesme4': candidatesme4, 'formme1': formme1})

    def post(self, request):
        formme1 = ResumeForm2(request.POST, request.FILES)
        if formme1.is_valid():
            fgh1 = formme1.save()
            return redirect('pdfME4', pk=fgh1.pk)


class pdfME4(View):
    def get(self, request, pk, *args, **kwargs):
        candidateme4 = Resume.objects.get(pk=pk)
        template_pathme4 = 'resume4ME.html'
        contextme4 = {
            "candidateme4": candidateme4,
        }
        responseme4 = HttpResponse(content_type='applicationme4/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        responseme4['Content-Disposition'] = "filename=ME_RESUME4.pdf"
        templateme4 = get_template(template_pathme4)
        html1 = templateme4.render(contextme4)
        pisa_status = pisa.CreatePDF(html1, dest=responseme4)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return responseme4


class FormME5(View):
    def get(self, request):
        formme1 = ResumeForm2()
        candidatesme5 = Resume.objects.all()
        return render(request, 'form1ME.html', {'candidatesme5': candidatesme5, 'formme1': formme1})

    def post(self, request):
        formme1 = ResumeForm2(request.POST, request.FILES)
        if formme1.is_valid():
            fgh1 = formme1.save()
            return redirect('pdfME5', pk=fgh1.pk)


class pdfME5(View):
    def get(self, request, pk, *args, **kwargs):
        candidateme5 = Resume.objects.get(pk=pk)
        template_pathme5 = 'resume5ME.html'
        contextme5 = {
            "candidateme5": candidateme5,
        }
        responseme5 = HttpResponse(content_type='applicationme5/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        responseme5['Content-Disposition'] = "filename=ME_RESUME5.pdf"
        templateme5 = get_template(template_pathme5)
        html1 = templateme5.render(contextme5)
        pisa_status = pisa.CreatePDF(html1, dest=responseme5)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return responseme5


class FormEE1(View):
    def get(self, request):
        formme1 = ResumeForm2()
        candidatesee1 = Resume.objects.all()
        return render(request, 'form1ME.html', {'candidatesee1': candidatesee1, 'formme1': formme1})

    def post(self, request):
        formme1 = ResumeForm2(request.POST, request.FILES)
        if formme1.is_valid():
            fgh1 = formme1.save()
            return redirect('pdfEE1', pk=fgh1.pk)


class pdfEE1(View):
    def get(self, request, pk, *args, **kwargs):
        candidateee1 = Resume.objects.get(pk=pk)
        template_pathee1 = 'resume1EE.html'
        contextee1 = {
            "candidateee1": candidateee1,
        }
        responseee1 = HttpResponse(content_type='applicationee1/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        responseee1['Content-Disposition'] = "filename=EE_RESUME1.pdf"
        templateee1 = get_template(template_pathee1)
        html1 = templateee1.render(contextee1)
        pisa_status = pisa.CreatePDF(html1, dest=responseee1)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return responseee1


class FormEE2(View):
    def get(self, request):
        formme1 = ResumeForm2()
        candidatesee2 = Resume.objects.all()
        return render(request, 'form1ME.html', {'candidatesee2': candidatesee2, 'formme1': formme1})

    def post(self, request):
        formme1 = ResumeForm2(request.POST, request.FILES)
        if formme1.is_valid():
            fgh1 = formme1.save()
            return redirect('pdfEE2', pk=fgh1.pk)


class pdfEE2(View):
    def get(self, request, pk, *args, **kwargs):
        candidateee2 = Resume.objects.get(pk=pk)
        template_pathee2 = 'resume2EE.html'
        contextee2 = {
            "candidateee2": candidateee2,
        }
        responseee2 = HttpResponse(content_type='applicationee2/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        responseee2['Content-Disposition'] = "filename=EE_RESUME2.pdf"
        templateee2 = get_template(template_pathee2)
        html1 = templateee2.render(contextee2)
        pisa_status = pisa.CreatePDF(html1, dest=responseee2)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return responseee2


class FormEE3(View):
    def get(self, request):
        formme1 = ResumeForm2()
        candidatesee3 = Resume.objects.all()
        return render(request, 'form1ME.html', {'candidatesee3': candidatesee3, 'formme1': formme1})

    def post(self, request):
        formme1 = ResumeForm2(request.POST, request.FILES)
        if formme1.is_valid():
            fgh1 = formme1.save()
            return redirect('pdfEE3', pk=fgh1.pk)


class pdfEE3(View):
    def get(self, request, pk, *args, **kwargs):
        candidateee3 = Resume.objects.get(pk=pk)
        template_pathee3 = 'resume3EE.html'
        contextee3 = {
            "candidateee3": candidateee3,
        }
        responseee3 = HttpResponse(content_type='applicationee3/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        responseee3['Content-Disposition'] = "filename=EE_RESUME3.pdf"
        templateee3 = get_template(template_pathee3)
        html1 = templateee3.render(contextee3)
        pisa_status = pisa.CreatePDF(html1, dest=responseee3)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return responseee3


class FormEE4(View):
    def get(self, request):
        formme1 = ResumeForm2()
        candidatesee4 = Resume.objects.all()
        return render(request, 'form1ME.html', {'candidatesee4': candidatesee4, 'formme1': formme1})

    def post(self, request):
        formme1 = ResumeForm2(request.POST, request.FILES)
        if formme1.is_valid():
            fgh1 = formme1.save()
            return redirect('pdfEE4', pk=fgh1.pk)


class pdfEE4(View):
    def get(self, request, pk, *args, **kwargs):
        candidateee4 = Resume.objects.get(pk=pk)
        template_pathee4 = 'resume4EE.html'
        contextee4 = {
            "candidateee4": candidateee4,
        }
        responseee4 = HttpResponse(content_type='applicationee4/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        responseee4['Content-Disposition'] = "filename=EE_RESUME4.pdf"
        templateee4 = get_template(template_pathee4)
        html1 = templateee4.render(contextee4)
        pisa_status = pisa.CreatePDF(html1, dest=responseee4)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return responseee4


class FormEE5(View):
    def get(self, request):
        formme1 = ResumeForm2()
        candidatesee5 = Resume.objects.all()
        return render(request, 'form1ME.html', {'candidatesee5': candidatesee5, 'formme1': formme1})

    def post(self, request):
        formme1 = ResumeForm2(request.POST, request.FILES)
        if formme1.is_valid():
            fgh1 = formme1.save()
            return redirect('pdfEE5', pk=fgh1.pk)


class pdfEE5(View):
    def get(self, request, pk, *args, **kwargs):
        candidateee5 = Resume.objects.get(pk=pk)
        template_pathee5 = 'resume5EE.html'
        contextee5 = {
            "candidateee5": candidateee5,
        }
        responseee5 = HttpResponse(content_type='applicationee5/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        responseee5['Content-Disposition'] = "filename=EE_RESUME5.pdf"
        templateee5 = get_template(template_pathee5)
        html1 = templateee5.render(contextee5)
        pisa_status = pisa.CreatePDF(html1, dest=responseee5)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return responseee5


class FormECE1(View):
    def get(self, request):
        formme1 = ResumeForm2()
        candidatesee1 = Resume.objects.all()
        return render(request, 'form1ME.html', {'candidatesee1': candidatesee1, 'formme1': formme1})

    def post(self, request):
        formme1 = ResumeForm2(request.POST, request.FILES)
        if formme1.is_valid():
            fgh1 = formme1.save()
            return redirect('pdfECE1', pk=fgh1.pk)


class pdfECE1(View):
    def get(self, request, pk, *args, **kwargs):
        candidateee1 = Resume.objects.get(pk=pk)
        template_pathee1 = 'resume1ECE.html'
        contextee1 = {
            "candidateee1": candidateee1,
        }
        responseee1 = HttpResponse(content_type='applicationece1/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        responseee1['Content-Disposition'] = "filename=ECE_RESUME1.pdf"
        templateee1 = get_template(template_pathee1)
        html1 = templateee1.render(contextee1)
        pisa_status = pisa.CreatePDF(html1, dest=responseee1)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return responseee1


class FormECE2(View):
    def get(self, request):
        formme1 = ResumeForm2()
        candidatesee2 = Resume.objects.all()
        return render(request, 'form1ME.html', {'candidatesee2': candidatesee2, 'formme1': formme1})

    def post(self, request):
        formme1 = ResumeForm2(request.POST, request.FILES)
        if formme1.is_valid():
            fgh1 = formme1.save()
            return redirect('pdfECE2', pk=fgh1.pk)


class pdfECE2(View):
    def get(self, request, pk, *args, **kwargs):
        candidateee2 = Resume.objects.get(pk=pk)
        template_pathee2 = 'resume2ECE.html'
        contextee2 = {
            "candidateee2": candidateee2,
        }
        responseee2 = HttpResponse(content_type='applicationece2/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        responseee2['Content-Disposition'] = "filename=ECE_RESUME2.pdf"
        templateee2 = get_template(template_pathee2)
        html1 = templateee2.render(contextee2)
        pisa_status = pisa.CreatePDF(html1, dest=responseee2)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return responseee2


class FormECE3(View):
    def get(self, request):
        formme1 = ResumeForm2()
        candidatesee3 = Resume.objects.all()
        return render(request, 'form1ME.html', {'candidatesee3': candidatesee3, 'formme1': formme1})

    def post(self, request):
        formme1 = ResumeForm2(request.POST, request.FILES)
        if formme1.is_valid():
            fgh1 = formme1.save()
            return redirect('pdfECE3', pk=fgh1.pk)


class pdfECE3(View):
    def get(self, request, pk, *args, **kwargs):
        candidateee3 = Resume.objects.get(pk=pk)
        template_pathee3 = 'resume3ECE.html'
        contextee3 = {
            "candidateee3": candidateee3,
        }
        responseee3 = HttpResponse(content_type='applicationece3/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        responseee3['Content-Disposition'] = "filename=ECE_RESUME3.pdf"
        templateee3 = get_template(template_pathee3)
        html1 = templateee3.render(contextee3)
        pisa_status = pisa.CreatePDF(html1, dest=responseee3)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return responseee3


class FormECE4(View):
    def get(self, request):
        formme1 = ResumeForm2()
        candidatesee4 = Resume.objects.all()
        return render(request, 'form1ME.html', {'candidatesee4': candidatesee4, 'formme1': formme1})

    def post(self, request):
        formme1 = ResumeForm2(request.POST, request.FILES)
        if formme1.is_valid():
            fgh1 = formme1.save()
            return redirect('pdfECE4', pk=fgh1.pk)


class pdfECE4(View):
    def get(self, request, pk, *args, **kwargs):
        candidateee4 = Resume.objects.get(pk=pk)
        template_pathee4 = 'resume4ECE.html'
        contextee4 = {
            "candidateee4": candidateee4,
        }
        responseee4 = HttpResponse(content_type='applicationece4/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        responseee4['Content-Disposition'] = "filename=ECE_RESUME4.pdf"
        templateee4 = get_template(template_pathee4)
        html1 = templateee4.render(contextee4)
        pisa_status = pisa.CreatePDF(html1, dest=responseee4)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return responseee4


class FormECE5(View):
    def get(self, request):
        formme1 = ResumeForm2()
        candidatesee5 = Resume.objects.all()
        return render(request, 'form1ME.html', {'candidatesee5': candidatesee5, 'formme1': formme1})

    def post(self, request):
        formme1 = ResumeForm2(request.POST, request.FILES)
        if formme1.is_valid():
            fgh1 = formme1.save()
            return redirect('pdfECE5', pk=fgh1.pk)


class pdfECE5(View):
    def get(self, request, pk, *args, **kwargs):
        candidateee5 = Resume.objects.get(pk=pk)
        template_pathee5 = 'resume5ECE.html'
        contextee5 = {
            "candidateee5": candidateee5,
        }
        responseee5 = HttpResponse(content_type='applicationece5/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        responseee5['Content-Disposition'] = "filename=ECE_RESUME5.pdf"
        templateee5 = get_template(template_pathee5)
        html1 = templateee5.render(contextee5)
        pisa_status = pisa.CreatePDF(html1, dest=responseee5)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return responseee5


class FormBank1(View):
    def get(self, request):
        formbnk1 = ResumeForm3()
        candidatesbnk1 = Resume.objects.all()
        return render(request, 'form1Banking.html', {'candidatesbnk1': candidatesbnk1, 'formbnk1': formbnk1})

    def post(self, request):
        formbnk1 = ResumeForm3(request.POST, request.FILES)
        if formbnk1.is_valid():
            fgh1 = formbnk1.save()
            return redirect('pdfBANK1', pk=fgh1.pk)


class pdfBANK1(View):
    def get(self, request, pk, *args, **kwargs):
        candidatebnk1 = Resume.objects.get(pk=pk)
        template_pathbnk1 = 'resume1Banking.html'
        contextbnk1 = {
            "candidatebnk1": candidatebnk1,
        }
        responsebnk1 = HttpResponse(content_type='applicationbnk1/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        responsebnk1['Content-Disposition'] = "filename=BANK_RESUME1.pdf"
        templatebnk1 = get_template(template_pathbnk1)
        html1 = templatebnk1.render(contextbnk1)
        pisa_status = pisa.CreatePDF(html1, dest=responsebnk1)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return responsebnk1


class FormBank2(View):
    def get(self, request):
        formbnk2 = ResumeForm3()
        candidatesbnk2 = Resume.objects.all()
        return render(request, 'form2Banking.html', {'candidatesbnk2': candidatesbnk2, 'formbnk2': formbnk2})

    def post(self, request):
        formbnk2 = ResumeForm3(request.POST, request.FILES)
        if formbnk2.is_valid():
            fgh1 = formbnk2.save()
            return redirect('pdfBANK2', pk=fgh1.pk)


class pdfBANK2(View):
    def get(self, request, pk, *args, **kwargs):
        candidatebnk2 = Resume.objects.get(pk=pk)
        template_pathbnk2 = 'resume2Banking.html'
        contextbnk2 = {
            "candidatebnk2": candidatebnk2,
        }
        responsebnk2 = HttpResponse(content_type='applicationbnk2/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        responsebnk2['Content-Disposition'] = "filename=BANK_RESUME2.pdf"
        templatebnk2 = get_template(template_pathbnk2)
        html1 = templatebnk2.render(contextbnk2)
        pisa_status = pisa.CreatePDF(html1, dest=responsebnk2)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return responsebnk2


class FormBank3(View):
    def get(self, request):
        formbnk3 = ResumeForm3()
        candidatesbnk3 = Resume.objects.all()
        return render(request, 'form3Banking.html', {'candidatesbnk3': candidatesbnk3, 'formbnk3': formbnk3})

    def post(self, request):
        formbnk3 = ResumeForm3(request.POST, request.FILES)
        if formbnk3.is_valid():
            fgh1 = formbnk3.save()
            return redirect('pdfBANK3', pk=fgh1.pk)


class pdfBANK3(View):
    def get(self, request, pk, *args, **kwargs):
        candidatebnk3 = Resume.objects.get(pk=pk)
        template_pathbnk3 = 'resume3Banking.html'
        contextbnk3 = {
            "candidatebnk3": candidatebnk3,
        }
        responsebnk3 = HttpResponse(content_type='applicationbnk3/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        responsebnk3['Content-Disposition'] = "filename=BANK_RESUME3.pdf"
        templatebnk3 = get_template(template_pathbnk3)
        html1 = templatebnk3.render(contextbnk3)
        pisa_status = pisa.CreatePDF(html1, dest=responsebnk3)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return responsebnk3


class FormBank4(View):
    def get(self, request):
        formbnk4 = ResumeForm3()
        candidatesbnk4 = Resume.objects.all()
        return render(request, 'form4Banking.html', {'candidatesbnk4': candidatesbnk4, 'formbnk4': formbnk4})

    def post(self, request):
        formbnk4 = ResumeForm3(request.POST, request.FILES)
        if formbnk4.is_valid():
            fgh1 = formbnk4.save()
            return redirect('pdfBANK4', pk=fgh1.pk)


class pdfBANK4(View):
    def get(self, request, pk, *args, **kwargs):
        candidatebnk4 = Resume.objects.get(pk=pk)
        template_pathbnk4 = 'resume4Banking.html'
        contextbnk4 = {
            "candidatebnk4": candidatebnk4,
        }
        responsebnk4 = HttpResponse(content_type='applicationbnk4/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        responsebnk4['Content-Disposition'] = "filename=BANK_RESUME4.pdf"
        templatebnk4 = get_template(template_pathbnk4)
        html1 = templatebnk4.render(contextbnk4)
        pisa_status = pisa.CreatePDF(html1, dest=responsebnk4)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return responsebnk4


class FormBank5(View):
    def get(self, request):
        formbnk5 = ResumeForm3()
        candidatesbnk5 = Resume.objects.all()
        return render(request, 'form5Banking.html', {'candidatesbnk5': candidatesbnk5, 'formbnk5': formbnk5})

    def post(self, request):
        formbnk5 = ResumeForm3(request.POST, request.FILES)
        if formbnk5.is_valid():
            fgh1 = formbnk5.save()
            return redirect('pdfBANK5', pk=fgh1.pk)


class pdfBANK5(View):
    def get(self, request, pk, *args, **kwargs):
        candidatebnk5 = Resume.objects.get(pk=pk)
        template_pathbnk5 = 'resume5Banking.html'
        contextbnk5 = {
            "candidatebnk5": candidatebnk5,
        }
        responsebnk5 = HttpResponse(content_type='applicationbnk5/pdf')
        # response['Content-Disposition'] = "attachment; filename=RESUME.pdf"
        responsebnk5['Content-Disposition'] = "filename=BANK_RESUME5.pdf"
        templatebnk5 = get_template(template_pathbnk5)
        html1 = templatebnk5.render(contextbnk5)
        pisa_status = pisa.CreatePDF(html1, dest=responsebnk5)
        if pisa_status.err:
            return HttpResponse('we had some errors <pre>' + html1 + '</pre>')
        return responsebnk5
