# check the password is weak or mediam, ans strong;
password="secur"

if len(password)<6:
   strength="weak"
elif len(password) <=10:
   strength="medium"
else:
   strength="strong"

print("password strongth is:",strength)       