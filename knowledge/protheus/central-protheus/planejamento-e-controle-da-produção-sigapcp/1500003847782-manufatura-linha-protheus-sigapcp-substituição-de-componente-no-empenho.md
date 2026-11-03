---
article_id: 1500003847782
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: fa42f7049f82e055934defe99cf43c37b193736381a27d0405c5bfd5b61e3eed
fetched_at: '2026-06-28T22:42:47.039226+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Substituição de componente no empenho
type: support-article
updated_at: '2021-10-15T19:16:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003847782-Manufatura-Linha-Protheus-SIGAPCP-Substitui%C3%A7%C3%A3o-de-componente-no-empenho
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:30 min**  
**Dúvida**Quais os critérios para listagem das **OPs - Ordens de Produção** quando se faz a substituição de componentes na rotina **MATA200 - Cadastro de Estruturas**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Quando se realiza a substituição de um componente por outro, o Sistema procura pelas **OPs** com o status **Prevista** ou **Em Aberto** que tenham o produto pai no qual o componente em questão foi substituído e lista somente as **OPs** que atendem a essa condição.
