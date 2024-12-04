import os
from  env.key_ini import  key_ini

key_ini("./env/.keys")
print(os.environ["GOOGLE_CSE_ID"])

