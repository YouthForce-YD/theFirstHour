
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EvidenceStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stepLabelBn', models.CharField(max_length=10)),
                ('stepNumber', models.PositiveSmallIntegerField(unique=True)),
                ('instructionBn', models.CharField(max_length=255)),
                ('instructionEn', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['stepNumber'],
            },
        ),
        migrations.CreateModel(
            name='Situation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('titleBn', models.CharField(max_length=200)),
                ('titleEn', models.CharField(max_length=200)),
                ('iconName', models.CharField(default='shield-alert', max_length=60)),
                ('immediateActionBn', models.TextField()),
                ('immediateActionEn', models.TextField()),
                ('actionBtnBn', models.CharField(default='রিপোর্ট করুন', max_length=100)),
                ('actionBtnEn', models.CharField(default='Report Now', max_length=100)),
                ('displayOrder', models.PositiveSmallIntegerField(default=0)),
                ('isActive', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['displayOrder', 'id'],
            },
        ),
        migrations.CreateModel(
            name='SupportChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channelType', models.CharField(choices=[('emergency', 'Emergency Hotline'), ('helpline', 'National Helpline'), ('cyberPolice', 'Police Cyber Support'), ('platform', 'Platform Report'), ('peerSupport', 'Peer Support')], max_length=30)),
                ('badgeBn', models.CharField(blank=True, max_length=100)),
                ('badgeEn', models.CharField(blank=True, max_length=100)),
                ('titleBn', models.CharField(max_length=200)),
                ('titleEn', models.CharField(max_length=200)),
                ('phoneDisplayBn', models.CharField(blank=True, max_length=50)),
                ('phoneDisplayEn', models.CharField(blank=True, max_length=50)),
                ('phoneDial', models.CharField(blank=True, max_length=30)),
                ('callBtnBn', models.CharField(blank=True, max_length=100)),
                ('callBtnEn', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('externalUrl', models.URLField(blank=True)),
                ('descriptionBn', models.TextField(blank=True)),
                ('descriptionEn', models.TextField(blank=True)),
                ('iconName', models.CharField(default='phone', max_length=60)),
                ('displayOrder', models.PositiveSmallIntegerField(default=0)),
                ('isActive', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['displayOrder', 'id'],
            },
        ),
    ]
