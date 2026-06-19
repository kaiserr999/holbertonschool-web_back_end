#!/usr/bin/env python3
"""Module contenant une fonction de création de tâche asynchrone.

Ce module définit une fonction qui encapsule wait_random dans
un objet asyncio.Task, permettant de planifier son exécution
sans être elle-même une coroutine.
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Crée une tâche asyncio à partir de wait_random.

    Cette fonction régulière (non asynchrone) génère et retourne
    un objet asyncio.Task qui exécutera wait_random avec le délai
    maximal donné en argument.

    Args:
        max_delay: la valeur maximale du délai pour wait_random.

    Returns:
        Un objet asyncio.Task encapsulant la coroutine wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
