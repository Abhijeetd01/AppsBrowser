from django.db import models

# Create your models here.

class DataEm(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    price = models.FloatField(blank=True, null=True)
    developer = models.CharField(max_length=255, blank=True)
    reviewers = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True)
    dev_website = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    content_rating = models.CharField(max_length=45, blank=True)
    date_published = models.DateField(blank=True, null=True)
    operating_system = models.CharField(max_length=255, blank=True)
    downloads = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, blank=True)
    developer_link = models.TextField(blank=True)
    app_url = models.TextField()
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    rating = models.FloatField(blank=True, null=True)
    cluster_id = models.IntegerField()
    lang_id = models.CharField(max_length=5, blank=True)


    class Meta:
        db_table = 'data_em'