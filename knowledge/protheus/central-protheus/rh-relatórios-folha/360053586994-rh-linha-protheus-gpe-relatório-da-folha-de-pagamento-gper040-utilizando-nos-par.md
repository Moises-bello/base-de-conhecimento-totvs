---
article_id: 360053586994
category: RH - Relatórios Folha
content_hash: 54a7c166b3aa5e059af1fc3b8e28b9364850f79f19a943d00452529aa675e8af
fetched_at: '2026-06-28T22:43:17.573175+00:00'
product: protheus
section_id: 360010843854
source: central-protheus
title: RH - Linha Protheus - GPE - Relatório da folha de pagamento (GPER040) utilizando
  nos parâmetros, numero de pagamento = 99
type: support-article
updated_at: '2024-08-26T14:19:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053586994-RH-Linha-Protheus-GPE-Relat%C3%B3rio-da-folha-de-pagamento-GPER040-utilizando-nos-par%C3%A2metros-numero-de-pagamento-99
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25909123412247) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao calcular a folha de pagamento de um autônomo com números de pagamento diferentes (por exemplo: número de pagamento 04 e outro com número de pagamento 05), ao emitir a folha de pagamento com o número de pagamento 99, a verba base de IR, ID 0015, soma a base de IR da semana 04 e 05.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**O sistema irá somar o valor total, considerando também o acumulado dos pagamentos anteriores do mesmo período.   
Não há tratamento específico para a base do IR na semana 99 no relatório da folha. Exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089540874)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089540994)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089541094)  
O sistema soma a base de IR da semana 04 R$ 752,30 + base IR semana 05 R$ 1576,47 = R$ 2.328,77

Para executar a conferência do Imposto de Renda, utilize o relatório da DARF (GPER050).

**Saiba mais:**

[RH - Relatórios Folha](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010843854-RH-Relat%C3%B3rios-Folha)
