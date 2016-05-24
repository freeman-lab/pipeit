from pipeit import Pipeline

pipeline = Pipeline()

@pipeline.source
def init(path='', engine=None):
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
pipeline.init().add().display()
pipeline.init().add().subtract().display()