from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


PROVINCES = (
    (1, 'Province 1'),
    (2, 'Province 2'),
    (3, 'Bagmati'),
    (4, 'Gandaki'),
    (5, 'Lumbini'),
    (6, 'Karnali'),
    (7, 'Sudurpaschim'),
)

SEX = (('M', 'Male'), ('F', 'Female'))

YES_NO = (('Y', 'Yes'), ('N', 'No'))

STAGES = (('Mild', 'Mild'), ('Moderate', 'Moderate'), ('Severe', 'Severe'))

SMOKER_STATUS = (
    ('regular', 'Regular Smoker'),
    ('occasional', 'Occasional smoking habit'),
    ('quit', 'Has smoking habit but recently quit'),
    ('never', 'Never had smoking habit')
)

USER_TYPES = (('patient', 'Patient'), ('doctor', 'Doctor'), ('hospital', 'Hospital'))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, null=True, blank=True)
    phone_no = models.CharField(max_length=10, null=True, blank=True)

    hospital_name = models.CharField(max_length=32, null=True, blank=True)
    hospital_ward_name = models.CharField(max_length=32, null=True, blank=True)

    address = models.CharField(max_length=32, null=True, blank=True)
    province = models.IntegerField(choices=PROVINCES, null=True, blank=True)

    occupation = models.CharField(max_length=34, null=True, blank=True)
    sex = models.CharField(choices=SEX, max_length=1, null=True, blank=True)

    age = models.PositiveIntegerField(null=True, blank=True)
    day_of_pcr_positive = models.PositiveIntegerField(null=True, blank=True)
    PCR_CT_value = models.DecimalField(decimal_places=5, max_digits=10, null=True, blank=True)
    vaccination_status = models.CharField(max_length=1, choices=YES_NO, null=True, blank=True)

    prevalent_conditions = models.JSONField(null=True, blank=True)
    stage_of_patient = models.CharField(max_length=8, choices=STAGES, null=True, blank=True)
    comorbidity_problems = models.JSONField(null=True, blank=True)
    smoking_status = models.CharField(max_length=10, choices=SMOKER_STATUS, null=True, blank=True)

    user_type = models.CharField(max_length=8, choices=USER_TYPES, default='patient')

    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='assigned')

    def __str__(self) -> str:
        return f'{self.name} [{self.user.username}]'
    
    def get_assigned_count(self):
        return self.user.assigned.count()
    
    def get_assigned_all(self):
        assigned = self.user.assigned.all()
        return [patient.name for patient in assigned]


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
