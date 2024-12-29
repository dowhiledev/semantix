"""Types for the Agentic Loop."""

from typing import Callable, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from semantix.llms import BaseLLM
    from semantix.types.prompt import Tool


class Agent:
    """Agent in a multi-agent system."""

    def __init__(
        self,
        llm: "BaseLLM",
        role: str,
        goal: str,
        backstory: Optional[str],
        tools: List["Tool"],
    ) -> None:
        """Initialize the agent."""
        self.llm = llm
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.tools = tools

    def task(self, func: Callable) -> "Task":
        """Create a task for the agent."""
        task_args = func.__annotations__
        task_return = task_args.pop("return", None)
        task_description = func.__doc__ or ""
        return Task(self, func.__name__, task_args, task_return, task_description)


class Task:
    """Task for an agent."""

    def __init__(
        self,
        agent: "Agent",
        task_name: str,
        task_args: dict,
        task_return: type,
        task_description: str,
    ) -> None:
        """Initialize the task."""
        self.agent = agent
        self.__name__ = task_name
        self.task = task_name.replace("_", " ").title()
        self.task_args = task_args
        self.task_return = task_return
        self.task_description = task_description

    def __call__(self, **kwargs: dict) -> None:
        """Call the task."""
        # TODO: Implement the task execution
        print(
            f"""
            {self.agent.role} - {self.agent.goal}
            {self.agent.backstory}
            {self.task} - {self.task_description}
            Args: {kwargs}
            """
        )


class Manager:
    """Manager for the agents."""

    def __init__(
        self, llm: "BaseLLM", tasks: list[Task], goal: Optional[str], annotations: dict
    ) -> None:
        """Initialize the manager with the tasks, goal, and annotations."""
        self.llm = llm
        self.tasks = tasks
        self.goal = goal
        self.inputs = annotations
        self.final_output_type = self.inputs.pop("return", None)

    def __call__(self, *args: tuple, **kwargs: dict) -> None:
        """Call the manager."""
        resolved_kwargs = self.resolve_args_kwargs(args, kwargs)
        print(resolved_kwargs)
        # TODO: Implement the Agentic Loop
        plan: dict[str, dict] = {
            "do_something": {"a": 1},
            "do_something_different": {"a": "two", "b": 2},
            "do_something_else": {"a": 3.0},
        }
        for _task, _args in plan.items():
            task = next(task for task in self.tasks if task.__name__ == _task)
            task(**_args)

    def resolve_args_kwargs(self, args: tuple, kwargs: dict) -> dict:
        """Resolve the arguments and keyword arguments."""
        mapped_args = dict(zip(self.inputs.keys(), args))
        new_args = {**mapped_args, **kwargs}
        self.validate(new_args)
        return new_args

    def validate(self, kwargs: dict) -> None:
        """Validate the arguments."""
        error_msg = []
        missing_keys = [k for k in self.inputs.keys() if k not in kwargs]
        if missing_keys:
            error_msg.append(f"Missing arguments: {missing_keys}")
        unnecessary_keys = [k for k in kwargs.keys() if k not in self.inputs]
        if unnecessary_keys:
            error_msg.append(f"Invalid arguments: {unnecessary_keys}")

        for key, value in kwargs.items():
            expected_type = self.inputs.get(key)
            if expected_type:
                origin = getattr(expected_type, "__origin__", None)
                if origin:
                    if not isinstance(value, origin):
                        error_msg.append(
                            f"Incorrect type for argument '{key}': expected {expected_type}, got {type(value)}"
                        )
                elif not isinstance(value, expected_type):
                    error_msg.append(
                        f"Incorrect type for argument '{key}': expected {expected_type}, got {type(value)}"
                    )

        if error_msg:
            raise ValueError(" and ".join(error_msg))
