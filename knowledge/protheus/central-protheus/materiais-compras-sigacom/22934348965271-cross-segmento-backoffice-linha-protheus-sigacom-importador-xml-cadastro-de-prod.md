---
article_id: 22934348965271
category: Materiais - Compras (SIGACOM)
content_hash: c23b0a59738f843f8699569cc93b6443a752406ba8e5f47baa88c089d59c817f
fetched_at: '2026-06-28T22:41:10.599555+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Importador XML - Cadastro
  de Produto x Cliente
type: support-article
updated_at: '2024-04-20T01:19:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22934348965271-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Importador-XML-Cadastro-de-Produto-x-Cliente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22934348938007) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**  
Como realizar o Cadastro de Produto x Cliente para utilização Importador XML nas notas fiscais de devolução ?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Todas as versões  
  
**Solução**

Para realizar as **integrações** dos **XMLs** na rotina **importador XML** sobre **notas fiscais de devolução**, o sistema utiliza como base o cadastro produto x cliente.  
Ele será responsavel por realizar o DE/PARA do **código do produto que consta no XML** para o **código do produto interno.**  
Esse processo de DE/PARA é realizado justamente porque nem sempre o código do produto que o fornecedor utiliza é o mesmo que foi cadastado no sistema protheus, exemplo:

**XML do Fornecedor:** 057400166  
**Produto:** GB B&K GIBY&GABY SPRAY P.ASSAD  
**Código:** 057400166

**Protheus**  
**Produto:** SAPATO  
**Código:** 15

Na rotina Produto x Cliente, utilize o campo **Cod.Prod.Cli** para inserir o código do produto do fornecedor (XML) conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22934348941079)

Veja que mesmo sendo o mesmo produto, existe uma diferença utilizada no código do fornecedor (057400166) com código cadastrado no protheus (15).

O cadastro amarração produto x cliente será responsavel por identificar que o código 057400166 enviado no XML representa o mesmo produto 15 cadastrado no protheus.

Para saber qual código o fornecedor utiliza no xml, basta localizar a TAG cProd;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22934348943639)

***Saiba Mais:***

[Importador XML - Guia de Referencia (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)

[Tabelas e Rotinas](https://tdn.totvs.com/pages/releaseview.action?pageId=485869224)

[https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/Pagina%20CENTRALIZADORA)
