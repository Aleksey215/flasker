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
- [x] html templates created<br/>
- [x] setting bootstrap<br/>
- [x] created custom errors and rendering<br/>
- [x] created form for creation users<br/>
- [x] settings management with pydantic<br/>
- [x] add flashed messages

### what need do:
- [ ] create and connect "static files"<br/>
- [ ] create and connect database<br/>
- [ ] use SQLAlchemy<br/>
- [ ] set up migrations for database<br/>
- [ ] create hashing passwords<br/>
- [ ] create post model and form<br/>
- [ ] create a user dashbord<br/>
- [ ] create basig admin page<br/>
- [ ] deploy app