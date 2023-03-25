# Generated by Django 4.0.6 on 2023-03-25 13:46

import course.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name=' عنوان ')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name=' آدرس اسلاگ ')),
                ('description', models.TextField(blank=True, null=True, verbose_name=' توضیحات ')),
                ('course_content', models.TextField(blank=True, null=True, verbose_name='توضیحات کوتاه')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='قیمت ')),
                ('image', models.ImageField(blank=True, default=course.models.get_default_course_image, null=True, upload_to=course.models.get_course_image_filepath, verbose_name='تصویر دوره ')),
                ('status', models.CharField(blank=True, choices=[('New Course', 'دوره جدید'), ('Course in progress', 'دوره در حال برگزاری'), ('Course update', 'دوره در حال بروز رسانی'), ('The course is over', 'دوره به اتمام رسیده')], max_length=25, verbose_name=' وضعیت ')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name=' تاریخ ایجاد ')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name=' تاریخ آپدیت ')),
                ('view_count', models.IntegerField(blank=True, null=True, verbose_name=' تعداد بازدید')),
                ('sell_count', models.IntegerField(blank=True, null=True, verbose_name=' تعداد فروش ')),
                ('is_active', models.BooleanField(default=True, verbose_name='وضعیت فعال بودن دوره')),
                ('is_free', models.BooleanField(default=True, verbose_name='رایگان ')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category', verbose_name=' دسته بندی ')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=' مدرس دوره ')),
            ],
            options={
                'verbose_name': 'دوره',
                'verbose_name_plural': ' دوره ها',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name=' عنوان ')),
                ('description', models.TextField(blank=True, null=True, verbose_name=' توضیحات ')),
                ('duration_video', models.CharField(max_length=20, verbose_name='تایم ویدیو')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name=' آدرس اسلاگ ')),
                ('video', models.FileField(upload_to=course.models.get_video_filepath, verbose_name=' ویدیو دوره ')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name=' تاریخ ایجاد ')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name=' تاریخ آپدیت ')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course', verbose_name='دوره مرتبط')),
            ],
            options={
                'verbose_name': 'ویدیو',
                'verbose_name_plural': 'بخش ویدیو ها',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=350, null=True, verbose_name=' نظرهات ')),
                ('user_ip', models.CharField(blank=True, max_length=20, verbose_name=' آی پی کاربر ')),
                ('status', models.CharField(blank=True, choices=[('readed', 'readed'), ('unreaded', 'unreaded'), ('close', 'close')], max_length=25, verbose_name=' وضعیت پیام ')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name=' تاریخ ایجاد ')),
                ('modify_date', models.DateTimeField(auto_now=True, verbose_name=' تاریخ آپدیت ')),
                ('is_active', models.BooleanField(default=True, verbose_name=' وضعیت فعال بودن ')),
                ('author_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=' کاربر مربوط ')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course', verbose_name=' دوره مرتبط ')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'بخش نظرات',
            },
        ),
    ]
