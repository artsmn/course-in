# Generated by Django 3.1.3 on 2020-11-26 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Course name')),
                ('description', models.TextField(max_length=128, verbose_name='Course description')),
                ('is_active', models.BooleanField(verbose_name='Is Active')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Lessons name')),
                ('description', models.TextField(max_length=128, verbose_name='Lesson description')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
        migrations.CreateModel(
            name='LessonNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('text', models.TextField(verbose_name='Text')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LessonNodeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Image name')),
                ('image', models.ImageField(upload_to='lesson_image/')),
                ('lesson_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.lessonnode')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.tutor', verbose_name='Tutor'),
        ),
    ]