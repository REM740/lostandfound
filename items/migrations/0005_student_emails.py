from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_add_department_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='founditem',
            name='claimed_by_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='founditem',
            name='found_by_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='lostitem',
            name='lost_by_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
