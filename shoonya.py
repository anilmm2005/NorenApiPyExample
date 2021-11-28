from NorenRestApiPy.NorenApi import PriceType, BuyorSell, ProductType
from api_helper import NorenApiPy, get_time
import logging
import hashlib

logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

#credentials
user        = ${{secret.user}}
u_pwd       = ${{secret.u_pwd}}
factor2     = ${{secret.factor2}}
vc          = ${{secret.vc}}
app_key     = ${{secret.app_key}}
imei        = ${{secret.imei}}


ret = api.login(userid=user, password=u_pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)
print(ret)
