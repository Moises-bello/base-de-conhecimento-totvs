---
article_id: 1500001536342
category: Materiais - Compras (SIGACOM)
content_hash: ea11aa725e66f3ffdf72014cc4a4b14a3dbbf36da9d0ab65a72a29c6eda5462b
fetched_at: '2026-06-28T22:41:19.947238+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML - Vínculo
  com pedido de compras
type: support-article
updated_at: '2026-01-08T18:28:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001536342-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML-V%C3%ADnculo-com-pedido-de-compras
---

**Dúvida**

Quando utilizado o importador XML ou TOTVS Colaboração, como é feito o vínculo com o pedido de compras ?  
  
**Ambiente**  
Protheus – Compras – A partir da versão 12.25  
  
**Solução**

Para que o vínculo seja efetuado de forma automática, o arquivo XML deve conter duas tags: xPed e nItemPed, conforme especificado no manual da NFE 4.0.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100327974)

Saiba mais em :   [Identificação de Tags no XML, para vinculo de pedido de compras.](https://tdn.totvs.com/pages/releaseview.action?pageId=285649232)

Para esse processo esta disponível o ponto de entrada a baixo:

[TC02035 - A140IVPED - Ponto para vincular pedidos de compras ao importar um documento.](https://tdn.totvs.com/x/U-f7DQ)

***Observação :***

Pode utilizar o vínculo manual em "Outras Ações -> Item Pedido" na alteração da NF importada, diretamente no Monitor do Importador ou na rotina de Documento de Entrada (MATA103), conforme o procedimento padrão.

Abaixo, uma ilustração da opção manual no Monitor do Importador XML ou Totvs Colaboração

Ilustração da opção manual no Monitor do Importador XML ou Totvs Colaboração:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412583027351)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412593621911)

**Importante**:

**Para que o vínculo seja feito de forma automática, além de ter um Pedido de Compra cadastrado para o fornecedor e para o produto em questão, é fundamental que haja a amarração Produto x Fornecedor. Para maiores informações segue documentação abaixo.**

**Caso o parâmetro MV\_XMLCAUT esteja ativo, o vínculo com o pedido de compra só será habilitado após realizar a revisão cadastral do documento, conforme documentação abaixo:**

[Cross Segmentos - Totvs Backoffice Protheus - Legenda "Docto Pendente de Revisão Cadastral" - Automação Cadastral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15923820729495-Cross-Segmentos-Totvs-Backoffice-Protheus-Legenda-Docto-Pendente-de-Revis%C3%A3o-Cadastral-Automa%C3%A7%C3%A3o-Cadastral)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML - Amarração de Produto x Fornecedor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22924903652887-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML-Amarra%C3%A7%C3%A3o-de-Produto-x-Fornecedor)

***Saiba Mais :***

[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Integração Importador XML x TOTVS Transmite](http://xn--cross%20segmento%20-%20backoffice%20(linha%20protheus)%20-%20sigacom%20-%20integrao%20importador%20xml%20x%20totvs%20transmite-ulk18b/)

[TC02035 - A140IVPED - Ponto para vincular pedidos de compras ao importar um documento.](https://tdn.totvs.com/pages/releaseview.action?pageId=285649232)

[TC06 - Erros (Códigos)](https://tdn.totvs.com/pages/viewpage.action?pageId=271663193)

[TOTVS Colaboração - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/releaseview.action?pageId=271661626)

[Importador XML - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/viewpage.action?pageId=485858148)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML - Amarração de Produto x Fornecedor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22924903652887-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML-Amarra%C3%A7%C3%A3o-de-Produto-x-Fornecedor)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
