---
article_id: 4411789631127
category: Escrita Fiscal - CIAP
content_hash: 0f898f52641360cfc58b088adb7022b06352ac0953ae34933f76d50f1122ec04
fetched_at: '2026-06-28T22:39:33.985289+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Qual é o critério
  para preenchimento do FA_TIPO e FA_MOTIVO?
type: support-article
updated_at: '2021-10-29T20:04:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411789631127-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Qual-%C3%A9-o-crit%C3%A9rio-para-preenchimento-do-FA-TIPO-e-FA-MOTIVO
---

**Dúvida**

Qual é o critério para preenchimento do FA\_TIPO e FA\_MOTIVO?

**Ambiente**Protheus – Fiscal – A partir da versão 11.80  
  
**Solução**

Os campos FA\_TIPO e FA\_MOTIVO são preenchidos automaticamente pelo sistema conforme o processo realizado, exemplo:

FA\_TIPO = 1 (Apropriação Mensal) gera mensalmente esta informação.

Agora o critério do FA\_MOTIVO é por exemplo uma baixa por perda, devolução, saída, transferência.

Quando faço uma baixa no item por saída/perda, o FA\_TIPO recebe  = 2 e o FA\_MOTIVO = 3 (opção do MATA906, ações relacionadas - Baixar)
