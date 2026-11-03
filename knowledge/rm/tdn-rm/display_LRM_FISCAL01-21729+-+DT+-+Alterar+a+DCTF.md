---
content_hash: ebf791fa2fe1da4124d0e330ffec31e43af700a389d4f2a547cb3cc8c014b680
fetched_at: '2026-06-29T00:11:45.062569+00:00'
page_id: '819060869'
product: rm
source: tdn-rm
title: FISCAL01-21729 - DT - Alterar a DCTF
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-21729+-+DT+-+Alterar+a+DCTF
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | DCTF |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-21729 |

## **02. SITUAÇÃO/REQUISITO**

Alterar a geração da DCTF para não considerar os tributos da Reinf a partir de 2024.

Conforme informado pela Receita Federal, a partir de janeiro de 2024 a DCTFWeb passa a apurar os valores dos tributos de retenção de Imposto de Renda, CSLL, PIS e Cofins escriturados na EFD-Reinf.

Com isto os valores destes tributos gerados na Rotina da DCTF, não deverão ser mais informados.

Manter 2 Layout no Totvs compartilhamento, um Layout com a alteração e outro sem alteração.

## **03. SOLUÇÃO**

Alterado o filtro do layout para deixar de considerar guias dos tributos:

* IRPJ
* IRRF
* PISIMPORT
* COFINSIMPORT
* CONTRIBSOCIALRF
* COSIRF
* IRRFPJ
* IRRFIMPORT
* CSLLRF

O layout DCTF-Antes\_2024 contém a regra anterior que considera os tributos removidos e também deve ser publicado.

Disponível a partir da biblioteca 12.1.2302
