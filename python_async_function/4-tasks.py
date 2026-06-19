
#!/usr/bin/env python3
"""Module contenant une coroutine pour exécuter plusieurs tâches.

Ce module définit une fonction qui lance plusieurs instances de
task_wait_random en concurrence et collecte leurs résultats au
fur et à mesure qu'ils se terminent.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Lance n tâches task_wait_random en concurrence et les ordonne.

    Cette coroutine crée n tâches via task_wait_random avec le délai
    maximal max_delay, les exécute en parallèle, et retourne la liste
    des délais obtenus, triée par ordre croissant, en se basant sur
    leur ordre d'achèvement plutôt que sur un tri explicite.

    Args:
        n: le nombre de tâches à lancer.
        max_delay: la valeur maximale du délai pour chaque tâche.

    Returns:
        La liste des délais (float) en ordre croissant.
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
