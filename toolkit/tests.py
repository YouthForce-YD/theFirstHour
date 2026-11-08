from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from toolkit.models import Situation, EvidenceStep, SupportChannel, IncidentReport


class ToolkitFeatureTests(TestCase):
    def setUp(self):
        self.testClient = Client()
        self.testUser = User.objects.create_user(
            username='testUser',
            password='TestPassword123!'
        )
        self.secondaryUser = User.objects.create_user(
            username='secondaryUser',
            password='TestPassword123!'
        )
        self.sampleSituation = Situation.objects.create(
            slug='accountHacked',
            titleBn='অ্যাকাউন্ট হ্যাক হয়েছে',
            titleEn='Account Hacked',
            immediateActionBn='পাসওয়ার্ড পরিবর্তন করুন',
            immediateActionEn='Change password immediately',
            detailedStepsBn='ধাপ ১\nধাপ ২',
            detailedStepsEn='Step 1\nStep 2',
            isActive=True
        )
        self.sampleEvidenceStep = EvidenceStep.objects.create(
            stepLabelBn='১',
            stepNumber=1,
            instructionBn='স্ক্রিনশট সংরক্ষণ করুন',
            instructionEn='Save screenshot evidence'
        )
        self.sampleChannel = SupportChannel.objects.create(
            channelType='emergency',
            titleBn='জাতীয় জরুরি সেবা',
            titleEn='National Emergency Service',
            phoneDial='999',
            isActive=True
        )

    def testHomeViewUnauthenticated(self):
        response = self.testClient.get(reverse('toolkit:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'অ্যাকাউন্ট হ্যাক হয়েছে')
        self.assertContains(response, 'জাতীয় জরুরি সেবা')

    def testHomeViewAuthenticated(self):
        self.testClient.force_login(self.testUser)
        response = self.testClient.get(reverse('toolkit:home'))
        self.assertEqual(response.status_code, 200)

    def testSituationDetailViewFound(self):
        response = self.testClient.get(reverse('toolkit:situationDetail', kwargs={'slug': 'accountHacked'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'পাসওয়ার্ড পরিবর্তন করুন')

    def testSituationDetailViewNotFound(self):
        response = self.testClient.get(reverse('toolkit:situationDetail', kwargs={'slug': 'nonExistentSlug'}))
        self.assertEqual(response.status_code, 404)

    def testRegisterViewGet(self):
        response = self.testClient.get(reverse('toolkit:register'))
        self.assertEqual(response.status_code, 200)

    def testRegisterViewPostSuccess(self):
        registrationData = {
            'username': 'newRegisteredUser',
            'password1': 'StrongSecret987!',
            'password2': 'StrongSecret987!',
        }
        response = self.testClient.post(reverse('toolkit:register'), registrationData)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('toolkit:dashboard'))
        self.assertTrue(User.objects.filter(username='newRegisteredUser').exists())

    def testLoginViewGetAndPost(self):
        response = self.testClient.get(reverse('toolkit:login'))
        self.assertEqual(response.status_code, 200)

        loginData = {
            'username': 'testUser',
            'password': 'TestPassword123!',
        }
        loginResponse = self.testClient.post(reverse('toolkit:login'), loginData)
        self.assertEqual(loginResponse.status_code, 302)
        self.assertRedirects(loginResponse, reverse('toolkit:dashboard'))

    def testDashboardRequiresLogin(self):
        response = self.testClient.get(reverse('toolkit:dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('toolkit:login'), response.url)

    def testSaveIncidentAndDashboardListing(self):
        self.testClient.force_login(self.testUser)
        incidentPayload = {
            'situationId': self.sampleSituation.id,
            'offenderUsername': 'badActor123',
            'offenderProfileUrl': 'https://facebook.com/badActor123',
            'incidentDetails': 'Received suspicious threatening messages.',
            'requestPeerSupport': 'on',
            'contactPreference': 'email@example.com',
            'evidenceSteps': [self.sampleEvidenceStep.id],
        }
        saveResponse = self.testClient.post(reverse('toolkit:saveIncident'), incidentPayload)
        self.assertEqual(saveResponse.status_code, 302)
        self.assertRedirects(saveResponse, reverse('toolkit:dashboard'))

        createdReport = IncidentReport.objects.filter(user=self.testUser).first()
        self.assertIsNotNone(createdReport)
        self.assertEqual(createdReport.offenderUsername, 'badActor123')
        self.assertEqual(createdReport.status, 'supportRequested')
        self.assertEqual(createdReport.completedEvidenceSteps.count(), 1)

        dashboardResponse = self.testClient.get(reverse('toolkit:dashboard'))
        self.assertEqual(dashboardResponse.status_code, 200)
        self.assertContains(dashboardResponse, 'badActor123')

    def testDeleteIncidentSecurity(self):
        sampleReport = IncidentReport.objects.create(
            user=self.testUser,
            situation=self.sampleSituation,
            incidentDetails='Private user data',
            status='saved'
        )
        self.testClient.force_login(self.secondaryUser)
        unauthorizedDelete = self.testClient.post(
            reverse('toolkit:deleteIncident', kwargs={'reportId': sampleReport.id})
        )
        self.assertEqual(unauthorizedDelete.status_code, 404)
        self.assertTrue(IncidentReport.objects.filter(id=sampleReport.id).exists())

        self.testClient.force_login(self.testUser)
        authorizedDelete = self.testClient.post(
            reverse('toolkit:deleteIncident', kwargs={'reportId': sampleReport.id})
        )
        self.assertEqual(authorizedDelete.status_code, 302)
        self.assertRedirects(authorizedDelete, reverse('toolkit:dashboard'))
        self.assertFalse(IncidentReport.objects.filter(id=sampleReport.id).exists())

    def testLogoutView(self):
        self.testClient.force_login(self.testUser)
        logoutResponse = self.testClient.post(reverse('toolkit:logout'))
        self.assertEqual(logoutResponse.status_code, 302)
        self.assertRedirects(logoutResponse, reverse('toolkit:home'))
