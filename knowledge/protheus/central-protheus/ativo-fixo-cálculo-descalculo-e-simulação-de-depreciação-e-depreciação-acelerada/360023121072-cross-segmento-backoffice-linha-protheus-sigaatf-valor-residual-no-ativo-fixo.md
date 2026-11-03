---
article_id: 360023121072
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: b545c843d3b49a028655224e8a0149a00e5d21d0b46c2d5ab5c0db49a376956f
fetched_at: '2026-06-28T22:41:43.233438+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF -  VALOR RESIDUAL NO ATIVO
  FIXO
type: support-article
updated_at: '2022-11-28T19:48:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023121072-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-VALOR-RESIDUAL-NO-ATIVO-FIXO
---

**Dúvida**ONDE INFORMAR VALOR RESIDUAL NO ATIVO FIXO?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo A partir da versão 12  
  
  
**Solução:**

Na inclusão do bem,  rotina de cadastro de ativo (ATFA012):

Campo N3\_VORIG1 -> Informar o valor original do bem (aquisição)

Campo N3\_VRDACM1 -> Informar o valor que o bem já sofreu depreciação (depreciação acumulada).

Para o tipo de depreciação linear o sistema considera como valor residual o Valor Original - depreciação Acumulada.

Por esse motivo, não temos um campo, especifico, para valor residual.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021139231/mceclip0.png)

Obs. O Campo de Depreciação acumulada está disponível para preenchimento somente na inclusão do Bem.

Saiba Mais

* [ATFA230 - É possível incluir taxa em um bem já classificado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020378972-MP-SIGAATF-ATFA230-%C3%89-poss%C3%ADvel-incluir-taxa-em-um-bem-j%C3%A1-classificado?source=search)
* [ALTERAÇÃO DA TAXA DE DEPRECIAÇÃO - ATFA230](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009750972-MP-SIGAATF-ALTERA%C3%87%C3%83O-DA-TAXA-DE-DEPRECIA%C3%87%C3%83O-ATFA230?source=search)
