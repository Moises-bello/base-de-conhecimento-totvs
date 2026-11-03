---
article_id: 360037160113
category: Call Center - Dúvidas Gerais
content_hash: c35efc4f17d046c444591d7e23ac97afd0e69ae1f475c763a8548a6447dce93f
fetched_at: '2026-06-28T22:41:26.795751+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: 'Cross Segmentos -TOTVS Backoffice (Linha Protheus)- SIGATMK-Uso do Monitor
  de Supervisão '
type: support-article
updated_at: '2022-06-17T19:18:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037160113-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Uso-do-Monitor-de-Supervis%C3%A3o
---

**Dúvida**

É possível utilizar a funcionalidade de Monitor de Supervisão ( **TMKC030** )  quando o operador estiver utilizando a rotina **TMKA271**?  
  
**Ambiente**

Cross Segmentos -TOTVS Backoffice (Linha Protheus)- SIGATMK- todas as versões.

**Solução**

A rotina de Monitor do Supervisor visualiza os atendimentos telemarketing, televendas e telecobrança, se o operador estiver configurado para todos os atendimentos, no momento em que não é feito nenhuma ação, o browser deste atendimento é a rotina **TMKA271**.

Da rotina **TMKA271** é chamada as demais rotinas em segunda camada, conforme o atendimento que for efetuado.

A ideia principal da rotina **TMKC030** é buscar os atendimentos com base nos grupos de atendimentos existentes (**SU0**) , nos operadores (**SU7**), os atendimentos em si, buscado da tabela auxiliar **SUV**, não há busca voltada diretamente para rotina **TMKA271**, **TMKA272** e assim por diante.

Enquanto não houver nenhuma ação, o monitor não irá mostrar nada ao operador - supervisor, a partir do momento que for dado o incluir, o monitor começará a a monitorar a aba que o operador estiver logado.

No exemplo abaixo, sempre começará como telemarketing que é a primeira aba de atendimento, se  mudar o operador para a aba de televendas, a consulta somente mudará após a inserção de dados.

![](https://totvssuporte.zendesk.com/attachments/token/22mIm8XJDebsT4ve2u3E7c00d/?name=monitor+supervis%C3%A3o.gif)
