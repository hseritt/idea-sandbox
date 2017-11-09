
Install pyenv. You can get it from Github:

```
$ curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash
```

Next, add the following code to the end of your /home//.bashrc file (or to .bash_profile if you're on a Redhat style system):

```bash
export PATH="/home/hseritt/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Source your .bashrc (or .bash_profile if you're using a RedHat style system) file so that pyenv and helper executables will now be in your path:

```
$ . .bashrc 
```

Install the latest version of Python:

```
$ pyenv install 3.6.3
```

Go to a directory that houses your apps/development work:

```
$ cd projects
$ mkdir django-blog
$ cd django-blog
$ pyenv global 3.6.3
$ pyenv virtualenv django-blog
$ pyenv local django-blog
$ source activate django-blog
$ wget https://github.com/hseritt/django-blog/archive/master.zip
$ unzip master.zip
$ mv django-blog-master/* .
$ rm -rf django-blog-master/ master.zip
$ pip install -r requirements.txt
$ cd blog
$ ./manage.py makemigrations
```

If you have not set up a Postgresql database server, you will see an error similar to this:

```
django.db.utils.OperationalError: could not connect to server: Connection refused
	Is the server running on host "127.0.0.1" and accepting
	TCP/IP connections on port 5432?

```

You can set up a Postgresql database for this app or you like, you can use sqlite3 while you get this up and running. Make this change inside blog/settings.py:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'blog.db',
    }
}
```

```
$ ./manage.py migrate
$ ./manage.py createsuperuser
```

Now, you can start the server with:

```
$ ./runserver.sh
```

If you're trying to access it from a remote machine, you will see an error similar to this when you open http://<remote_ip>:8000 :

```
DisallowedHost at /
Invalid HTTP_HOST header: '192.168.15.34:8000'. You may need to add '192.168.15.34' to ALLOWED_HOSTS.
Request Method:	GET
Request URL:	http://192.168.15.34:8000/
Django Version:	1.11.5
Exception Type:	DisallowedHost
Exception Value:	
Invalid HTTP_HOST header: '192.168.15.34:8000'. You may need to add '192.168.15.34' to ALLOWED_HOSTS.
```

If so, then open your blog/settings.py file change ALLOWED_HOSTS to be:

```python
ALLOWED_HOSTS = ['192.168.15.34',]
```

_Of course, your ip address will likely be different._

