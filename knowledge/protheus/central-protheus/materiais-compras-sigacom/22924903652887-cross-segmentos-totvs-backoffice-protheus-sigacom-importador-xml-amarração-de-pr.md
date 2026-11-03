---
article_id: 22924903652887
category: Materiais - Compras (SIGACOM)
content_hash: 77db5e35a4777f029a70378fc89bddc83d968a384ad6f6c53407303b9e6e9720
fetched_at: '2026-06-28T22:41:19.897852+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML - Amarração
  de Produto x Fornecedor
type: support-article
updated_at: '2024-05-06T13:08:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22924903652887-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML-Amarra%C3%A7%C3%A3o-de-Produto-x-Fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22924903624983) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Como realizar o Cadastro de Produto x Fornecedor para utilização Importador XML ?

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Todas as versões

**Solução**

Para realizar as integração dos XMLs na rotina de importação XML, o sistema utiliza como base o cadastro de produto x fornecedor. Essa base será responsável por fazer o mapeamento do **código do produto presente no XML** para o **código interno do produto no sistema Protheus**.

Esse processo de mapeamento, ou **"DE/PARA"**, é necessário porque nem sempre o código do produto utilizado pelo fornecedor é o mesmo que foi cadastrado no sistema Protheus.

Por exemplo:

**Produto do Fornecedor:** 057400166  
**Produto:** GB B&K GIBY&GABY SPRAY P.ASSAD  
**Código:** 057400166

**Produto cadastrado no Protheus**  
**Produto:** Massa e Textura  
**Código:** 50

Na rotina Produto x Fornecedor, você pode utilizar o campo **"Cod.Prod.For"** para inserir o código do produto do fornecedor, conforme exemplificado abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22925182955287)

Neste exemplo, mesmo sendo o mesmo produto, há uma diferença entre o código utilizado pelo fornecedor (057400166) e o código cadastrado no sistema Protheus (50).

O cadastro de amarração entre produto e fornecedor será responsável por identificar que o código 057400166 enviado no XML representa o mesmo produto 50 cadastrado no Protheus.

Para determinar qual código o fornecedor utiliza no XML, você pode localizar a TAG **<cProd>**.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/22924903628183)**

***Saiba Mais:***

[Importador XML - Guia de Referencia (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)

[Tabelas e Rotinas](https://tdn.totvs.com/pages/releaseview.action?pageId=485869224)

[https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS](Pagina%20CENTRALIZADORA)
