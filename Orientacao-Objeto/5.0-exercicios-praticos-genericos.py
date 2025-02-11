"""
Exercícios de Classes e Métodos Genéricos em Python
 Criando uma Lista Genérica
Crie uma classe ListaGenerica que pode armazenar uma lista de qualquer tipo de dado. Implemente os seguintes métodos:

adicionar(item: T): Adiciona um item à lista.
remover() -> T: Remove e retorna o último item da lista.
mostrar_lista(): Exibe todos os itens da lista.
💡 Teste armazenando números, strings e objetos personalizados.

 Criando uma Fila Genérica
Implemente uma classe FilaGenerica<T> que representa uma fila (FIFO - First In, First Out). Deve conter os métodos:

enfileirar(item: T): Adiciona um item ao final da fila.
desenfileirar() -> T: Remove e retorna o primeiro item da fila.
tamanho() -> int: Retorna o número de itens na fila.
💡 Teste com diferentes tipos de dados.

 Criando um Dicionário Genérico
Crie uma classe DicionarioGenerico<K, V> que funciona como um dicionário genérico. Ela deve ter:

adicionar(chave: K, valor: V): Adiciona um par chave-valor ao dicionário.
remover(chave: K) -> V: Remove e retorna o valor associado à chave.
obter(chave: K) -> V: Retorna o valor associado à chave.
mostrar_dicionario(): Exibe todos os pares chave-valor.
💡 Teste armazenando diferentes combinações de tipos.



"""