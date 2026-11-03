---
article_id: 13295317828247
category: Evento S-2240
content_hash: 333659e664ab895237f7be3a5f47cab24aeb6ab7eedfa8f6d411d6513c424111
fetched_at: '2026-06-28T22:45:23.611584+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Descrição das Atividades Tarefas
  por funcionario
type: support-article
updated_at: '2025-03-12T20:57:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13295317828247-RH-Linha-Protheus-MDT-eSocial-S-2240-Descri%C3%A7%C3%A3o-das-Atividades-Tarefas-por-funcionario
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24789953595031) Tempo aproximado para leitura: **00:02:00min** **Dúvida**Descrição das Atividades, t*ag* <dscAtivDes>, Tarefas por funcionário o que é necessário saber?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Ao realizar a inclusão, alteração ou exclusão de uma tarefa a um funcionário pela rotina *MDTA090* é gerado o evento S-2240, porém caso o parâmetro ***MV\_NG2TDES*** esteja definido como "**1**" (sem aspas) pode ocorrer de que ao finalizar a exclusão de alguma tarefa o funcionário fique sem nenhuma outra tarefa vinculada e envie o evento com a *tag* <**dscAtivDes**> em branco.   
Um exemplo é o seguinte, caso o funcionário esteja sendo excluído da única tarefa que realiza, após salvar o cadastro, ficará sem nenhuma tarefa vinculada e por esse motivo a *tag* será enviada vazia.   
O sistema permite concluir o cadastro pois aceita que o funcionário seja excluído de uma tarefa antes de ser vinculado a outra.   
Dessa forma, após excluir o funcionário da única tarefa que realiza e enviar a tag <**dscAtivDes**> vazia no evento S-2240, deve-se vinculá-lo a alguma outra tarefa para que o sistema saiba que nova descrição enviar. Após vincular o funcionário à nova tarefa exercida o sistema irá retificar automaticamente o evento S-2240 ao *SIGATAF/Middleware* e dessa forma irá enviar o conteúdo da tag <**dscAtivDes**> preenchida.

**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
