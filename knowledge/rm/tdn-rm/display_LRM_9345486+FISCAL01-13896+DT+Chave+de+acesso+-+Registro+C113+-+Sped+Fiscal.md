---
content_hash: 126e114128270484d245fb131669565c93c64326357e09798c0cd1995eedb5e4
fetched_at: '2026-06-29T00:10:51.478464+00:00'
page_id: '568919849'
product: rm
source: tdn-rm
title: 9345486 FISCAL01-13896 DT Chave de acesso - Registro C113 - Sped Fiscal
type: documentation
url: https://tdn.totvs.com/display/LRM/9345486+FISCAL01-13896+DT+Chave+de+acesso+-+Registro+C113+-+Sped+Fiscal
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Sped Fiscal |
| Ticket: | 9345486 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13896 |

## **02. SITUAÇÃO/REQUISITO**

Cliente entrou em contato informando que ao gerar movimentos de emissão própria o campo 10 do registro C113 do Sped fiscal não é gerado o valor da chave de acesso.

## **03. SOLUÇÃO**

Implementado no Registro C113, o mesmo tratamento existente no Campo 09 - Chave de Acesso do Registro C100 - que é gerado com a chave preenchida no lançamento fiscal e caso não esteja preenchida é gerado com a chave da tabela TNFEESTADUAL
