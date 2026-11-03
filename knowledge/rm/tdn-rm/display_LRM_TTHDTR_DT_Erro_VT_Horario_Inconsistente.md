---
content_hash: 7ea5c7b04348ae76136cfa07b0f1f7f51417a5170324836d5ff5481633005e3f
fetched_at: '2026-06-29T00:06:09.524346+00:00'
page_id: '203755552'
product: rm
source: tdn-rm
title: TTHDTR_DT_Erro_VT_Horario_Inconsistente
type: documentation
url: https://tdn.totvs.com/display/LRM/TTHDTR_DT_Erro_VT_Horario_Inconsistente
version: 1
---

# ERRO NO CÁLCULO DE VALE TRANSPORTE QUANDO EXISTEM DADOS INCONSISTENTES NO CADASTRO DE HORÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Vale Transporte* |
| **Situação/Requisito:** | *Quando é utilizado o RMChronus, e existem dados inconsistentes no cadastro de Horário, está retornando erro no cálculo do Vale Transporte.* |
| **Solução/Implementação:** | *Tratar no cálculo do Vale Transporte para, caso o cadastro de Horário possua dados inconsistentes, não chame o serviço do RMChronus para a contagem de dias de trabalho da jornada.*  *Neste caso, o processo seguirá o mesmo tratamento de clientes que não utilizam o RMChronus.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTHDTR* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
