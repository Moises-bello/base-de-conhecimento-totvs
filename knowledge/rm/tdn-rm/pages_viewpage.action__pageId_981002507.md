---
content_hash: 09bfaa0fc6d877d72ebf1017f0e6eb3233d0fa6bacde0f4ecab16da43bb2bfa5
fetched_at: '2026-06-29T00:12:15.643227+00:00'
page_id: '981002507'
product: rm
source: tdn-rm
title: Valores da Prestação de Serviço do CT-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=981002507
version: 4
---

# vPrest - Valores da Prestação de Serviço do CT-e

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **vPrest** | **[infCte](https://tdn.totvs.com/pages/viewpage.action?pageId=981000770)** | **1-1** | **Grupo** | **Valores da Prestação de Serviço** |
| vTPrest | vPrest | 1-1 | Elemento | TMOV.VALORLIQUIDO |
| vRec | vPrest | 1-1 | Elemento | Retorna o valor da fórmula contida no campo TTMV.CODFRMRATEIOLAN.  Caso não exista nenhuma fórmula nesse campo, será gerado com TMOV.VALORLIQUIDO |
| **Comp** | **vPrest** | **0-n** | **Grupo** | **Componentes do Valor da Prestação** |
| xNome | Comp | 1-1 | Elemento | O campo será gerado de acordo com qual campo do Movimento está preenchido com o valor, de acordo com as opções abaixo:  DESPACHO - TMOV.VLRDESPACHO;  PEDAGIO - TMOV.VLRPEDAGIO;  SEC/CAT - TMOV.VLRSECCAT;  FRETEOUTROS - TMOV.VLRFRETEOUTROS; |
| vComp | Comp | 1-1 | Elemento | TMOV.VLRDESPACHO, TMOV.VLRSECCAT, TMOV.VLRPEDAGIO e TMOV.VLRFRETEOUTROS |
