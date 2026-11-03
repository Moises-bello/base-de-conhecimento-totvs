---
content_hash: d6b426eebabd46cf017b14d261b6530ec5dbc1672c1cb82e90e81f4575a999f7
fetched_at: '2026-06-29T00:06:02.600555+00:00'
page_id: '198947539'
product: rm
source: tdn-rm
title: TSYPST_DT_CALCMEDJOR_Mes_Atual
type: documentation
url: https://tdn.totvs.com/display/LRM/TSYPST_DT_CALCMEDJOR_Mes_Atual
version: 2
---

# CALCMEDJOR DUPLICANDO VALOR DO MES ATUAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Função de fórmula CALCMEDJOR* |
| **Situação/Requisito:** | *Função de fórmula CALCMEDJOR está acumulando o valor do evento do envelope corrente duas vezes, quando o sindicato está parametrizado para considerar o mês atual.* |
| **Solução/Implementação:** | *Ajustar a função de fórmula CALCMEDJOR para que, no caso do evento constar no envelope corrente, considerar somente o valor em memória durante o cálculo. Verificar se a chamada está sendo feita de uma execução de cálculo, ou de outro módulo externo. Neste caso, o valor deverá ser carregado da tabela de ficha financeira.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSYPST* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.7* |
