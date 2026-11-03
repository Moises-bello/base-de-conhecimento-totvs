---
content_hash: d7e12636d688e247eb481996a3403687d23ba2746e8c91ef0817767b259d4b21
fetched_at: '2026-06-29T00:10:22.514094+00:00'
page_id: '496817003'
product: rm
source: tdn-rm
title: 5332893 FISCAL01-8733 DT EFD - Contribuições - Registro F550
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496817003
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Rotina Federal EFD Contribuições |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar a Rotina EFD Contribuições os Valores referentes a Devolução para o Registro F550 não estão sendo considerados nos campos  
04 - VL\_DESC\_PIS e 09 - VL\_DESC\_COFINS.

**03. SOLUÇÃO**

Foi realizada uma implementação para que estes Lançamentos Fiscais (Devolução de Venda) sejam considerados no Registro F550.

**04. REGRAS**

1 - Filtrar Lançamentos Fiscais de Entrada

2 - Lançamento Marcados como Devolução na Natureza de Operação

3 - Lançamentos dentro do próprio Período de geração da Rotina.
