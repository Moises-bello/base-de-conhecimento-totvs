---
content_hash: b0d5446a0ca5e29871ff03a98bd5a5d5f953088871a16937048f9847f18a4018
fetched_at: '2026-06-29T00:09:52.939061+00:00'
page_id: '439702965'
product: rm
source: tdn-rm
title: 658862 FOPCALCULO01-140 Contribuição Sindical
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=439702965
version: 1
---

# Contribuição Sindical

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Plataforma RM |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Contribuição Sindical |
| **Situação/Requisito:** | Caso o funcionário tenha desconto de Diferença De Contribuição Sindical em Fevereiro com data de pagamento em Março (Exemplo 06/03) e gerado um histórico de Contribuição Sindical, o sistema não  gera o evento de Desconto de Contribuição Sindical do ano atual. ( Código de Cálculo 0012 no processo de lançamento da folha de Pagamento) |
| **Solução/Implementação:** | Criado o campo Diferença de contribuição Sindical que identifica se o registro do histórico está relacionado ou não a um evento de diferença. Desta forma não impede que o sistema lance o evento de desconto quando tem o evento de diferença no mesmo caixa. |
| **Tickets relacionados:** | 658662 |
