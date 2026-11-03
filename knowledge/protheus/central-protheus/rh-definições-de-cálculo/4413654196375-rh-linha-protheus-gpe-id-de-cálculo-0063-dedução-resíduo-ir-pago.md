---
article_id: 4413654196375
category: RH - Definições de Cálculo
content_hash: 6c65173fdece6f0cc952d1ba5202f5025a9597243df1631204bebae035f26f09
fetched_at: '2026-06-28T22:43:22.241282+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE -  ID de cálculo 0063 (Dedução Resíduo IR Pago)
type: support-article
updated_at: '2026-06-26T16:39:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413654196375-RH-Linha-Protheus-GPE-ID-de-c%C3%A1lculo-0063-Dedu%C3%A7%C3%A3o-Res%C3%ADduo-IR-Pago
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31648335656471) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Qual a funcionalidade do ID de cálculo **0063** (Dedução Resíduo IR Pago)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Este ID é gerado em situações onde a empresa possui pagamento em **regime caixa** e no cálculo do **adiantamento** há uma redução na base de IR, ou seja, **ocorre devolução do valor de IR que foi descontado na Folha referente período anterior.**  
  
**Exemplo**:  
**>** Empresa **regime caixa**Na Folha de Pagamento de Janeiro/2020 com data de pagamento em 05/02/2020, o Funcionário tinha somente um dependente, houve o desconto do IR no valor de R$ 64,79 no ID 0066.  
No Adiantamento Salarial de Fevereiro com data de pagamento 20/02/2020, a empresa cadastrou mais dependentes para o Funcionário, onde ele passou de um para quatro dependentes.  
Este Funcionário iniciou Férias em Fevereiro e recebeu o Adiantamento proporcional aos dias trabalhados, pois o parâmetro **MV\_ADTOPRO** está com **S,** portanto, no roteiro ADI com data de pagamento 20/02/2020, ele recebeu R$ 400,00.  
  
O sistema entende que o Funcionário neste caso, teve um **desconto de IR indevido** no valor de R$ 64,79, pois o correto seria um desconto de R$ 52,08 no Adiantamento.  
A rotina recalcula e devolve o valor de R$ 12,71 como provento, sendo o líquido de Adiantamento (ID 0546), a soma da devolução do IR + o valor do Adiantamento.  
  
  
  
**Saiba Mais:**  
[RH - Linha Protheus - GPE - Como calcular Adiantamento Salarial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007489951-RH-Linha-Protheus-GPE-Como-calcular-adiantamento-salarial)
