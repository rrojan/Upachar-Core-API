from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'name',
            'phone_no',
            'hospital_name',
            'hospital_ward_name',
            'address',
            'province',
            'occupation',
            'sex',
            'age',
            'day_of_pcr_positive',
            'PCR_CT_value',
            'vaccination_status',
            'prevalent_conditions',
            'stage_of_patient',
            'comorbidity_problems',
            'smoking_status',
        )

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'name',
        )


class RegisterSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    password1 = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'profile')

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password1'])

        profile_data = validated_data.pop('profile')
        
        try:
            obj = Profile.objects.get(user=user)
            obj.delete()
        except:
            pass

        profile = Profile.objects.create(
            user = user,
            name = profile_data['name'],
            phone_no = profile_data['phone_no'],
            hospital_name = profile_data['hospital_name'],
            hospital_ward_name = profile_data['hospital_ward_name'],
            address = profile_data['address'],
            province = profile_data['province'],
            occupation = profile_data['occupation'],
            sex = profile_data['sex'],
            age = profile_data['age'],
            day_of_pcr_positive = profile_data['day_of_pcr_positive'],
            PCR_CT_value = profile_data['PCR_CT_value'],
            vaccination_status = profile_data['vaccination_status'],
            prevalent_conditions = profile_data['prevalent_conditions'],
            stage_of_patient = profile_data['stage_of_patient'],
            comorbidity_problems = profile_data['comorbidity_problems'],
            smoking_status = profile_data['smoking_status'],
        )
        user.save()
        profile.save()

        return user
