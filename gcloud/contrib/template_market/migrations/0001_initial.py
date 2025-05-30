# Generated by Django 3.2.15 on 2024-12-16 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TemplateSharedRecord",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("project_id", models.IntegerField(default=-1, help_text="项目 ID", verbose_name="项目 ID")),
                ("template_id", models.IntegerField(db_index=True, help_text="模板 ID", verbose_name="模板 ID")),
                ("creator", models.CharField(default="", max_length=32, verbose_name="创建者")),
                ("create_at", models.DateTimeField(auto_now_add=True, verbose_name="创建时间")),
                ("update_at", models.DateTimeField(auto_now=True, verbose_name="更新时间")),
                ("extra_info", models.JSONField(blank=True, null=True, verbose_name="额外信息")),
            ],
            options={
                "verbose_name": "模板共享记录 TemplateSharedRecord",
                "verbose_name_plural": "模板共享记录 TemplateSharedRecord",
            },
        ),
    ]
