---
article_id: 12969026890007
category: Materiais - Compras (SIGACOM)
content_hash: 076faf4918d2038f89068f65960faa159acfe53e0d33c7977e22a86017a0631c
fetched_at: '2026-06-28T22:41:17.537407+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - É possível Importar
  um documento do Tipo Beneficiamento Classificado ?
type: support-article
updated_at: '2024-05-23T13:22:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12969026890007-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-%C3%89-poss%C3%ADvel-Importar-um-documento-do-Tipo-Beneficiamento-Classificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23689564587543) Tempo aproximado para leitura: **00:03 min****Dúvida**  
Regras de importação de documentos do Tipo de Beneficiamento com status já Classificado no Documento de Entrada.  
  
**Ambiente**Protheus – Compras – A partir da versão 12  
  
**Solução**

Sistema não efetua a classificação de documento do Tipo B (Beneficiamento), pois não há um vínculo automático com a nota fiscal de origem em TAG do arquivo XML.

Mesmo que efetuemos as configurações dos parâmetros **MV\_COMCOL1 , MV\_XMLCFBN e MV\_COMCOL2,**este documento será gerado com o status igual "A Classificar". 

Caso tenha necessidade de importação documento do Tipo Beneficiamento já Classificado, será necessário utilizar o Ponto de Entrada A140IGRV para realizar o vinculo com a NF de origem.

[A140IGRV - A140IGRV (totvs.com.br)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=6085827)

***Saiba Mais :***

* [Importador XML - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/releaseview.action?pageId=485858148)
* [IX10 - Integração Importador XML x TOTVS Transmite](https://tdn.totvs.com/x/m1tyK)
* [Pontos de Entrada disponíveis nas funções](http://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)
* [Parâmetros Envolvidos](http://tdn.totvs.com/pages/releaseview.action?pageId=485869217)
* [Tabelas e rotinas](http://tdn.totvs.com/pages/releaseview.action?pageId=485869224)
* [Códigos de Erros](http://tdn.totvs.com/pages/releaseview.action?pageId=485869227)
* [Importador XML ou Totvs Colaboração: Como executar as funções de carga SEM utilizar o schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040549593-MP-SIGACOM-Importador-XML-ou-Totvs-Colabora%C3%A7%C3%A3o-Como-executar-as-fun%C3%A7%C3%B5es-de-carga-SEM-utilizar-o-schedule)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
