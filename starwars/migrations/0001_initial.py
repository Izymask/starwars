# Generated by Django 2.2.8 on 2019-12-22 15:32

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nickname', models.CharField(blank=True, max_length=100, verbose_name='surnom')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'joueur',
                'verbose_name_plural': 'joueurs',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brawn', models.PositiveSmallIntegerField(default=0, verbose_name='vigueur')),
                ('agility', models.PositiveSmallIntegerField(default=0, verbose_name='agilité')),
                ('intellect', models.PositiveSmallIntegerField(default=0, verbose_name='intelligence')),
                ('cunning', models.PositiveSmallIntegerField(default=0, verbose_name='ruse')),
                ('willpower', models.PositiveSmallIntegerField(default=0, verbose_name='volonté')),
                ('presence', models.PositiveSmallIntegerField(default=0, verbose_name='présence')),
                ('force', models.PositiveSmallIntegerField(default=0, verbose_name='force')),
                ('morality', models.PositiveSmallIntegerField(default=50, verbose_name='moralité')),
                ('conflit', models.PositiveSmallIntegerField(default=0, verbose_name='conflit')),
                ('astrogation', models.PositiveSmallIntegerField(default=0, verbose_name='astrogation')),
                ('athletics', models.PositiveSmallIntegerField(default=0, verbose_name='athlétisme')),
                ('charm', models.PositiveSmallIntegerField(default=0, verbose_name='charme')),
                ('coercion', models.PositiveSmallIntegerField(default=0, verbose_name='coercition')),
                ('computers', models.PositiveSmallIntegerField(default=0, verbose_name='informatique')),
                ('cool', models.PositiveSmallIntegerField(default=0, verbose_name='calme')),
                ('coordination', models.PositiveSmallIntegerField(default=0, verbose_name='coordination')),
                ('deception', models.PositiveSmallIntegerField(default=0, verbose_name='tromperie')),
                ('discipline', models.PositiveSmallIntegerField(default=0, verbose_name='sang froid')),
                ('leadership', models.PositiveSmallIntegerField(default=0, verbose_name='commandement')),
                ('mechanics', models.PositiveSmallIntegerField(default=0, verbose_name='mécanique')),
                ('medecine', models.PositiveSmallIntegerField(default=0, verbose_name='médecine')),
                ('negociation', models.PositiveSmallIntegerField(default=0, verbose_name='négociation')),
                ('perception', models.PositiveSmallIntegerField(default=0, verbose_name='perception')),
                ('piloting', models.PositiveSmallIntegerField(default=0, verbose_name='pilotage')),
                ('resilience', models.PositiveSmallIntegerField(default=0, verbose_name='résistance')),
                ('skulduggery', models.PositiveSmallIntegerField(default=0, verbose_name='magouilles')),
                ('stealth', models.PositiveSmallIntegerField(default=0, verbose_name='discretion')),
                ('streetwise', models.PositiveSmallIntegerField(default=0, verbose_name='système D')),
                ('survival', models.PositiveSmallIntegerField(default=0, verbose_name='survie')),
                ('vigilance', models.PositiveSmallIntegerField(default=0, verbose_name='vigilance')),
                ('brawl', models.PositiveSmallIntegerField(default=0, verbose_name='pugilat')),
                ('gunnery', models.PositiveSmallIntegerField(default=0, verbose_name='artillerie')),
                ('melee', models.PositiveSmallIntegerField(default=0, verbose_name='corps à corps')),
                ('ranged_heavy', models.PositiveSmallIntegerField(default=0, verbose_name='distance (armes lourdes)')),
                ('ranged_light', models.PositiveSmallIntegerField(default=0, verbose_name='distance (armes légères)')),
                ('core_world', models.PositiveSmallIntegerField(default=0, verbose_name='mondes du noyau')),
                ('education', models.PositiveSmallIntegerField(default=0, verbose_name='education')),
                ('lore', models.PositiveSmallIntegerField(default=0, verbose_name='culture')),
                ('outer_rim', models.PositiveSmallIntegerField(default=0, verbose_name='bordure exterieure')),
                ('underworld', models.PositiveSmallIntegerField(default=0, verbose_name='pègre')),
                ('xenology', models.PositiveSmallIntegerField(default=0, verbose_name='xénologie')),
                ('name', models.CharField(max_length=50, verbose_name='nom')),
                ('species', models.CharField(choices=[('human', 'humain'), ('twilek', "twi'lek"), ('bothan', 'bothan'), ('droid', 'droïde'), ('gand', 'gand'), ('rodian', 'rodien'), ('trandoshan', 'trandoshan'), ('wookie', 'wookie'), ('cerean', 'céréen'), ('keldor', "kel'dor"), ('mirialan', 'mirialan'), ('nautolan', 'nautolan'), ('togruta', 'togruta'), ('zabrak', 'zabrak'), ('creature', 'créature')], max_length=20, verbose_name='espèce')),
                ('actual_health', models.PositiveSmallIntegerField(default=0, verbose_name='santé actuelle')),
                ('actual_strain', models.PositiveSmallIntegerField(default=0, verbose_name='stress actuel')),
                ('critical_wounds', models.PositiveSmallIntegerField(default=0, verbose_name='blessures critiques')),
                ('total_experience', models.PositiveIntegerField(default=0)),
                ('actual_experience', models.PositiveSmallIntegerField(default=0)),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='characters', to=settings.AUTH_USER_MODEL, verbose_name='joueur')),
            ],
            options={
                'verbose_name': 'personnage',
                'verbose_name_plural': 'personnages',
            },
        ),
    ]
