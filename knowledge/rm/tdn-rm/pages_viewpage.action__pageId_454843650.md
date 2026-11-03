---
content_hash: 6fe14579be3eb009c3ee3bf4bb7a1a0d9d1175284b52648875085f37ed8f5b91
fetched_at: '2026-06-29T00:10:13.164340+00:00'
page_id: '454843650'
product: rm
source: tdn-rm
title: Processo Conversor Contribuição Sindical
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454843650
version: 7
---

falseATENÇÃO:

A partir da release **12.1.2606**, esta rotina foi descontinuada, pois sua funcionalidade passou a ser atendida pelo **eSocial**.

Este processo foi criado com o objetivo de converter as informações antes contidas na tela Dados Anuais da RAIS | eSocial. O processo está disponível em Configurações | Conversor Contribuição Sindical.

Na etapa "Parâmetros" temos os seguintes campos:

**'Mês'** vem com um valor default 1. É utilizado quando não tem registro na tabela  'PCONTRIBUICAOPATRONAL' que é associada a tabela pai 'PRAISPARSEC', pois nessa tabela teria as informações mensais da Contribuição Sindical e caso esses valores não existam, serão criados na tabela nova com o Mês padrão 1.

**'Sobrepor dados existentes'** serve para sobrepor os registros existentes. Caso tenha algum registro já gravado nas tabelas novas 'PCONTRIBUICAOSINDICAL' e 'PVALORCONTRIBUICAOSINDICAL' e o mesmo registro tenha nas tabelas antigas 'PRAISPARSEC' e 'PCONTRIBUICAOPATRONAL', os dados serão substituídos pelos antigos.

Observação

* Na tela 'Dados Anuais da RAIS | eSocial' ' era possível incluir as informações referentes a 'Contribuição Patronal' sendo que o campo 'Mês' era de preenchimento obrigatório. Dessa forma quando executado o processo se o Mês Padrão for diferente do Mês da tela de 'Contribuição Patronal' o valor gravado no final do processo é o existente da tela de  'Contribuição Patronal' .
* Na conversão será levado por padrão o parâmetro  "Enviar para RAIS" marcado, caso possua algum registro já marcado para esse ano o mesmo ficará desmarcado.

**Artigos relacionados**

* <https://tdn.totvs.com/pages/viewpage.action?pageId=452705168>
