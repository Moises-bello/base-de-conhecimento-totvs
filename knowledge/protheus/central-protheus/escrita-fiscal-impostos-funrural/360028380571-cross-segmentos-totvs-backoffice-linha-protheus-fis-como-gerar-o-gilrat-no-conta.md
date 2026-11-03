---
article_id: 360028380571
category: Escrita Fiscal - Impostos - Funrural
content_hash: 9743b42480839bd1a5d444b48af7ca4e912da3e9e4e45071acfe7b37c4685d03
fetched_at: '2026-06-28T22:39:28.111084+00:00'
product: protheus
section_id: 1500001549822
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como gerar o GILRAT
  no contas à pagar pelo pedido de venda.
type: support-article
updated_at: '2021-06-29T13:41:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028380571-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gerar-o-GILRAT-no-contas-%C3%A0-pagar-pelo-pedido-de-venda
---

**Dúvida**

Cliente precisa que o GILRAT seja de sua responsabilidade, como gerar o título no contas à pagar?  
  
**Ambiente**

Protheus – Faturamento – A partir da versão 11.80.  
  
**Solução**

Para que o cliente gere esse título no contas à pagar é necessário compreender a seguinte situação no cadastro do cliente:

Quando o cliente é **Pessoa Física** o campo Fisica/Jurid (A1\_PESSOA) = Será gerado automaticamente um título no **contas à pagar**, pois a responsabilidade sempre é da empresa.

1 - Quando o cliente é PJ e o campo Tipo (A1\_TIPO) = R (Revendedor) = Será gerado um título de abatimento no contas a receber;

2 - Quando o cliente é PJ e o campo Tipo (A1\_TIPO) = F (Consumidor final) = Será gerado um título no **contas à pagar;**

3- Quando o cliente é PJ e o campo TIPO (A1\_TIPO) = L (Produtor Rural) = Será gerado um título no **contas à pagar**.
