from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('code', models.CharField(max_length=20, unique=True)),
                ('status', models.CharField(default='open', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'app_label': 'elections',
            },
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='candidates',
                    to='elections.election',
                )),
                ('name', models.CharField(max_length=200)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'app_label': 'elections',
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Ballot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='ballots',
                    to='elections.election',
                )),
                ('voter_name', models.CharField(max_length=200)),
                ('ranking', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'app_label': 'elections',
            },
        ),
        migrations.AlterUniqueTogether(
            name='ballot',
            unique_together={('election', 'voter_name')},
        ),
    ]
