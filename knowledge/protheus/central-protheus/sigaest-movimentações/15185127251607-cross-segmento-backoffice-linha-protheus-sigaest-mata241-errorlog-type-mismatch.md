---
article_id: 15185127251607
category: SIGAEST - MOVIMENTAÇÕES
content_hash: cccc92c83983e6a48270d85a62b390ddac99a32fee531d58a04379b6fb9fc42c
fetched_at: '2026-06-28T22:38:56.950611+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA241 - Error.log
  type mismatch on .AND.  on MAAVALPERM(MATXALC.PRX)
type: support-article
updated_at: '2023-06-09T14:16:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15185127251607-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA241-Error-log-type-mismatch-on-AND-on-MAAVALPERM-MATXALC-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15185107710359) Tempo aproximado para leitura: **00:02:11 min****Ocorrência**

Ao tentar estornar uma Movimentação Interna Múltipla (MATA241) é exibido o error.log**: "***type mismatch on .AND. on MAAVALPERM(MATXALC.PRX)***"**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**Este erro é causado por conta do tipo do Parâmetro MV\_RESTTM estar configurado com tipo Caractere. O padrão deste parâmetro é ser do tipo Lógico.

**Solução**Acesse ao Configurador ou APSDU e altere o tipo do Parâmetro de Caractere (C) para Lógico (L). Abaixo imagem dele no seu tipo padrão:

![](https://totvssuporte.zendesk.com/attachments/token/5N06QaE7ol7IFcdplv16U6bT6/?name=image.png)

Após essa alteração, o problema tende a não ocorrer mais. Caso persista, sugerimos acionar à nossa equipe de Suporte evidenciando a data do fonte e print do parâmetro em questão.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
