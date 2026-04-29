## 11.5 Reloading modules

Sometimes a Python program imports a module, but then the source code of the imported module needs to be changed. Since modules are executed only once when imported, changing the module's source does not affect the running Python instance. Instead of restarting the entire Python program, the reload() function can be used to reload and re-execute the changed module. The reload() function is located in the importlib standard library module.

Consider the following module, which can send an email using a Google gmail account:

> **send_gmail.py: Sends a single email through gmail.**
> ```python
> import smtplib
> from email.mime.text import MIMEText
> 
> header = "Hello. This is an automated email.

"
> 
> def send(subject, to, frm, text):
>     # The message to send
>     msg = MIMEText(header + text)
>     msg["Subject"] = subject
>     msg["To"] = to
>     msg["From"] = frm
> 
>     # Connect to gmail's email server and send
>     s = smtplib.SMTP("smtp.gmail.com", port=587)
>     s.ehlo()
>     s.starttls()
>     s.login(user=frm, password="password")
>     s.sendmail(frm, [to], msg.as_string())
>     s.quit()
> 
> if __name__ == "__main__":
>     send(
>         subject="A coupon for you!",
>         to="billgates@microsoft.com",
>         frm="JohnnysHotDogs1@gmail.com",
>         text="Enjoy!")
> ```
> ```
> To: billgates@microsoft.com
> From: JohnnysHotDogs1@gmail.com
> Subject: A coupon for you!
> 
> Hello. This is an automated email.
> 
> Enjoy!
> ```

The send_coupons.py script below imports send_gmail.py as a module, using the send function to deliver important messages to customers.

> **send_coupons.py: Automates emails to loyal customers.**
> ```python
> import os
> from importlib import reload
> import send_gmail
> 
> mod_time = os.path.getmtime(send_gmail.__file__)
> 
> emails = [  # Could be large list or stored in file
>     "billgates@microsoft.com",
>     "president@whitehouse.gov",
>     "benedictxvi@vatican.va"
> ]
> 
> my_email = "JohnnysHotDogs1@gmail.com"
> subject = "A coupon for you!"
> text = ("As a loyal customer of Johnny's HotDogs, "
>         "here is a coupon for 1 free bratwurst!")
> 
> for addr in emails:
>     send_gmail.send(subject, addr, my_email, text)
> 
>     # Check if file has been modified
>     last_mod = os.path.getmtime(send_gmail.__file__) 
>     if last_mod > mod_time:
>         mod_time = last_mod
>         reload(send_gmail)
> ```

If thousands of emails are being sent, the program should not be stopped because rerunning the program could cause duplicate emails to be sent to some users, and Johnny's HotDogs might annoy their customers. If Johnny wants to change the content of the header string in the send_gmail module without stopping the program, then the variable's value in send_gmail.py's *source code* can be updated and reloaded.

When send_coupons.py imports send_gmail, a global variable mod_time stores the time when send_gmail.py was last modified, using the os.path.getmtime() function. The __file__ special name contains the path to a module in the computer file system, e.g., the value of send_gmail.__file__ might be "C:\Users\Johnny\send_gmail.py". A comparison is made to the original modification time at the end of the for loop &ndash; if the modification time is greater than the original, then the module's source code has been updated and the module should be reloaded.

Modifying the header string in send_gmail.py to "This is an important message from Johnny" while the program is running causes the module to be reloaded, which alters the contents of the emails.

> **Modifying send_gmail.py while the program is running updates the email contents.**
> ```python
> import smtplib
> from email.mime.text import MIMEText
> 
> header = "This is an important message from Johnny!"
> 
> def send(subject, to, frm, txt):
>     # ...
> ```
> ```
> To: president@whitehouse.gov
> From: JohnnysHotDogs1@gmail.com
> Subject: A coupon for you!
> 
> This is an important message from Johnny!
> 
> As a loyal customer of Johnny's HotDogs, 
> here is a coupon for 1 free bratwurst!
> ```

The reload function reloads a module in place. When reload(send_gmail) returns, the namespace of the send_gmail module will contain updated definitions. The call to send_gmail.send() still accesses the same send_gmail module object, but the definition of send() will have been updated.

Importing attributes directly using "from", and then reloading the corresponding module, will *not* update the imported attributes.

> **Reloading modules doesn't affect attributes imported using 'from'.**
> | from importlib import reload import send_gmail from send_gmail import header  print(f"Original value of header: {header}")  print("
(---- send_gmail.py source code edited ----)")  print("
Reloading send_gmail
") reload(send_gmail)  print(f"header: {header}") print(f"send_gmail.header: {send_gmail.header}") |
> | `Original value of header: Hello. This is an automated email.  (---- send_gmail.py edited ----)  Reloading send_gmail.  header: Hello. This is an automated email. send_gmail.header: Hello from Johnny's Hotdogs!` |

Reloading modules is typically useful in long-running programs, when restarting and initializing the entire program may be an expensive operation. A common scenario is a web server that is communicating with multiple clients on the internet. Instead of restarting the server and disconnecting all of the clients, a single module can be reloaded dynamically as the server runs.

### PARTICIPATION ACTIVITY: Reloading modules.

**1.** Modules cannot be reloaded if they have already been imported.
Answer: **False**
*The purpose of the reload function is to reload modules that have changed since importation.*

**2.** The reload function modifies a module in place.
Answer: **True**
*reload() also returns the module but can be ignored.*

**3.** Reloading a module is useful when restarting a program is prohibitively costly.
Answer: **True**
*Reloading is often done in server programs, where shutting down a server may disconnect clients.*