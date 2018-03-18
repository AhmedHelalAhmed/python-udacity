from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC79abc185f7b09d093e1f6ba16fb19e37"
# Your Auth Token from twilio.com/console
auth_token  = "28c28276b2949d99826165415503955e"

client = Client(account_sid,

                auth_token)

message = client.messages.create(
    to="+2***********", #your number
    from_="+12163501159", #twilio number
    body=". . . Python test test")

print(message.sid)

#https://www.twilio.com/user/account
#https://www.twilio.com/console/phone-numbers/getting-started
#https://www.twilio.com/console/phone-numbers/verified
#https://www.twilio.com/docs/quickstart/python/sms