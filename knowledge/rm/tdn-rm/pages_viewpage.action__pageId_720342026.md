---
content_hash: 97df5287c37021aba83c58362f892da330d4f91284f08fb4aa0b48e767ba4d1b
fetched_at: '2026-06-29T00:11:26.756222+00:00'
page_id: '720342026'
product: rm
source: tdn-rm
title: FISCAL01-18452 - DT - R-1000 - Órgão Público vinculado à União
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=720342026
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD Reinf - Eventos Cadastrais - R-1000 |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18452 |

## **02. SITUAÇÃO/REQUISITO**

Gerar o campo indUnião no registro R1000 da EFD Reinf.

O campo deve ser gerado somente em versões do layout 2.1.1 e superiores.

O campo recebe o valor 1 caso a filial tenha em seu cadastro selecionado a opção Órgão Público — Federal, caso contrário o campo recebe o valor 0.

## **03. SOLUÇÃO**

Adicionada a geração do registro conforme a definição no manual da REINF [versão 2,1.1](http://sped.rfb.gov.br/pasta/show/6041).

Disponível a partir da biblioteca 12.1.2205
