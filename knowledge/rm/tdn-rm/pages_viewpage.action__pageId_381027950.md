---
content_hash: 7132f69d6b43b183a2bcd53b6d5e0ada50e7583e59059db81fafaf5c5ed65806
fetched_at: '2026-06-29T00:09:02.870546+00:00'
page_id: '381027950'
product: rm
source: tdn-rm
title: 2401160 FINANCEIRO01-5760 DT Após realizar a baixa parcial de um lançamento
  com boleto, o sistema está gerando um novo boleto com valor zerado.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=381027950
version: 1
---

# Inconsistência na baixa parcial de boletos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Baixa de Lançamentos / Boletos |
| **Situação/Requisito:** | Após realizar a baixa parcial de um lançamento com boleto, o sistema está gerando um novo boleto com seu valor zerado. Somente após a geração de código de barras é que o valor é preenchido, porém com o valor original do lançamento. |
| **Solução/Implementação:** | Melhoria na baixa de boletos provenientes do Educacional. Após baixa parcial, o sistema irá gerar um novo boleto com o valor restante do lançamento. |
| **Tickets relacionados:** | 2401160 |
| **Requisito:** | FIN.038 |
