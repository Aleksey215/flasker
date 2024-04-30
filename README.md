# flasker
Educational project

### Start project
``` console
flask run
```

Debug:
``` console
flask run --debug
```

### HTML templates
<b>base.html</b> - main template(in this file setting up for app front end (bootstrap))<br/>
<b>index.html</b> - application main page<br/>
<b>navbar.html</b> - navigation on app in header<br/>
<b>user.html</b> - user profile page<br/>
<b>name.html</b> - page with form for creation user

<b>404.html</b> - custom page for error 404
<b>500.html</b> - custom page for error 500

### what was done:
[x] html templates created
[x] setting bootstrap
[x] created custom errors and rendering
[x] created form for creation users

### what need do:
[_] create and connect "static files"
[_] create and connect database
[_] use SQLAlchemy
[_] set up migrations for database
[_] create hashing passwords
[_] create post model and form
[_] create a user dashbord
[_] create basig admin page
[_] deploy app