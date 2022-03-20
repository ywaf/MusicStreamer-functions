import os
import firebase_admin
from firebase_admin import db
from firebase_admin import auth
from firebase_admin import credentials

a = {
  "type": "service_account",
  "project_id": "musicstreamer-sdd",
  "private_key_id": "db8b6a2f7dc8dcf6e7005e530d645098fb242adc",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDV2dJBQ0/eAeaf\nRnTO76+iMMfjrvXelrM7S3KgYLCfH7bCAOhgPZ+Bn9MyZsW9EtM0krLxJZbf5j0u\nLVH69BTNqsYqfpBqAdPVKWJh2UcKHGTbZW80tOLlHIDh2fYIyGN5FLTSRHoiHiIo\nWfRDwurg8zSKjLJH2eH0dNLv1tyHijkncaVbv/c+R8xRgIQruGR1Ts4Ds4cgNGsU\nhnLT9W1+1q/GWB9H9GmE+h4O0vsiOQlncSRRECdjVbuiKtxLDIqW/Z9yCoFoGxls\n9p7CcTMSo21ry9HC8+aZmVjp0tJINBL3b4WPLNUlys2+oHR5AXvmM24NAxjYjoaL\nlU7u2yw3AgMBAAECggEAVUCRW9goSlKKrHtrjKWr6GY3AdMZjIOabyx8RWhWcRE1\nC/FNsjRO1t+u09x5vw72qPJEqPL5y0efoz2I/Zj5hCYs+vraupAA8W0enfB/LA42\nvOoao7Hq9DhhPuhj94tfcIErNtn6sIg/yMNXp/3YIhaCnytI1XEMbaZ3Awsufk+H\nK519e4qLYPzAgWVJq9cyt2ffvvJGyzA7ChiwKtX9IbgDzDVqAX8GsR9Ct8mYxbDL\ny76boU6OrFoy9AhCexhB/GdWOyCl0TGUA2incefZxOqjhIrfBaiQ+MSoz081wF9o\nTU6jTNc56tbA4xDnNKti0RSJnPT54RWxfDaYEN3+8QKBgQDwQZT3IN80L4kFe+bJ\nM7Kc6pswkPMZi+VD2PnOi0Git3M85WbV8KwOQTlmH0yjbkSZRfz2qV0uJj6HooRJ\nlTZNTcSw/fQXov+07BBvlQtd3Dqbz1E7uYSYXsllbF8+EwS/kJM/PR7Fds5cTKHO\ns9/lLuall4isTtPHwTkUCgfARwKBgQDj3Ubo7C5kJPFA7oonroVDFHyp5iNrdBJr\nh5uceXA8ntdGw4P/PaZF6Y2pAdcHEEQBt1KQ3ZMAV+pMcE09fo0voBexle2DzRlD\nqLz2qLu2/w3IISL8rjhJLOMriuURubjy2bG/jCthdMRKbfR0V0UN8brNqrZlrbBu\ngy7vEFSckQKBgQCZYVTnnC3C1CIGxT3l70I1GTVwAOmhwoTgFrIMIS0K41EHbHCF\nXnuJMiyhvJOhtnDG5T6EfkVFhBbhYmhPzZl4KpDKaaYePOpAJ4Cqq50xE7q649S5\na0tyNvkd7dyz9VJPtc27TprJd3pwxF98ZasnVhTbXG1di4l6eimlWG3wWwKBgFw/\npQl/NHjOi+0hpUTTXpf9n0qZJRXHc/2cdN8wOsQP+k9nr/SRXNNI7lTRrd/qMd4P\n/ZkwWub0sKIphNu0dCwnv+/hJrsJOYUutvGU9gnr0ASJhcSOM7NMPNvP61T1v25x\nu4g0kwttXlpTkXfYLNisWFgTGKypWJgk+8dE8TxBAoGAGzE399xEP89mNE4YPccB\nRS+jqDqjgYzqRf3/u/XE1IgFw/2sCwBXodA9pXD0KmLBO1oZvPx+6EmjrBkR/3qD\nck4Jv2Dy6XiNDmGRSF16EcHp8JuROe/EW9lZX9362VemyaPX0Vzu1TdoOyGxbHFS\nLRr/uQV3dlRSO+AfRs6y5CA=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-shj6g@musicstreamer-sdd.iam.gserviceaccount.com",
  "client_id": "112551480839027074177",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-shj6g%40musicstreamer-sdd.iam.gserviceaccount.com"
}

cred = credentials.Certificate(a)  # use actions secrets!!
firebase_admin.initialize_app(cred)
decoded_token = auth.verify_id_token("")
uid = decoded_token['uid']
print(decoded_token)
print(uid)

