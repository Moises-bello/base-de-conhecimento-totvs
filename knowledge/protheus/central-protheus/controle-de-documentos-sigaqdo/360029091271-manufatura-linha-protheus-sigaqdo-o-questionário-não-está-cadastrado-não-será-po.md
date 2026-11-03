---
article_id: 360029091271
category: Controle de Documentos (SIGAQDO)
content_hash: e8abeae47c9a3e2d906ab4ece097ab81b749efe2167709fe67fa706c42a8b4a7
fetched_at: '2026-06-28T22:42:29.210586+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - O questionário não está cadastrado.
  Não será possível realizar a distribuição
type: support-article
updated_at: '2021-05-26T11:59:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029091271-Manufatura-Linha-Protheus-SIGAQDO-O-question%C3%A1rio-n%C3%A3o-est%C3%A1-cadastrado-N%C3%A3o-ser%C3%A1-poss%C3%ADvel-realizar-a-distribui%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Na rotina **QDOA050- Cadastro de Documentos** ao distribuir um documento é exibida a mensagem **O questionário não está cadastrado. Não será possível realizar a distribuição.**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**Essa mensagem é apresentada porque na rotina **QDOA050**, o campo **Real. Quest.** está preenchido como **Sim**.  
  
**Solução**Para que a mensagem não seja apresentada é necessário cadastrar um questionário na rotina **QAXA050 - Questionários**. Desta forma, será feito o vínculo do documento com um questionário que será apresentado para preenchimento no momento da baixa da pendência de leitura do documento. Em geral, este questionário é aplicado para confirmar que o usuário leu e entendeu o documento.  
  
**Importante**  
Para que não seja obrigatório vincular questionários, altere o parâmetro **MV\_QAQUEST - Define se Inclui / Responde Questionario** para **N**.
