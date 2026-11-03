---
article_id: 13294696060695
category: Evento S-2240
content_hash: 627a893a52ad333ef4670be58caa760f4174752b913abae7064849e8e0cf49cb
fetched_at: '2026-06-28T22:45:23.608368+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Descrição das Atividades Cadastro
  do funcionario
type: support-article
updated_at: '2025-03-03T18:19:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13294696060695-RH-Linha-Protheus-MDT-eSocial-S-2240-Descri%C3%A7%C3%A3o-das-Atividades-Cadastro-do-funcionario
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Descrição das Atividades, tag <dscAtivDes>, Cadastro do funcionario o que é necessário saber?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Ao realizar o cadastro de um novo funcionário ou alterar um funcionário existente (desde que ele não tenha um evento S-2240 comunicado ao SIGATAF/Middleware) é gerado o evento S-2240, porém caso o parâmetro *MV\_NG2TDES* esteja definido como "**1**" (sem aspas) não existe como vincular uma tarefa ao funcionário antes de finalizar esse cadastro.   
Dessa forma ao finalizar o cadastro de um funcionário na rotina *GPEA010* o evento S-2240 será gerado com a tag <**dscAtivDes**> em branco.   
Nesse caso, após realizar o cadastro do funcionário e ser gerado o evento S-2240 com a tag vazia, deve-se vincular o funcionário cadastrado/alterado a alguma tarefa para que o sistema saiba que descrição enviar na tag <**dscAtivDes**>.   
Após vincular o funcionário a alguma tarefa o sistema irá retificar automaticamente o evento S-2240 ao SIGATAF/Middleware e dessa forma irá enviar o conteúdo da tag <**dscAtivDes**> preenchida.

**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
