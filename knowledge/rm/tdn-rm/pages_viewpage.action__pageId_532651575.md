---
content_hash: ba605ff99828899b6edd88838513ade50abf0fe2e5a4d8d756120f7f6cef8a58
fetched_at: '2026-06-29T00:10:36.528204+00:00'
page_id: '532651575'
product: rm
source: tdn-rm
title: FISCAL01-11891 DT EFD-Contribuições 2020 Gerar o Registro 1011
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=532651575
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD-Contribuições |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11891 |

## **02. SITUAÇÃO/REQUISITO**

Implementar a geração do registro 1011 na EFD Contribuições

## **03. SOLUÇÃO**

**Funcionalidade: Geração do registro 1011 da EFD Contribuições**  
Cenário I: Geração do registro 1011  
Dado que a data de início de geração é maior ou igual a 01/01/2020  
E existem lançamentos fiscais que geram C170 e com PIS/COFINS e tributos discutidos do item  
Ao gerar a EFD Contribuições no gerador de saída, o registro 1011 deve ser preenchido.  
  
Cenário II: Não Geração do registro 1011  
Dado que a data de início de geração é menor ou igual a 01/01/2020  
E existem lançamentos fiscais que geram C170 e com PIS/COFINS e tributos discutidos do item  
Ao gerar a EFD Contribuições no gerador de saída, o registro 1011 não deve ser exibido.

| Número | Campo | Origem |
| --- | --- | --- |
| 1 | REG | Fixo "1011" |
| 2 | REG\_REF | Não ligado |
| 3 | CHAVE\_DOC | Não ligado |
| 4 | COD\_PART | Não ligado |
| 5 | COD\_ITEM | TPRODUTO.CODPRD |
| 6 | DT\_OPER | DLAF.DATALF |
| 7 | VL\_OPER | DITEM.VALORMERC |
| 8 | CST\_PIS | DTRBITEM.SITTRIBUTARIA |
| 9 | VL\_BC\_PIS | DTRBITEM.BASETRB |
| 10 | ALIQ\_PIS | DTRBITEM.ALIQTRB |
| 11 | VL\_PIS | DTRBITEM.VALORTRB |
| 12 | CST\_COFINS | DTRBITEM.SITTRIBUTARIA |
| 13 | VL\_BC\_COFINS | DTRBITEM.BASETRB |
| 14 | ALIQ\_COFINS | DTRBITEM.ALIQTRB |
| 15 | VL\_COFINS | DTRBITEM.VALORTRB |
| 16 | CST\_PIS\_SUSP | DITEMTRIBDISCUTIDOS.CODSITTRIBUTARIA |
| 17 | VL\_BC\_PIS\_SUSP | DITEMTRIBDISCUTIDOS.BASETRB |
| 18 | ALIQ\_PIS\_SUSP | DITEMTRIBDISCUTIDOS.ALIQUOTA |
| 19 | VL\_PIS\_SUSP | DITEMTRIBDISCUTIDOS.VALOR |
| 20 | CST\_COFINS\_SUSP | DITEMTRIBDISCUTIDOS.CODSITTRIBUTARIA |
| 21 | VL\_BC\_COFINS\_SUSP | DITEMTRIBDISCUTIDOS.BASETRB |
| 22 | ALIQ\_COFINS\_SUSP | DITEMTRIBDISCUTIDOS.ALIQUOTA |
| 23 | VL\_COFINS\_SUSP | DITEMTRIBDISCUTIDOS.VALOR |
| 24 | COD\_CTA | DITEM.CODCONTA |
| 25 | COD\_CCUS |  |
| 26 | DESC\_DOC\_OPER |  |
