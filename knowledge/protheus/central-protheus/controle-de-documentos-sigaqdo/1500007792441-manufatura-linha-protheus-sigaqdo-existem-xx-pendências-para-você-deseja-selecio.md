---
article_id: 1500007792441
category: Controle de Documentos (SIGAQDO)
content_hash: 5d30c6072a2f9e3ec3fcb62d1ed165fe759774a31b2a780c01b0deb101cd4291
fetched_at: '2026-06-28T22:42:29.074824+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Existem xx Pendências para você. Deseja
  Selecioná-las agora
type: support-article
updated_at: '2021-05-06T12:58:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007792441-Manufatura-Linha-Protheus-SIGAQDO-Existem-xx-Pend%C3%AAncias-para-voc%C3%AA-Deseja-Selecion%C3%A1-las-agora
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**No módulo **SIGAQDO - Controle de Documentos**, ao acessar a rotina **QDOA030 - Pendências** é exibida a mensagem **Existem XX Pendências para você. Deseja Selecioná-las agora?**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**A mensagem sempre será exibida quando o usuário possuir pendências, ou seja, quando o campo **QD1\_PENDEN - Pendência** for igual à **P-Pendente** e acessar qualquer rotina do módulo **24 - Controle de Documentos** e não somente ao acessar a rotina **QDOA030**.  
  
**Solução**Não existe parâmetro ou **PE - Ponte de Entrada** que iniba a exibição desta mensagem.  
Para que a mensagem não seja mais exibida é necessário efetuar a baixa de todas as pendências do usuário em questão por meio da rotina **QDOA030**.
