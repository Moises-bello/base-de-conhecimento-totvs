---
article_id: 41266840652823
category: Financeiro - Viagens
content_hash: 6aa9f811b9bd23f1b3641c62322a1bc36daf75f83ca065571c9e3256e66ebfa3
fetched_at: '2026-06-28T22:38:21.258819+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA666 - Ajuste manual
  do campo de valor do adiantamento (FW5_VALOR)
type: support-article
updated_at: '2026-06-16T17:57:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41266840652823-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA666-Ajuste-manual-do-campo-de-valor-do-adiantamento-FW5-VALOR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41266848767255) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Quando é possível inserir valor manualmente no adiantamento?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

O adiantamento liberado para ajuste manual no valor, seria somente na rotina de viagens **FINA665**, mas neste caso não deve configurar valores no **Wizard da rotina FINA691**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41266848773399)

Na inclusão da solicitação de viagem, não pode ser marcado a opção adiantamento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41266840640023)

Caso deixe conforme exemplo acima, na rotina de viagens **FINA665, irá ser liberado a inclusão de adiantamento de qualquer valor.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41266840640919)

Mas caso deseje deixar um valor fixo, é preciso definir na rotina **FINA691**, localizado no primeiro print desta documentação. Na rotina **FINA666**, no momento só é possível definir um valor fixo para o adiantamento e limitações quantidades por dia.

Saiba mais: [Viagens - Financeiro - P12](https://tdn.totvs.com/display/public/PROT/Viagens+-+Financeiro+-+P12)
