name = "rezutil"
version = "1.3.3"
requires = ["python-2.7+,<4"]
build_command = "python {root}/install.py"


def commands():
    global env
    env["PYTHONPATH"].prepend("{root}/python")
