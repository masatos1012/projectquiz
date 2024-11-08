# Generated by Django 4.2.11 on 2024-11-04 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("quizapp", "0004_rename_user_customuser"),
    ]

    operations = [
        migrations.RemoveField(model_name="session", name="user",),
        migrations.RemoveField(model_name="useranswer", name="user",),
        migrations.AddField(
            model_name="session",
            name="session_key",
            field=models.CharField(
                default="default_session_key",
                max_length=255,
                unique=True,
                verbose_name="セッションキー",
            ),
        ),
        migrations.AddField(
            model_name="useranswer",
            name="session_key",
            field=models.CharField(
                default="default_session_key", max_length=40, verbose_name="セッションキー"
            ),
        ),
        migrations.AlterField(
            model_name="session",
            name="current_question",
            field=models.ForeignKey(
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="quizapp.question",
                verbose_name="現在の問題ID",
            ),
        ),
        migrations.DeleteModel(name="CustomUser",),
    ]
