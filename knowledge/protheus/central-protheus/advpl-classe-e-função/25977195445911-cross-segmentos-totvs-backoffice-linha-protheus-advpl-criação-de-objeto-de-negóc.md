---
article_id: 25977195445911
category: ADVPL - Classe e Função
content_hash: 9977dfd432cf019b67857515e58bef5ebcf19bb2c520103d8578978355b4c355
fetched_at: '2026-06-28T22:40:21.555825+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Criação de Objeto
  de Negócio SmartView com TLPP
type: support-article
updated_at: '2025-09-30T20:45:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25977195445911-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Cria%C3%A7%C3%A3o-de-Objeto-de-Neg%C3%B3cio-SmartView-com-TLPP
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25977154688407)*Tempo aproximado para leitura: 00:02:00 min

**Dúvida**  
Como criar um novo Objeto de Negócio no SmartView?

**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.2310

**Solução**  
Desenvolver um fonte, em **TLPP**, utilizando a Classe **IntegratedProvider,**e realizar a compilação em seu RPO para que o mesmo encontre-se disponível na sessão **Objetos de Negócio**para a utilização dentro do SmartView.  
  
**Obs:** Importante reiniciar o Server após a compilação, para que o fonte seja devidamente compilado no ambiente REST, que é onde os Objetos de Negócios são localizados pelo SmartView.  
  
Exemplo:

```
#include "msobject.ch"  
#include "totvs.framework.treports.integratedprovider.th"  
  
namespace custom.materiais.produtos.integratedprovider  
  
@totvsFrameworkTReportsIntegratedProvider(active=.T., team="SIGACOM", tables="SB1", name="Materiais", country="ALL", initialRelease="12.1.2210")  
class SB1TReportsBusinessObject from totvs.framework.treports.integratedprovider.IntegratedProvider  
public method new() as object  
public method getData() as object  
public method getSchema() as object  
endclass  
  
method new() class SB1TReportsBusinessObject  
_Super:new()  
//Define a Área  
self:appendArea("Compras")  
  
//Define o nome do Objeto de Negócio  
self:setDisplayName("Produtos")  
  
//Define a descrição do Objeto de Negócio  
self:setDescription("Produtos do Protheus")  
  
return self  
  
method getData() as object class SB1TReportsBusinessObject  
local cQuery as character  
  
//Define a quantidade máxima por página (Default 100)  
self:setPageSize(200)  
  
//Define a query do Objeto de Negócio  
cQuery := "SELECT #QueryFields# FROM " + RetSQLName("SB1") + " WHERE #QueryWhere#"  
self:setQuery(cQuery)  
  
//Define o campo de ordenação da query  
self:setOrder("B1_COD")  
  
//Define o where da query  
self:setWhere("B1_FILIAL = '"+ FWxFilial('SB1') +"' AND D_E_L_E_T_ = ' '")  
  
return self:oData  
  
method getSchema() as object class SB1TReportsBusinessObject  
  
self:addProperty("Filial", "Filial", "string", "Filial", "B1_FILIAL")  
self:addProperty("Codigo", "Codigo", "string", "Código", "B1_COD")  
self:addProperty("Descricao", "Descricao", "string", "Descricao","B1_DESC")  
self:addProperty("Tipo", "Tipo", "string", "Tipo","B1_TIPO")  
self:addProperty("Unidade", "Unidade de medida", "string", "Unidade","B1_UM")  
self:addProperty("Revisao", "Revisao", "date", "Revisao","B1_UREV")  
  
return self:oSchema
```

**![Obj_Negocio.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25977154691479)**

**Saiba mais**  
[Smart View - Protheus como Fonte de Dados Nativa](https://tdn.totvs.com/display/public/framework/Smart+View+-+Protheus+como+Fonte+de+Dados+Nativa)  
[Smart View - Criação de Objetos de Negócios](https://tdn.totvs.com/pages/releaseview.action?pageId=625448935)  
[Smart View - Annotation no objeto de negócio](https://tdn.totvs.com/pages/releaseview.action?pageId=754622417)
