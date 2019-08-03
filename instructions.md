# Instructions

## Run the Django App locally

1. Download Miniconda3 for your OS:<br>  <https://docs.conda.io/en/latest/miniconda.html>

2. Install Miniconda3 following the instructions for your OS  
<https://conda.io/projects/conda/en/latest/user-guide/install/index.html>

3. Once installed, open Anaconda Prompt if you use Windows or Bash if you use Linux and run the following commands:
```
conda init
```

4. Create a Python 3.6 virtual environment.
```
conda create -n djangoenv python=3.6
```

Select yes when prompted

5. Activate the environment you justed created.
```
conda activate djangoenv
```

6. Install all requirements found in /Path/to/project/.../code/requirements.txt:

```
pip install -r requirements.txt
```

7. Once the requirements are installed, use <https://www.miniwebtool.com/django-secret-key-generator/> to generate
a random SECRET_KEY.   Edit /Path/to/project/.../code/ktel/settings.py and add the key in line 23.

8. Once this is done, run the following commands in Anaconda prompt or Bash:

```
cd /Path/to/project/.../code/
python manage.py runserver 4041
```

9. Open <http://127.0.0.1/4041> in your browser. <br>

## View the App online

Open <http://patrasktel.eu-west-3.elasticbeanstalk.com/> in your browser.<br>
<br>

## Using the Admininstrator Page

Open <http://127.0.0.1/4041/admin> or <http://patrasktel.eu-west-3.elasticbeanstalk.com/admin> in your browser.  
Log in using:<br>  
  username: `admin`  
  password: `root1234`  
   <br><strong>Warning</strong>: 
   All changes are permanent!!! 
