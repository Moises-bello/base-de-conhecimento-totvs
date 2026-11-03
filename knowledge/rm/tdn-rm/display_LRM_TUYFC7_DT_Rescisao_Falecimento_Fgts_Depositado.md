---
content_hash: 85c3807a164478c15913de72b1a4e58b8a4b3bdd5267d937bf8057b075b45814
fetched_at: '2026-06-29T00:08:19.261311+00:00'
page_id: '266981531'
product: rm
source: tdn-rm
title: TUYFC7_DT_Rescisao_Falecimento_Fgts_Depositado
type: documentation
url: https://tdn.totvs.com/display/LRM/TUYFC7_DT_Rescisao_Falecimento_Fgts_Depositado
version: 2
---

# RESCISÃO POR FALECIMENTO DEVE LANÇAR EVENTOS DE FGTS DEPOSITADO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Rescisão* | *Cálculo de Rescisão* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Rescisão** | *Cálculo de Rescisão* | | *Rescisão Complementar* | *Cálculo de Rescisão Complementar* | |
| **Cadastros Iniciais:** | *Cadastro de Rescisão* |
| **Parâmetro(s):** | *Tipo da Demissão* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *TUYFC7, TVXNKW* |
| **Requisito (ISSUE):** | *Folha* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server, Oracle* |
| **Tabelas Utilizadas:** | *PFUNC, PFFINANC* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Nas rescisões com os tipos de demissão de falecimento, códigos 8, F e P, eram lançados os CC's de FGTS 26 e 31, semelhante à demissão tipo 2 - Iniciativa do Empregador sem Justa Causa.

Cliente alegou que no caso de falecimento devem ser lançados os CC's de FGTS semelhantes à demissão tipo 4 - Iniciativa do Empregado sem Justa Causa, códigos de cálculo 73 e 133.

Foi realizada a troca dos CC's de FGTS no cálculo das rescisões com tipo de demissão 8, F e P.
