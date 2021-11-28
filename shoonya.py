from NorenRestApiPy.NorenApi import PriceType, BuyorSell, ProductType
from api_helper import NorenApiPy, get_time
import logging
import hashlib

logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

#credentials
user        = 'FA42707'
u_pwd       = 'Subuin@321'
factor2     = 'ARNPM5630L'
vc          = 'FA42707_U'
app_key     = 'APILi23112021LOP09I1D911A'
imei        = '9000530962'


ret = api.login(userid=user, password=u_pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)
print(ret)
