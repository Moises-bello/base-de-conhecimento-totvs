---
article_id: 360027508832
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: d6cc4037261e463e2cd7e09ae820b9936a17ba81d189b99b41fe785396b9d20b
fetched_at: '2026-06-28T22:38:31.056050+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP - FAT - Erro no Parâmetro FWFormGridModel: Id DA1_INDLOT inválido on FWFORMGRIDMODEL:GETVALUE(FWFORMGRIDMODEL.PRX)'
type: support-article
updated_at: '2021-04-28T15:54:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027508832-MP-FAT-Erro-no-Par%C3%A2metro-FWFormGridModel-Id-DA1-INDLOT-inv%C3%A1lido-on-FWFORMGRIDMODEL-GETVALUE-FWFORMGRIDMODEL-PRX
---

**Ocorrência**

Ao incluir uma tabela de preço apresenta errorlog:   
*erro no parâmetro **FWFormGridModel: Id DA1\_INDLOT inválido on FWFORMGRIDMODEL:GETVALUE(FWFORMGRIDMODEL.PRX)*** como resolver?  
   
 **Ambiente**

Microsiga Protheus – Faturamento – A partir da versão 11.80  
   
**Solução**

O sistema esta encontrando alguma inconsistência no campo **DA1\_INDLOT**utilizado no processo que esta realizando na tabela de preço **OMSA010**. Solicito que valide:  
  
- Se o campo existe em seu **SX3**;  
- Se esta como usado no **Configurador - SIGACFG**;  
- Se o nível do campo foi alterado;  
- Se a estrutura da **SX3** do campo esta de acordo com o padrão, dicionario disponível no portal para consulta.
