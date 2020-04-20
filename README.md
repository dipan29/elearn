# IAE-Elearn Work Enlistment
Institute of Academic Excellence Online Learning Platform
<hr />

* on course list page having issues with images and all   ✅
* play video box not auto sizing to the video  ✅
* multiple demo field add feature  
* change password add feature instead of reset password (keep both)  ✅
* change profile page and add these features from this form https://goo.gl/forms/8HwD0l2gZ7JLSaIJ3  ✅
* make coupon codes course specific, I guess that is better than global. Also allow global or course wise.  ✅

* multi-level directory of category (Course (GATE) -> ECE, this much)  

*For the enroll Part*  
People can enroll for a course that will have 10 sub courses, you may call me to understand this. Say for example you have GATE->ECE->Analog Electronics. Now there can be 10 subjects under course. If someone purchases GATE course, he will get 10 enrolls automatically as sir will allow each one of them individually. Mane people will buy main category course like GATE->ECE, but will have 10 sub category will behave as independent course, which can be individually enabled in enrolls. **This is a important feature sir told me, just today**.  


otp based login, purchase course notification and course payment sucessfull notification -> I will give you apis, you will cURL them.  
Basically on course cart, just send a notification to pay.  
and if the admin approves mane the enroll then ekta sms jabey approved. Will show the APIs, easy.  


* databse targetted front page (Site Title, Description, Image, Gradient Points, Site Logo & and the three meta datas)  ✅

META DESCRIPTION , FB & Twitter Cards -> you missed this last time  

<hr />

Write a done, beside it, once done.

<hr />

#### To get started, pull this repository. Then ->  
 
virtualenv iae  
iae\scripts\activate  
pip install -r requirements.txt  
python manage.py makemigrations  
python manage.py migrate  
python manage.py createsuperuser  
python manage.py runserver  
  
python manage.py collectstatic (for debug not true)