# " Matching engine | Search API"
light-weight service for sorting, ranking, and displaying a list of skilled service providers. 





# Stack
<ul>

<li>Django</li>
<li>Django Rest Framework </li>
<li>Sqlite </li>
<li>Virtualenv </li>
<li>Flake8</li>
<li>pytest</li>
<li>Makefile</li>

</ul>


 
 
## Installation
<p> Create VirtualEnv</p>

```bash
$ make init
```
 
 
<p>  Create virtual-env</p>

```bash
$ source env/bin/activate
```

<p>  Install depencies</p>

```bash
$  make install_devs
```

<p>  Django migration</p>

```bash
$  make django_migrations
```

<p>Plant the seed</p>

```bash
$ make plant_seed
```

<p>Init local server. http://127.0.0.1:8000/</p>

```bash
$ make run
```

####  API end-points:
<ul>
<li>/api/search</li>
</ul>


####  API Params:
<p>q: <b>Required</b> ex: "Mathematics" </p>
<p>include: <b>Optional</b> --> include only object matching  the given term </p>
<p>exclude: <b>Optional</b>  to exclude objects from response </p>
<p>is_active: <b>Optional</b> --> true | false</p>

### Sample response on Postman:

####  Params:
q: Mathematics
include: Gutmann LLC
![Alt text](/git_image/p3.png "test locally" )