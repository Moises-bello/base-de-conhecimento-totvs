---
article_id: 18507918015767
category: Materiais - Compras (SIGACOM)
content_hash: bc7c006938b5163dd1e90651ed332069e0aa787b9d385b0c0f6562f103bf6293
fetched_at: '2026-06-28T22:41:12.864101+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - Como é gravado o Tipo de Frete
  (DS_TPFRETE) ao Importar o Xml?
type: support-article
updated_at: '2024-06-13T17:14:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18507918015767-Cross-Segmentos-Totvs-Backoffice-Protheus-Como-%C3%A9-gravado-o-Tipo-de-Frete-DS-TPFRETE-ao-Importar-o-Xml
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18507874109719) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como é gravado o Tipo de Frete (DS\_TPFRETE) ao Importar o Xml?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - Todas as versões  
  
**Solução**

Visando um melhor entendimento de como será feito a importação de um XML de conhecimento de frete e seu valor de tipo de frete.

**CTE (Sempre validando CNPJ e IE)**

***Obs:*** Caso documento seja inserido utilizado produto frete, informado no parâmetro MV\_XMLPFCT ou através do P.E, tipo de frete será = F (FOB)

**Documentação Completa : [Regra tipo de frete - Conhecimento de Frete](https://tdn.totvs.com/pages/releaseview.action?pageId=629753043)**

Para manipular a gravação das tabelas SDS e SDT durante a importação do CT-e, sugerimos o uso do ponto de entrada MT116XMLCT. Este ponto de entrada é utilizado. Para mais informações, consulte a documentação completa do ponto de entrada no seguinte link: [Ponto de Entrada MT116XMLCT](https://tdn.totvs.com/pages/releaseview.action?pageId=243012688)

***Saiba Mais:***

* [IX08007 - Importador XML - Regra tipo de frete - Conhecimento de Frete](https://tdn.totvs.com/display/PROT/IX08007+-+Importador+XML+-+Regra+tipo+de+frete+-+Conhecimento+de+Frete) .
* [TC07012 - Totvs Colaboração - Regra tipo de frete - Conhecimento de Frete](https://tdn.totvs.com/pages/releaseview.action?pageId=629753043)
* [Importador XML - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/releaseview.action?pageId=485858148)
* [Pontos de Entrada disponíveis nas funções](http://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)
* [Parâmetros Envolvidos](http://tdn.totvs.com/pages/releaseview.action?pageId=485869217)
* [Tabelas e rotinas](http://tdn.totvs.com/pages/releaseview.action?pageId=485869224)
* [Códigos de Erros](http://tdn.totvs.com/pages/releaseview.action?pageId=485869227)
* [Diferenças TOTVS Colaboração e Importador XML](http://tdn.totvs.com/pages/releaseview.action?pageId=501478281)
* [Importador XML ou Totvs Colaboração: Como executar as funções de carga SEM utilizar o schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040549593-MP-SIGACOM-Importador-XML-ou-Totvs-Colabora%C3%A7%C3%A3o-Como-executar-as-fun%C3%A7%C3%B5es-de-carga-SEM-utilizar-o-schedule)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
