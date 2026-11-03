---
content_hash: da3e02bc36fa81eae934b9c4f5f0aedebc8c0234523cec3953029ddcd3ed67d4
fetched_at: '2026-06-29T00:10:37.026788+00:00'
page_id: '533750462'
product: rm
source: tdn-rm
title: FISCAL01-11730 DT EFD REINF - Eventos R-20xx de Filiais distintas mas com CNPJ
  Iguais
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-11730+DT+EFD+REINF+-+Eventos+R-20xx+de+Filiais+distintas+mas+com+CNPJ+Iguais
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração dos Eventos R-20xx da EFD-REINF |
| Ticket: | FISCAL01-11730 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11730 |

## **02. SITUAÇÃO/REQUISITO**

Quando existem duas filiais com o mesmo CNPJ os eventos estão sendo gerados em duplicidade. Deve ser realizado acerto para que seja gerado apenas um evento com os valores agregados.

## **03. SOLUÇÃO**

No processo de geração dos eventos R-20xx EFD REINF os eventos serão agrupados também pelo CNPJ da filial em vez do código da filial.

Eventos alterados: R-2010, R-2020, R-2040, R-2050 e R-2060.
