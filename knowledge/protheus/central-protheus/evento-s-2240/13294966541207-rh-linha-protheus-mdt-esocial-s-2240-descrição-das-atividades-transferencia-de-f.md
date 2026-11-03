---
article_id: 13294966541207
category: Evento S-2240
content_hash: 89a7b4d17e67a7024e1e45ee59204cc7d802c6131425529f8a12dbcac4fdf047
fetched_at: '2026-06-28T22:45:23.614833+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Descrição das Atividades Transferencia
  de funcionario
type: support-article
updated_at: '2025-03-03T18:19:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13294966541207-RH-Linha-Protheus-MDT-eSocial-S-2240-Descri%C3%A7%C3%A3o-das-Atividades-Transferencia-de-funcionario
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372890522647) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Descrição das Atividades, *tag* <dscAtivDes>, Transferencia de funcionario o que é necessário saber?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Ao realizar a transferência de empresa ou filial de um funcionário é gerado o evento S-2240, porém caso o parâmetro ***MV\_NG2TDES*** esteja definido como "**1**" (sem aspas) não existe como vincular uma tarefa ao funcionário na empresa ou filial destino antes de realizar a transferência da filial origem.   
Dessa forma ao finalizar a transferência do funcionário para a empresa ou filial destino através da rotina *GPEA180* o evento S-2240 será gerado com a *tag* <**dscAtivDes**> em branco.   
Nesse caso, após realizar a transferência do funcionário e ser gerado o evento S-2240 com a tag vazia, deve-se entrar na empresa ou filial destino e vincular o funcionário transferido a alguma tarefa para que o sistema saiba que descrição enviar na *tag* <**dscAtivDes**>.   
Após vincular o funcionário a alguma tarefa na empresa ou filial destino o sistema irá retificar automaticamente o evento S-2240 ao SIGATAF/Middleware e dessa forma irá enviar o conteúdo da tag <**dscAtivDes**> preenchida. **Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
