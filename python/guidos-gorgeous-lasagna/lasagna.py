""" Definição de constantes e funções. """
EXPECTED_BAKE_TIME = 40  # Tempo esperado de cozimento em minutos
PREPARATION_TIME = 2  # Tempo de preparo por camada em minutos

def bake_time_remaining(elapsed_bake_time: int) -> int:
    """
    Calcula o tempo restante de cozimento da lasanha.

    Args:
        elapsed_bake_time (int): Tempo que a lasanha já passou no forno.

    Returns:
        int: Minutos restantes para completar o cozimento.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers: int) -> int:
    """
    Calcula o tempo de preparo da lasanha com base no número de camadas.

    Args:
        number_of_layers (int): Número de camadas da lasanha.

    Returns:
        int: Tempo total de preparo em minutos.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """
    Calcula o tempo total gasto até agora (preparo + forno).

    Args:
        number_of_layers (int): Número de camadas preparadas.
        elapsed_bake_time (int): Tempo já passado no forno.

    Returns:
        int: Tempo total decorrido em minutos.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time