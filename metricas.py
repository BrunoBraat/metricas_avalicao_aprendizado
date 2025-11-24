def calcular_metricas(VP, VN, FP, FN):
    # Acurácia
    acuracia = (VP + VN) / (VP + VN + FP + FN)
    
    # Sensibilidade (Recall)
    sensibilidade = VP / (VP + FN) if (VP + FN) != 0 else 0
    
    # Especificidade
    especificidade = VN / (VN + FP) if (VN + FP) != 0 else 0
    
    # Precisão
    precisao = VP / (VP + FP) if (VP + FP) != 0 else 0
    
    # F-score
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