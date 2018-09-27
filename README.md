# Python 3 environment with requirements.txt

A Binder-compatible repo with a `requirements.txt` file.

## Notes
The `requirements.txt` file should list all Python libraries that your notebooks
depend on, and they will be installed using:

```
pip install -r requirements.txt
```

The base Binder image contains no extra dependencies, so be as
explicit as possible in defining the packages that you need. This includes
specifying explict versions wherever possible.

In this example we include the library `seaborn`, and our notebook uses it
to plot a figure. 
