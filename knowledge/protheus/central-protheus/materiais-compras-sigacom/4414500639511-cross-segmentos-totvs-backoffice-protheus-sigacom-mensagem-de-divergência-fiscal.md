---
article_id: 4414500639511
category: Materiais - Compras (SIGACOM)
content_hash: e58d4adba086a29fee199048d4aad1560f6432353bf84db0fc5460b9aa43e19b
fetched_at: '2026-06-28T22:41:20.182700+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Mensagem de " Divergência
  Fiscal " ao gerar documento no Monitor do Colaboração / Importador XML
type: support-article
updated_at: '2024-06-07T18:38:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414500639511-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Mensagem-de-Diverg%C3%AAncia-Fiscal-ao-gerar-documento-no-Monitor-do-Colabora%C3%A7%C3%A3o-Importador-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24033541270039) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Sobre a Mensagem de " Divergência Fiscal " ao gerar documento no Monitor do Colaboração / Importador XML

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414493138071)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**A mensagem de "Divergência Fiscal" referente aos impostos que é exibida ao gerar um Documento no Monitor do Totvs Colaboração ou Importador XML é uma mensagem apenas informativa caso exista impostos no XML importado, onde o sistema apenas confronta essas informações de impostos do XML, com os de uma TES informada ou não no Monitor.  
Na importação não é feita nenhuma tratativa, e o que valerá para o documento a ser gerado de fato serão as informações/configurações de impostos da TES informada no processo da Classificação da Nota.  
  
Dessa forma não há uma correção a ser realizada. Pode-se no caso informar uma TES no Monitor para efeito de comparação na aba "Impostos", que conforme informado é apenas informativo, e o que valerá para a inclusão do documento de fato são as informações de impostos da TES informadas no processo da classificação da Nota.

***Saiba Mais:***

* [Cross Segmento - Backoffice Protheus - SIGACOM - Impostos na rotina do Importador/Totvs Colaboração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4428159240983)
* [Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Integração Importador XML x TOTVS Transmite](http://xn--cross%20segmento%20-%20backoffice%20(linha%20protheus)%20-%20sigacom%20-%20integrao%20importador%20xml%20x%20totvs%20transmite-ulk18b/)
* [Importador XML - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/releaseview.action?pageId=485858148)
* [Pontos de Entrada disponíveis nas funções](http://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)
* [Parâmetros Envolvidos](http://tdn.totvs.com/pages/releaseview.action?pageId=485869217)
* [Tabelas e rotinas](http://tdn.totvs.com/pages/releaseview.action?pageId=485869224)
* [Códigos de Erros](http://tdn.totvs.com/pages/releaseview.action?pageId=485869227)
* [Diferenças TOTVS Colaboração e Importador XML](http://tdn.totvs.com/pages/releaseview.action?pageId=501478281)
* [Importador XML ou Totvs Colaboração: Como executar as funções de carga SEM utilizar o schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040549593-MP-SIGACOM-Importador-XML-ou-Totvs-Colabora%C3%A7%C3%A3o-Como-executar-as-fun%C3%A7%C3%B5es-de-carga-SEM-utilizar-o-schedule)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
