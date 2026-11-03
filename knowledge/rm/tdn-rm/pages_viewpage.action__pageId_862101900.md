---
content_hash: 18e6d3a8e8fe6d42d08f0baa0b06fa3b1880b31353de3df808c2d9c237aa3c6b
fetched_at: '2026-06-29T00:11:55.485731+00:00'
page_id: '862101900'
product: rm
source: tdn-rm
title: FISCAL01-23525 - NFSE - Número da Inscrição da obra (SP)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862101900
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Fiscal |
| Processo | NFS-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-23506 |

## **02. SITUAÇÃO/REQUISITO**

Ao enviar NFS-e prefeitura de São Paulo/SP não gera o Número da inscrição da obra.

## **03. SOLUÇÃO**

Remoção da regra que trazia o projeto vinculado ao item/nota apenas para Campinas e Salvador, agora vai trazer pra qualquer município.   
Adicionada verificação caso a lista de projetos retornada seja nula, mas haja cadastro do campo complementar de Inscrição Municipal da Obra.

Disponível à partir da biblioteca 12.1.2310
