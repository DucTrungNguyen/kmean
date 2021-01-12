# Generated by Django 3.1.5 on 2021-01-11 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tuvan',
            fields=[
                ('matv', models.AutoField(db_column='MaTV', primary_key=True, serialize=False)),
                ('kctam', models.FloatField(blank=True, db_column='KCTAM', null=True)),
                ('macn', models.TextField(blank=True, db_column='MaCN', null=True)),
                ('toadotam', models.TextField(blank=True, db_column='ToadoTAM', null=True)),
                ('manguoidung', models.TextField(blank=True, db_column='MaNguoiDung', null=True)),
                ('makdt', models.TextField(blank=True, db_column='MaKDT', null=True)),
            ],
            options={
                'db_table': 'TUVAN',
                'managed': False,
            },
        ),
        # migrations.CreateModel(
        #     name='Chuyennganh',
        #     fields=[
        #         ('macn', models.TextField(blank=True, db_column='MaCN', primary_key=True, serialize=False)),
        #         ('tencn', models.TextField(blank=True, db_column='TenCN', null=True)),
        #         ('makdt', models.TextField(blank=True, db_column='MaKDT', null=True)),
        #         ('tenbang', models.TextField(blank=True, db_column='TenBang', null=True)),
        #     ],
        #     options={
        #         'db_table': 'CHUYENNGANH',
        #     },
        # ),
        # migrations.CreateModel(
        #     name='Ctdaotao',
        #     fields=[
        #         ('mamh', models.TextField(blank=True, db_column='MaMH', primary_key=True, serialize=False)),
        #         ('sttmh', models.IntegerField(blank=True, db_column='SttMH', null=True)),
        #         ('tenmh', models.TextField(blank=True, db_column='TenMH', null=True)),
        #         ('tinchi', models.TextField(blank=True, db_column='TinCHI', null=True)),
        #         ('makdt', models.TextField(blank=True, db_column='MaKDT', null=True)),
        #     ],
        #     options={
        #         'db_table': 'CTDAOTAO',
        #     },
        # ),
        # migrations.CreateModel(
        #     name='Khoadaotao',
        #     fields=[
        #         ('makdt', models.TextField(blank=True, db_column='MaKDT', primary_key=True, serialize=False)),
        #         ('tenkdt', models.TextField(blank=True, db_column='TenKDT', null=True)),
        #     ],
        #     options={
        #         'db_table': 'KHOADAOTAO',
        #     },
        # ),
        # migrations.CreateModel(
        #     name='Nguoidung',
        #     fields=[
        #         ('manguoidung', models.AutoField(db_column='MaNguoiDung', primary_key=True, serialize=False)),
        #         ('tennguoidung', models.TextField(blank=True, db_column='TenNguoiDung', null=True)),
        #         ('quyennguoidung', models.IntegerField(blank=True, db_column='QuyenNguoiDung', null=True)),
        #         ('tendangnhap', models.TextField(blank=True, db_column='TenDangNhap', null=True)),
        #         ('matkhau', models.TextField(blank=True, db_column='MatKhau', null=True)),
        #     ],
        #     options={
        #         'db_table': 'NGUOIDUNG',
        #     },
        # ),
        # migrations.CreateModel(
        #     name='Sinhvien',
        #     fields=[
        #         ('masv', models.TextField(blank=True, db_column='MaSV', primary_key=True, serialize=False)),
        #         ('ho', models.TextField(blank=True, db_column='Ho', null=True)),
        #         ('ten', models.TextField(blank=True, db_column='Ten', null=True)),
        #     ],
        #     options={
        #         'db_table': 'SINHVIEN',
        #     },
        # ),
        # migrations.CreateModel(
        #     name='MonhocChuyennganhLoc',
        #     fields=[
        #         ('id', models.AutoField(primary_key=True, serialize=False)),
        #         ('macn', models.ForeignKey(blank=True, db_column='MaCN', null=True, on_delete=django.db.models.deletion.CASCADE, to='student.chuyennganh')),
        #         ('makdt', models.ForeignKey(blank=True, db_column='MaKDT', null=True, on_delete=django.db.models.deletion.CASCADE, to='student.khoadaotao')),
        #         ('mamh', models.ForeignKey(blank=True, db_column='MaMH', null=True, on_delete=django.db.models.deletion.CASCADE, to='student.ctdaotao')),
        #     ],
        #     options={
        #         'db_table': 'MONHOC_CHUYENNGANH_LOC',
        #     },
        # ),
        # migrations.CreateModel(
        #     name='MonhocChuyennganh',
        #     fields=[
        #         ('id', models.AutoField(primary_key=True, serialize=False)),
        #         ('sttmh', models.IntegerField(blank=True, db_column='SttMH', null=True)),
        #         ('makdt', models.TextField(blank=True, db_column='MaKDT', null=True)),
        #         ('macn', models.ForeignKey(blank=True, db_column='MaCN', null=True, on_delete=django.db.models.deletion.CASCADE, to='student.chuyennganh')),
        #         ('mamh', models.ForeignKey(blank=True, db_column='MaMH', null=True, on_delete=django.db.models.deletion.CASCADE, to='student.ctdaotao')),
        #     ],
        #     options={
        #         'db_table': 'MONHOC_CHUYENNGANH',
        #     },
        # ),
        # migrations.CreateModel(
        #     name='Diemsv2',
        #     fields=[
        #         ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
        #         ('diem', models.FloatField(blank=True, db_column='Diem', null=True)),
        #         ('macn', models.ForeignKey(blank=True, db_column='MaCN', null=True, on_delete=django.db.models.deletion.CASCADE, to='student.chuyennganh')),
        #         ('makdt', models.ForeignKey(blank=True, db_column='MaKDT', null=True, on_delete=django.db.models.deletion.CASCADE, to='student.khoadaotao')),
        #         ('mamh', models.ForeignKey(blank=True, db_column='MaMH', null=True, on_delete=django.db.models.deletion.CASCADE, to='student.ctdaotao')),
        #         ('masv', models.ForeignKey(blank=True, db_column='MaSV', null=True, on_delete=django.db.models.deletion.CASCADE, to='student.sinhvien')),
        #     ],
        #     options={
        #         'db_table': 'DIEMSV2',
        #         'managed': True,
        #     },
        # ),
    ]
