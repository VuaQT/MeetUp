# Generated by Django 2.0.6 on 2018-06-25 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('email', models.CharField(db_index=True, max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_commented', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='EventGeneral',
            fields=[
                ('id', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('photo_path', models.CharField(max_length=500)),
                ('start_date', models.DateField(db_index=True)),
                ('end_date', models.DateField()),
                ('number_like', models.IntegerField()),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_liked', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Participate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_participated', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('username', models.CharField(db_index=True, max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='EventContent',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='event.EventGeneral')),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.EventGeneral'),
        ),
        migrations.AddField(
            model_name='participate',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.EventGeneral'),
        ),
        migrations.AddField(
            model_name='participate',
            name='visitor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Visitor'),
        ),
        migrations.AddField(
            model_name='like',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.EventGeneral'),
        ),
        migrations.AddField(
            model_name='like',
            name='visitor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Visitor'),
        ),
        migrations.AddField(
            model_name='eventgeneral',
            name='c_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Category'),
        ),
        migrations.AddField(
            model_name='comment',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.EventGeneral'),
        ),
        migrations.AddField(
            model_name='comment',
            name='visitor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.Visitor'),
        ),
        migrations.AddIndex(
            model_name='participate',
            index=models.Index(fields=['visitor_id', 'event_id'], name='event_parti_visitor_a29021_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='participate',
            unique_together={('visitor_id', 'event_id')},
        ),
        migrations.AddIndex(
            model_name='like',
            index=models.Index(fields=['visitor_id', 'event_id'], name='event_like_visitor_f9e522_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('visitor_id', 'event_id')},
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['visitor_id', 'event_id'], name='event_comme_visitor_b975c6_idx'),
        ),
    ]
