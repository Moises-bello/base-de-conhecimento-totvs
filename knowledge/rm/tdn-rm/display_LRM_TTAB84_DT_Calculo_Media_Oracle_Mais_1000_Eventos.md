---
content_hash: d84d68bba227b52af964bb8eceea7c0b22a95c738feb3d1d9aebac565c63336b
fetched_at: '2026-06-29T00:06:07.884471+00:00'
page_id: '201739697'
product: rm
source: tdn-rm
title: TTAB84_DT_Calculo_Media_Oracle_Mais_1000_Eventos
type: documentation
url: https://tdn.totvs.com/display/LRM/TTAB84_DT_Calculo_Media_Oracle_Mais_1000_Eventos
version: 1
---

# CÁLCULO DE MÉDIA EM ORACLE COM MAIS DE 1000 EVENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cálculo de Média* |
| **Situação/Requisito:** | *Erro na sentença SQL que seleciona os registros na ficha financeira para o cálculo da média, quando existem mais de 1000 eventos que incidem na média.*  *O Oracle não permite mais de 1000 opções na cláusula IN.* |
| **Solução/Implementação:** | *Alterar a sentença SQL que seleciona os registros na ficha financeira para o cálculo da média, para não utilizar IN quando existirem mais de 1000 eventos que incidem na média.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTAB84* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
