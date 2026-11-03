---
content_hash: 318c528bfc1e3ae111e9c93b42284bdb0c8c54ccb531559f2ed11fbfa2ac283a
fetched_at: '2026-06-29T00:06:20.745436+00:00'
page_id: '223154186'
product: rm
source: tdn-rm
title: TTAFDS_DT_Funcao_CALCMEDJOR_Comissionista
type: documentation
url: https://tdn.totvs.com/display/LRM/TTAFDS_DT_Funcao_CALCMEDJOR_Comissionista
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
| **Chamados   relacionados:** | *TTAFDS* |
| **Versões/Release:** | *11.82.43* |
