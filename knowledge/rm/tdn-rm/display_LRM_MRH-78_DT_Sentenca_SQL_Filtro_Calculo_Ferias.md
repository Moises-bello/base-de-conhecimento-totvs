---
content_hash: 06dff2c4a1a13ee1d3c8b476feed37eed31e01a97c6bd51f4087b0869d325d24
fetched_at: '2026-06-29T00:08:21.501296+00:00'
page_id: '268827351'
product: rm
source: tdn-rm
title: MRH-78_DT_Sentenca_SQL_Filtro_Calculo_Ferias
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-78_DT_Sentenca_SQL_Filtro_Calculo_Ferias
version: 112
---

# SENTENÇA SQL COM PARÂMETROS NO FILTRO DE SELEÇÃO DO MÓDULO DE CÁLCULO DE FÉRIAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Cálculo de Férias* |
| **Situação/Requisito:** | *Na seleção de funcionários da tela do processo de Cálculo das Férias, quando é utilizado filtro com parâmetros contendo o mesmo nome de parâmetros internos, é exibida mensagem de erro na sentença SQL.*  *No caso do cliente, foi utilizado filtro com sentença SQL contendo parâmetros com os nomes DATAINICIO e DATAFIM. Estes nomes já eram utilizados no SELECT interno dos funcionários selecionados para o processo.* |
| **Solução/Implementação:** | *Foram alterados os nomes internos dos parâmetros no SELECT dos funcionários selecionados para o processo, para que o usuário possa utilizar o filtro desejado.* |
| **Chamados relacionados:** | MRH-78 |
| **Requisito (ISSUE):** | MRH-78 |

divs
