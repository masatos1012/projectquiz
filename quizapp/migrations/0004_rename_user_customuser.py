# Generated by Django 4.2.11 on 2024-11-04 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("quizapp", "0003_remove_useranswer_answers_useranswer_is_correct_and_more"),
    ]

    operations = [
        migrations.RenameModel(old_name="User", new_name="CustomUser",),
    ]
