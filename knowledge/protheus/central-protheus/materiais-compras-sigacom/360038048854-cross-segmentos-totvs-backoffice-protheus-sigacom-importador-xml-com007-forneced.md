---
article_id: 360038048854
category: Materiais - Compras (SIGACOM)
content_hash: c388334429d08f6262939f3cbeefb82d457369b5e765ea3158b2d8b2bfc2a314
fetched_at: '2026-06-28T22:41:08.952934+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador Xml - COM007
  - Fornecedor/Cliente inexistente na base
type: support-article
updated_at: '2026-03-04T14:34:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038048854-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-Xml-COM007-Fornecedor-Cliente-inexistente-na-base
---

**Dúvida**

COM007 - Fornecedor/Cliente inexistente na base.

**Ambiente**  
Protheus – Compras – A partir da versão 12  
  
**Causa**  
O erro COM007 pode ser exibido pelo Totvs Colaboração / Importador Xml quando o sistema não encontra, no cadastro do fornecedor/cliente, um registro vinculado ao CNPJ e à Inscrição Estadual informados no arquivo XML.  
  
**Solução**  
Ao tentar importar o XML, o sistema apresenta o erro COM007 no campo CKO\_CODERR. O que deve ser revisado no processo?

**Revisar:**

* Verifique se o campo de inscrição estadual do cadastro está preenchido conforme o que está no XML. TAG: **<IE></IE>**
* O nome do fornecedor conter carácter especial  retirar do cadastro e refazer o teste. TAG: **<xNome></xNome>**
* Verificar se o CFOP do arquivo está vinculado aos parâmetros **MV\_XMLCFBN** e/ou **MV\_XMLCFDV**, pois caso positivo, a busca passa a ser pelo cadastro de cliente (**SA1**) devido ao tipo da nota ser alterado para Beneficiamento ou Devolução.

**Assita nossos vídeos How To Disponíveis para correção do erro:**

[How To | Importador XML - Correção do erro COM007 - Parte 1/2](https://www.youtube.com/watch?v=RF_FQnZKaqE&t=3s)

[How To | Importador XML - Correção do erro COM007 - Parte 2/2](https://www.youtube.com/watch?v=v528ExXi0AM&t=1s)

***Saiba Mais :***

* [MP - SIGACOM - Códigos de erro Totvs Colaboração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017527792-MP-SIGACOM-C%C3%B3digos-de-erro-Totvs-Colabora%C3%A7%C3%A3o)
* [TOTVS Colaboração - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/releaseview.action?pageId=271661626)
* [Importador XML - Guia de Referencia (SIGACOM)](https://tdn.totvs.com/pages/viewpage.action?pageId=485858148)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
