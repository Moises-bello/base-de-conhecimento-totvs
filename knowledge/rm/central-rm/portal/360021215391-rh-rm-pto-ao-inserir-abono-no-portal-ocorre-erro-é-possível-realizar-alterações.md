---
article_id: 360021215391
category: Portal
content_hash: 3d7007aa0c9a25f1864c5a278e79ca405740c4666d12d8783522779b05ce57f4
fetched_at: '2026-06-28T22:46:37.900843+00:00'
product: rm
section_id: 1500000835141
source: central-rm
title: 'RH - RM - PTO - Ao inserir abono no portal ocorre erro: ''É possível realizar
  alterações somente a partir  do dia'''
type: support-article
updated_at: '2025-01-27T17:20:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021215391-RH-RM-PTO-Ao-inserir-abono-no-portal-ocorre-erro-%C3%89-poss%C3%ADvel-realizar-altera%C3%A7%C3%B5es-somente-a-partir-do-dia
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16780691534231) Tempo aproximado para leitura: 00:01:00 min*****Dúvida**Ao inserir um abono no portal aparece a mensagem de erro abaixo, o que fazer ?

Processo interrompido com erros: É possível realizar alterações somente a partir do dia XX-XX-XXXX

**Ambiente**RM -  Automação de Ponto - Todas as versões  
  
**Solução**

Para correção, acesse no Automação de Ponto o menu **Configurações | Parametrizador**, ao abrir o assistente selecione o processo **RM Portal** e avance.  Localize o grupo de quiosque que está associado ao funcionário.

Selecione o grupo e clique no botão parametrizar, avance etapa Gestão por Escala e marque  o parametro  "**A partir do período ativo"**  
  
Após marcar o parametro , avance as demais etapas até concluir e realize a inclusão do Abono.

![portal.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29533082092439)

Para identificar o grupo do portal vinculado ao funcionario, edite o cadastro do funcionario e confira o campo 'Código do Grupo de Quiosque' localizado na guia identificação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29533082103959)  
  
**Saiba mais:**[Gestão Por Escala](https://tdn.totvs.com/pages/viewpage.action?pageId=452718997)
