# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2022-11-23 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=100)),
                ('term1key', models.CharField(max_length=100)),
                ('term1value', models.CharField(max_length=100)),
                ('term2key', models.CharField(max_length=100)),
                ('term2value', models.CharField(max_length=100)),
                ('term3key', models.CharField(max_length=100)),
                ('term3value', models.CharField(max_length=100)),
                ('term4key', models.CharField(max_length=100)),
                ('term4value', models.CharField(max_length=100)),
                ('term5key', models.CharField(max_length=100)),
                ('term5value', models.CharField(max_length=100)),
                ('term6key', models.CharField(max_length=100)),
                ('term6value', models.CharField(max_length=100)),
                ('term7key', models.CharField(max_length=100)),
                ('term7value', models.CharField(max_length=100)),
                ('term8key', models.CharField(max_length=100)),
                ('term8value', models.CharField(max_length=100)),
                ('term9key', models.CharField(max_length=100)),
                ('term9value', models.CharField(max_length=100)),
                ('term10key', models.CharField(max_length=100)),
                ('term10value', models.CharField(max_length=100)),
                ('term11key', models.CharField(max_length=100)),
                ('term11value', models.CharField(max_length=100)),
                ('term12key', models.CharField(max_length=100)),
                ('term12value', models.CharField(max_length=100)),
                ('term13key', models.CharField(max_length=100)),
                ('term13value', models.CharField(max_length=100)),
                ('term14key', models.CharField(max_length=100)),
                ('term14value', models.CharField(max_length=100)),
                ('term15key', models.CharField(max_length=100)),
                ('term15value', models.CharField(max_length=100)),
                ('term16key', models.CharField(max_length=100)),
                ('term16value', models.CharField(max_length=100)),
                ('term17key', models.CharField(max_length=100)),
                ('term17value', models.CharField(max_length=100)),
                ('term18key', models.CharField(max_length=100)),
                ('term18value', models.CharField(max_length=100)),
                ('term19key', models.CharField(max_length=100)),
                ('term19value', models.CharField(max_length=100)),
                ('term20key', models.CharField(max_length=100)),
                ('term20value', models.CharField(max_length=100)),
                ('term21key', models.CharField(max_length=100)),
                ('term21value', models.CharField(max_length=100)),
                ('term22key', models.CharField(max_length=100)),
                ('term22value', models.CharField(max_length=100)),
                ('term23key', models.CharField(max_length=100)),
                ('term23value', models.CharField(max_length=100)),
                ('term24key', models.CharField(max_length=100)),
                ('term24value', models.CharField(max_length=100)),
                ('term25key', models.CharField(max_length=100)),
                ('term25value', models.CharField(max_length=100)),
                ('term26key', models.CharField(max_length=100)),
                ('term26value', models.CharField(max_length=100)),
                ('term27key', models.CharField(max_length=100)),
                ('term27value', models.CharField(max_length=100)),
                ('term28key', models.CharField(max_length=100)),
                ('term28value', models.CharField(max_length=100)),
                ('term29key', models.CharField(max_length=100)),
                ('term29value', models.CharField(max_length=100)),
                ('term30key', models.CharField(max_length=100)),
                ('term30value', models.CharField(max_length=100)),
                ('term31key', models.CharField(max_length=100)),
                ('term31value', models.CharField(max_length=100)),
                ('term32key', models.CharField(max_length=100)),
                ('term32value', models.CharField(max_length=100)),
                ('term33key', models.CharField(max_length=100)),
                ('term33value', models.CharField(max_length=100)),
                ('term34key', models.CharField(max_length=100)),
                ('term34value', models.CharField(max_length=100)),
                ('term35key', models.CharField(max_length=100)),
                ('term35value', models.CharField(max_length=100)),
                ('term36key', models.CharField(max_length=100)),
                ('term36value', models.CharField(max_length=100)),
                ('term37key', models.CharField(max_length=100)),
                ('term37value', models.CharField(max_length=100)),
                ('term38key', models.CharField(max_length=100)),
                ('term38value', models.CharField(max_length=100)),
                ('term39key', models.CharField(max_length=100)),
                ('term39value', models.CharField(max_length=100)),
                ('term40key', models.CharField(max_length=100)),
                ('term40value', models.CharField(max_length=100)),
                ('term41key', models.CharField(max_length=100)),
                ('term41value', models.CharField(max_length=100)),
                ('term42key', models.CharField(max_length=100)),
                ('term42value', models.CharField(max_length=100)),
                ('term43key', models.CharField(max_length=100)),
                ('term43value', models.CharField(max_length=100)),
                ('term44key', models.CharField(max_length=100)),
                ('term44value', models.CharField(max_length=100)),
                ('term45key', models.CharField(max_length=100)),
                ('term45value', models.CharField(max_length=100)),
                ('term46key', models.CharField(max_length=100)),
                ('term46value', models.CharField(max_length=100)),
                ('term47key', models.CharField(max_length=100)),
                ('term47value', models.CharField(max_length=100)),
                ('term48key', models.CharField(max_length=100)),
                ('term48value', models.CharField(max_length=100)),
                ('term49key', models.CharField(max_length=100)),
                ('term49value', models.CharField(max_length=100)),
                ('term50key', models.CharField(max_length=100)),
                ('term50value', models.CharField(max_length=100)),
                ('term51key', models.CharField(max_length=100)),
                ('term51value', models.CharField(max_length=100)),
                ('term52key', models.CharField(max_length=100)),
                ('term52value', models.CharField(max_length=100)),
                ('term53key', models.CharField(max_length=100)),
                ('term53value', models.CharField(max_length=100)),
                ('term54key', models.CharField(max_length=100)),
                ('term54value', models.CharField(max_length=100)),
                ('term55key', models.CharField(max_length=100)),
                ('term55value', models.CharField(max_length=100)),
                ('term56key', models.CharField(max_length=100)),
                ('term56value', models.CharField(max_length=100)),
                ('term57key', models.CharField(max_length=100)),
                ('term57value', models.CharField(max_length=100)),
                ('term58key', models.CharField(max_length=100)),
                ('term58value', models.CharField(max_length=100)),
                ('term59key', models.CharField(max_length=100)),
                ('term59value', models.CharField(max_length=100)),
                ('term60key', models.CharField(max_length=100)),
                ('term60value', models.CharField(max_length=100)),
                ('term61key', models.CharField(max_length=100)),
                ('term61value', models.CharField(max_length=100)),
                ('term62key', models.CharField(max_length=100)),
                ('term62value', models.CharField(max_length=100)),
                ('term63key', models.CharField(max_length=100)),
                ('term63value', models.CharField(max_length=100)),
                ('term64key', models.CharField(max_length=100)),
                ('term64value', models.CharField(max_length=100)),
                ('term65key', models.CharField(max_length=100)),
                ('term65value', models.CharField(max_length=100)),
                ('term66key', models.CharField(max_length=100)),
                ('term66value', models.CharField(max_length=100)),
                ('term67key', models.CharField(max_length=100)),
                ('term67value', models.CharField(max_length=100)),
                ('term68key', models.CharField(max_length=100)),
                ('term68value', models.CharField(max_length=100)),
                ('term69key', models.CharField(max_length=100)),
                ('term69value', models.CharField(max_length=100)),
                ('term70key', models.CharField(max_length=100)),
                ('term70value', models.CharField(max_length=100)),
                ('term71key', models.CharField(max_length=100)),
                ('term71value', models.CharField(max_length=100)),
                ('term72key', models.CharField(max_length=100)),
                ('term72value', models.CharField(max_length=100)),
                ('term73key', models.CharField(max_length=100)),
                ('term73value', models.CharField(max_length=100)),
                ('term74key', models.CharField(max_length=100)),
                ('term74value', models.CharField(max_length=100)),
                ('term75key', models.CharField(max_length=100)),
                ('term75value', models.CharField(max_length=100)),
                ('term76key', models.CharField(max_length=100)),
                ('term76value', models.CharField(max_length=100)),
                ('term77key', models.CharField(max_length=100)),
                ('term77value', models.CharField(max_length=100)),
                ('term78key', models.CharField(max_length=100)),
                ('term78value', models.CharField(max_length=100)),
                ('term79key', models.CharField(max_length=100)),
                ('term79value', models.CharField(max_length=100)),
                ('term80key', models.CharField(max_length=100)),
                ('term80value', models.CharField(max_length=100)),
                ('term81key', models.CharField(max_length=100)),
                ('term81value', models.CharField(max_length=100)),
                ('term82key', models.CharField(max_length=100)),
                ('term82value', models.CharField(max_length=100)),
                ('term83key', models.CharField(max_length=100)),
                ('term83value', models.CharField(max_length=100)),
                ('term84key', models.CharField(max_length=100)),
                ('term84value', models.CharField(max_length=100)),
                ('term85key', models.CharField(max_length=100)),
                ('term85value', models.CharField(max_length=100)),
                ('term86key', models.CharField(max_length=100)),
                ('term86value', models.CharField(max_length=100)),
                ('term87key', models.CharField(max_length=100)),
                ('term87value', models.CharField(max_length=100)),
                ('term88key', models.CharField(max_length=100)),
                ('term88value', models.CharField(max_length=100)),
                ('term89key', models.CharField(max_length=100)),
                ('term89value', models.CharField(max_length=100)),
                ('term90key', models.CharField(max_length=100)),
                ('term90value', models.CharField(max_length=100)),
                ('term91key', models.CharField(max_length=100)),
                ('term91value', models.CharField(max_length=100)),
                ('term92key', models.CharField(max_length=100)),
                ('term92value', models.CharField(max_length=100)),
                ('term93key', models.CharField(max_length=100)),
                ('term93value', models.CharField(max_length=100)),
                ('term94key', models.CharField(max_length=100)),
                ('term94value', models.CharField(max_length=100)),
                ('term95key', models.CharField(max_length=100)),
                ('term95value', models.CharField(max_length=100)),
                ('term96key', models.CharField(max_length=100)),
                ('term96value', models.CharField(max_length=100)),
                ('term97key', models.CharField(max_length=100)),
                ('term97value', models.CharField(max_length=100)),
                ('term98key', models.CharField(max_length=100)),
                ('term98value', models.CharField(max_length=100)),
                ('term99key', models.CharField(max_length=100)),
                ('term99value', models.CharField(max_length=100)),
                ('term100key', models.CharField(max_length=100)),
                ('term100value', models.CharField(max_length=100)),
            ],
        ),
    ]
