---
article_id: 360015862432
category: Contabilidade Gerencial - Integração EAI PIMS Protheus
content_hash: 3e17dadc6c57924bc1065b578608bde79bce0adf381999de0541cfecc289d7bd
fetched_at: '2026-06-28T22:40:54.195309+00:00'
product: protheus
section_id: 1500001537541
source: central-protheus
title: MP - SIGACTB - INTEGRAÇÃO EAI PIMS x PROTHEUS / USO DE CONDIÇÃO NO ADAPTER
type: support-article
updated_at: '2021-04-28T22:07:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015862432-MP-SIGACTB-INTEGRA%C3%87%C3%83O-EAI-PIMS-x-PROTHEUS-USO-DE-CONDI%C3%87%C3%83O-NO-ADAPTER
---

**Ocorrência**

Na Integração pims a partir do bloqueio de calendário com o adapter periodgbalance, foi configurada condição para não gerar informação para uma filial especifica, porem ao realizar o procedimento de integração não considera esta condição, gerando informação para a filial

**Ambiente**PROTHEUS – Contabilidade Gerencial – A partir da versão 11.80  
   
 **Causa**

Quando utilizar a expressão de filtro ADVPL No Adapter EAI este deve retornar true para executar o adapter e caso de retorno falso ele não executara o Adapter.

**Solução**

Neste cenário deve utilizar a variável global cFilAnt que indica a filial logada no momento da execução da integração por mensagem  única, como por exemplo, cFilAnt == "01", ou seja somente quando estiver  logado na filial 01 será executado o adapter, e não deverá ser utilizado as tabelas envolvidas no processo, pois não temos exatamente o posicionamento de tais tabelas no momento da integração.
