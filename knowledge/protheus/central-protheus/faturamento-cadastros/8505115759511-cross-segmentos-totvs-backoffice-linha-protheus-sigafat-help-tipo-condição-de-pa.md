---
article_id: 8505115759511
category: Faturamento - Cadastros
content_hash: 88c558087281be87c5d63d09aea4afe938bcdfe7f93689c6df77c7b0fc66ab2e
fetched_at: '2026-06-28T22:38:35.529616+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help Tipo (Condição
  de Pagamento)
type: support-article
updated_at: '2022-08-29T19:29:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8505115759511-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-Tipo-Condi%C3%A7%C3%A3o-de-Pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao tentar incluir uma condição de pagamento tipo 7, apresenta o Help Tipo - Tipo de condição de pagamento, são validos os seguinte tipo: ....

![help_tipo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8505027125911/help_tipo.png)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - Todas as versões  
  
**Causa**  
Existe uma validação de usuário no campo **E4\_TIPO**.  
  
**Solução**O campo **E4\_TIPO**esta com uma validação de usuário que não permite o uso da condição tipo 7, no padrão a validação é necessária e permite a inclusão da condição.  
  
Orientamos que inclua a tipo 7 na mensagem, ou retire a validação de usuário caso não utilize em customizações a informação.

![padrao.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8505072525591/padrao.png)
