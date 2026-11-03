---
content_hash: 2c98f0be9d18b0169929918e3bae77f12211bf09a673e5a1886ec65094e2099a
fetched_at: '2026-06-29T00:11:46.629034+00:00'
page_id: '823803384'
product: rm
source: tdn-rm
title: FISCAL01-21953 - TPF - NFS São Paulo - Tag de alíquota com formato incorreto.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=823803384
version: 3
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | NFSe |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-21953 |

## **02. SITUAÇÃO/REQUISITO**

Ao fazer a emissão de NFS-e para São Paulo/SP via TPF e o XML está com o formato da tag da alíquota incorreto.

A tag é gerada com o valor da alíquota dividido por 100.

O manual do layout da Prefeitura Paulista determina que a tag seja gerada sem divisão por 100.

Imagem

Com esta diferença de formatos da tag a nota é rejeitada.

## **03. SOLUÇÃO**

Ajustada a geração da tag aliquota da NFSe quando o TPF é usado.  
O valor deixa de usar a base 100.  
Exemplo 3% de alíquota era gerado como 0.0300, com o ajuste passa a ser 3.0000.  
A solução foi aplicada em todas as tags de alíquota do XML.

Disponível a partir da biblioteca 12.1.2302
