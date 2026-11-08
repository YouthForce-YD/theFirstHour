
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toolkit', '0002_incidentreport'),
    ]

    operations = [
        migrations.AddField(
            model_name='situation',
            name='detailedStepsBn',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='situation',
            name='detailedStepsEn',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='situation',
            name='platformGuideBn',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='situation',
            name='platformGuideEn',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='situation',
            name='whatNotToDoBn',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='situation',
            name='whatNotToDoEn',
            field=models.TextField(blank=True),
        ),
    ]
