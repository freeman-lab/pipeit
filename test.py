from pipeit import Pipeline

def test_constructor():
    pipeline = Pipeline()

def test_source():
    pipeline = Pipeline()

    @pipeline.source
    def f():
        return 0

    assert pipeline.f().data == 0

def test_pipe():
    pipeline = Pipeline()

    @pipeline.source
    def f():
        return 0

    @pipeline.pipe
    def g(data):
        return data + 1

    assert pipeline.f().g().data == 1

def test_sink():
    pipeline = Pipeline()

    @pipeline.source
    def f():
        return 0

    @pipeline.sink
    def g(data):
        return data

    assert pipeline.f().g() == 0

def test_all():
    pipeline = Pipeline()

    @pipeline.source
    def f():
        return 0

    @pipeline.pipe
    def g(data):
        return data + 1

    @pipeline.sink
    def h(data):
        return data

    assert pipeline.f().h() == 0
    assert pipeline.f().g().h() == 1
    assert pipeline.f().g().g().h() == 2