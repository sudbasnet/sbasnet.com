from django.db import models


class Intro(models.Model):
    topic = models.CharField(max_length=200)
    rank = models.IntegerField(blank=True)
    img = models.CharField(max_length=200)
    body = models.TextField()
    date_added = models.DateTimeField()

    def __str__(self):
        return self.topic


class CareerSummary(models.Model):
    topic = models.CharField(max_length=10)
    body = models.TextField()
    date_added = models.DateTimeField()

    def __str__(self):
        return self.topic


class Resume(models.Model):
    section = models.CharField(max_length=200)  # Work Experience
    title = models.CharField(max_length=100)  # Software Engineer
    # University of Nebraska - Lincoln
    place = models.CharField(max_length=500)
    place_url = models.CharField(max_length=200, default=None)  # unl.edu
    started = models.DateField
    ended = models.DateField
    show_default = models.CharField(max_length=500)
    details = models.TextField(default=None)

    def __str__(self):
        return self.title


class WorkExperience(models.Model):
    title = models.CharField(max_length=100)
    where = models.CharField(max_length=200)
    office_url = models.CharField(max_length=100)
    additional_info = models.CharField(max_length=200, blank=True, null=True)
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
    responsibilities = models.TextField()

    collapsable = models.TextField(blank=True, null=True)
    button_text = models.CharField(blank=True, null=True, max_length=20)

    def __str__(self):
        return self.title


class Education(models.Model):
    degree = models.CharField(max_length=100)
    where = models.CharField(max_length=200)
    office_url = models.CharField(max_length=100)
    additional_info = models.CharField(max_length=250, blank=True, null=True)
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
    points = models.TextField()
    collapsable = models.TextField(blank=True, null=True)
    button_text = models.CharField(blank=True, null=True, max_length=20)

    def __str__(self):
        return self.degree


class Skill(models.Model):
    type = models.CharField(max_length=100)
    skills = models.TextField()
    expandable = models.TextField()
    type_rank = models.IntegerField()

    def __str__(self):
        return self.type


class Art(models.Model):
    rank = models.IntegerField(blank=True, null=True)
    thumbnail_label = models.CharField(max_length=200)
    description = models.TextField()
    static_img_path = models.CharField(max_length=200)

    def __str__(self):
        return self.thumbnail_label
