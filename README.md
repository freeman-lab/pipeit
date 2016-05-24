# pipeit

> tiny package for making pipelines in python

This package makes it easy to build simple pipelines in Python. It assumes functions come in one of three flavors

|----------|-------------|
| `source` | takes options and returns data |
| `pipe` | takes data and options and returns data |
| `sink` | takes data and options and has side effects |

and you just string them together
```
source ----> pipe ----> pipe -----> sink
```

## install

Use `pip` to install, compatible with Python 2.7+ and 3.4+

```
pip install pipeit
```

## example

```python
from pipeit import Pipeline
pipeline = Pipeline()

@pipeline.source
def init():
  return 0

@pipeline.pipe
def add(data):
  return data + 1

@pipeline.pipe
def subtract(data):
  return data - 1

@pipeline.sink
def display(data):
  print data

pipeline.init().display()
>> 0
pipeline.init().add().display()
>> 1
pipeline.init().add().subtract().display()
>> 0
```

## usage

Create a new `pipeline` using the constructor.

```python
from pipeit import Pipeline
pipeline = Pipeline()
```

Then define functions for your pipeline using decorators provided by the `pipeline` object. You can either put `@pipeline.pipe` above your function definition, or use the methods directly as in `pipeline.pipe(func)`.

#### `source`

Define a source like this

```python
@pipeline.source
def init():
  return 0
```
A `source` can take any arguments, and must return `data` that will be the input to subsequent commands.

#### `pipe`

Define a pipe like this

```python
@pipeline.pipe
def add(data):
  return data + 1
```
The first argument of a `pipe` must be `data`, the other arguments can be anything, and a `pipe` must return something.

#### `sink`

Define a sink like this

```python
@pipeline.sink
def display(data):
  print data
```
The first argument of a `sink` must be `input`, the other arguments can be anything, and a `sink` can have side effects (like printing, or saving, or plotting) but shouldn't return anything.

Once constructed, you can use your `pipeline` by chaining methods

```python
pipeline.init().add().display()
```
