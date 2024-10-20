# Generated by Django 5.1.2 on 2024-10-20 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('catalyst_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='company_summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(blank=True, db_column='file_name', max_length=100, null=True)),
                ('added_by', models.CharField(blank=True, db_column='added_by', max_length=200, null=True)),
                ('total_count', models.IntegerField(blank=True, db_column='total_count', null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='created_date', null=True)),
            ],
            options={
                'db_table': 'company_summary',
                'ordering': ('-id',),
            },
        ),
        migrations.AddField(
            model_name='users',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='users',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='users',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='users',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='users',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_id',
            field=models.IntegerField(blank=True, db_column='company_id', default=None, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.CharField(blank=True, db_column='country', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='current_emp_est',
            field=models.IntegerField(blank=True, db_column='current_emp_est', null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='domain',
            field=models.CharField(blank=True, db_column='domain', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='industry',
            field=models.CharField(blank=True, db_column='industry', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='linkedin_url',
            field=models.CharField(blank=True, db_column='linkedin_url', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='locality',
            field=models.CharField(blank=True, db_column='locality', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(blank=True, db_column='name', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='size_range',
            field=models.CharField(blank=True, db_column='size_range', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='total_emp_est',
            field=models.IntegerField(blank=True, db_column='total_emp_est', null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='year_founded',
            field=models.IntegerField(blank=True, db_column='year_founded', null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(db_column='username', max_length=150, unique=True),
        ),
    ]
