---
article_id: 13295811404567
category: Evento S-2240
content_hash: eaf2e001c4ef64e37873c998fcb0bb1ab0a7227c563aa6f8bc1e265a8ffd23b8
fetched_at: '2026-06-28T22:45:23.605410+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Descrição das Atividades Ambiente
  Físico
type: support-article
updated_at: '2025-03-03T18:20:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13295811404567-RH-Linha-Protheus-MDT-eSocial-S-2240-Descri%C3%A7%C3%A3o-das-Atividades-Ambiente-F%C3%ADsico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372891348503) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Descrição das Atividades, t*ag* <dscAtivDes>, Ambiente Físico o que é necessário saber?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Ao realizar o cadastro de um um funcionário a um ambiente pela rotina *MDTA165* é gerado o evento S-2240, porém caso o parâmetro **MV\_NG2TDES** esteja definido como "**1**" (sem aspas) e não haja nenhuma tarefa vinculada ao funcionário através da rotina de tarefas por funcionário (*MDTA090*) pode ocorrer de que o evento S-2240 seja enviado com a *tag* <***dscAtivDes***> em branco.   
Dessa forma, após cadastrar o funcionário ao ambiente e enviar a *tag* <**dscAtivDes**> em branco no evento S-2240, deve-se vincular o funcionário a uma tarefa através da rotina *MDTA090* para que o sistema saiba que descrição de atividades enviar para o funcionário.   
Após vincular o funcionário a uma tarefa o sistema irá retificar automaticamente o evento S-2240 ao *SIGATAF/Middleware* e dessa forma irá enviar o conteúdo da *tag* <**dscAtivDes**> preenchida.

**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
