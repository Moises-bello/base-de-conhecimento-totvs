---
article_id: 13296080425879
category: Evento S-2240
content_hash: 1c65be874a05fa310ee1a8d58465c495e58f7c4aa0386121194d48627d10ddde
fetched_at: '2026-06-28T22:45:23.630192+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Em que cenários pode acontecer
  de o funcionário ficar sem tarefa na integração com o SIGATAF/Middleware
type: support-article
updated_at: '2025-03-12T21:00:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13296080425879-RH-Linha-Protheus-MDT-eSocial-S-2240-Em-que-cen%C3%A1rios-pode-acontecer-de-o-funcion%C3%A1rio-ficar-sem-tarefa-na-integra%C3%A7%C3%A3o-com-o-SIGATAF-Middleware
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24789838374423) Tempo aproximado para leitura: **00:02:00min** **Dúvida**Em que cenários pode acontecer de o funcionário ficar sem tarefa na integração com o SIGATAF/Middleware e o que fazer nesses casos?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Na integração do evento S-2240 ao *SIGATAF/Middleware* deve ser configurado o parâmetro **MV\_NG2TDES** que é responsável por definir qual a descrição das atividades exercidas pelo funcionário será enviada na *tag* <**dscAtivDes**> (para saber mais sobre o parâmetro **MV\_NG2TDES** acesse: <https://tdn.totvs.com/x/liWJJQ>).   
Caso o parâmetro esteja definido como "**1**" (sem aspas) o sistema irá considerar as tarefas do funcionário para saber qual descrição enviar na *tag* <**dscAtivDes**>. Porém, podem ocorrer situações em que o funcionário que está sendo enviado ao *SIGATAF/Middleware* esteja sem nenhuma tarefa vinculada e esse é um comportamento esperado.   
As rotinas que podem gerar o evento S-2240 nessa situação, ou seja, sem nenhum conteúdo na tag <dscAtivDes> são: cadastro de funcionário (*GPEA010*), transferência de funcionário (*GPEA180*), tarefas por funcionário (*MDTA090*) e cadastro de ambiente físico (*MDTA165*).  
Consulte os artigos abaixo para saber mais:  
[RH - Linha Protheus - MDT - eSocial - S-2240 - Descrição das Atividades Cadastro do funcionario](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13294696060695-RH-Linha-Protheus-MDT-eSocial-S-2240-Descri%C3%A7%C3%A3o-das-Atividades-Cadastro-do-funcionario)  
[RH - Linha Protheus - MDT - eSocial - S-2240 - Descrição das Atividades Transferencia de funcionario](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13294966541207-RH-Linha-Protheus-MDT-eSocial-S-2240-Descri%C3%A7%C3%A3o-das-Atividades-Transferencia-de-funcionario)  
[RH - Linha Protheus - MDT - eSocial - S-2240 - Descrição das Atividades Tarefas por funcionario](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13295317828247-RH-Linha-Protheus-MDT-eSocial-S-2240-Descri%C3%A7%C3%A3o-das-Atividades-Tarefas-por-funcionario)  
[RH - Linha Protheus - MDT - eSocial - S-2240 - Descrição das Atividades Ambiente Físico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13295811404567-RH-Linha-Protheus-MDT-eSocial-S-2240-Descri%C3%A7%C3%A3o-das-Atividades-Ambiente-F%C3%ADsico) **Saiba Mais  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)**
