---
article_id: 19668739031575
category: Materiais - Compras (SIGACOM)
content_hash: 33802f201e435844fc2a98eb18c6dd2aa786f8d906bc7dca9fb84d626e572f3b
fetched_at: '2026-06-28T22:41:12.907065+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM  - Após processar schedule,
  não é apresentado na opção Reprocessar o XML da filial correta.
type: support-article
updated_at: '2024-06-13T17:26:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19668739031575-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ap%C3%B3s-processar-schedule-n%C3%A3o-%C3%A9-apresentado-na-op%C3%A7%C3%A3o-Reprocessar-o-XML-da-filial-correta
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19668727261847) Tempo aproximado para leitura: **03:00:00 min** **Dúvida** Após processar schedule, não é apresentado na opção Reprocessar o XML da filial correta.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - Todas as versões  
  
**Solução**Uma das possibilidades é:

Verificar se foi configurado Schedule para rotina SCHEDCOMCOL , pois é necessário configurar TODOS os grupos e filiais que os documentos possam pertencer para que seja importado para o monitor no grupo e filial correto e assim ser apresentado na opção Reprocessar da Empresa /Filial correspondente.

Ex: T1 / D MG 01

      T1 / D MG 02

      T2 / D SP 01

      T2 / D SP 02

Para mais detalhes consulte a Documentação abaixo:

[Integração Importador XML](https://tdn.totvs.com/pages/releaseview.action?pageId=678583195#Funcionalidades-Agendamento)

***Saiba Mais:***

* [Importador XML - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/releaseview.action?pageId=485858148)
* [Pontos de Entrada disponíveis nas funções](http://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)
* [Parâmetros Envolvidos](http://tdn.totvs.com/pages/releaseview.action?pageId=485869217)
* [Tabelas e rotinas](http://tdn.totvs.com/pages/releaseview.action?pageId=485869224)
* [Códigos de Erros](http://tdn.totvs.com/pages/releaseview.action?pageId=485869227)
* [Diferenças TOTVS Colaboração e Importador XML](http://tdn.totvs.com/pages/releaseview.action?pageId=501478281)
* [Importador XML ou Totvs Colaboração: Como executar as funções de carga SEM utilizar o schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040549593-MP-SIGACOM-Importador-XML-ou-Totvs-Colabora%C3%A7%C3%A3o-Como-executar-as-fun%C3%A7%C3%B5es-de-carga-SEM-utilizar-o-schedule)
* [Pontos de Entrada](https://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
