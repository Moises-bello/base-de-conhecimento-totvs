---
content_hash: a7a4e8873c2b014df807eedd7fb19157696df831d4c503d15b77d04eb368a1e3
fetched_at: '2026-06-29T00:12:08.473836+00:00'
page_id: '936464908'
product: rm
source: tdn-rm
title: FISCAL01-25646 - DT - Ajuste para a regra de geração do vICMSDif da NFe
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=936464908
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | NFS-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25646 |

## **02. SITUAÇÃO/REQUISITO**

Ao emitir uma NF-e com diferimento de ICMS de 100% para o estado do Ceará, os campos do grupo de ICMS (CST 51) estão sendo levados zerados no XML da nota fiscal.  
Contudo, conforme verificado em legislação específica do Estado do Ceará, mesmo em operações com diferimento total, os campos relacionados ao ICMS devem ser preenchidos no XML com os valores corretos, e não zerados.  
O sistema só faz o preenchimento destes campos para o estado do Rio de Janeiro é necessário que o preenchimento seja feito para todos os casos em que os valores estejam informados no movimento.

## **03. SOLUÇÃO**

Foi feita uma alteração para não mais remover os valores do grupo ICMS51 se o estado for diferente de Rio de Janeiro.

Disponível a partir da biblioteca 12.1.2406
