Cálculo de Métricas de Avaliação de Aprendizado
📖 Descrição
Este projeto tem como objetivo calcular as principais métricas utilizadas para avaliar modelos de classificação em Machine Learning.
As métricas são derivadas da matriz de confusão, que organiza os resultados em:
- VP: Verdadeiros Positivos
- VN: Verdadeiros Negativos
- FP: Falsos Positivos
- FN: Falsos Negativos

⚙️ Métricas Implementadas
As métricas calculadas neste projeto são:
|  |  | 
|  | (VP+VN)/(VP+VN+FP+FN) | 
|  | (VP)/(VP+FN) | 
|  | (VN)/(VN+FP) | 
|  | (VP)/(VP+FP) | 
|  | 2\cdot \frac{Precisão\cdot Sensibilidade}{Precisão+Sensibilidade} | 



🐍 Exemplo em Python
def calcular_metricas(VP, VN, FP, FN):
    acuracia = (VP + VN) / (VP + VN + FP + FN)
    sensibilidade = VP / (VP + FN) if (VP + FN) != 0 else 0
    especificidade = VN / (VN + FP) if (VN + FP) != 0 else 0
    precisao = VP / (VP + FP) if (VP + FP) != 0 else 0
    fscore = (2 * precisao * sensibilidade) / (precisao + sensibilidade) if (precisao + sensibilidade) != 0 else 0
    
    return {
        "Acurácia": acuracia,
        "Sensibilidade": sensibilidade,
        "Especificidade": especificidade,
        "Precisão": precisao,
        "F-score": fscore
    }

# Exemplo de matriz de confusão arbitrária
VP, VN, FP, FN = 50, 40, 10, 5
metricas = calcular_metricas(VP, VN, FP, FN)

for nome, valor in metricas.items():
    print(f"{nome}: {valor:.2f}")



📌 Resultado esperado (com VP=50, VN=40, FP=10, FN=5)
- Acurácia: 0.90
- Sensibilidade: 0.91
- Especificidade: 0.80
- Precisão: 0.83
- F-score: 0.87

🎯 Objetivo
O foco deste projeto é compreender como cada métrica funciona e como elas podem ser aplicadas para avaliar o desempenho de modelos de classificação.

🚀 Próximos Passos
- Implementar testes com diferentes matrizes de confusão.
- Comparar métricas em cenários de classes desbalanceadas.
- Integrar com bibliotecas como scikit-learn para validação.

👉 Esse README já está pronto para ser usado no seu repositório.
Quer que eu também prepare uma versão com visualização gráfica da matriz de confusão (heatmap em Python) para enriquecer ainda mais o projeto?
