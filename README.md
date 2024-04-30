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
[x] html templates created<br/>
[x] setting bootstrap<br/>
[x] created custom errors and rendering<br/>
[x] created form for creation users

### what need do:
[_] create and connect "static files"<br/>
[_] create and connect database<br/>
[_] use SQLAlchemy<br/>
[_] set up migrations for database<br/>
[_] create hashing passwords<br/>
[_] create post model and form<br/>
[_] create a user dashbord<br/>
[_] create basig admin page<br/>
[_] deploy app