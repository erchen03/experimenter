# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-05 19:28
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("experiments", "0015_auto_20180703_1922"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExperimentComment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "section",
                    models.CharField(
                        choices=[
                            ("overview", "Overview"),
                            ("population", "Population"),
                            ("branches", "Firefox & Branches"),
                            ("objectives", "Objectives"),
                            ("analysis", "Analysis"),
                            ("risks", "Risks"),
                            ("testing", "Testing"),
                        ],
                        max_length=255,
                    ),
                ),
                ("text", models.TextField()),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "experiment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="experiments.Experiment",
                    ),
                ),
            ],
            options={
                "verbose_name": "Experiment Comment",
                "verbose_name_plural": "Experiment Comments",
                "ordering": ("created_on",),
            },
        )
    ]