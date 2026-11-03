---
content_hash: 9b863f610622b4653f502c75d5e44a72de9362a3f615199d470653e40410d149
fetched_at: '2026-06-29T00:10:51.438068+00:00'
page_id: '567759464'
product: rm
source: tdn-rm
title: 9720327 FISCAL01-13970- DT Reinf CNO
type: documentation
url: https://tdn.totvs.com/display/LRM/9720327+FISCAL01-13970-+DT+Reinf+CNO
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | REINF |
| Ticket: | 9720327 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-13970 |

## **02. SITUAÇÃO/REQUISITO**

Alterar a geração dos eventos da Reinf para os registros R-2020 e R-2010. Antes o evento era gerado agrupando CPF/CNPJ, Cliente/Fornecedor e Código Nacional de Obra, ocasionando erro no envio da rotina caso tenha lançamentos fiscais com múltiplos Clientes/Fornecedores utilizando mesmo código CNO,

## **03. SOLUÇÃO**

O sistema irá agrupar baseado no código CNO:

* Caso o código CNO esteja preenchido o agrupamento é realizado por Código CGC e Código CNO;
* Caso o código CNO não esteja preenchido o agrupamento é realizado por Código CGC, Código da Coligada do Cliente/Fornecedor e Código do Cliente/Fornecedor.
