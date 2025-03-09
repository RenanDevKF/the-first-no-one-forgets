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
        
    def get_most_frequent_numbers(self, top_n=15):
        """Retorna os números mais frequentes nos sorteios."""
        all_numbers = self.data.iloc[:, 1:].values.flatten()
        freq_series = pd.Series(all_numbers).value_counts()
        return freq_series.head(top_n)