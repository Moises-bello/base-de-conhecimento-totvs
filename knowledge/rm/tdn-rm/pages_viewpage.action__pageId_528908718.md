---
content_hash: 65646d3951e68a3620eddd2ef62e213263acd0ca3d2a8ae4e0b7b57f8fa9922a
fetched_at: '2026-06-29T00:10:35.362669+00:00'
page_id: '528908718'
product: rm
source: tdn-rm
title: FISCAL01-11275 DT Parâmetros TSS Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=528908718
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Transmissão de Eventos Reinf |
| Ticket: | - |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11275 |

## **02. SITUAÇÃO/REQUISITO**

Passa-se a utilizar os parâmetros de certificado e webservice do TSS nos parâmetros do Fiscal ao invés dos parâmetros da NF-e

## **03. SOLUÇÃO**

Dado que o sistema está parametrizado com webservice do TSS e certificados válidos no TOTVS Gestão Fiscal - Integração TSS  
E ainda que a parametrização de NF-e para certificado e webservice estejam inválidas,  
Ao enviar ou consultar um evento da Reinf pelo RM  
Então, o sistema deve realizar a transmissão e consulta sem problemas técnicos.
