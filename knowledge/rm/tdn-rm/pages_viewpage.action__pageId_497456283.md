---
content_hash: eff69f3861b14ce7c9dd635d93c4c7d263f2a792266a9174ec0f352049793237
fetched_at: '2026-06-29T00:10:22.567922+00:00'
page_id: '497456283'
product: rm
source: tdn-rm
title: 5911035  FISCAL01-9667 DT Sintegra - Registro "88STITNF"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=497456283
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Rotina Estadual Sintegra |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar a rotina SPED Fiscal o sistema apresenta no campo 02 do registro C170 (NUM\_ITEM - Número sequencial do item no documento fiscal) um número sequencial, já na rotina Sintegra, para o mesmo lançamento, o sistema apresenta no campo 9 do registro 88STITNF (Número de Item), o valor da coluna NUMITEM da tabela DITEM, mesmo que não esteja em um sequencial.

## **03. SOLUÇÃO**

Ajuste na geração do campo 9 (Número do Item) do Registro 88STITNF para ser preenchido conforme o registro C170 do SPED Fiscal (com um Sequencial) e NÃO com o valor do campo NUMITEM dos Itens do Lançamento Fiscal.
