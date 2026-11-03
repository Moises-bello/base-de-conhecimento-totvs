---
article_id: 360028830271
category: TAF - REINF
content_hash: b1b04c318a6b431b9374a3be63efd7b3a26317a7e6a5447ee53736a64aa38050
fetched_at: '2026-06-28T22:41:33.599737+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Alteração do Tipo Default
  para Campos Caractere de VARCHAR para CHAR (SGBDs Oracle e PostgreSQL)
type: support-article
updated_at: '2023-03-31T17:08:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028830271-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Altera%C3%A7%C3%A3o-do-Tipo-Default-para-Campos-Caractere-de-VARCHAR-para-CHAR-SGBDs-Oracle-e-PostgreSQL
---

**Dúvida**  
Alteração do Tipo Default para Campos Caractere de VARCHAR para CHAR (SGBDs Oracle e PostgreSQL).  
  
 **Ambiente**  
Protheus – TAF – A partir da versão 11.80  
  
**Solução**Algumas queries executadas nos SGBDs Oracle e PostgreSQL estavam apresentando comportamento diferente após alteração do tipo default para campos caractere de **CHAR** para **VARCHAR**.

**Implementação:**

-O tipo **CHAR** volta a ser o tipo padrão para campos caractere.

-O tipo **VARCHAR** será assumido como padrão, somente se a chave [DBAccess - Seção [Environment], chave TrimRightSpace](http://tdn.totvs.com/pages/viewpage.action?pageId=281987780) for habilitada.  
  
[DBAccess - Seção](http://tdn.totvs.com/pages/viewpage.action?pageId=281987780)[[Environment], chave TrimRightSpace](http://tdn.totvs.com/pages/viewpage.action?pageId=281987780):  
<http://tdn.totvs.com/pages/viewpage.action?pageId=281987780>

Como paliativo, o tipo padrão para campos caractere pode ser modificado através da chave [DBAccess - Seção [Environment], chave StringType](http://tdn.totvs.com/pages/viewpage.action?pageId=331850180) no arquivo INI do DBAccess, nesse caso, StringType=CHAR.  
  
<http://tdn.totvs.com/pages/viewpage.action?pageId=331850180>  
  
Link contendo as informações acima:

<http://tdn.totvs.com/pages/viewpage.action?pageId=331850252>
