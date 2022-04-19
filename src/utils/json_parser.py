import orjson


class ORJSONDecoder:

    def __init__(self, **kwargs):
        self.options = kwargs

    def decode(self, obj):
        return orjson.loads(obj)


class ORJSONEncoder:

    def __init__(self, **kwargs):
        self.options = kwargs

    def encode(self, obj):
        return orjson.dumps(obj)
