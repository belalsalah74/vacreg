# Generated by Django 4.1.1 on 2022-10-12 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vac', '0002_alter_vaccineshot_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccineshot',
            name='city',
            field=models.CharField(choices=[('1', '15 May'), ('2', 'Al Azbakeyah'), ('3', 'Al Basatin'), ('4', 'Tebin'), ('5', 'El-Khalifa'), ('6', 'El darrasa'), ('7', 'Aldarb Alahmar'), ('8', 'Zawya al-Hamra'), ('9', 'El-Zaytoun'), ('10', 'Sahel'), ('11', 'El Salam'), ('12', 'Sayeda Zeinab'), ('13', 'El Sharabeya'), ('14', 'Shorouk'), ('15', 'El Daher'), ('16', 'Ataba'), ('17', 'New Cairo'), ('18', 'El Marg'), ('19', 'Ezbet el Nakhl'), ('20', 'Matareya'), ('21', 'Maadi'), ('22', 'Maasara'), ('23', 'Mokattam'), ('24', 'Manyal'), ('25', 'Mosky'), ('26', 'Nozha'), ('27', 'Waily'), ('28', 'Bab al-Shereia'), ('29', 'Bolaq'), ('30', 'Garden City'), ('31', 'Hadayek El-Kobba'), ('32', 'Helwan'), ('33', 'Dar Al Salam'), ('34', 'Shubra'), ('35', 'Tura'), ('36', 'Abdeen'), ('37', 'Abaseya'), ('38', 'Ain Shams'), ('39', 'Nasr City'), ('40', 'New Heliopolis'), ('41', 'Masr Al Qadima'), ('42', 'Mansheya Nasir'), ('43', 'Badr City'), ('44', 'Obour City'), ('45', 'Cairo Downtown'), ('46', 'Zamalek'), ('47', 'Kasr El Nile'), ('48', 'Rehab'), ('49', 'Katameya'), ('50', 'Madinty'), ('51', 'Rod Alfarag'), ('52', 'Sheraton'), ('53', 'El-Gamaleya'), ('54', '10th of Ramadan City'), ('55', 'Helmeyat Alzaytoun'), ('56', 'New Nozha'), ('57', 'Capital New'), ('58', 'Giza'), ('59', 'Sixth of October'), ('60', 'Cheikh Zayed'), ('61', 'Hawamdiyah'), ('62', 'Al Badrasheen'), ('63', 'Saf'), ('64', 'Atfih'), ('65', 'Al Ayat'), ('66', 'Al-Bawaiti'), ('67', 'ManshiyetAl Qanater'), ('68', 'Oaseem'), ('69', 'Kerdasa'), ('70', 'Abu Nomros'), ('71', 'Kafr Ghati'), ('72', 'Manshiyet Al Bakari'), ('73', 'Dokki'), ('74', 'Agouza'), ('75', 'Haram'), ('76', 'Warraq'), ('77', 'Imbaba'), ('78', 'Boulaq Dakrour'), ('79', 'Al Wahat Al Baharia'), ('80', 'Omraneya'), ('81', 'Moneeb'), ('82', 'Bin Alsarayat'), ('83', 'Kit Kat'), ('84', 'Mohandessin'), ('85', 'Faisal'), ('86', 'Abu Rawash'), ('87', 'Hadayek Alahram'), ('88', 'Haraneya'), ('89', 'Hadayek October'), ('90', 'Saft Allaban'), ('91', 'Smart Village'), ('92', 'Ard Ellwaa')], default='1', max_length=255),
        ),
    ]
