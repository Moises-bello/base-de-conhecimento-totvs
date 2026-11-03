---
article_id: 21123400723223
category: RH - Integração de Titulo
content_hash: bc1526d7f56899affca85b51bb3c07b3b681fff48c6bddfe23fb8384942d53c9
fetched_at: '2026-06-28T22:43:36.297252+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Definição de títulos não apresenta tabelas para
  configuração
type: support-article
updated_at: '2025-07-14T20:42:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21123400723223-RH-Linha-Protheus-GPE-Defini%C3%A7%C3%A3o-de-t%C3%ADtulos-n%C3%A3o-apresenta-tabelas-para-configura%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21123432924183) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Na rotina de Definição de títulos (GPEM640) , não são apresentadas as tabelas para configuração.  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
  
**Causa**Esse erro ocorre devido a rotina GPEM640 (Definição de Títulos) na configuração do ITEM do Menu no Configurador não possuir as tabelas selecionadas para busca e configuração na definição de título.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21123400710935)

**Solução**

1. Acessar via configurador Ambiente -> Cadastros -> Menus -> Gestão de Pessoal -> Títulos - Definição -> Adicionar e na rotina GPEM640 incluir os flags nas tabelas RC0, SRA, SRC, SRD, SRR conforme padrão. Após esta manutenção, as tabelas deverão ser apresentadas corretamente na definição de títulos e na consulta de tabelas genéricas.

![](https://totvssuporte.zendesk.com/attachments/token/dnitExAZ3a0zPnXPZez8AfpOU/?name=inline314781899.png)

Saiba Mais:  
[Página Centralizadora da Geração , Manutenção e Integração de títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
