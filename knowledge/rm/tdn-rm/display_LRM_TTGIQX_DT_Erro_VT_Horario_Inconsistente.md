---
content_hash: f71dba462575e994b522997bbb2fd9452069fb59a4777a0136e9e0bb09f3ea32
fetched_at: '2026-06-29T00:06:09.489155+00:00'
page_id: '203755261'
product: rm
source: tdn-rm
title: TTGIQX_DT_Erro_VT_Horario_Inconsistente
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGIQX_DT_Erro_VT_Horario_Inconsistente
version: 2
---

# ERRO NO CÁLCULO DE VALE TRANSPORTE QUANDO EXISTEM DADOS INCONSISTENTES NO CADASTRO DE HORÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Vale Transporte* |
| **Situação/Requisito:** | *Quando é utilizado o RMChronus, e existem dados inconsistentes no cadastro de Horário, está retornando erro no cálculo do Vale Transporte.* |
| **Solução/Implementação:** | *Tratar no cálculo do Vale Transporte para, caso o cadastro de Horário possua dados inconsistentes, não chame o serviço do RMChronus para a contagem de dias de trabalho da jornada.*  *Neste caso, o processo seguirá o mesmo tratamento de clientes que não utilizam o RMChronus.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTGIQX* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
