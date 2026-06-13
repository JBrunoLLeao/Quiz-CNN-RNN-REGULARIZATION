QUESTIONS = [

# ==========================================================
# CNN (18)
# ==========================================================

{
    "topic": "CNN",
    "question": "Qual é a principal vantagem das camadas convolucionais em relação às camadas totalmente conectadas para imagens?",
    "options": [
        "Eliminam completamente o overfitting",
        "Compartilham pesos e capturam padrões locais",
        "Dispensam funções de ativação",
        "Reduzem o número de classes"
    ],
    "answer": "Compartilham pesos e capturam padrões locais",
    "explanation": "CNNs exploram padrões locais e compartilham pesos, reduzindo o número de parâmetros."
},

{
    "topic": "CNN",
    "question": "Qual é a função principal de um filtro convolucional?",
    "options": [
        "Aumentar o tamanho da imagem",
        "Detectar características específicas",
        "Reduzir o número de canais",
        "Substituir pooling"
    ],
    "answer": "Detectar características específicas",
    "explanation": "Filtros aprendem padrões como bordas, texturas e formas."
},

{
    "topic": "CNN",
    "question": "O que o Max Pooling faz?",
    "options": [
        "Aumenta a resolução",
        "Reduz dimensões preservando características relevantes",
        "Cria novos filtros",
        "Remove canais"
    ],
    "answer": "Reduz dimensões preservando características relevantes",
    "explanation": "Max Pooling reduz a dimensão espacial mantendo informações importantes."
},

{
    "topic": "CNN",
    "question": "Em Conv2D(32, (3,3)), o número 32 representa:",
    "options": [
        "Quantidade de filtros",
        "Tamanho da imagem",
        "Stride",
        "Número de classes"
    ],
    "answer": "Quantidade de filtros",
    "explanation": "A camada aprende 32 filtros distintos."
},

{
    "topic": "CNN",
    "question": "Qual função de ativação é mais utilizada em CNNs modernas?",
    "options": [
        "Sigmoid",
        "Tanh",
        "ReLU",
        "Softmax"
    ],
    "answer": "ReLU",
    "explanation": "ReLU reduz problemas de gradiente e acelera o treinamento."
},

{
    "topic": "CNN",
    "question": "Qual é o objetivo do Data Augmentation?",
    "options": [
        "Reduzir o dataset",
        "Aumentar artificialmente a diversidade dos dados",
        "Eliminar overfitting completamente",
        "Substituir validação"
    ],
    "answer": "Aumentar artificialmente a diversidade dos dados",
    "explanation": "Transformações aumentam a variedade de exemplos vistos pela rede."
},

{
    "topic": "CNN",
    "question": "Qual das opções é um exemplo de Data Augmentation?",
    "options": [
        "Rotação de imagens",
        "Cross Entropy",
        "Dropout",
        "Batch Size"
    ],
    "answer": "Rotação de imagens",
    "explanation": "Rotações ajudam a gerar novas versões das imagens."
},

{
    "topic": "CNN",
    "question": "Qual camada geralmente aparece ao final de uma CNN para classificação?",
    "options": [
        "Conv2D",
        "Pooling",
        "Dense",
        "Flatten"
    ],
    "answer": "Dense",
    "explanation": "A camada Dense produz as probabilidades finais."
},

{
    "topic": "CNN",
    "question": "Qual a função da camada Flatten?",
    "options": [
        "Criar filtros",
        "Transformar mapas de características em vetor",
        "Aplicar convolução",
        "Reduzir ruído"
    ],
    "answer": "Transformar mapas de características em vetor",
    "explanation": "Flatten converte a saída 2D/3D em vetor para as camadas densas."
},

{
    "topic": "CNN",
    "question": "Por que CNNs possuem menos parâmetros que redes totalmente conectadas equivalentes?",
    "options": [
        "Não possuem pesos",
        "Compartilham pesos",
        "Não usam gradiente",
        "Usam apenas uma camada"
    ],
    "answer": "Compartilham pesos",
    "explanation": "O compartilhamento de pesos reduz drasticamente os parâmetros."
},

{
    "topic": "CNN",
    "question": "O que acontece quando aumentamos o número de filtros?",
    "options": [
        "A rede pode aprender mais características",
        "A imagem aumenta",
        "A rede deixa de aprender",
        "O dataset cresce"
    ],
    "answer": "A rede pode aprender mais características",
    "explanation": "Mais filtros permitem capturar padrões mais diversos."
},

{
    "topic": "CNN",
    "question": "O parâmetro rescale=1./255 serve para:",
    "options": [
        "Aumentar resolução",
        "Normalizar pixels",
        "Adicionar filtros",
        "Remover ruído"
    ],
    "answer": "Normalizar pixels",
    "explanation": "Os valores são convertidos para o intervalo [0,1]."
},

{
    "topic": "CNN",
    "question": "Qual função de perda é normalmente usada em classificação binária?",
    "options": [
        "MAE",
        "MSE",
        "Binary Crossentropy",
        "Huber"
    ],
    "answer": "Binary Crossentropy",
    "explanation": "É a função mais comum para classificação binária."
},

{
    "topic": "CNN",
    "question": "Qual camada ajuda a reduzir overfitting durante o treinamento?",
    "options": [
        "Dropout",
        "Flatten",
        "Pooling",
        "Input"
    ],
    "answer": "Dropout",
    "explanation": "Dropout desativa neurônios aleatoriamente."
},

{
    "topic": "CNN",
    "question": "Qual é a saída típica de uma camada Softmax?",
    "options": [
        "Valores negativos",
        "Probabilidades que somam 1",
        "Apenas zeros",
        "Mapas convolucionais"
    ],
    "answer": "Probabilidades que somam 1",
    "explanation": "Softmax converte logits em distribuição de probabilidades."
},

{
    "topic": "CNN",
    "question": "Qual é a principal aplicação das CNNs?",
    "options": [
        "Processamento de imagens",
        "Banco de dados",
        "Compiladores",
        "Redes sociais"
    ],
    "answer": "Processamento de imagens",
    "explanation": "CNNs foram desenvolvidas principalmente para visão computacional."
},

{
    "topic": "CNN",
    "question": "O que significa treinamento supervisionado?",
    "options": [
        "Dados possuem rótulos",
        "Dados sem rótulos",
        "Sem função de perda",
        "Sem validação"
    ],
    "answer": "Dados possuem rótulos",
    "explanation": "Cada exemplo possui uma resposta esperada."
},

{
    "topic": "CNN",
    "question": "Uma CNN que apresenta excelente desempenho no treino e ruim no teste provavelmente sofre de:",
    "options": [
        "Underfitting",
        "Overfitting",
        "Normalização",
        "Pooling"
    ],
    "answer": "Overfitting",
    "explanation": "O modelo memorizou o treino e não generaliza bem."
},

# ==========================================================
# REGULARIZATION (14)
# ==========================================================

{
    "topic": "Regularization",
    "question": "O que significa generalização?",
    "options": [
        "Memorizar treino",
        "Desempenhar bem em dados não vistos",
        "Reduzir parâmetros",
        "Aumentar épocas"
    ],
    "answer": "Desempenhar bem em dados não vistos",
    "explanation": "Generalização mede a capacidade de funcionar em novos dados."
},

{
    "topic": "Regularization",
    "question": "Quando ocorre overfitting?",
    "options": [
        "Treino ruim e teste ruim",
        "Treino muito bom e teste ruim",
        "Treino e teste excelentes",
        "Treino interrompido cedo"
    ],
    "answer": "Treino muito bom e teste ruim",
    "explanation": "O modelo memoriza padrões específicos do treino."
},

{
    "topic": "Regularization",
    "question": "Qual técnica reduz overfitting removendo neurônios aleatoriamente?",
    "options": [
        "Pooling",
        "Dropout",
        "Softmax",
        "Flatten"
    ],
    "answer": "Dropout",
    "explanation": "Dropout força a rede a aprender representações mais robustas."
},

{
    "topic": "Regularization",
    "question": "Qual é uma solução comum para reduzir overfitting?",
    "options": [
        "Mais dados",
        "Mais ruído na saída",
        "Menos validação",
        "Remover função de perda"
    ],
    "answer": "Mais dados",
    "explanation": "Mais exemplos ajudam a melhorar a generalização."
},

{
    "topic": "Regularization",
    "question": "Modelos muito complexos tendem a apresentar:",
    "options": [
        "Alto bias",
        "Alta variância",
        "Baixo ruído",
        "Sem erro"
    ],
    "answer": "Alta variância",
    "explanation": "Modelos complexos são mais suscetíveis ao overfitting."
},

{
    "topic": "Regularization",
    "question": "Qual técnica interrompe o treinamento antes do overfitting?",
    "options": [
        "Early Stopping",
        "Pooling",
        "Flatten",
        "Softmax"
    ],
    "answer": "Early Stopping",
    "explanation": "O treinamento para quando a validação deixa de melhorar."
},

{
    "topic": "Regularization",
    "question": "Qual é o objetivo da regularização L2?",
    "options": [
        "Penalizar pesos muito grandes",
        "Aumentar filtros",
        "Criar neurônios",
        "Remover rótulos"
    ],
    "answer": "Penalizar pesos muito grandes",
    "explanation": "L2 adiciona uma penalização baseada no tamanho dos pesos."
},

{
    "topic": "Regularization",
    "question": "Qual é o objetivo da regularização?",
    "options": [
        "Melhorar generalização",
        "Aumentar memória",
        "Criar dados",
        "Eliminar treinamento"
    ],
    "answer": "Melhorar generalização",
    "explanation": "Regularização reduz o risco de overfitting."
},

{
    "topic": "Regularization",
    "question": "Bias elevado normalmente está associado a:",
    "options": [
        "Underfitting",
        "Overfitting",
        "Data Augmentation",
        "Dropout"
    ],
    "answer": "Underfitting",
    "explanation": "Modelos simples demais apresentam alto bias."
},

{
    "topic": "Regularization",
    "question": "Variância elevada normalmente está associada a:",
    "options": [
        "Generalização perfeita",
        "Overfitting",
        "Poucos parâmetros",
        "Normalização"
    ],
    "answer": "Overfitting",
    "explanation": "Alta variância indica sensibilidade excessiva aos dados."
},

{
    "topic": "Regularization",
    "question": "Qual conjunto de dados é usado para monitorar generalização durante o treinamento?",
    "options": [
        "Treino",
        "Validação",
        "Teste final",
        "Backup"
    ],
    "answer": "Validação",
    "explanation": "O conjunto de validação acompanha o desempenho durante o treino."
},

{
    "topic": "Regularization",
    "question": "Uma diferença pequena entre treino e teste geralmente indica:",
    "options": [
        "Boa generalização",
        "Overfitting severo",
        "Erro de implementação",
        "Dados duplicados"
    ],
    "answer": "Boa generalização",
    "explanation": "Resultados semelhantes sugerem comportamento consistente."
},

{
    "topic": "Regularization",
    "question": "Qual técnica aumenta artificialmente a diversidade dos dados?",
    "options": [
        "Data Augmentation",
        "Softmax",
        "Flatten",
        "Dense"
    ],
    "answer": "Data Augmentation",
    "explanation": "Transformações geram exemplos adicionais."
},

{
    "topic": "Regularization",
    "question": "O erro total pode ser visto como combinação de:",
    "options": [
        "Bias, variância e ruído",
        "Pooling e convolução",
        "Softmax e Dense",
        "Treino e teste"
    ],
    "answer": "Bias, variância e ruído",
    "explanation": "Essa decomposição é fundamental para entender generalização."
},

# ==========================================================
# RNN (18)
# ==========================================================

{
    "topic": "RNN",
    "question": "Qual característica diferencia RNNs de redes feedforward tradicionais?",
    "options": [
        "Possuem memória de estados anteriores",
        "Usam apenas convoluções",
        "Não usam gradientes",
        "Não possuem pesos"
    ],
    "answer": "Possuem memória de estados anteriores",
    "explanation": "RNNs mantêm um estado oculto ao longo da sequência."
},

{
    "topic": "RNN",
    "question": "Qual tipo de dado é mais adequado para RNNs?",
    "options": [
        "Sequências temporais",
        "Planilhas",
        "Arquivos ZIP",
        "Imagens isoladas"
    ],
    "answer": "Sequências temporais",
    "explanation": "RNNs foram projetadas para dados sequenciais."
},

{
    "topic": "RNN",
    "question": "Qual aplicação é típica de RNNs?",
    "options": [
        "Análise de sentimentos",
        "Compressão ZIP",
        "SQL",
        "Firewall"
    ],
    "answer": "Análise de sentimentos",
    "explanation": "O contexto textual é importante em NLP."
},

{
    "topic": "RNN",
    "question": "O estado oculto de uma RNN representa:",
    "options": [
        "Informações acumuladas da sequência",
        "Somente a entrada atual",
        "A saída final",
        "O tamanho do dataset"
    ],
    "answer": "Informações acumuladas da sequência",
    "explanation": "Ele funciona como uma memória da sequência."
},

{
    "topic": "RNN",
    "question": "Por que RNNs são úteis para texto?",
    "options": [
        "Capturam dependências entre palavras",
        "Eliminam treinamento",
        "Substituem embeddings",
        "Não usam pesos"
    ],
    "answer": "Capturam dependências entre palavras",
    "explanation": "Palavras anteriores influenciam o significado das seguintes."
},

{
    "topic": "RNN",
    "question": "Qual problema clássico afeta RNNs profundas?",
    "options": [
        "Gradientes desaparecendo",
        "Excesso de filtros",
        "Falta de convolução",
        "Ausência de rótulos"
    ],
    "answer": "Gradientes desaparecendo",
    "explanation": "Dependências longas podem ser difíceis de aprender."
},

{
    "topic": "RNN",
    "question": "Qual arquitetura foi criada para reduzir o problema de gradientes desaparecendo?",
    "options": [
        "LSTM",
        "Perceptron",
        "Regressão Linear",
        "KNN"
    ],
    "answer": "LSTM",
    "explanation": "LSTMs utilizam mecanismos de memória mais eficientes."
},

{
    "topic": "RNN",
    "question": "O que significa a sigla LSTM?",
    "options": [
        "Long Short-Term Memory",
        "Linear State Transfer Model",
        "Learning State Machine",
        "Long Sequence Transfer Method"
    ],
    "answer": "Long Short-Term Memory",
    "explanation": "É a arquitetura recorrente mais conhecida."
},

{
    "topic": "RNN",
    "question": "Qual vantagem principal das LSTMs?",
    "options": [
        "Capturar dependências de longo prazo",
        "Eliminar pesos",
        "Reduzir classes",
        "Substituir validação"
    ],
    "answer": "Capturar dependências de longo prazo",
    "explanation": "As portas ajudam a preservar informações relevantes."
},

{
    "topic": "RNN",
    "question": "Qual tarefa pode ser resolvida com RNNs?",
    "options": [
        "Previsão de séries temporais",
        "Instalação de software",
        "Criação de banco de dados",
        "Compilação"
    ],
    "answer": "Previsão de séries temporais",
    "explanation": "O histórico influencia valores futuros."
},

{
    "topic": "RNN",
    "question": "Em NLP, a ordem das palavras é importante porque:",
    "options": [
        "Afeta o significado da frase",
        "Reduz memória",
        "Aumenta pixels",
        "Remove contexto"
    ],
    "answer": "Afeta o significado da frase",
    "explanation": "A sequência altera a interpretação do texto."
},

{
    "topic": "RNN",
    "question": "Qual componente armazena informação passada em uma RNN?",
    "options": [
        "Estado oculto",
        "Softmax",
        "Pooling",
        "Filtro"
    ],
    "answer": "Estado oculto",
    "explanation": "Ele transporta contexto ao longo do tempo."
},

{
    "topic": "RNN",
    "question": "Uma RNN pode processar:",
    "options": [
        "Sequências de tamanhos variáveis",
        "Apenas vetores fixos",
        "Somente imagens",
        "Somente números inteiros"
    ],
    "answer": "Sequências de tamanhos variáveis",
    "explanation": "Essa é uma das vantagens das arquiteturas recorrentes."
},

{
    "topic": "RNN",
    "question": "Qual área utiliza amplamente RNNs?",
    "options": [
        "Processamento de Linguagem Natural",
        "Renderização 3D",
        "Redes elétricas",
        "Criptografia"
    ],
    "answer": "Processamento de Linguagem Natural",
    "explanation": "Textos são sequências naturais."
},

{
    "topic": "RNN",
    "question": "O treinamento de RNNs utiliza:",
    "options": [
        "Backpropagation Through Time",
        "K-Means",
        "Árvore de decisão",
        "Busca binária"
    ],
    "answer": "Backpropagation Through Time",
    "explanation": "A retropropagação é aplicada ao longo da sequência temporal."
},

{
    "topic": "RNN",
    "question": "Qual é o objetivo das portas em uma LSTM?",
    "options": [
        "Controlar fluxo de informação",
        "Criar filtros",
        "Gerar imagens",
        "Reduzir classes"
    ],
    "answer": "Controlar fluxo de informação",
    "explanation": "As portas decidem o que lembrar e esquecer."
},

{
    "topic": "RNN",
    "question": "Uma sequência de palavras é um exemplo de:",
    "options": [
        "Dado sequencial",
        "Imagem RGB",
        "Dataset tabular",
        "Filtro convolucional"
    ],
    "answer": "Dado sequencial",
    "explanation": "A ordem dos elementos possui significado."
},

{
    "topic": "RNN",
    "question": "Qual é o principal objetivo de uma RNN?",
    "options": [
        "Modelar dependências em sequências",
        "Detectar bordas em imagens",
        "Reduzir resolução",
        "Eliminar overfitting"
    ],
    "answer": "Modelar dependências em sequências",
    "explanation": "RNNs aprendem relações temporais e contextuais."
}

]
