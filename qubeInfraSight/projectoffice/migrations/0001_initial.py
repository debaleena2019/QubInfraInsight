# Generated by Django 2.2.2 on 2019-06-13 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('tao', models.CharField(max_length=100)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerCommChannel',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('comm_type', models.CharField(max_length=32)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=20)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectoffice.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=32)),
                ('project_code', models.CharField(max_length=32)),
                ('project_type', models.CharField(max_length=32)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=32)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectoffice.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectAttributes',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('project_attribute', models.CharField(max_length=32)),
                ('project_value', models.CharField(max_length=32)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=32)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectoffice.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('isd_code', models.CharField(max_length=32)),
                ('std_code', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=32)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=20)),
                ('comm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectoffice.CustomerCommChannel')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=32)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=20)),
                ('comm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectoffice.CustomerCommChannel')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAdditionalAttribute',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('add_attribute', models.CharField(max_length=20)),
                ('add_value', models.CharField(max_length=20)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=20)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectoffice.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('add_type', models.CharField(max_length=32)),
                ('line1', models.CharField(max_length=32)),
                ('line2', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('state', models.CharField(max_length=32)),
                ('country', models.CharField(max_length=32)),
                ('pin', models.CharField(max_length=32)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=20)),
                ('comm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectoffice.CustomerCommChannel')),
            ],
        ),
    ]
