---
article_id: 360049503733
category: RH - Folha de Pagamento
content_hash: 0fc3c81ac05d7dec267ae1e1f8970f9dda9d4bcb30e24ce3b97e41ce120d348a
fetched_at: '2026-06-28T22:44:13.170559+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular o DSR HE mensalista sempre sobre
  30 dias independente da quantidade dos dias do mês
type: support-article
updated_at: '2024-09-12T21:44:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049503733-RH-Linha-Protheus-GPE-Como-calcular-o-DSR-HE-mensalista-sempre-sobre-30-dias-independente-da-quantidade-dos-dias-do-m%C3%AAs
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26337353409815) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Como fazer com que o cálculo do DSR de HE  e DSR adicional noturno para mensalistas na folha seja sempre sobre 30 dias independente da quantidade de dias do mês?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para que o cálculo de DSR de horas extras para mensalistas seja sempre calculado sobre 30 dias, é necessário que o parâmetro **MV\_TPCALEN** fique com 2, assim o Cadastro de Calendário será montado sinteticamente e o sistema permitirá manipular a quantidade de dias uteis e DSR diretamente nos campos abaixo:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26337325404055)  
  
**IMPORTANTE:**   
1. Quando parâmetro MV\_TPCALEN esta com 2, o sistema não calcula o DSR proporcional em admissões, férias, rescisões e afastamentos, pois não tem um calendário analítico para fazer essa verificação.

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
