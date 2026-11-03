---
article_id: 360025854552
category: RH - Folha de Pagamento
content_hash: de77b46410374300e094bad419b5fe08bbd38aaae45713a30cd7ce092eddfff5
fetched_at: '2026-06-28T22:44:16.134892+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Pagamento de Comissão no Adiantamento
type: support-article
updated_at: '2025-08-12T12:45:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025854552-RH-Linha-Protheus-GPE-Pagamento-de-Comiss%C3%A3o-no-Adiantamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26334284210455) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como deve ser realizado o pagamento da comissão no Adiantamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O pagamento da comissão no adiantamento deve ser realizado na mesma verba de Adiantamento (ID 0006), pois se calculado na mesma verba de comissão, acarretará problemas futuros na DIRF e eSocial:

1. O valor do adiantamento em si é de R$ 1.200,00, porém será pago mais R$ 1.300,00 de comissão no adiantamento, portanto, lancei um valor de R$ 2.500,00 na verba de ID 0006 no roteiro ADI, abaixo cálculo da adiantamento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025255331)  
  
2. Ao fazer o fechamento do roteiro ADI, a verba Desconto de Adiantamento (ID 0007) foi carregada automaticamente para a tabela RGB (Lançamentos por Funcionários), e foi necessário realizar o lançamento da verba de comissão (verba 179 no meu teste), pois no desconto do adiantamento consta o valor pago da comissão no roteiro ADI:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025236072)  
  
3. No cálculo da folha foi apresentada somente uma verba de desconto de adiantamento e o valor da folha ficou correto:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025236252)

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
