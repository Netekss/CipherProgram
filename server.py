import secrets
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from cipher.encode import encode_cipher
from cipher.decode import decode_cipher

app = FastAPI()
security = HTTPBasic()


def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, "superuser")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.post("/encode/{string}")
def encoding(string: str, user: str = Depends(authenticate)):
    return encode_cipher(string)


@app.post("/decode/{string}/{key}")
def decoding(string: str, key: str, user: str = Depends(authenticate)):
    return decode_cipher(string, key)
