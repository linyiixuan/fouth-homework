Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import itchat
█


>>> itchat.login()
Getting uuid of QR code.
Downloading QR code.
Please scan the QR code to log in.
Please press confirm on your phone.
Loading the contact, this may take a little while.
--- Logging error ---
Traceback (most recent call last):
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\logging\__init__.py", line 996, in emit
    stream.write(msg)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\idlelib\run.py", line 362, in write
    return self.shell.write(s, self.tags)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\idlelib\rpc.py", line 608, in __call__
    value = self.sockio.remotecall(self.oid, self.name, args, kwargs)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\idlelib\rpc.py", line 220, in remotecall
    return self.asyncreturn(seq)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\idlelib\rpc.py", line 251, in asyncreturn
    return self.decoderesponse(response)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\idlelib\rpc.py", line 271, in decoderesponse
    raise what
UnicodeEncodeError: 'UCS-2' codec can't encode characters in position 24-24: Non-BMP character not supported in Tk
Call stack:
  File "<string>", line 1, in <module>
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\idlelib\run.py", line 144, in main
    ret = method(*args, **kwargs)
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\idlelib\run.py", line 474, in runcode
    exec(code, self.locals)
  File "<pyshell#1>", line 1, in <module>
  File "C:\Users\HP\AppData\Local\Programs\Python\Python36\lib\site-packages\itchat\components\login.py", line 80, in login
    logger.info('Login successfully as %s' % self.storageClass.nickName)
Unable to print the message and arguments - possible formatting error.
Use the traceback above to help find the error.


>>> friends = itchat.get_friends(update = True )[0:]

>>> male=female = other =0
>>> for i in friends[1:]: 
 	sex = i["Sex"] 
 	if sex ==1: 
 		male +=1 
 	elif sex ==2: 
 		female += 1 
 	else: 
 		other +=1
 		

 		


>>> total =len(friends[1:])


>>> print("男性好友：%.2f%%" % (float(male) / total * 100))
男性好友：46.05%


>>> print("女性好友：%.2f%%" % (float(female) / total * 100))
女性好友：48.68%
>>> print("其他：%.2f%%" % (float(other) / total * 100))
其他：5.26%
>>> 
