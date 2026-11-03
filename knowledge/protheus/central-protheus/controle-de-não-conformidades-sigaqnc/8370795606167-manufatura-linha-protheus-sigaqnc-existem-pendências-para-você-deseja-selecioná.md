---
article_id: 8370795606167
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 561a95e443c8f4e8656aa5dd0be6e3b418ce206ef90c142e6a1f2d3f9ecf8610
fetched_at: '2026-06-28T22:42:27.941611+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Existem pendências para você. Deseja
  selecioná-las agora
type: support-article
updated_at: '2022-08-23T17:58:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8370795606167-Manufatura-Linha-Protheus-SIGAQNC-Existem-pend%C3%AAncias-para-voc%C3%AA-Deseja-selecion%C3%A1-las-agora
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao acessar o módulo **SIGAQNC - Controle de Não Conformidades** é exibida a mensagem **Existem pendências para você. Deseja selecioná-las agora?**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Causa**Esta mensagem é exibida quando o parâmetro **MV\_QNCPERG - Habilita pergunta de pendências para o usuário ao se logar no QNC** está com o conteúdo igual à **1-Habilita** e neste caso, ao responder **Sim** à esta pergunta é aberta a rotina **QNCA050 - Pendências** para que seja possível realizar a baixa das pendências.  
  
**Solução**Para que a mensagem não seja exibida, o conteúdo do parâmetro **MV\_QNCPERG** deve ser alterado para **2-Desabilita**.  
  
**Importante**  
A alteração deste parâmetro impacta para todos os usuários, ou seja, desativando o parâmetro, a mensagem não será mais exibida para nenhum usuário.
