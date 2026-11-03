---
content_hash: 201cd48b3ac7e0951ef416bea434f114814a3a5dc58127f8d90493a6371de2f4
fetched_at: '2026-06-29T00:11:33.445284+00:00'
page_id: '759946359'
product: rm
source: tdn-rm
title: FISCAL01-19285 - DT - Alterações Registro 0021 ECF para versão 009
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=759946359
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Gerador de Saídas | ECF |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-19783 |

## **02. SITUAÇÃO/REQUISITO**

A partir da versão 9 (2023) as alterações abaixo devem ser realizadas no Registro 0021, porém estas alterações não podem ter efeito retroativo, ou seja, se o cliente gerar um arquivo da ECF em versões anteriores o comportamento do registro deve ser mantido conforme a regra atual (Antes da alteração).

* Campo 5 - ND\_PATVD: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 7 - ND\_REPENEC: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 8 - ND\_REICOMP: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 9 - IND\_RETAERO: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 11 - IND\_RESIDUOS\_SOLIDOS: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 12 - IND\_RECOPA: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 13 - IND\_COPA\_DO\_MUNDO: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 15 - IND\_REPNBL\_REDES: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 16 - IND\_REIF: Passa a ser gerado de forma Fixa com o Valor **N**
* Campo 17 - IND\_OLIMPIADAS: Deverá ser renomeado para "IND\_OUTROS - outros tipos de benefícios fiscais"

## **03. SOLUÇÃO**

Foi realizado ajuste no layout ECF para correta geração do registro 0021 na geração com versão do layout 009.

Disponível à partir da biblioteca 12.1.2205
