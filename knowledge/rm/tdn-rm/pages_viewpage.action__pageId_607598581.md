---
content_hash: 3e3a95a1301ad4a7dac433525a841a178053adda856def95f7ed3d1facb790e7
fetched_at: '2026-06-29T00:10:58.918274+00:00'
page_id: '607598581'
product: rm
source: tdn-rm
title: 10515404 FISCAL01-15238 Divergência na geração do EFD PIS/COFINS e EFD ICMS/IPI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=607598581
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS BackOffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | SPED Fiscal |
| País: | Brasil |
| Ticket: | 10515404 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15238 |

## **02. SITUAÇÃO/REQUISITO**

Cliente deseja que nos Speds Fiscal e Contribuições, Registro 0200, seja gerado no campo 3 as informações com caractere especial.

O cliente utiliza o TIF, e informou que o Sped Fiscal gera com caractere especial. Já o EFD Contribuições não.

Com isso, ao cruzar as informações no TIF é apresentada inconsistência.

## **03. SOLUÇÃO**

Ajustado a rotina de Geração de Saídas EFD e SPED Fiscal a fim de ajustar a remoção de caracteres especiais do campo03 do registo 0200 do gerador de saídas.
