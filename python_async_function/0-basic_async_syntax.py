#!/usr/bin/env python3
"""Module contenant une coroutine asynchrone simple.

Ce module définit une fonction qui illustre l'utilisation de base
de la programmation asynchrone en Python avec async/await.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Attend un délai aléatoire avant de le retourner.

    Cette coroutine attend de manière asynchrone pendant une durée
    aléatoire comprise entre 0 et max_delay (inclus), puis retourne
    cette durée sous forme de nombre flottant.

    Args:
        max_delay: la valeur maximale du délai (10 par défaut).

    Returns:
        Le délai (float) effectivement attendu.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
