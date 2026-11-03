---
article_id: 11263312078231
category: RH - 13º salário
content_hash: 19a4bdaec2b09e97349cda77c2318048e6b0b7d75cea847e3e04a289a0befd9d
fetched_at: '2026-06-28T22:44:00.487838+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo dos encargos não são realizados na 2ª parcela
  do 13º salário
type: support-article
updated_at: '2025-08-20T13:50:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11263312078231-RH-Linha-Protheus-GPE-C%C3%A1lculo-dos-encargos-n%C3%A3o-s%C3%A3o-realizados-na-2%C2%AA-parcela-do-13%C2%BA-sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18897914655639) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Cálculo dos encargos não são realizados na 2ª parcela do 13º salário  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Causa**Incidência CP eSocial errada, informado indevidamente incidência 22 para verbas que não são de 13º maternidade.  
  
**Solução**Entre na rotina de **Verbas (GPEA040)**, pelo caminho **Atualizações > Definições de cálculos >Verbas (GPEA040)**, localize as verbas de provento de 13º calculadas no roteiro 132 - 2º parcela, e na aba eSocial, no campo **Cd. Inc. CP** informe a incidência correta:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11263261118743)  
  
A incidência 22 é **exclusiva** para 13º licença maternidade, onde quando informado 22, conforme SEI 16120, não é calculado os encargos sobre a verba.

**Saber Mais:**

[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
Essas **documentações** também podem ser acessadas através da **Carolina**, veja como acessar a assistente virtual, via **Protheus** ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>
