---
content_hash: 62c4c777c5b6d9176eaaa57dc1351f0dec33dcc8f23274f1d935459c14e320dd
fetched_at: '2026-06-29T00:06:02.580968+00:00'
page_id: '198947439'
product: rm
source: tdn-rm
title: TSVCGK_DT_CALCMEDJOR_Mes_Atual
type: documentation
url: https://tdn.totvs.com/display/LRM/TSVCGK_DT_CALCMEDJOR_Mes_Atual
version: 1
---

# CALCMEDJOR DUPLICANDO VALOR DO MES ATUAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Função de fórmula CALCMEDJOR* |
| **Situação/Requisito:** | *Função de fórmula CALCMEDJOR está acumulando o valor do evento do envelope corrente duas vezes, quando o sindicato está parametrizado para considerar o mês atual.* |
| **Solução/Implementação:** | *Ajustar a função de fórmula CALCMEDJOR para que, no caso do evento constar no envelope corrente, considerar somente o valor em memória durante o cálculo. Verificar se a chamada está sendo feita de uma execução de cálculo, ou de outro módulo externo. Neste caso, o valor deverá ser carregado da tabela de ficha financeira.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSVCGK* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.40* |
