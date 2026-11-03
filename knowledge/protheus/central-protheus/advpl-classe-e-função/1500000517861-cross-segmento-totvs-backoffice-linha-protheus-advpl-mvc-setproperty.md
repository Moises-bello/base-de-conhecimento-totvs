---
article_id: 1500000517861
category: ADVPL - Classe e Função
content_hash: f4dbb4ebf3d79be43f8c8ff2b101ca3fe541c5832e6826970a394a37502ace11
fetched_at: '2026-06-28T22:40:17.050655+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - MVC - SetProperty
type: support-article
updated_at: '2022-04-13T11:48:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000517861-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-MVC-SetProperty
---

**Dúvida**  
Como mudar a propriedade do campo em ***MVC*** em tempo de execução ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL – A partir da versão 12.  
  
**Solução**

Para alterarmos uma propriedade do ***MVC*** podemos utilizar o método ***SetProperty***(), porém antes é necessário recriar o bloco *BuildFeature* através da classe ***FwBuildFeature***()  
**Exemplo:**

`bBloc:=FWBuildFeature(STRUCT_FEATURE_VALID,"U_zMyVal(), .T.")`

`oStFilho:SetProperty("B2_COD", MODEL_FIELD_VALID,bBloc )`

**Observação:**  
Quando chamamos a função diretamente no dicionário ***SX3***o ***MVC*** faz isto automaticamente.  
  
**Saiba Mais**  
**[FWBuildFeature](https://tdn.totvs.com/display/framework/FWBuildFeature%C2%A0)**

**[FWFormModelStruct](https://tdn.totvs.com/display/framework/FWFormModelStruct)**
