---
content_hash: c4b851a6b359a87295f07f0eb0f40d575dafd637a0701ac9fec442888c736e96
fetched_at: '2026-06-29T00:10:38.858241+00:00'
page_id: '545257613'
product: rm
source: tdn-rm
title: 7578567 FISCAL01-11690 DT Equiparação EFD Fiscal e EFD Contribuições - 0450
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=545257613
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD Contribuições |
| Ticket: | 7578567 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11690 |

## **02. SITUAÇÃO/REQUISITO**

Cliente solicita que a geração do registro 0450, no arquivo da rotina EFD Contribuições (SPED Pis/Cofins), seja semelhante a geração do registro 0450, no arquivo da rotina SPED Fiscal, com relação a mesma validação aplicada ao campo 2 (COD\_INF), do SPED Fiscal, agrupando a codificação quando o conteúdo for o mesmo.

## **03. SOLUÇÃO**

Dado que em um determinado período existem conteúdos das observações (campo complementar INFCOMPLDOCFISCAL)  iguais para diferentes lançamentos fiscais e/ou situações tributárias:  
Ao Gerar a EFD Contribuições, os Registros 0450 devem ser único por conteúdo (03-TXT)  e os C110 que possuam o mesmo conteúdo (03-TXT\_COMPL),  devem reutilizar o mesmo  02-COD\_INF que referencia o 0450.
