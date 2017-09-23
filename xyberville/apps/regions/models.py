from django.db import models


class Province(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'province'
        verbose_name_plural = 'provinces'

    def __unicode__(self):
        return self.name


class Regency(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    province = models.ForeignKey(
        'regions.Province', to_field='code', db_column='province_code'
    )

    class Meta:
        verbose_name = 'regency'
        verbose_name_plural = 'regencies'

    def __unicode__(self):
        return self.name


class District(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)

    regency = models.ForeignKey(
        'regions.Regency', to_field='code', db_column='regency_code'
    )

    class Meta:
        verbose_name = 'district'
        verbose_name_plural = 'districts'

    def __unicode__(self):
        return self.name


class Village(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    district = models.ForeignKey(
        'regions.District', to_field='code', db_column='district_code'
    )

    class Meta:
        verbose_name = 'village'
        verbose_name_plural = 'villages'

    def __unicode__(self):
        return self.name
