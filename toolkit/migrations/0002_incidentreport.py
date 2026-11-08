
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolkit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='IncidentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offenderUsername', models.CharField(blank=True, max_length=200)),
                ('offenderProfileUrl', models.URLField(blank=True, max_length=500)),
                ('incidentDetails', models.TextField()),
                ('requestPeerSupport', models.BooleanField(default=False)),
                ('contactPreference', models.CharField(blank=True, max_length=200)),
                ('status', models.CharField(choices=[('saved', 'প্রমাণ সংরক্ষিত / Evidence Saved'), ('supportRequested', 'সহায়তা চাওয়া হয়েছে / Support Requested'), ('resolved', 'সমাধান হয়েছে / Resolved')], default='saved', max_length=30)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('completedEvidenceSteps', models.ManyToManyField(blank=True, to='toolkit.evidencestep')),
                ('situation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='toolkit.situation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incidentReports', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-createdAt'],
            },
        ),
    ]
