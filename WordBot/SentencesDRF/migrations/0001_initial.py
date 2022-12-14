# Generated by Django 4.0 on 2022-09-27 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_Category', models.CharField(db_index=True, default='Fist_category', max_length=50, verbose_name='Question_catagory')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_fild', models.CharField(max_length=200)),
                ('catagory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='SentencesDRF.category')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_fild', models.CharField(max_length=100)),
                ('right_answer', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='SentencesDRF.question')),
            ],
            options={
                'order_with_respect_to': 'question',
                'unique_together': {('question', 'answer_fild')},
            },
        ),
    ]
