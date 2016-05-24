from pipeit import Pipeline

pipeline = Pipeline()

@pipeline.source
def init(path='', engine=None):
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
pipeline.init().add().display()
pipeline.init().add().subtract().display()