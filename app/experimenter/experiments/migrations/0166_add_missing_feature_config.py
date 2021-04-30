# Generated by Django 3.1.8 on 2021-04-29 17:22

from django.db import migrations


def set_feature_config(apps, schema_editor):
    NimbusExperiment = apps.get_model("experiments", "NimbusExperiment")
    NimbusFeatureConfig = apps.get_model("experiments", "NimbusFeatureConfig")
    applications = {
        "firefox-desktop": "Firefox Desktop",
        "fenix": "Fenix",
        "ios": "iOS",
    }

    for application_slug, application_name in applications.items():
        feature_slug = f"no-feature-{application_slug}"
        feature_name = f"No Feature {application_name}"
        feature_config, _ = NimbusFeatureConfig.objects.get_or_create(
            slug=feature_slug, name=feature_name, application=application_slug
        )
        NimbusExperiment.objects.filter(application=application_slug).update(
            feature_config=feature_config
        )


class Migration(migrations.Migration):

    dependencies = [
        ("experiments", "0165_add_published_dto"),
    ]

    operations = [
        migrations.RunPython(set_feature_config),
    ]
