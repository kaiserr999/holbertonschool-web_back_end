#!/usr/bin/env python3
"""Module contenant une fonction de mesure de temps d'exécution.

Ce module définit une fonction qui mesure le temps total
nécessaire pour exécuter plusieurs coroutines en concurrence,
puis calcule la moyenne par coroutine.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Mesure le temps moyen d'exécution de wait_n par coroutine.

    Cette fonction lance wait_n(n, max_delay), mesure la durée totale
    d'exécution avec le module time, puis retourne cette durée
    divisée par n, c'est-à-dire le temps moyen par coroutine.

    Args:
        n: le nombre de coroutines à lancer.
        max_delay: la valeur maximale du délai pour chaque coroutine.

    Returns:
        Le temps moyen d'exécution par coroutine (float).
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
