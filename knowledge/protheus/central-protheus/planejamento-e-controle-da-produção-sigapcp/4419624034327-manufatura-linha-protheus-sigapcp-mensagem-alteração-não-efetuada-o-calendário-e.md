---
article_id: 4419624034327
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 1841684523bad87b58197af735d933874866b4efaccb0eb2e2bd9769a70d7062
fetched_at: '2026-06-28T22:42:44.423416+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem Alteração Não Efetuada, o
  calendário escolhido está sendo usado por um projeto, tarefa ou recurso.
type: support-article
updated_at: '2022-01-20T10:43:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419624034327-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-Altera%C3%A7%C3%A3o-N%C3%A3o-Efetuada-o-calend%C3%A1rio-escolhido-est%C3%A1-sendo-usado-por-um-projeto-tarefa-ou-recurso
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:55 min****Ocorrência**Ao tentar gravar uma alteração de calendário no **MATA780 - Cadastro de Calendários**, o usuário recebe a mensagem **Alteração Não Efetuada, o calendário escolhido está sendo usado por um projeto, tarefa ou recurso**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa mensagem é apresentada quando o Sistema encontra algum registro na tabela **AF8 - Projetos** contendo no campo **AF8\_CALEND - Calendário Utilizado** o calendário que se pretende alterar.   
  
**Solução**Para permitir a alteração mesmo tendo um projeto vinculado ao calendário, deve-se alterar o parâmetro **MV\_ALTCLD - Permite a alteração de cadastro de calendários em uso** para **.T.**. Com este conteúdo o Sistema irá alertar o usuário de que o calendário está vinculado a projeto, mas permitirá a alteração do calendário.
