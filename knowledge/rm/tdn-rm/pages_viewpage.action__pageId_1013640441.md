---
content_hash: 76a942dc2437253c0984bda4aa35f15ab24f96dfe426fd94e5470387675d2eef
fetched_at: '2026-06-29T00:05:47.420361+00:00'
page_id: '1013640441'
product: rm
source: tdn-rm
title: 'Regras:'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1013640441
version: 4
---

Abaixo algumas regras para entendimento junto a integração do RM com o Suricato .

1- **Cadastro de Seção X Centro de Custo**

Para que o código do centro de custo do funcionário seja enviado na  integração e demonstrado no Log,  deverá ser preenchido no cadastro de seção em Dados contábeis o número do Centro de Custo . 

2-  **Rescisão X TSA**

Ao cadastrar uma rescisão a informação da data de demissão não é replicada para o suricato, quando essa data é em competência futura. A situação do funcionário permanecerá ativo.  
Conforme regra o funcionário deverá estar como ativo até a data. Maiores informações veja em: [Rescisão X TSA](https://tdn.totvs.com/pages/viewpage.action?pageId=223182523)
