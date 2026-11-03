---
article_id: 4407771559575
category: Evento S-2240
content_hash: 61862178e3717a189cbe8ce9cf3d5aecab9d850121fe76afb7c4d225bfaffe55
fetched_at: '2026-06-28T22:45:23.558915+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Como é buscada a informação
  de descrição das atividades realizadas (tag <dscAtivDes>) no evento S-2240
type: support-article
updated_at: '2025-03-03T18:02:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407771559575-RH-Linha-Protheus-MDT-eSocial-S-2240-Como-%C3%A9-buscada-a-informa%C3%A7%C3%A3o-de-descri%C3%A7%C3%A3o-das-atividades-realizadas-tag-dscAtivDes-no-evento-S-2240
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372287298583)** Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Como é buscada a informação de descrição das atividades realizadas (**tag <dscAtivDes>**) no evento **S-2240**?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**No evento **S-2240** do eSocial deve-se enviar na tag <**dscAtivDe**s> a descrição das atividades, físicas ou mentais, realizadas pelo trabalhador na empresa. No SIGAMDT, essa informação pode ser enviada de maneiras diferentes e o que indica qual a maneira a ser considerada é o parâmetro MV\_NG2TDES. O parâmetro possui algumas opções: **1= Tarefa; 2= Cargo; 3= Função; 4= Cargo + Tarefa** e o sistema obedecerá o que for definido nele para compor a informação da descrição da atividade realizada. Abaixo está definido como a informação é composta de acordo com cada uma das opções do parâmetro.  
  
**1. Descrição pela** **Tarefa** (**MV\_NG2TDES = 1**):  
Caso o parâmetro MV\_NG2TDES esteja com o conteúdo igual a "**1**" (sem aspas), o sistema irá buscar todas as tarefas vinculadas ao funcionário através da rotina de Tarefas por Funcionário (MDTA090). Tendo todas as tarefas vinculadas ao funcionário, o sistema irá compor a descrição a ser enviada na tag <**dscAtivDes**> buscando o conteúdo do campo "**Descrição**" (TN5\_DESCRI) do cadastro de tarefas. Caso o conteúdo do campo "**Descrição**" (TN5\_DESCRI) esteja vazio, o sistema irá compor a descrição a ser enviada na tag <**dscAtivDes**> com o conteúdo do campo "**Nome Tarefa**" (TN5\_NOMTAR).  
  
![](https://tdn.totvs.com/download/attachments/629745046/Tarefa.png?version=3&modificationDate=1630002288787&api=v2)  
  
**2. Descrição pelo Cargo (MV\_NG2TDES = 2):**Caso o parâmetro MV\_NG2TDES esteja com o conteúdo igual a "**2**" (sem aspas), o sistema irá buscar o cargo vinculado ao funcionário através do campo "**Cargo**" (RA\_CARGO) do cadastro de funcionários (GPEA010). Tendo o cargo do funcionário, o sistema irá compor a descrição a ser enviada na tag <**dscAtivDes**> buscando o conteúdo do campo "**Ds.Detalhada**" (Q3\_MEMO1) do cadastro de cargos. Caso o conteúdo do campo "**Ds.Detalhada**" (Q3\_MEMO1) esteja vazio, o sistema irá compor a descrição a ser enviada na tag <**dscAtivDes**> com o conteúdo do campo "**Desc.Sumaria**" (Q3\_DESCSUM) do cadastro de cargos.  
  
![](https://tdn.totvs.com/download/attachments/629745046/Cargo.png?version=2&modificationDate=1630002282187&api=v2)  
  
**3. Descrição pela Função (MV\_NG2TDES = 3):**Caso o parâmetro MV\_NG2TDES esteja com o conteúdo igual a "**3**" (sem aspas), o sistema irá buscar a função vinculada ao funcionário através do campo "**Cod. Funcao**" (RA\_CODFUNC) do cadastro de funcionários (GPEA010). Tendo a função do funcionário, o sistema irá compor a descrição a ser enviada na tag <**dscAtivDes**> buscando o conteúdo do campo "**Requisitos**" (RJ\_MEMOREQ) do cadastro de funções. Caso o conteúdo do campo "Requisitos" (RJ\_MEMOREQ) esteja vazio o sistema irá compor a descrição a ser enviada na tag <**dscAtivDes**> com o conteúdo do campo "**Descricao**" (RJ\_DESC) do cadastro de funções.  
  
![](https://tdn.totvs.com/download/attachments/629745046/Fun%C3%A7%C3%A3o.png?version=1&modificationDate=1630002219817&api=v2)

**4. Descrição pelo Cargo + Tarefa (MV\_NG2TDES = 4):**Caso o parâmetro MV\_NG2TDES esteja com o conteúdo igual a "**4**" (sem aspas), o sistema irá buscar o cargo vinculado ao funcionário através do campo "**Cargo**" (RA\_CARGO) do cadastro de funcionários (GPEA010) e também todas as tarefas vinculadas ao funcionário através da rotina de Tarefas por Funcionário (MDTA090). Tendo o cargo e todas as tarefas vinculadas ao funcionário, o sistema irá compor a descrição a ser enviada na tag <**dscAtivDes**> buscando primeiramente o conteúdo do campo "**Ds.Detalhada**" (Q3\_MEMO1). Caso o conteúdo do campo "**Ds.Detalhada**" (Q3\_MEMO1) esteja vazio o sistema irá compor a descrição a ser enviada na tag <**dscAtivDes**> com o conteúdo do campo "**Desc.Sumaria**" (Q3\_DESCSUM). Após buscar a descrição referente ao cargo, o sistema irá buscar a descrição das tarefas realizadas pelo funcionário buscando o conteúdo do campo "Descrição" (TN5\_DESCRI) do cadastro de tarefas. Caso o conteúdo do campo "**Descrição**" (TN5\_DESCRI) esteja vazio, o sistema irá compor a descrição a ser enviada na tag <**dscAtivDes**> com o conteúdo do campo "**Nome Tarefa**" (TN5\_NOMTAR). Portanto, a descrição a ser enviada na tag <**dscAtivDes**> será composta pela junção das informações do cargo e das tarefas a que o funcionário está vinculado.  
  
![](https://tdn.totvs.com/download/attachments/629745046/Cargo.png?version=2&modificationDate=1630002282187&api=v2)  
  
![](https://tdn.totvs.com/download/attachments/629745046/Tarefa.png?version=3&modificationDate=1630002288787&api=v2)  
  
**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
