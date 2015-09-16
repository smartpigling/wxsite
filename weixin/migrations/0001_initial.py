# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import weixin.models.message


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=32, verbose_name='\u8d26\u6237\u540d')),
                ('uuid', models.CharField(max_length=64, verbose_name='\u8d26\u6237\u6807\u8bc6')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u6709\u6548\u72b6\u6001')),
            ],
            options={
                'verbose_name': '\u8d26\u6237',
                'verbose_name_plural': '\u8d26\u6237',
            },
        ),
        migrations.CreateModel(
            name='Button',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='\u6807\u9898')),
                ('type', models.CharField(choices=[(b'click', '\u70b9\u51fb\u63a8\u4e8b\u4ef6'), (b'view', '\u8df3\u8f6cURL'), (b'scancode_push', '\u626b\u7801\u63a8\u4e8b\u4ef6'), (b'scancode_waitmsg', '\u626b\u7801\u63a8\u4e8b\u4ef6\u4e14\u5f39\u51fa\u201c\u6d88\u606f\u63a5\u6536\u4e2d\u201d\u63d0\u793a\u6846'), (b'pic_sysphoto', '\u5f39\u51fa\u7cfb\u7edf\u62cd\u7167\u53d1\u56fe'), (b'pic_photo_or_album', '\u5f39\u51fa\u62cd\u7167\u6216\u8005\u76f8\u518c\u53d1\u56fe'), (b'pic_weixin', '\u5f39\u51fa\u5fae\u4fe1\u76f8\u518c\u53d1\u56fe\u5668'), (b'location_select', '\u5f39\u51fa\u5730\u7406\u4f4d\u7f6e\u9009\u62e9\u5668')], max_length=20, blank=True, help_text='\u81ea\u5b9a\u4e49\u83dc\u5355\u63a5\u53e3\u6309\u94ae\u7c7b\u578b\uff0c\u6ce8\u610f\u9664click\u548cview\u4e8b\u4ef6\u5916\uff0c\u5176\u4f59\u4e8b\u4ef6\u9700\u8981\u5fae\u4fe1iPhone5.4.1\u4ee5\u4e0a\u7248\u672c\u652f\u6301\u3002', null=True, verbose_name='\u54cd\u5e94\u52a8\u4f5c\u7c7b\u578b')),
                ('key', models.CharField(help_text='\u4e8b\u4ef6KEY\u503c\uff0c\u7528\u4e8e\u4e0e\u4e8b\u4ef6\u54cd\u5e94\u89c4\u5219\u5173\u8054\u3002\u8df3\u8f6cURL\u578b\u7684\u83dc\u5355\u65e0\u9700\u6b64\u9879\u3002', max_length=128, verbose_name='KEY\u503c', blank=True)),
                ('url', models.URLField(help_text='\u7528\u4e8e\u8df3\u8f6cURL\u7c7b\u578b\u83dc\u5355\u7684\u94fe\u63a5\u3002', verbose_name='\u7f51\u9875\u94fe\u63a5', blank=True)),
                ('position', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
            ],
            options={
                'verbose_name': '\u81ea\u5b9a\u4e49\u83dc\u5355',
                'verbose_name_plural': '\u81ea\u5b9a\u4e49\u83dc\u5355',
            },
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=1, verbose_name='\u7c7b\u578b', choices=[(b'M', '\u516c\u4f17\u53f7\uff08\u670d\u52a1\u53f7/\u8ba2\u9605\u53f7\uff09'), (b'Q', '\u4f01\u4e1a\u53f7')])),
                ('token', models.CharField(help_text='\u586b\u5199\u5fae\u4fe1\u516c\u4f17\u53f7\u63a5\u53e3\u914d\u7f6e\u91cc\u7684Token(\u4ee4\u724c)\uff0c3-32\u4e2a\u5b57\u7b26\u3002', max_length=32, verbose_name='Token')),
                ('app_id', models.CharField(default=b'', help_text='\u5f00\u53d1\u8005\u8d26\u53f7\u552f\u4e00\u51ed\u8bc1AppID(\u5e94\u7528ID)', max_length=32, verbose_name='AppId/CorpId', blank=True)),
                ('secret', models.CharField(default=b'', help_text='\u5f00\u53d1\u8005\u8d26\u53f7\u552f\u4e00\u51ed\u8bc1\u5bc6\u94a5AppSecret(\u5e94\u7528\u5bc6\u94a5)', max_length=64, verbose_name='AppSecret', blank=True)),
                ('encoding_aes_key', models.CharField(default=b'', help_text='\u6d88\u606f\u52a0\u5bc6\u5bc6\u94a5EncodingAESKey', max_length=43, verbose_name='EncodingAESKey', blank=True)),
                ('owner', models.ForeignKey(verbose_name='\u8d26\u6237', to='weixin.Account')),
            ],
            options={
                'verbose_name': '\u516c\u4f17\u53f7/\u4f01\u4e1a\u53f7\u914d\u7f6e',
                'verbose_name_plural': '\u516c\u4f17\u53f7/\u4f01\u4e1a\u53f7\u914d\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=3, verbose_name='\u7c7b\u578b', choices=[(b'ISP', '\u5185\u90e8\u5904\u7406'), (b'OSP', '\u5916\u90e8\u540c\u6b65\u5904\u7406'), (b'OAP', '\u5916\u90e8\u5f02\u6b65\u5904\u7406')])),
                ('pool', models.CharField(max_length=4, null=True, verbose_name='\u961f\u5217\u6c60\u7f16\u53f7', blank=True)),
                ('ident', models.CharField(max_length=128, null=True, verbose_name='\u7ebf\u7a0b\u7f16\u53f7', blank=True)),
                ('user_message', models.CharField(default=b'', max_length=1000, verbose_name='\u7528\u6237\u6d88\u606f', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u8d77\u65f6\u95f4')),
                ('processed_status', models.CharField(default=b'W', max_length=1, verbose_name='\u5904\u7406\u72b6\u6001', choices=[(b'W', '\u7b49\u5f85\u5904\u7406'), (b'S', '\u5904\u7406\u6210\u529f'), (b'F', '\u5904\u7406\u5931\u8d25')])),
                ('processed_message', models.CharField(max_length=64, null=True, verbose_name='\u72b6\u6001\u6d88\u606f', blank=True)),
                ('processed_at', models.DateTimeField(null=True, verbose_name='\u5904\u7406\u65f6\u95f4', blank=True)),
                ('reply', models.CharField(max_length=10000, null=True, verbose_name='\u8fd4\u56de\u5185\u5bb9', blank=True)),
                ('belonging', models.ForeignKey(verbose_name='\u8d26\u6237', to='weixin.Account')),
            ],
            options={
                'verbose_name': '\u4e8b\u4ef6\u8bb0\u5f55',
                'verbose_name_plural': '\u4e8b\u4ef6\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='EventReplyRule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='\u8be5\u540d\u79f0\u4ec5\u7528\u4e8e\u5217\u8868\u663e\u793a', max_length=100, verbose_name='\u663e\u793a\u540d\u79f0')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('event_type', models.CharField(max_length=20, verbose_name='\u4e8b\u4ef6\u7c7b\u578b', choices=[(b'subscribe', '\u5173\u6ce8\u4e8b\u4ef6\u63a8\u9001'), (b'unsubscribe', '\u53d6\u6d88\u5173\u6ce8\u4e8b\u4ef6\u63a8\u9001'), (b'CLICK', '\u70b9\u51fb\u83dc\u5355\u62c9\u53d6\u6d88\u606f\u65f6\u7684\u4e8b\u4ef6\u63a8\u9001'), (b'VIEW', '\u70b9\u51fb\u83dc\u5355\u8df3\u8f6c\u94fe\u63a5\u65f6\u7684\u4e8b\u4ef6\u63a8\u9001'), (b'location_select', '\u5f39\u51fa\u5730\u7406\u4f4d\u7f6e\u9009\u62e9\u5668\u7684\u4e8b\u4ef6\u63a8\u9001'), (b'scancode_push', '\u626b\u7801\u63a8\u4e8b\u4ef6\u7684\u4e8b\u4ef6\u63a8\u9001'), (b'scancode_waitmsg', '\u626b\u7801\u63a8\u4e8b\u4ef6\u4e14\u5f39\u51fa\u201c\u6d88\u606f\u63a5\u6536\u4e2d\u201d\u63d0\u793a\u6846\u7684\u4e8b\u4ef6\u63a8\u9001')])),
                ('event_key', models.CharField(max_length=50, verbose_name='\u4e8b\u4ef6KEY\u503c', blank=True)),
                ('res_msg_type', models.CharField(help_text='\u5185\u90e8\u5904\u7406\u8868\u793a\u7531\u672c\u5e94\u7528\u901a\u8fc7\u6307\u5b9a\u7684\u8fd4\u56de\u5185\u5bb9\u5bf9\u6d88\u606f\u8fdb\u884c\u54cd\u5e94\uff0c\u5916\u90e8\u5904\u7406\u8868\u793a\u7531\u5916\u90e8\u5e94\u7528\u5bf9\u6d88\u606f\u8fdb\u884c\u5904\u7406\uff0c\u518d\u4ea4\u7531\u672c\u5e94\u7528\u56de\u590d\u5230\u7528\u6237\u3002\u5176\u4e2d\u540c\u6b65\u5904\u7406\u8868\u793a\u672c\u5e94\u7528\u4f1a\u7b49\u5f85\u5904\u7406\u63a5\u53e3\u5e76\u5b9e\u65f6\u8fd4\u56de\uff0c\u5f02\u6b65\u5904\u7406\u8868\u793a\u672c\u5e94\u7528\u4f1a\u76f4\u63a5\u8fd4\u56de\u7528\u6237\u7a7a\u4fe1\u606f\uff0c\u5728\u63a5\u6536\u5230\u5904\u7406\u7ed3\u679c\u540e\u518d\u5411\u7528\u6237\u8fd4\u56de\u3002\u6ce8\u610f\u5916\u90e8\u5f02\u6b65\u5904\u7406\u9700\u8981\u4f7f\u7528\u5230\u5fae\u4fe1\u5ba2\u670d\u63a5\u53e3\uff0c\u5982\u65e0\u8be5\u63a5\u53e3\u6743\u9650\uff0c\u5219\u8be5\u6a21\u5f0f\u65e0\u6cd5\u5b9e\u73b0\u3002', max_length=10, verbose_name='\u54cd\u5e94\u5904\u7406\u65b9\u5f0f', choices=[(b'ishdl', '\u5185\u90e8\u540c\u6b65\u5904\u7406'), (b'oahdl', '\u5916\u90e8\u5f02\u6b65\u5904\u7406'), (b'oshdl', '\u5916\u90e8\u540c\u6b65\u5904\u7406')])),
                ('pool', models.CharField(max_length=4, null=True, verbose_name='\u961f\u5217\u6c60\u7f16\u53f7', blank=True)),
                ('msg_object_object_id', models.CharField(help_text='\u8981\u8fd4\u56de\u7684\u6d88\u606f\u4e3b\u4f53', max_length=255, null=True, verbose_name='\u5173\u8054\u6d88\u606f', blank=True)),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u751f\u6548')),
            ],
            options={
                'verbose_name': '\u4e8b\u4ef6\u54cd\u5e94\u89c4\u5219',
                'verbose_name_plural': '\u4e8b\u4ef6\u54cd\u5e94\u89c4\u5219',
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='\u8be5\u540d\u79f0\u4ec5\u7528\u4e8e\u5217\u8868\u663e\u793a', max_length=100, verbose_name='\u663e\u793a\u540d\u79f0')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('exact_match', models.BooleanField(verbose_name='\u5b8c\u5168\u5339\u914d')),
                ('owner', models.ForeignKey(verbose_name='\u8d26\u6237', to='weixin.Account')),
            ],
            options={
                'verbose_name': '\u5173\u952e\u5b57',
                'verbose_name_plural': '\u5173\u952e\u5b57',
            },
        ),
        migrations.CreateModel(
            name='LocTrack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lng', models.FloatField(verbose_name='\u7ecf\u5ea6')),
                ('lat', models.FloatField(verbose_name='\u7eac\u5ea6')),
                ('precision', models.FloatField(verbose_name='\u7cbe\u5ea6')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('belonging', models.ForeignKey(verbose_name='\u8d26\u6237', to='weixin.Account')),
            ],
            options={
                'verbose_name': '\u5730\u7406\u4f4d\u7f6e\u4e0a\u62a5\u8bb0\u5f55',
                'verbose_name_plural': '\u5730\u7406\u4f4d\u7f6e\u4e0a\u62a5\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='MediaItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='\u8be5\u540d\u79f0\u4ec5\u7528\u4e8e\u5217\u8868\u663e\u793a', max_length=100, verbose_name='\u663e\u793a\u540d\u79f0')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('description', models.CharField(max_length=2000, verbose_name='\u63cf\u8ff0')),
                ('file', models.FileField(help_text='\u4e0a\u4f20\u7684\u6587\u4ef6\u4e0d\u5927\u4e8e5M', upload_to=weixin.models.message.media_file_rename, verbose_name='\u6587\u4ef6')),
                ('owner', models.ForeignKey(verbose_name='\u8d26\u6237', to='weixin.Account')),
            ],
            options={
                'verbose_name': '\u5a92\u4f53\u6587\u4ef6',
                'verbose_name_plural': '\u5a92\u4f53\u6587\u4ef6',
            },
        ),
        migrations.CreateModel(
            name='MediaMsg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='\u8be5\u540d\u79f0\u4ec5\u7528\u4e8e\u5217\u8868\u663e\u793a', max_length=100, verbose_name='\u663e\u793a\u540d\u79f0')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('item', models.ForeignKey(verbose_name='\u6587\u4ef6', to='weixin.MediaItem')),
                ('owner', models.ForeignKey(verbose_name='\u8d26\u6237', to='weixin.Account')),
            ],
            options={
                'verbose_name': '\u5a92\u4f53\u6d88\u606f',
                'verbose_name_plural': '\u5a92\u4f53\u6d88\u606f',
            },
        ),
        migrations.CreateModel(
            name='MsgReplyRule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='\u8be5\u540d\u79f0\u4ec5\u7528\u4e8e\u5217\u8868\u663e\u793a', max_length=100, verbose_name='\u663e\u793a\u540d\u79f0')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('res_msg_type', models.CharField(help_text='\u5185\u90e8\u5904\u7406\u8868\u793a\u7531\u672c\u5e94\u7528\u901a\u8fc7\u6307\u5b9a\u7684\u8fd4\u56de\u5185\u5bb9\u5bf9\u6d88\u606f\u8fdb\u884c\u54cd\u5e94\uff0c\u5916\u90e8\u5904\u7406\u8868\u793a\u7531\u5916\u90e8\u5e94\u7528\u5bf9\u6d88\u606f\u8fdb\u884c\u5904\u7406\uff0c\u518d\u4ea4\u7531\u672c\u5e94\u7528\u56de\u590d\u5230\u7528\u6237\u3002\u5176\u4e2d\u540c\u6b65\u5904\u7406\u8868\u793a\u672c\u5e94\u7528\u4f1a\u7b49\u5f85\u5904\u7406\u63a5\u53e3\u5e76\u5b9e\u65f6\u8fd4\u56de\uff0c\u5f02\u6b65\u5904\u7406\u8868\u793a\u672c\u5e94\u7528\u4f1a\u76f4\u63a5\u8fd4\u56de\u7528\u6237\u7a7a\u4fe1\u606f\uff0c\u5728\u63a5\u6536\u5230\u5904\u7406\u7ed3\u679c\u540e\u518d\u5411\u7528\u6237\u8fd4\u56de\u3002\u6ce8\u610f\u5916\u90e8\u5f02\u6b65\u5904\u7406\u9700\u8981\u4f7f\u7528\u5230\u5fae\u4fe1\u5ba2\u670d\u63a5\u53e3\uff0c\u5982\u65e0\u8be5\u63a5\u53e3\u6743\u9650\uff0c\u5219\u8be5\u6a21\u5f0f\u65e0\u6cd5\u5b9e\u73b0\u3002', max_length=10, verbose_name='\u54cd\u5e94\u5904\u7406\u65b9\u5f0f', choices=[(b'ishdl', '\u5185\u90e8\u540c\u6b65\u5904\u7406'), (b'oahdl', '\u5916\u90e8\u5f02\u6b65\u5904\u7406'), (b'oshdl', '\u5916\u90e8\u540c\u6b65\u5904\u7406')])),
                ('pool', models.CharField(max_length=4, null=True, verbose_name='\u961f\u5217\u6c60\u7f16\u53f7', blank=True)),
                ('msg_object_object_id', models.CharField(help_text='\u8981\u8fd4\u56de\u7684\u6d88\u606f\u4e3b\u4f53', max_length=255, null=True, verbose_name='\u5173\u8054\u6d88\u606f', blank=True)),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u751f\u6548')),
            ],
            options={
                'verbose_name': '\u6d88\u606f\u54cd\u5e94\u89c4\u5219',
                'verbose_name_plural': '\u6d88\u606f\u54cd\u5e94\u89c4\u5219',
            },
        ),
        migrations.CreateModel(
            name='NewsMsg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='\u8be5\u540d\u79f0\u4ec5\u7528\u4e8e\u5217\u8868\u663e\u793a', max_length=100, verbose_name='\u663e\u793a\u540d\u79f0')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u56fe\u6587\u6d88\u606f',
                'verbose_name_plural': '\u56fe\u6587\u6d88\u606f',
            },
        ),
        migrations.CreateModel(
            name='NewsMsgItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='\u8be5\u540d\u79f0\u4ec5\u7528\u4e8e\u5217\u8868\u663e\u793a', max_length=100, verbose_name='\u663e\u793a\u540d\u79f0')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('description', models.CharField(max_length=2000, verbose_name='\u63cf\u8ff0')),
                ('pic_large', models.ImageField(help_text='\u4e3a\u4fdd\u8bc1\u663e\u793a\u6548\u679c\uff0c\u8bf7\u4e0a\u4f20\u5927\u5c0f\u4e3a360*200\uff08\u6216\u540c\u6bd4\u4f8b\uff09\u7684\u56fe\u7247', upload_to=weixin.models.message.news_large_pic_rename, verbose_name='\u5927\u56fe')),
                ('pic_small', models.ImageField(help_text='\u4e3a\u4fdd\u8bc1\u663e\u793a\u6548\u679c\uff0c\u8bf7\u4e0a\u4f20\u5927\u5c0f\u4e3a200*200\uff08\u6216\u540c\u6bd4\u4f8b\uff09\u7684\u56fe\u7247', upload_to=weixin.models.message.news_small_pic_rename, verbose_name='\u5c0f\u56fe')),
                ('url', models.URLField(verbose_name='\u8df3\u8f6c\u94fe\u63a5')),
                ('owner', models.ForeignKey(verbose_name='\u8d26\u6237', to='weixin.Account')),
            ],
            options={
                'verbose_name': '\u56fe\u6587\u6d88\u606f\u4e3b\u4f53',
                'verbose_name_plural': '\u56fe\u6587\u6d88\u606f\u4e3b\u4f53',
            },
        ),
        migrations.CreateModel(
            name='NewsMsgItemMapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.IntegerField(default=1, verbose_name='\u6392\u5e8f')),
                ('newsmsg', models.ForeignKey(to='weixin.NewsMsg')),
                ('newsmsgitem', models.ForeignKey(verbose_name='\u6d88\u606f', to='weixin.NewsMsgItem')),
            ],
            options={
                'ordering': ['position'],
                'db_table': 'weixin_msg_newsmsg_items',
                'verbose_name': '\u56fe\u6587\u6d88\u606f\u5173\u8054',
                'verbose_name_plural': '\u56fe\u6587\u6d88\u606f\u5173\u8054',
            },
        ),
        migrations.CreateModel(
            name='QyAgent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agent_id', models.IntegerField(verbose_name='\u5e94\u7528ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u5e94\u7528\u540d\u79f0')),
                ('config', models.ForeignKey(verbose_name='\u6240\u5c5e\u4f01\u4e1a\u53f7', to='weixin.Config')),
            ],
            options={
                'verbose_name': '\u4f01\u4e1a\u53f7\u5e94\u7528\u914d\u7f6e',
                'verbose_name_plural': '\u4f01\u4e1a\u53f7\u5e94\u7528\u914d\u7f6e',
            },
        ),
        migrations.CreateModel(
            name='TextMsg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='\u8be5\u540d\u79f0\u4ec5\u7528\u4e8e\u5217\u8868\u663e\u793a', max_length=100, verbose_name='\u663e\u793a\u540d\u79f0')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('content', models.CharField(help_text='\u6d88\u606f\u5185\u5bb9', max_length=2000, verbose_name='\u5185\u5bb9')),
                ('owner', models.ForeignKey(verbose_name='\u8d26\u6237', to='weixin.Account')),
            ],
            options={
                'verbose_name': '\u6587\u5b57\u6d88\u606f',
                'verbose_name_plural': '\u6587\u5b57\u6d88\u606f',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('openid', models.CharField(max_length=64, verbose_name='OpenID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u52a0\u5165\u65f6\u95f4')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6709\u6548')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u5220\u9664')),
                ('belonging', models.ForeignKey(verbose_name='\u8d26\u6237', to='weixin.Account')),
            ],
            options={
                'verbose_name': '\u5fae\u4fe1\u7528\u6237',
                'verbose_name_plural': '\u5fae\u4fe1\u7528\u6237',
            },
        ),
        migrations.AddField(
            model_name='newsmsg',
            name='items',
            field=models.ManyToManyField(help_text='\u6d88\u606f\u4e3b\u4f53\uff0c\u6700\u591a\u652f\u630110\u4e2a\u3002', to='weixin.NewsMsgItem', verbose_name='\u56fe\u6587\u6d88\u606f', through='weixin.NewsMsgItemMapping'),
        ),
        migrations.AddField(
            model_name='newsmsg',
            name='owner',
            field=models.ForeignKey(verbose_name='\u8d26\u6237', to='weixin.Account'),
        ),
        migrations.AddField(
            model_name='msgreplyrule',
            name='agent',
            field=models.ForeignKey(verbose_name='\u4f01\u4e1a\u5e94\u7528', blank=True, to='weixin.QyAgent', null=True),
        ),
        migrations.AddField(
            model_name='msgreplyrule',
            name='msg_object_content_type',
            field=models.ForeignKey(related_name='msg_obj', blank=True, to='contenttypes.ContentType', help_text='\u6307\u5b9a\u8fd4\u56de\u7684\u6d88\u606f\u7c7b\u578b', null=True, verbose_name='\u54cd\u5e94\u6d88\u606f\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='msgreplyrule',
            name='owner',
            field=models.ForeignKey(verbose_name='\u8d26\u6237', to='weixin.Account'),
        ),
        migrations.AddField(
            model_name='loctrack',
            name='user',
            field=models.ForeignKey(verbose_name='\u7528\u6237', to='weixin.User'),
        ),
        migrations.AddField(
            model_name='keyword',
            name='rule',
            field=models.ForeignKey(verbose_name='\u5173\u8054\u89c4\u5219', to='weixin.MsgReplyRule'),
        ),
        migrations.AddField(
            model_name='eventreplyrule',
            name='agent',
            field=models.ForeignKey(verbose_name='\u4f01\u4e1a\u5e94\u7528', blank=True, to='weixin.QyAgent', null=True),
        ),
        migrations.AddField(
            model_name='eventreplyrule',
            name='msg_object_content_type',
            field=models.ForeignKey(related_name='event_msg_obj', blank=True, to='contenttypes.ContentType', help_text='\u6307\u5b9a\u8fd4\u56de\u7684\u6d88\u606f\u7c7b\u578b', null=True, verbose_name='\u54cd\u5e94\u6d88\u606f\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='eventreplyrule',
            name='owner',
            field=models.ForeignKey(verbose_name='\u8d26\u6237', to='weixin.Account'),
        ),
        migrations.AddField(
            model_name='event',
            name='from_user',
            field=models.ForeignKey(verbose_name='\u5fae\u4fe1\u7528\u6237', blank=True, to='weixin.User', null=True),
        ),
        migrations.AddField(
            model_name='button',
            name='agent',
            field=models.ForeignKey(verbose_name='\u4f01\u4e1a\u5e94\u7528', blank=True, to='weixin.QyAgent', null=True),
        ),
        migrations.AddField(
            model_name='button',
            name='owner',
            field=models.ForeignKey(verbose_name='\u8d26\u6237', to='weixin.Account'),
        ),
        migrations.AddField(
            model_name='button',
            name='parent',
            field=models.ForeignKey(verbose_name=b'\xe7\x88\xb6\xe7\xba\xa7\xe8\x8f\x9c\xe5\x8d\x95', blank=True, to='weixin.Button', null=True),
        ),
    ]
