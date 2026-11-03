---
content_hash: a265447d54e431b5a0a78dab33bc5c2c5f5c309afee3f484326af721b2e967b9
fetched_at: '2026-06-29T00:11:37.889183+00:00'
page_id: '778782748'
product: rm
source: tdn-rm
title: FISCAL01-20356 - DT - Valor de ICMS-ST não calculado na escrituração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=778782748
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Escrituração |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-20356 |

## **02. SITUAÇÃO/REQUISITO**

Ao escriturar um movimento, o valor do campo "Valor de ICMSST" não é preenchido no Item do Lançamento Fiscal e na Situação Tributária (campo "Valor ST") se a flag "ICMS S.T. Considera Redução no Cálculo do ICMS Próprio" estiver marcada na regra de ICMS da natureza do movimento.  
O valor é preenchido corretamente se a flag estiver desmarcada.

## **03. SOLUÇÃO**

Correção para o cálculo do ICMS ST na escrituração quando a flag "ICMS S.T. Considera Redução no Cálculo do ICMS Próprio" estiver marcada na regra de ICMS da natureza do movimento.

Campos

Disponível a partir da biblioteca 12.1.2302
