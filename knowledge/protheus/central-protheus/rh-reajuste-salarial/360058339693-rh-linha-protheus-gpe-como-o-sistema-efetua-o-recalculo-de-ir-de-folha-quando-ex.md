---
article_id: 360058339693
category: RH - Reajuste Salarial
content_hash: e57b3d7c84ce31711cd6a57e389111d892279ec651f8a77d39d73f542886fd81
fetched_at: '2026-06-28T22:43:15.896990+00:00'
product: protheus
section_id: 360010855214
source: central-protheus
title: RH - Linha Protheus - GPE - Como o sistema efetua o recalculo de IR de folha
  quando existe férias e reajuste salarial
type: support-article
updated_at: '2025-09-15T11:49:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058339693-RH-Linha-Protheus-GPE-Como-o-sistema-efetua-o-recalculo-de-IR-de-folha-quando-existe-f%C3%A9rias-e-reajuste-salarial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26410956273175) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como o sistema efetua o recalculo de IR de folha quando existe férias e reajuste salarial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Quando existe férias no cálculo da folha, o sistema efetua um recalculo das verbas de férias. 

**Segue exemplo pra entendimento:**

**Calculo de férias - Inicio 04/09/24 a 23/09/24 - Pagamento em 02/09/24  
Reajuste Salarial após o calculo das férias**

Soma das verbas de diferença de férias = 221,06 + 105,71 + 8,05 + 2,13 + 66,32 + 22,10 = R$ 425,37 **(verba A21- Base Ir férias Diferença (ID 0100)**  
O sistema então recalcula somando a base de Ir férias **(A07 - ID 0016)+ base de IR diferença (A21 - ID 0100)**  
6.082,40+ 425,37 = R$ 6.507,77\* 27.5% = 1.789,63 - 896,00 (dedução legal) = R$ 893,63 - 776,66 (518 - ID 0067) = **R$ 116,97 (523 - ID 0101)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26410956276887)

**OBS**. A base de IR deve ser calculada separadamente da Base de IR Folha, bem como a dedução do INSS.   
<https://tdn.totvs.com/pages/releaseview.action?pageId=152800518>

O sistema só gera a diferença de IR, se as férias e a diferença forem pagas no mesmo período de apuração Ex: férias pagas em 02/09 com desconto de IR, com reajuste salarial na folha de 09/2024 paga em 30/09/2024.

**Saiba mais:**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
