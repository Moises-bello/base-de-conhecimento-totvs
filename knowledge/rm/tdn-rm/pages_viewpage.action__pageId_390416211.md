---
content_hash: e3a847296d8ae5cd16d8640a17fc72c74ffe43904988a12dc3aa697a211022b0
fetched_at: '2026-06-29T00:09:09.029079+00:00'
page_id: '390416211'
product: rm
source: tdn-rm
title: 3527627 FOPCALCULO01-4459 Salário Composto via dataserver
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=390416211
version: 1
---

# Salário Composto

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Salário Composto |
| **Situação/Requisito:** | Ao utilizar o método 'SaveRecord' para inserir informações de salário composto no Data Server 'FopSalCompostoData' é apresentada a mensagem de erro: 'Você não está autorizado a inserir registros'. |
| **Solução/Implementação:** | No TOTVS Folha de Pagamento foi identificado que ao utilizar o dataserver "FopSalCompostoData" através do webservice, o mesmo retorna um erro informando que não é possível inserir registros. Foi identificado uma inconsistência na permissão. Foi feito a alteração |
| **Tickets relacionados:** | 3527627 |
