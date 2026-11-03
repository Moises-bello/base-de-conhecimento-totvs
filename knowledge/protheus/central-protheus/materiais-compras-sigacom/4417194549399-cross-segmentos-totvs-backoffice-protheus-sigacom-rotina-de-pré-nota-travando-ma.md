---
article_id: 4417194549399
category: Materiais - Compras (SIGACOM)
content_hash: 11799ffc78701c4d1b46e7d3b3f0f8ec5b5060744fe6a45ac6eb8f259f842121
fetched_at: '2026-06-28T22:41:25.299484+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Rotina de Pré-Nota
  Travando  ( MATA140 ) '
type: support-article
updated_at: '2021-12-27T13:26:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417194549399-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rotina-de-Pr%C3%A9-Nota-Travando-MATA140
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Rotina de Pré-Nota ( MATA140 ) Travando  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras- Todas as versões  
  
**Solução**Sobre questão de travamento na rotina de Pré-Nota de Entrada (MATA140) das ocorrências que existem mapeadas, elas foram solucionadas ao desabilitar as customizações existentes no ambiente em questão.

Abaixo seguem orientações para este procedimento de desativar as customizações (seguir os dois tópicos para uma desativação mais efetiva):

1 - [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como desabilitar customizações através do catálogo de personalização do Configurador?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018286552-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-desabilitar-customiza%C3%A7%C3%B5es-atrav%C3%A9s-do-cat%C3%A1logo-de-personaliza%C3%A7%C3%A3o-do-Configurador-?source=search)  
Quando executar este processo conferir na tabela XX7, o campo X7\_STATUS de todos os registros deverá constar igual a 2.

2 - E insira também a chave IXBLOG = NORUN no Appserver do Protheus:  [desabilitar através da chave IXBLOG = NORUN no Appserver do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292)

Além de desabilitar as customizações também é recomentado estar com o ambiente com as últimas atualizações disponíveis do Compras, do link abaixo:

[Pacotes de Atualização - Compras](https://tdn.totvs.com/pages/viewpage.action?pageId=522011099)

***Saiba Mais:***

* [Pacotes de Atualização - Compras](https://tdn.totvs.com/pages/viewpage.action?pageId=522011099)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
