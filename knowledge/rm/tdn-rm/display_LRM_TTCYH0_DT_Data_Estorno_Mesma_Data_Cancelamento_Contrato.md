---
content_hash: 177ecd9f49ff02604457a8e901d1cb32fdacd1a2d9e82905e2d3c46e010aff8b
fetched_at: '2026-06-29T00:06:14.266136+00:00'
page_id: '209453581'
product: rm
source: tdn-rm
title: TTCYH0_DT_Data_Estorno_Mesma_Data_Cancelamento_Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/TTCYH0_DT_Data_Estorno_Mesma_Data_Cancelamento_Contrato
version: 3
---

# Data de Estorno com mesma Data do Cancelamento do Contrato

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *TOTVS Educacional.* |
| **Módulo:** | **Gestão Educacional*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cancelar contrato* | *Cancelar contrato.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Processo de Cancelamento de contrato.* | *Cancelar contrato.* | |
| **Cadastros Iniciais:** | *1) Contrato cadastrado.*  *2) Contrato com contabilização gerada* |
| **Parâmetro(s):** | **1) Educacional | Integração | Contábil | Considera a data de cancelamento do contrato para a data do estorno contábil no processo de cancelamento de contrato. MARCADO;*.* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas utilizadas:** | *SCONTRATO, CPARTIDA, CCONTA, CHIST* |
| **Sistema(s) operacional(is):** | *Windows 7* |
| **Versões/Release:** | *11.83.55* |

## Descrição

Para permitir que a data dos estornos contábeis gerados no processo de Cancelamento de Contrato seja igual à data informada para o cancelamento do contrato, foi criado um novo parâmetro no sistema:

Parâmetros > Integração > Contábil > "Considera a data de cancelamento do contrato para a data do estorno contábil no processo de cancelamento de contrato". 

Somente com este novo parâmetro habilitado os estornos da contabilização receberão a mesma data informada no processo de "Cancelar contrato". Com o parâmetro desabilitado, o processo continuará como antes, ou seja, a data dos lançamentos de estorno continuará igual à data de execução do processo.

## Procedimento para Utilização

       1.            Marcar o novo parâmetro:

Parâmetros > Integração > Contábil > "Considera a data de cancelamento do contrato para a data do estorno contábil no processo de cancelamento de contrato"

       2.            Executar o processo de Cancelar contrato, utilizando um contrato que esteja contabilizado.

       3.            Durante o processo, informar a data do Cancelamento como sendo uma data diferente da de hoje.

       4.            O estorno gerado, e a contabilização da diferença será gerado com a data informada durante o processo.

       5.            Com o parâmetro desmarcado, o comportamento do sistema se manterá o mesmo.
