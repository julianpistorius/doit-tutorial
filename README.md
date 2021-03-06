# Playing with `doit`

See the [doit tutorial](https://pydoit.org/tutorial_1.html)

Note: This code is for the instructions up to the 
[section on 'clean'](https://pydoit.org/tutorial_1.html#clean).

- [ ] Complete the rest of the tutorial

## To use this code

1. Install [pipenv](https://pipenv.readthedocs.io/) (if you don't already have it):

```bash
brew install pipenv
```

2. Install `graphviz`:

```bash
brew install graphviz
```

3. Install the dependencies by running the following in the same directory as 
the `Pipfile` file:

```bash
pipenv install
```

4. Activate the virtual environment:

```bash
pipenv shell
``` 

5. Run the `doit` workflow:

```bash
doit
```

You should see something like:

```
$ doit
.  imports
.  dot
.  draw
```

6. Check that the files were created:

```bash
ls -l requests*
```

You should see something like:

```
$ ls -l requests*
-rw-r--r--  1 johndoe  staff    164 Mar  4 10:28 requests.models.deps
-rw-r--r--  1 johndoe  staff    404 Mar  4 10:28 requests.models.dot
-rw-r--r--  1 johndoe  staff  37154 Mar  4 10:28 requests.models.png
``` 

7. Check that the `requests.models.png` looks like the one in the tutorial.


## Exercises for the reader

- [ ] Add a task which creates the `projects` directory
- [ ] Add a task which clones the requests repository into the `projects` 
directory