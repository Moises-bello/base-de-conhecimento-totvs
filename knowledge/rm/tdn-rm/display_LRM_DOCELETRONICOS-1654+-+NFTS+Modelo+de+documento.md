---
content_hash: cecda9d931dd9ea919b959e6958044a14efac65df8e40ac908fa96de5999e4b3
fetched_at: '2026-06-29T00:05:53.198964+00:00'
page_id: '1068194575'
product: rm
source: tdn-rm
title: DOCELETRONICOS-1654 - NFTS Modelo de documento
type: documentation
url: https://tdn.totvs.com/display/LRM/DOCELETRONICOS-1654+-+NFTS+Modelo+de+documento
version: 1
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | NFTS Webservice |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | DOCELETRONICOS-1654 |

## **02. SITUAÇÃO/REQUISITO**

Ao criar uma nota de NFTS e enviá-la para a Prefeitura de São Paulo, o XML é gerado com apenas a opção 1 – Dispensado de emissão de documento fiscal.  
   
Solicitado a implementação das demais opções da tag "tipoDocumento", que pode assumir os seguintes valores:  
   
1 – Dispensado de emissão de documento fiscal  
2 – Com emissão de documento fiscal autorizado pelo município  
3 – Sem emissão de documento fiscal, embora obrigado.

## **03. SOLUÇÃO/COMPORTAMENTO**

Implementado a solução da NFTS do gerador de saídas, onde o cliente pode informar o valor que desejar nos parâmetros de modelo ISS.
