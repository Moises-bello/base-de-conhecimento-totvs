---
content_hash: 20df10e53cba128cb1efa20ece507cb14a021ad43565fd44304fa58211f7107f
fetched_at: '2026-06-29T00:09:52.289935+00:00'
page_id: '438288814'
product: rm
source: tdn-rm
title: DT Serviço para retorno do valor do ISS para E-Social
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=438288814
version: 1
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Serviço para retorno do valor do ISS para E-Social |
| **Situação/Requisito:** | Deve ser elaborada evolução do parametrizador do Financeiro, de modo que seja possível determinar o(s) valor(es) opcional(is) do Financeiro que correspondem ao Valor do ISS para o pagamento a Autônomo.  Hoje a equipe do RH busca dados do Autônomo no Financeiro por meio de sentença SQL. A partir do momento que o valor do ISS será definido por parâmetro, passaremos a passar as informações para o RH através de um serviço.  A equipe do RH se prontificou a disponibilizar um recurso para ajudar na definição do serviço.. |
| **Solução/Implementação:** | Foi disponibilizados os seguintes serviços:   * ObterAutonomosFluxusPagtoPeriodo: Retorna os clientes/fornecedores de RPA * ObterValoresPagtoAutonomoFluxus: Retorna os valores dos lançamentos do autonomo agrupados por filial/baixa |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-9486> |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
