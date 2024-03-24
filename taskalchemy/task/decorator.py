from typing import Callable, TypeVar, ParamSpec

TaskReturnValue = TypeVar('TaskReturnValue')
TaskParams = ParamSpec('TaskParams')

class FullyDefinedTaskDefinition:
    def __init__(self)



class BackgroundTaskContainer:
    def __init__(self, f: Callable[TaskParams, TaskReturnValue]):
        self.f = f

    def __call__(self, *args: TaskParams.args, **kwargs: TaskParams.kwargs) -> TaskReturnValue:
        print("Calling BackgroundTaskContainer")
        return self.f(*args, **kwargs)


def task(f: Callable[TaskParams, TaskReturnValue]) -> BackgroundTaskContainer:

    return BackgroundTaskContainer(f)


@task
def test_task():
    print("Ola Mundo")


test_task()