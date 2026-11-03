---
article_id: 360048954653
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 8c317ce4eeb38ed0deaaf4dc87d412f3163e92864c9165708727a476089705cd
fetched_at: '2026-06-28T22:42:27.999921+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Não foi possível gravar o(s) anexo(s)
  pois a(s) etapa(s) abaixo não estão cadastrada(s) no plano de ação
type: support-article
updated_at: '2024-10-22T18:35:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048954653-Manufatura-Linha-Protheus-SIGAQNC-N%C3%A3o-foi-poss%C3%ADvel-gravar-o-s-anexo-s-pois-a-s-etapa-s-abaixo-n%C3%A3o-est%C3%A3o-cadastrada-s-no-plano-de-a%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**No módulo **SIGAQNC - Controle de Não Conformidades**, ao tentar relacionar um documento anexo por meio da opção **Outras Ações/Doc. Anexo** na rotina **QNCA030 - Cadastro de Plano de Ação** é exibida a mensagem **Não foi possível gravar o(s) anexo(s) pois a(s) etapa(s) abaixo não estão cadastrada(s) no plano de ação**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Causa**A mensagem é exibida quando existe um modelo de etapa relacionado ao plano de ação no campo **Modelo/Grupo** da rotina **QNCA030**, e neste caso, no momento em que o anexo está sendo inserido, as etapas pré-definidas no modelo ainda não foram determinadas para qual usuário e prazo de execução.   
  
**Solução**Para solucionar essa ocorrência, é necessário definir qual a **Mat Usr Resp** e o **Prazo Execuc** em **Outras Ações/Acao/Etap** na rotina **QNCA030**.
