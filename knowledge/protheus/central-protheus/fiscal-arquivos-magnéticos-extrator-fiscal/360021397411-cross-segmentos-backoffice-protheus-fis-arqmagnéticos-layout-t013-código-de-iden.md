---
article_id: 360021397411
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 2af8f1a53f8df1929d2fd976b149bae10089ee6fc5b8fceb33bc161234e8a728
fetched_at: '2026-06-28T22:42:07.871091+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T013
  Código de Identificação do Veículo C39_CODVEI Inexistente
type: support-article
updated_at: '2022-08-18T17:39:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021397411-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T013-C%C3%B3digo-de-Identifica%C3%A7%C3%A3o-do-Ve%C3%ADculo-C39-CODVEI-Inexistente
---

**Ocorrência**Erro 1 - Linha: 10 - O valor 'XXX1234' informado na coluna 6 para o campo Cod. de ident Veículo (C39\_CODVEI) não existe na base de dados.   
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, pois o código enviada para validação possui o caractere **"-"**, informado no campo DA3\_COD, porém quando o dado é validado no TAF esta sendo removido o caractere **"-"**.  
  
**Solução**Para solucionar esta ocorrência será necessário associar o ticket à Issue de manutenção **DSERTAF2-7237**.
