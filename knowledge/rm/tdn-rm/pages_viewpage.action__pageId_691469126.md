---
content_hash: 1c16ac99683d7518eaf3089195a89750cd7ed42f7a1c2ac884ddd2232c1a4ff4
fetched_at: '2026-06-29T00:11:21.304458+00:00'
page_id: '691469126'
product: rm
source: tdn-rm
title: FISCAL01-6722 - DT Registro C170 Campo 19 - EFD Contribuições
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=691469126
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD - Contribuições |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-6722 |

## **02. SITUAÇÃO/REQUISITO**

Ajuste na Rotina EFD para gerar o Campo 19 - IND\_APUR do registro C170

## **03. SOLUÇÃO**

Foi realizado um ajuste na geração do registro C170 para gerar o campo IND\_APUR conforme a gerado no SPED Fiscal.

0 - Mensal

1 - Decendial

Este campo terá origem no campo Apuração do Tributo ligado ao Período de Apuração de IPI da Coligada, Filial e período de geração da Rotina EFD.

obs.: Quando nenhuma destas opções estiveram selecionadas irá gerar o campo com o valor

0 - Mensal
