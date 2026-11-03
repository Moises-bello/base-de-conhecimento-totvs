---
content_hash: 08f81d159492ef6464313ef631d217353a6206a34b4a1e7cc990c596d98b9b76
fetched_at: '2026-06-29T00:10:56.719785+00:00'
page_id: '592754444'
product: rm
source: tdn-rm
title: 10261117 - FISCAL01-14737 -  Sped Fiscal - Preencher a série com zeros à esquerda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=592754444
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | SPED FISCAL |
| Ticket: | 10261117 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14737 |

## **02. SITUAÇÃO/REQUISITO**

Cliente gera o arquivo, ao realizar a conferência da série utilizada, no arquivo TXT foi verificado que serie para o tipo de documento 55 (NF-e) foi gerado com apenas 1 dígito quando o correto seria 3 dígitos.

## **03. SOLUÇÃO**

Foi realizada melhoria para que o campo série seja completado com zeros a esquerda, quando necessário no arquivo SPED FISCAL, tratamento realizado para os registros C100 e D100.
