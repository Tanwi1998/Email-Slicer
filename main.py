email=input("Enter Your Email Id:")
username=email[:email.index("@")]
domain=email[email.index("@")+1:len(email)]
print("Your Username is:", username)
print("Your Domain is:", domain)