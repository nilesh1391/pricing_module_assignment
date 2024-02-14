# PricingModuleProject

Assessment Project for Fyn Mobility

## Backend( Django )

#### Installing

open terminal and type

```
git clone https://github.com/nilesh1391/pricing_module_assignment.git
```

or you can download using the url below

```
https://github.com/nilesh1391/pricing_module_assignment.git
```

#### Requirements

To install requirements type

```
pip install -r requirements.txt
```

`To use Github api put your credentials in settings.py`

```
GIT_CLIENT_ID = 'your github client id'
GIT_CLIENT_SECRET = 'your github client secret'
```

To migrate the database open terminal in project directory and type

```
python manage.py makemigrations
python manage.py migrate
```

To run the program in local server use the following command

```
python manage.py runserver
```

Server will be available at `http://127.0.0.1:8000` in your browser

Don't Forget to whitelist your host origin using `django-cors-header` when using in production<br>
[See Documentation](https://pypi.org/project/django-cors-headers/)

#### Author

<blockquote>
Nilesh Tiwari<br>
Email: nileshtiwari1391@gmail.com
</blockquote>
