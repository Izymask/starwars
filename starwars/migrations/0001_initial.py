# Generated by Django 2.2.8 on 2020-01-01 13:01

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
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nom')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('destiny_usage_percentage', models.PositiveSmallIntegerField(default=10, verbose_name="pourcentage d'utilisation des jetons de destinée")),
                ('light_tokens', models.PositiveSmallIntegerField(default=0, verbose_name='light token')),
                ('dark_tokens', models.PositiveSmallIntegerField(default=0, verbose_name='dark token')),
            ],
            options={
                'verbose_name': 'campagne',
                'verbose_name_plural': 'campagnes',
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nom')),
                ('description', models.TextField(blank=True, verbose_name='description')),
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
                ('lightsaber', models.PositiveSmallIntegerField(default=0, verbose_name='sabre laser')),
                ('melee', models.PositiveSmallIntegerField(default=0, verbose_name='corps à corps')),
                ('ranged_heavy', models.PositiveSmallIntegerField(default=0, verbose_name='distance (armes lourdes)')),
                ('ranged_light', models.PositiveSmallIntegerField(default=0, verbose_name='distance (armes légères)')),
                ('core_world', models.PositiveSmallIntegerField(default=0, verbose_name='mondes du noyau')),
                ('education', models.PositiveSmallIntegerField(default=0, verbose_name='education')),
                ('lore', models.PositiveSmallIntegerField(default=0, verbose_name='culture')),
                ('outer_rim', models.PositiveSmallIntegerField(default=0, verbose_name='bordure exterieure')),
                ('underworld', models.PositiveSmallIntegerField(default=0, verbose_name='pègre')),
                ('xenology', models.PositiveSmallIntegerField(default=0, verbose_name='xénologie')),
                ('type', models.CharField(choices=[('pc', 'personnage joueur'), ('npc', 'personnage non joueur'), ('minion', 'sbire'), ('rival', 'rival'), ('nemesis', 'nemesis')], max_length=10, verbose_name='type')),
                ('species', models.CharField(choices=[('human', 'humain'), ('twilek', "twi'lek"), ('bothan', 'bothan'), ('droid', 'droïde'), ('gand', 'gand'), ('rodian', 'rodien'), ('trandoshan', 'trandoshan'), ('wookie', 'wookie'), ('cerean', 'céréen'), ('keldor', "kel'dor"), ('mirialan', 'mirialan'), ('nautolan', 'nautolan'), ('togruta', 'togruta'), ('zabrak', 'zabrak'), ('creature', 'créature')], max_length=20, verbose_name='espèce')),
                ('initiative', models.PositiveSmallIntegerField(default=0, verbose_name='initiative')),
                ('is_active', models.BooleanField(default=False, verbose_name='personnage actif ?')),
                ('is_fighting', models.BooleanField(default=False, verbose_name='en combat ?')),
                ('actual_health', models.PositiveSmallIntegerField(default=0, verbose_name='santé actuelle')),
                ('actual_strain', models.PositiveSmallIntegerField(default=0, verbose_name='stress actuel')),
                ('critical_wounds', models.PositiveSmallIntegerField(default=0, verbose_name='blessures critiques')),
                ('aiming', models.BooleanField(default=False, verbose_name='visée')),
                ('undercover', models.BooleanField(default=False, verbose_name='sous couverture')),
                ('guarded_stance', models.BooleanField(default=False, verbose_name='en garde')),
                ('dropped_prone', models.BooleanField(default=False, verbose_name='au sol')),
                ('actual_experience', models.PositiveSmallIntegerField(default=0, verbose_name='experience actuelle')),
                ('total_experience', models.PositiveIntegerField(default=0, verbose_name='experience totale')),
                ('money', models.PositiveSmallIntegerField(default=0, verbose_name='crédits')),
                ('campaign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='characters', to='starwars.Campaign', verbose_name='campagne')),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='characters', to=settings.AUTH_USER_MODEL, verbose_name='joueur')),
            ],
            options={
                'verbose_name': 'personnage',
                'verbose_name_plural': 'personnages',
            },
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nom')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('type', models.CharField(choices=[('attribute_modifier', "modificateur d'attribut"), ('health_modifier', 'modificateur de santé'), ('dice_pool_modifier', 'modificateur de dés'), ('strain_modifier', 'modificateur de stress')], max_length=20, verbose_name='type')),
                ('attribute', models.CharField(blank=True, choices=[('agility', 'agilité'), ('cunning', 'ruse'), ('brawn', 'vigueur'), ('intellect', 'intelligence'), ('presence', 'présence'), ('willpower', 'volonté'), ('force', 'force'), ('brawl', 'pugilat'), ('gunnery', 'artillerie'), ('lightsaber', 'sabre laser'), ('mechanics', 'mécanique'), ('medecine', 'médecine'), ('melee', 'corps à corps'), ('ranged_heavy', 'distance (armes lourdes)'), ('ranged_light', 'distance (armes légères)'), ('athletics', 'athlétisme'), ('astrogation', 'astrogation'), ('charm', 'charme'), ('coercion', 'coercition'), ('computers', 'informatique'), ('cool', 'calme'), ('coordination', 'coordination'), ('core_world', 'mondes du noyau'), ('deception', 'tromperie'), ('discipline', 'sang froid'), ('education', 'education'), ('leadership', 'commandement'), ('lore', 'culture'), ('negociation', 'negociation'), ('outer_rim', 'bordure exterieure'), ('perception', 'perception'), ('piloting', 'pilotage'), ('resilience', 'résistance'), ('skulduggery', 'magouilles'), ('stealth', 'discretion'), ('streetwise', 'système D'), ('survival', 'survie'), ('underworld', 'pègre'), ('vigilance', 'vigilance'), ('xenology', 'xénologie'), ('defense', 'défense'), ('max_health', 'santé max'), ('max_strain', 'stress max'), ('soak_value', "valeur d'encaissement")], max_length=15, verbose_name='attribut modifié')),
                ('dice', models.CharField(blank=True, choices=[('fortune', 'fortune'), ('misfortune', 'infortune'), ('aptitude', 'aptitude'), ('difficulty', 'difficulté'), ('mastery', 'maitrise'), ('challenge', 'défi'), ('force', 'force')], max_length=10, verbose_name='dé modifié')),
                ('opposite_test', models.BooleanField(default=False, verbose_name='effet sur un test en opposition ?')),
            ],
            options={
                'verbose_name': 'effet',
                'verbose_name_plural': 'effets',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nom')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('type', models.CharField(choices=[('weapon', 'arme'), ('armor', 'armure'), ('consumable', 'consommable'), ('misc', 'autre')], max_length=10, verbose_name='type')),
                ('weight', models.FloatField(default=0.0, verbose_name='encombrement')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='prix')),
                ('hard_point', models.PositiveIntegerField(default=0, verbose_name="emplacement d'améliorations")),
                ('skill', models.CharField(blank=True, choices=[('brawl', 'pugilat'), ('gunnery', 'artillerie'), ('lightsaber', 'sabre laser'), ('mechanics', 'mécanique'), ('medecine', 'médecine'), ('melee', 'corps à corps'), ('ranged_heavy', 'distance (armes lourdes)'), ('ranged_light', 'distance (armes légères)')], max_length=10, null=True, verbose_name='compétence associée')),
                ('range', models.CharField(blank=True, choices=[('engaged', 'corps à corps'), ('short', 'portée courte'), ('medium', 'portée moyenne'), ('long', 'portée longue'), ('extreme', 'portée extrème')], max_length=10, verbose_name='portée')),
                ('damage', models.PositiveSmallIntegerField(default=0, verbose_name='dégats')),
                ('critique', models.PositiveSmallIntegerField(default=0, verbose_name='critique')),
                ('soak_value', models.PositiveSmallIntegerField(default=0, verbose_name="valeur d'encaissement")),
                ('defense', models.PositiveSmallIntegerField(default=0, verbose_name='défense')),
            ],
            options={
                'verbose_name': 'objet',
                'verbose_name_plural': 'objets',
            },
        ),
        migrations.CreateModel(
            name='Talent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nom')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('activation_type', models.CharField(choices=[('active', 'actif'), ('passive', 'passif')], default='passive', max_length=7, verbose_name="type d'activation")),
            ],
            options={
                'verbose_name': 'talent',
                'verbose_name_plural': 'talents',
            },
        ),
        migrations.CreateModel(
            name='TalentEffect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modifier_value', models.IntegerField(default=0, verbose_name='valeur du modificateur')),
                ('activation_type', models.CharField(choices=[('active', 'actif'), ('passive', 'passif')], default='passive', max_length=7, verbose_name="type d'activation")),
                ('duration_type', models.CharField(blank=True, choices=[('direct', 'direct (one shot)'), ('permanent', 'permanent'), ('source_turn', 'nombre de tours (source)'), ('target_turn', 'nombre de tours (cible)'), ('fight', 'durée du combat')], max_length=11, verbose_name='type de durée')),
                ('nb_turn', models.IntegerField(default=0, verbose_name='nombre de tours')),
                ('effect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='starwars.Effect', verbose_name='effet')),
                ('talent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='effects', to='starwars.Talent', verbose_name='talent')),
            ],
            options={
                'verbose_name': 'effet de talent',
                'verbose_name_plural': 'effets de talents',
            },
        ),
        migrations.CreateModel(
            name='ItemEffect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modifier_value', models.IntegerField(default=0, verbose_name='valeur du modificateur')),
                ('activation_type', models.CharField(choices=[('active', 'actif'), ('passive', 'passif')], default='passive', max_length=7, verbose_name="type d'activation")),
                ('duration_type', models.CharField(blank=True, choices=[('direct', 'direct (one shot)'), ('permanent', 'permanent'), ('source_turn', 'nombre de tours (source)'), ('target_turn', 'nombre de tours (cible)'), ('fight', 'durée du combat')], max_length=11, verbose_name='type de durée')),
                ('nb_turn', models.IntegerField(default=0, verbose_name='nombre de tours')),
                ('effect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='starwars.Effect', verbose_name='effet')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='effects', to='starwars.Item', verbose_name='objet')),
            ],
            options={
                'verbose_name': "effet d'objet",
                'verbose_name_plural': "effets d'objet",
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='quantité')),
                ('equiped', models.BooleanField(default=False, verbose_name='équipé ?')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='starwars.Character', verbose_name='personnage')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='starwars.Item', verbose_name='objet')),
            ],
            options={
                'verbose_name': 'équipement',
                'verbose_name_plural': 'équipements',
            },
        ),
        migrations.CreateModel(
            name='CharacterEffect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modifier_value', models.IntegerField(default=0, verbose_name='valeur du modificateur')),
                ('activation_type', models.CharField(choices=[('active', 'actif'), ('passive', 'passif')], default='passive', max_length=7, verbose_name="type d'activation")),
                ('duration_type', models.CharField(blank=True, choices=[('direct', 'direct (one shot)'), ('permanent', 'permanent'), ('source_turn', 'nombre de tours (source)'), ('target_turn', 'nombre de tours (cible)'), ('fight', 'durée du combat')], max_length=11, verbose_name='type de durée')),
                ('nb_turn', models.IntegerField(default=0, verbose_name='nombre de tours')),
                ('effect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='starwars.Effect', verbose_name='effet')),
                ('source_character', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='generated_effects', to='starwars.Character', verbose_name='personnage source')),
                ('source_equipment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='generated_effects', to='starwars.Equipment', verbose_name='equipement source')),
                ('source_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='generated_effects', to='starwars.Item', verbose_name='objet source')),
                ('source_talent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='generated_effects', to='starwars.Talent', verbose_name='talent source')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_effects', to='starwars.Character', verbose_name='personnage cible')),
            ],
            options={
                'verbose_name': 'effet de personnages',
                'verbose_name_plural': 'effets de personnages',
            },
        ),
    ]
