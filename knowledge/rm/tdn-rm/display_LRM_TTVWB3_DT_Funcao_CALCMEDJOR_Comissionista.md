---
content_hash: 441bad7989dcadd3d9cf12715c186ed6339ef483f4c582ba2fa8b322ec7967ff
fetched_at: '2026-06-29T00:06:20.749197+00:00'
page_id: '223154256'
product: rm
source: tdn-rm
title: TTVWB3_DT_Funcao_CALCMEDJOR_Comissionista
type: documentation
url: https://tdn.totvs.com/display/LRM/TTVWB3_DT_Funcao_CALCMEDJOR_Comissionista
version: 1
---

# FUNÇÃO CALCMEDJOR PARA FUNCIONÁRIOS COMISSIONISTA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Função CALCMEDJOR* |
| **Situação/Requisito:** | *Função de fórmula CALCMEDJOR está considerando valor mensal duplicado para funcionários comissionista.* |
| **Solução/Implementação:** | *No cálculo de média normal para funcionários comissionistas, a média do tipo hora é calculada separada para a parte do salário nominal e para parte da comissão.*  *Entretanto no caso da função CALCMEDJOR, quando é média somente da hora, não deve fazer o cálculo duas vezes.* |
| **Chamados   relacionados:** | *TTVWB3* |
| **Versões/Release:** | *12.1.9* |
