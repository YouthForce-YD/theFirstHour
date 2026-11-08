from django.db import models
from django.contrib.auth.models import User


class Situation(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    titleBn = models.CharField(max_length=200)
    titleEn = models.CharField(max_length=200)
    iconName = models.CharField(max_length=60, default='shield-alert')
    immediateActionBn = models.TextField()
    immediateActionEn = models.TextField()
    detailedStepsBn = models.TextField(blank=True)
    detailedStepsEn = models.TextField(blank=True)
    whatNotToDoBn = models.TextField(blank=True)
    whatNotToDoEn = models.TextField(blank=True)
    platformGuideBn = models.TextField(blank=True)
    platformGuideEn = models.TextField(blank=True)
    actionBtnBn = models.CharField(max_length=100, default='রিপোর্ট করুন')
    actionBtnEn = models.CharField(max_length=100, default='Report Now')
    displayOrder = models.PositiveSmallIntegerField(default=0)
    isActive = models.BooleanField(default=True)

    class Meta:
        ordering = ['displayOrder', 'id']

    def __str__(self):
        return f"{self.titleBn} ({self.titleEn})"

    def getStepsListBn(self):
        return [line.strip() for line in self.detailedStepsBn.splitlines() if line.strip()]

    def getStepsListEn(self):
        return [line.strip() for line in self.detailedStepsEn.splitlines() if line.strip()]

    def getStepPairs(self):
        bnList = self.getStepsListBn()
        enList = self.getStepsListEn()
        maxLength = max(len(bnList), len(enList))
        pairs = []
        for idx in range(maxLength):
            bnText = bnList[idx] if idx < len(bnList) else ''
            enText = enList[idx] if idx < len(enList) else ''
            pairs.append({'index': idx + 1, 'bn': bnText, 'en': enText})
        return pairs


class EvidenceStep(models.Model):
    stepLabelBn = models.CharField(max_length=10)
    stepNumber = models.PositiveSmallIntegerField(unique=True)
    instructionBn = models.CharField(max_length=255)
    instructionEn = models.CharField(max_length=255)

    class Meta:
        ordering = ['stepNumber']

    def __str__(self):
        return f"{self.stepNumber}. {self.instructionEn}"


class SupportChannel(models.Model):
    channelTypes = [
        ('emergency', 'Emergency Hotline'),
        ('helpline', 'National Helpline'),
        ('cyberPolice', 'Police Cyber Support'),
        ('platform', 'Platform Report'),
        ('peerSupport', 'Peer Support'),
    ]

    channelType = models.CharField(max_length=30, choices=channelTypes)
    badgeBn = models.CharField(max_length=100, blank=True)
    badgeEn = models.CharField(max_length=100, blank=True)
    titleBn = models.CharField(max_length=200)
    titleEn = models.CharField(max_length=200)
    phoneDisplayBn = models.CharField(max_length=50, blank=True)
    phoneDisplayEn = models.CharField(max_length=50, blank=True)
    phoneDial = models.CharField(max_length=30, blank=True)
    callBtnBn = models.CharField(max_length=100, blank=True)
    callBtnEn = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    externalUrl = models.URLField(blank=True)
    descriptionBn = models.TextField(blank=True)
    descriptionEn = models.TextField(blank=True)
    iconName = models.CharField(max_length=60, default='phone')
    displayOrder = models.PositiveSmallIntegerField(default=0)
    isActive = models.BooleanField(default=True)

    class Meta:
        ordering = ['displayOrder', 'id']

    def __str__(self):
        return f"{self.titleBn} ({self.titleEn})"


class IncidentReport(models.Model):
    statusChoices = [
        ('saved', 'প্রমাণ সংরক্ষিত / Evidence Saved'),
        ('supportRequested', 'সহায়তা চাওয়া হয়েছে / Support Requested'),
        ('resolved', 'সমাধান হয়েছে / Resolved'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incidentReports')
    situation = models.ForeignKey(Situation, on_delete=models.SET_NULL, null=True)
    offenderUsername = models.CharField(max_length=200, blank=True)
    offenderProfileUrl = models.URLField(max_length=500, blank=True)
    incidentDetails = models.TextField()
    completedEvidenceSteps = models.ManyToManyField(EvidenceStep, blank=True)
    requestPeerSupport = models.BooleanField(default=False)
    contactPreference = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=30, choices=statusChoices, default='saved')
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-createdAt']

    def __str__(self):
        return f"{self.user.username} - {self.createdAt.strftime('%Y-%m-%d %H:%M')}"
