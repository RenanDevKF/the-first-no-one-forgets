import pandas as pd
import random
import matplotlib.pyplot as plt

class LotoFacilAnalyzer:
    def __init__(self, file_path=None):
        """Inicializa o analisador da Lotofácil."""
        self.file_path = file_path
        self.data = None
        self.most_frequent = None
        self.least_frequent = None
        if file_path:
            self.load_data(file_path)
            
    def load_data(self, file_path):
        """Carrega os resultados anteriores da Lotofácil."""
        self.data = pd.read_csv(file_path)
        print("Dados carregados com sucesso!")
        
        # Atualizar as listas de números mais e menos frequentes após carregar os dados
        self.most_frequent = self.get_most_frequent_numbers()
        self.least_frequent = self.get_least_frequent_numbers()

    def get_most_frequent_numbers(self, top_n=15):
        """Retorna os números mais frequentes nos sorteios."""
        all_numbers = self.data.iloc[:, 1:].values.flatten()
        freq_series = pd.Series(all_numbers).value_counts()
        return freq_series.head(top_n)  # Retorna como uma Series com os números mais frequentes
    
    def get_least_frequent_numbers(self, bottom_n=10):
        """Retorna os números menos sorteados."""
        all_numbers = self.data.iloc[:, 1:].values.flatten()
        freq_series = pd.Series(all_numbers).value_counts()
        return freq_series.tail(bottom_n)  # Retorna como uma Series com os números menos frequentes
    
    def get_number_delay(self):
        """Calcula o atraso de cada número (quantos sorteios sem sair)."""
        last_occurrence = {}
        for index, row in self.data.iterrows():
            for number in range(1, 26):
                if number in row.values:
                    last_occurrence[number] = index
                    
        delays = {num: len(self.data) - last_occurrence.get(num, 0) for num in range(1, 26)}
        return pd.Series(delays).sort_values(ascending=False)
    
    def suggest_numbers(self):
        # Garantir que existam elementos suficientes
        if len(self.most_frequent) < 10 or len(self.least_frequent) < 5:
            print("Erro: listas de números mais/menos frequentes estão vazias ou têm poucos elementos.")
            return []

        suggested = random.sample(self.most_frequent.index.tolist(), min(10, len(self.most_frequent))) + \
                    random.sample(self.least_frequent.index.tolist(), min(5, len(self.least_frequent)))

        return sorted(suggested)
    
    def plot_frequencies(self):
        """Plota um gráfico das frequências dos números."""
        freq_series = self.get_most_frequent_numbers(25)
        freq_series.sort_index().plot(kind='bar', figsize=(10,5), color='blue')
        plt.xlabel('Números')
        plt.ylabel('Frequência')
        plt.title('Frequência dos Números na Lotofácil')
        plt.show()
        
    def find_full_coverage_draws(self):
        """Encontra quantos sorteios foram necessários para cobrir todos os 25 números, exibindo os números não sorteados em ciclos incompletos."""
        
        seen_numbers = set()  # Conjunto de números já sorteados
        draws_needed = 0  # Contador de sorteios processados
        cycles = []  # Lista para armazenar a quantidade de sorteios por ciclo
        all_numbers = set(range(1, 26))  # Conjunto com todos os números possíveis (1 a 25)
        
        for index, row in self.data.iterrows():
            seen_numbers.update(row[1:].values)  # Adiciona os números do sorteio atual
            draws_needed += 1  # Incrementa o contador
            
            if len(seen_numbers) == 25:  # Se todos os números já saíram, o ciclo se encerra
                print(f"Ciclo encerrado após {draws_needed} sorteios.")
                cycles.append(draws_needed)  # Salva a quantidade de sorteios para o ciclo
                seen_numbers.clear()  # Reinicia os números sorteados
                draws_needed = 0  # Reinicia o contador
                
        # Caso o loop termine e ainda faltem números a serem sorteados
        missing_numbers = all_numbers - seen_numbers
        if missing_numbers:
            print(f"Números que ainda não foram sorteados neste ciclo incompleto: {sorted(missing_numbers)}")

        return cycles  # Retorna a lista com o número de sorteios necessários para cada ciclo completo

# Exemplo de uso (necessário arquivo CSV com resultados)
analyzer = LotoFacilAnalyzer('resultados_lotofacil_corrigido.csv')
print(analyzer.suggest_numbers())
analyzer.plot_frequencies()
print(f"Quantidade de sorteios necessários para que todos os números fossem sorteados: {analyzer.find_full_coverage_draws()}")

