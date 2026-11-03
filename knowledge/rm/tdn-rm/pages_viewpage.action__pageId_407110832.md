---
content_hash: 1e0fb3973fb90031d351014acb322269060e9406b2c12f6eedd7909cf558269a
fetched_at: '2026-06-29T00:09:11.510443+00:00'
page_id: '407110832'
product: rm
source: tdn-rm
title: 2982306 FOPCALCULO01-3844 Cálculo Folha - Interseção de Afastamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=407110832
version: 1
---

# Cálculo da Folha

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Funcionários | Envelope de Pagamento | Recalculo |
| **Situação/Requisito:** | Cliente lançou o grupo de eventos de folha para o empregado, mas o evento com o CC 1 (horas trabalhadas) apresenta erro: “Já foi adicionado um item com a mesma chave”. |
| **Solução/Implementação:** | No TOTVS Folha de Pagamento foi identificado que para um funcionário específico o sistema não consegue lançar um grupo de eventos pois informa que já foi adicionado um item com a mesma chave. Foi identificado que a situação ocorre pois o funcionário em questão tem dois afastamentos do mesmo tipo e motivo em que a data fim dos afastamentos são iguais, assim gerando um erro de duplicação de chave, foi feito um ajuste para que caso esta situação ocorra o sistema alerte para a impossibilidade de executar o processo e para o ajuste das datas finais dos afastamentos. |
| **Tickets relacionados:** | 2982306 |
