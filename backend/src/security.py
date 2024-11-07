from hashlib import md5
import jwt
import requests

salt = "NrRKEqcGJTGy7GI7XwgeHrDqC06p7qx5"
def encryptPassword(password : str) -> bool | str:
    decodedDict = jwt.decode(password, salt, algorithms=['HS256'])
    if decodedDict.get('origin', False) == "weLoveUL":
        return md5(decodedDict.get('content').encode()).hexdigest()
    return False

def verifyPassword(hashedPassword : str, password : str) -> bool:
    decodedDict = jwt.decode(password, salt, algorithms=['HS256'])
    if decodedDict.get('origin', False) == "weLoveUL":
        return md5(decodedDict.get('content').encode()).hexdigest() == hashedPassword
    return False

async def verifyGender(givenGender : str, firstName : str) -> bool:
    request = requests.get(f"https://api.genderize.io/?name={firstName}&country_id=US")
    if request.status_code == 200:
        return request.json()["gender"] == givenGender
    return False

async def verifyEmail(email : str) -> bool:
    try:
        return email[-10::] == "@ulaval.ca"
    except Exception as err:
        return False