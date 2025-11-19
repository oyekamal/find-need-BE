import os

local = os.environ.get("LOCAL", "True")


if local == "False":
    print("local settings...!")
    from .local_settings import *
else:
    print("docker settings...!")
    from .docker_settings import *
