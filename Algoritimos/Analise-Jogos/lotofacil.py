import pandas as pd
import random
import matplotlib.pyplot as plt

class LotoFacilAnalyzer:
    def __init__(self, file_path=None):
        """Inicializa o analisador da Lotofácil."""
        self.file_path = file_path
        self.data = None
        if file_path:
            self.load_data(file_path)
            
    def load_data(self, file_path):
        """Carrega os resultados anteriores da Lotofácil."""
        self.data = pd.read_csv(file_path)
        print("Dados carregados com sucesso!")