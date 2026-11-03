---
article_id: 360018298791
category: Financeiro
content_hash: 95f50d6f12ff57e5ad58bf0832d0ddd513f3b59170e78a9471c7dea81f3dd503
fetched_at: '2026-06-28T22:38:02.954570+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Error log Data width
  error - Field: A1_METR Value ou Data width error - Field: A2_METR Value'
type: support-article
updated_at: '2022-06-21T00:11:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018298791-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Error-log-Data-width-error-Field-A1-METR-Value-ou-Data-width-error-Field-A2-METR-Value
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência***Error log* **Data *width* *error* - *Field*: A1\_METR *Value* ou Data *width* *error* - *Field*: A2\_METR *Value***   
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois o tamanho limite do campo foi excedido.  
  
**Solução**Para solução verifique se o mesmo não atingiu o limite (ex: 9999), nesse caso aumente o tamanho do campo.  
  
Realize os seguintes passos abaixo:

* Acesse o **Configurador** > **Base de Dados** > **Dicionário** > **Base de dados**
* Selecione **Dicionário de dados** > Pesquise a tabela em questão (**SA1** ou **SA2**)
* Expandir o **Dicionário de dados** > Selecione **Campos** > Pesquise o campo em questão (**A1\_METR** ou **A2\_METR**)
* Altere os campos **Tamanho** e **Decimal** referente ao erro apresentado

**Exemplo**: *Error log Value*: -328718.000000   
Altere o campo **Tamanho** = 13  
**Decimal** = 6
