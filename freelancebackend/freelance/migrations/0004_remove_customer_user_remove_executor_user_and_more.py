# Generated by Django 4.2.5 on 2024-02-02 00:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "freelance",
            "0003_alter_authoring_review_date_alter_message_msg_date_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="user",
        ),
        migrations.RemoveField(
            model_name="executor",
            name="user",
        ),
        migrations.RemoveField(
            model_name="message",
            name="customer",
        ),
        migrations.RemoveField(
            model_name="message",
            name="executor",
        ),
        migrations.RemoveField(
            model_name="order",
            name="customer",
        ),
        migrations.RemoveField(
            model_name="ordering",
            name="customer",
        ),
        migrations.RemoveField(
            model_name="ordering",
            name="executor",
        ),
        migrations.RemoveField(
            model_name="ordering",
            name="order",
        ),
        migrations.RemoveField(
            model_name="ordering",
            name="service",
        ),
        migrations.RemoveField(
            model_name="service",
            name="executor",
        ),
        migrations.RemoveField(
            model_name="tag",
            name="order",
        ),
        migrations.RemoveField(
            model_name="tag",
            name="service",
        ),
        migrations.RemoveField(
            model_name="ticket",
            name="customer",
        ),
        migrations.RemoveField(
            model_name="ticket",
            name="executor",
        ),
        migrations.DeleteModel(
            name="Authoring",
        ),
        migrations.DeleteModel(
            name="Customer",
        ),
        migrations.DeleteModel(
            name="Executor",
        ),
        migrations.DeleteModel(
            name="Message",
        ),
        migrations.DeleteModel(
            name="Order",
        ),
        migrations.DeleteModel(
            name="Ordering",
        ),
        migrations.DeleteModel(
            name="Review",
        ),
        migrations.DeleteModel(
            name="Service",
        ),
        migrations.DeleteModel(
            name="Tag",
        ),
        migrations.DeleteModel(
            name="Ticket",
        ),
    ]
