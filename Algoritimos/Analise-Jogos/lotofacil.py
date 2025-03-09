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
    
    def get_least_frequent_numbers(self, bottom_n=10):
        """Retorna os números menos sorteados."""
        all_numbers = self.data.iloc[:, 1:].values.flatten()
        freq_series = pd.Series(all_numbers).value_counts()
        return freq_series.tail(bottom_n)
    
    def get_number_delay(self):
        """Calcula o atraso de cada número (quantos sorteios sem sair)."""
        last_occurrence = {}
        for index, row in self.data.iterrows():
            for number in range(1, 26):
                if number in row.values:
                    last_occurrence[number] = index
                    
        delays = {num: len(self.data) - last_occurrence.get(num, 0) for num in range(1, 26)}
        return pd.Series(delays).sort_values(ascending=False)