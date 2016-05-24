# pipeit

> tiny package for making pipelines in python

This package makes it easy to build simple pipelines in Python. It assumes functions come in one of three flavors
- a `source` takes options and return data
- a `pipe` takes data and options and returns data
- a `sink` takes data and options and has side effects

and you just string them together
```
source ----> pipe ----> pipe -----> sink
```

## install

Use `pip` to install, compatible with Python 2.7+ and 3.4+

```
pip install pipeit
```

### example

```python
from pipeit import Pipeline
pipeline = Pipeline()

@pipeline.source
def init():
  return 0

@pipeline.pipe
def add(input):
  return input + 1

@pipeline.pipe
def subtract(input):
  return input - 1

@pipeline.sink
def display(input):
  print input

pipeline.init().display()
>> 0
pipeline.init().add().display()
>> 1
pipeline.init().add().subtract().display()
>> 0
```

### usage

Create a new `pipeline` using the constructor.

```python
from pipeit import Pipeline
pipeline = Pipeline()
```

Then define functions for your pipeline using decorators provided by the `pipeline` object, putting `@pipeline.pipe` above your function definition. You can also use the decorator methods directly as in `pipeline.pipe(func)`.

#### `source`

Define a source like this

```python
@pipeline.source
def myfunc(option=None):
  return data
```
A `source` can take any arguments, and must return something that will be the input to subsequent commands.

#### `pipe`

Define a pipe like this

```python
@pipeline.pipe
def myfunc(input, option=None):
  return input
```
The first argument of a `pipe` must be `input`, the other arguments can be anything, and a `pipe` must return something.

#### `sink`

Define a sink like this

```python
@pipeline.sink
def myfunc(input, argument=None):
  print input
```
The first argument of a `sink` must be `input`, the other arguments can be anything, and a `sink` can have side effects (like printing, or saving, or plotting) but shouldn't return anything.
