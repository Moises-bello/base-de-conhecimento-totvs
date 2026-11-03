---
content_hash: 6586fa5f365d8aa0e4179aa1ae4e2785a1cc2f2646dfb8489a0fe2d544123505
fetched_at: '2026-06-29T00:12:13.407783+00:00'
page_id: '954099712'
product: rm
source: tdn-rm
title: FISCAL01-25407 - Recebimento de NF-e - TNFeInfNFePagDetPagCardTBand
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-25407+-+Recebimento+de+NF-e+-+TNFeInfNFePagDetPagCardTBand
version: 5
---

## ****01. DADOS GERAIS****

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Recebimento de NF-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25407 |

## **02. SITUAÇÃO/REQUISITO**

Ao realizar a importação de xml, cujo o valor da tag **<tBand>00</tBand>** é apresentado a mensagem de erro:

**Erro durante a tradução do XML.**  
**Chave de Acesso: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX**  
**Mensagem Original: Erro no documento XML (143, 11).. Erro de validação de instância: '00' não é um valor válido para TNFeInfNFePagDetPagCardTBand.**

A mensagem é apresentada devido ao valor 00, não ser valido (segundo o manual de orientação do contribuinte)

## **03. SOLUÇÃO**

Realizado ajuste para interpretar o valores que não estejam no manual de orientação do contribuinte.

Disponível à partir da biblioteca 12.1.2410
