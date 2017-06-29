# Deploy EC2

## requirements

**Python**
3.6.1

**pip**

```
$ pip install requiremnets.txt
```

## Create secret config files

### Project structure

```
project_folder/
	.conf_secret/
		settings_common.json
		settings_debug.json
		settings_deploy.json
	.django_app/
	...
	...
```
	
### settings_common.json example

```python
{
  "django": {
    "secret_key": "Django project secret key"
  }
}
```

### settings_debug.json example

```python
{
  "django": {
    "allowed_hosts": [
      "*"
    ]
  }
}
```

### settings_deploy.json example

```python
{
  "django": {
    "allowed_hosts": [
      "*"
    ]
  }
}
```

### runserver

```
# local developement
$ python3 manage.py runserver --settings=config.settings.debug
```
