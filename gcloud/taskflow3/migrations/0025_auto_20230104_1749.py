# Generated by Django 3.2.15 on 2023-01-04 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taskflow3", "0024_taskconfig"),
    ]

    operations = [
        migrations.AddField(
            model_name="taskflowinstance",
            name="extra_info",
            field=models.TextField(blank=True, null=True, verbose_name="额外信息"),
        ),
        migrations.AlterField(
            model_name="taskconfig",
            name="config_type",
            field=models.IntegerField(choices=[(1, "subprocess"), (2, "retry_params")], verbose_name="配置类型"),
        ),
        migrations.AlterField(
            model_name="taskconfig",
            name="config_value",
            field=models.CharField(
                choices=[
                    ("enable_independent_subprocess", "启用独立子流程"),
                    ("disable_independent_subprocess", "禁用独立子流程"),
                    ("enable_fill_retry_params", "启用节点重试填参"),
                    ("disable_fill_retry_params", "禁用节点重试填参"),
                ],
                max_length=512,
                verbose_name="配置值",
            ),
        ),
        migrations.AlterField(
            model_name="taskconfig",
            name="scope",
            field=models.IntegerField(choices=[(1, "project"), (2, "template"), (3, "task")], verbose_name="配置范围"),
        ),
    ]
