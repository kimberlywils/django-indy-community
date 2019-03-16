# Generated by Django 2.1.7 on 2019-03-16 00:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('sessions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AgentConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=30)),
                ('invitation', models.TextField(blank=True, max_length=4000)),
                ('token', models.CharField(blank=True, max_length=80)),
                ('status', models.CharField(max_length=20)),
                ('connection_type', models.CharField(max_length=20)),
                ('connection_data', models.TextField(blank=True, max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='AgentConversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connection_partner_name', models.CharField(max_length=30)),
                ('conversation_type', models.CharField(max_length=30)),
                ('message_id', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=20)),
                ('proof_state', models.CharField(blank=True, max_length=20)),
                ('conversation_data', models.TextField(blank=True, max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='IndyCredentialDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledger_creddef_id', models.CharField(max_length=40, unique=True)),
                ('creddef_name', models.CharField(max_length=40)),
                ('creddef_handle', models.CharField(max_length=40)),
                ('creddef_template', models.TextField(max_length=4000)),
                ('creddef_data', models.TextField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='IndyOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndyOrgRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indy_core.IndyOrganization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IndyProofRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proof_req_name', models.CharField(max_length=40, unique=True)),
                ('proof_req_description', models.TextField(max_length=4000)),
                ('proof_req_attrs', models.TextField(max_length=4000)),
                ('proof_req_predicates', models.TextField(blank=True, max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='IndySchema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledger_schema_id', models.CharField(max_length=40, unique=True)),
                ('schema_name', models.CharField(max_length=40)),
                ('schema_version', models.CharField(max_length=40)),
                ('schema', models.TextField(max_length=4000)),
                ('schema_template', models.TextField(max_length=4000)),
                ('schema_data', models.TextField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='IndySession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_name', models.CharField(blank=True, max_length=30, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sessions.Session')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IndyWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_name', models.CharField(max_length=30, unique=True)),
                ('wallet_config', models.TextField(blank=True, max_length=4000)),
            ],
        ),
        migrations.AddField(
            model_name='indyorganization',
            name='wallet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='indy_core.IndyWallet', to_field='wallet_name'),
        ),
        migrations.AddField(
            model_name='indycredentialdefinition',
            name='ledger_schema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indy_core.IndySchema'),
        ),
        migrations.AddField(
            model_name='indycredentialdefinition',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indy_core.IndyWallet', to_field='wallet_name'),
        ),
        migrations.AddField(
            model_name='agentconversation',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indy_core.IndyWallet', to_field='wallet_name'),
        ),
        migrations.AddField(
            model_name='agentconnection',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indy_core.IndyWallet', to_field='wallet_name'),
        ),
        migrations.AddField(
            model_name='indyuser',
            name='wallet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='indy_core.IndyWallet', to_field='wallet_name'),
        ),
    ]
