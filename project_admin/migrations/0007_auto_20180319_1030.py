# Generated by Django 2.0.3 on 2018-03-19 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_admin', '0006_auto_20180308_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('basename', models.CharField(max_length=200)),
                ('created', models.DateTimeField()),
                ('download_url', models.URLField()),
                ('source', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_admin.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMember',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, null=True)),
                ('date_joined', models.DateTimeField()),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_admin.ProjectGroup')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_admin.Project')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_admin.ProjectMember'),
        ),
        migrations.AddField(
            model_name='file',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_admin.Project'),
        ),
    ]