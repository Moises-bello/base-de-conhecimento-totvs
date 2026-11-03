---
article_id: 37999004930583
category: Financeiro - Contas a Receber
content_hash: e53accaeda91ffaf3699017d5d2c96da8827bea5ef21bbea6b6d040db4eb760f
fetched_at: '2026-06-28T22:38:12.535882+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Quando o cliente realiza
  o pagamento via depósito ao invés do pagamento do boleto. O que fazer
type: support-article
updated_at: '2026-01-28T18:38:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37999004930583-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Quando-o-cliente-realiza-o-pagamento-via-dep%C3%B3sito-ao-inv%C3%A9s-do-pagamento-do-boleto-O-que-fazer
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37999004907671) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Quando o cliente realiza o pagamento via depósito ao invés do pagamento do boleto. O que fazer para realizar a baixa do título sem gerar movimentação?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FINA040 - Todas as versões.  
  
**Solução**  
No cenário apresentado, o depósito efetuado não possui vínculo direto com o título a receber, o que inviabiliza a compensação entre o título e a movimentação bancária correspondente.

Para o tratamento da situação dentro do padrão operacional do Protheus, recomenda-se a realização da baixa do título por meio do motivo de baixa **“DACAO”**, o qual não gera movimentação bancária.

Esse procedimento permite a liquidação do título sem a geração de nova movimentação bancária, evitando duplicidades e garantindo a consistência do saldo bancário.
