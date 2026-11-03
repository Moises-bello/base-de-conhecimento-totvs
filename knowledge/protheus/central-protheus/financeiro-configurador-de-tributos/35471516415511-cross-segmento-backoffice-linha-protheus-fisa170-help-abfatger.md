---
article_id: 35471516415511
category: Financeiro - Configurador de Tributos
content_hash: 619083a1f32a9aad05b6a0aae5cba26e591a1df767741c74f38e0ff55df922ee
fetched_at: '2026-06-28T22:37:45.780376+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - FISA170 - Help: ABFATGER'
type: support-article
updated_at: '2025-10-07T18:43:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35471516415511-Cross-Segmento-Backoffice-Linha-Protheus-FISA170-Help-ABFATGER
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35471516397463) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Ao incluir uma regra financeira, é exibido o **Help: ABFATGER**. Problema: Não é possível vincular/amarrar uma regra financeira de abatimento a uma regra com fator gerador caixa.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210  
  
**Solução**  
Ao incluir uma regra financeira por meio do configurador de tributos para a geração do imposto no **Contas a Receber** durante a baixa, o campo **TP. Movto. (Tipo de Movimento)** da regra de título deve ser preenchido com a opção **2 – Impostos**. Essa configuração é necessária para que, ao selecionar o **Fato Gerador (2 – Caixa)** na regra financeira, o sistema não exiba a mensagem de Help.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35471516398999)

**Saiba mais**

[Financeiro - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)
