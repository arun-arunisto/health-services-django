# health-services-django

Health Services Project using the `django-framework`.

## How to usw this repository
First open command prompt and clone this repo using the below command
```commandline
git clone https://github.com/arun-arunisto/health-services-django.git
```
after cloning the repo navigate to the directory using the below command
```commandline
cd health-services-django
```
then create a virtual environment using the below command
```commandline
python -m venv myenv
```
then activate the virtual environment using the below command (below command is only applicable for windows)
```commandline
myenv\Scripts\activate
```
After activating the virtual environment install the `django` using below command
```commandline
pip install django
```
After successfully installed django use the below command to run the project
```commandline
python manage.py runserver
```
Then navigate to the url `http://localhost:8000/` the result will be look like below: (client login page)

![img.png](img.png)

`http://localhost:8000/care_portal` This page will navigate you to the other login options of `Agency` & `Staff`

![img_1.png](img_1.png)

Then click on the options it will lead you to the result of `staff_login` & `agency_login` like below

![img_2.png](img_2.png)
 