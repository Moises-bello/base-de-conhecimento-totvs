---
content_hash: 21122654dee8175d6db582853359f1b1d80073173d17d7872594d0cb968b50be
fetched_at: '2026-06-29T00:11:03.471358+00:00'
page_id: '623874405'
product: rm
source: tdn-rm
title: 11627224 FISCAL01-15780 DT Evento R-2055 - Referência de objeto não definida
  para uma instância de um objeto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=623874405
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | REINF |
| País: | Brasil |
| Ticket: | 11627224 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15780 |

## **02. SITUAÇÃO/REQUISITO**

     Ao gerar o evento R-2055 de uma entrada com o Tipo Emitente Empresa é apresentada uma inconsistência genérica:

     “Referência de objeto não definida para uma instância de um objeto. ”

## **03. SOLUÇÃO**

Ajustada a geração do Evento R-2055 para buscar os dados do fornecedor origem/destino quando   
o Lançamento estiver parametrizado desta forma e não gerar o Evento da Reinf quando não tiver cnpj/cpf   
vinculado ao cliente/fornecedor
