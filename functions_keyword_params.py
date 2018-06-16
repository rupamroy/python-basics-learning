def var_args(name, **kwargs):
    print(name)
    print(kwargs["description"])

var_args("Rupam", description="Loves python", feedback=None, pluralsight_subscriber=True)