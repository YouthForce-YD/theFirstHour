from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Situation, EvidenceStep, SupportChannel, IncidentReport


def homeView(request):
    situations = Situation.objects.filter(isActive=True)
    evidenceSteps = EvidenceStep.objects.all()
    supportChannels = SupportChannel.objects.filter(isActive=True)
    userReportsCount = 0

    if request.user.is_authenticated:
        userReportsCount = IncidentReport.objects.filter(user=request.user).count()

    contextData = {
        'situations': situations,
        'evidenceSteps': evidenceSteps,
        'supportChannels': supportChannels,
        'userReportsCount': userReportsCount,
    }
    return render(request, 'toolkit/home.html', contextData)


def situationDetailView(request, slug):
    situation = get_object_or_404(Situation, slug=slug, isActive=True)
    otherSituations = Situation.objects.filter(isActive=True).exclude(id=situation.id)
    evidenceSteps = EvidenceStep.objects.all()
    supportChannels = SupportChannel.objects.filter(isActive=True)

    contextData = {
        'situation': situation,
        'stepPairs': situation.getStepPairs(),
        'otherSituations': otherSituations,
        'evidenceSteps': evidenceSteps,
        'supportChannels': supportChannels,
    }
    return render(request, 'toolkit/situationDetail.html', contextData)


def registerView(request):
    if request.user.is_authenticated:
        return redirect('toolkit:dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'আপনার নিরাপদ অ্যাকাউন্ট তৈরি হয়েছে। / Your safe account has been created.')
            return redirect('toolkit:dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'toolkit/register.html', {'form': form})


def loginView(request):
    if request.user.is_authenticated:
        return redirect('toolkit:dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            nextUrl = request.GET.get('next') or 'toolkit:dashboard'
            return redirect(nextUrl)
    else:
        form = AuthenticationForm()

    return render(request, 'toolkit/login.html', {'form': form})


def logoutView(request):
    if request.method == 'POST':
        logout(request)
    return redirect('toolkit:home')


@login_required(login_url='toolkit:login')
def saveIncidentAction(request):
    if request.method == 'POST':
        situationId = request.POST.get('situationId')
        offenderUsername = request.POST.get('offenderUsername', '').strip()
        offenderProfileUrl = request.POST.get('offenderProfileUrl', '').strip()
        incidentDetails = request.POST.get('incidentDetails', '').strip()
        requestPeerSupport = request.POST.get('requestPeerSupport') == 'on'
        contactPreference = request.POST.get('contactPreference', '').strip()
        stepIds = request.POST.getlist('evidenceSteps')

        if incidentDetails:
            situation = Situation.objects.filter(id=situationId).first() if situationId else None
            reportStatus = 'supportRequested' if requestPeerSupport else 'saved'

            report = IncidentReport.objects.create(
                user=request.user,
                situation=situation,
                offenderUsername=offenderUsername,
                offenderProfileUrl=offenderProfileUrl,
                incidentDetails=incidentDetails,
                requestPeerSupport=requestPeerSupport,
                contactPreference=contactPreference,
                status=reportStatus,
            )

            if stepIds:
                steps = EvidenceStep.objects.filter(id__in=stepIds)
                report.completedEvidenceSteps.set(steps)

            messages.success(
                request,
                'আপনার তথ্যের রেকর্ড ও প্রমাণ লগ নিরাপদে সংরক্ষিত হয়েছে। / Your evidence log has been safely saved.'
            )
            return redirect('toolkit:dashboard')

    return redirect('toolkit:home')


@login_required(login_url='toolkit:login')
def dashboardView(request):
    reports = IncidentReport.objects.filter(user=request.user).select_related('situation').prefetch_related('completedEvidenceSteps')
    situations = Situation.objects.filter(isActive=True)
    evidenceSteps = EvidenceStep.objects.all()

    contextData = {
        'reports': reports,
        'situations': situations,
        'evidenceSteps': evidenceSteps,
    }
    return render(request, 'toolkit/dashboard.html', contextData)


@login_required(login_url='toolkit:login')
def deleteIncidentView(request, reportId):
    report = get_object_or_404(IncidentReport, id=reportId, user=request.user)
    if request.method == 'POST':
        report.delete()
        messages.success(request, 'রেকর্ডটি মুছে ফেলা হয়েছে। / Record deleted.')
    return redirect('toolkit:dashboard')
