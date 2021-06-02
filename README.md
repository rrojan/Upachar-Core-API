# Upachar_API

## API Docs:

admin login: admin, testing321

### URL Routes and Endpoints

- /api/register/ -> Register for an account. Use patient id as username.
    - Data in format
        ```
        {
            "username": "",
            "password1": "",
            "password2": "",
            "profile": {
                "name": "",
                "phone_no": "",
                "hospital_name": "",
                "hospital_ward_name": "",
                "address": "",
                "province": {((1, 'Province 1'), (2, 'Province 2'), (3, 'Bagmati'), (4, 'Gandaki'), (5, 'Lumbini'), (6, 'Karnali (7, 'Sudurpaschim'),)},
                "occupation": "",
                "sex": { (('M', 'Male'), ('F', 'Female'))},
                "age": 0,
                "day_of_pcr_positive": 0,
                "PCR_CT_value": 0.00,
                "vaccination_status": {(('Y', 'Yes'), ('N', 'No'))},
                "prevalent_conditions": {JSON with list},
                "stage_of_patient": {(('Mild', 'Mild'), ('Moderate', 'Moderate'), ('Severe', 'Severe'))},
                "comorbidity_problems": {JSON with list},
                "smoking_status": {(('regular', 'Regular Smoker'), ('occasional', 'Occasional smoking habit'), ('quit', 'Has smoking habit but recently quit'), ('never', 'Never had smoking habit')) }
            }
        }
        ```


- /api/get-token/ -> Pass patient ID (username) and password to get your unique token
    - Data in format:
        ```
        {
            "username": "",
            "password": ""
        }
        ```


- /api/questions/ -> Get a list of all questions currently marked active in database.


- /api/submit/ -> submit a response
    - Data in format: `{"user": {patient_pk (from get-token)}, "data": {JSON}}`. Example:
        ```
        {
            "user": 8,
            "data": {
                "1": [
                    1,
                    2,
                    3
                ],
                "2": "2",
                "3": [
                    "cetamol",
                    "brufin"
                ],
                "4": [
                    1,
                    2
                ],
                "5": "2",
                "6": "2",
                "7": "1",
                "8": [
                    2,
                    3,
                    4,
                    5
                ],
                "9": "2",
                "10": "1"
            }
        }
        ```

