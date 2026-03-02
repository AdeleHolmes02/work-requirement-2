def add_task(task_list: list[str], task: str) -> bool:
    cleaned = task.strip()
    if not cleaned:
        return False
    task_list.append(cleaned)
    return True


def remove_task(task_list: list[str], task: str) -> bool:
    cleaned = task.strip()
    if cleaned in task_list:
        task_list.remove(cleaned)
        return True
    return False