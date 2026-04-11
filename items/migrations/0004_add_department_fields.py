from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_founditem_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='founditem',
            name='department',
            field=models.CharField(
                blank=True,
                choices=[
                    ('CON', 'CON'),
                    ('YAL-CBA', 'YAL-CBA'),
                    ('CAS', 'CAS'),
                    ('COE', 'COE'),
                    ('CCS', 'CCS'),
                    ('CTH', 'CTH'),
                    ('CED', 'CED'),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name='lostitem',
            name='department',
            field=models.CharField(
                blank=True,
                choices=[
                    ('CON', 'CON'),
                    ('YAL-CBA', 'YAL-CBA'),
                    ('CAS', 'CAS'),
                    ('COE', 'COE'),
                    ('CCS', 'CCS'),
                    ('CTH', 'CTH'),
                    ('CED', 'CED'),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]
