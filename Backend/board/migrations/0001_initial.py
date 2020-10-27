# Generated by Django 3.1.2 on 2020-10-27 01:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User_Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField()),
                ('board_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.board')),
                ('user_pk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('board_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.board')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('content', models.TextField()),
                ('lock', models.BooleanField()),
                ('tab_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.tab')),
                ('type_pk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='board.type')),
                ('user_pk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('note_pk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='board.note')),
                ('tab_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.tab')),
                ('type_pk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='board.type')),
                ('user_pk', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='user_list',
            field=models.ManyToManyField(through='board.User_Board', to=settings.AUTH_USER_MODEL),
        ),
    ]
