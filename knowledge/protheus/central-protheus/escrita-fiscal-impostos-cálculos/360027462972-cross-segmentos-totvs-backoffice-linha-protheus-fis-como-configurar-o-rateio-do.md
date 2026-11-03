---
article_id: 360027462972
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 87a4ba51859c1a886cb8d3dee9dd7d26dd756ae60c14d1c786dfce57c2e91436
fetched_at: '2026-06-28T22:39:30.669489+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como configurar o
  rateio do PCC nos títulos do documento de entrada?
type: support-article
updated_at: '2025-11-21T17:40:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027462972-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-rateio-do-PCC-nos-t%C3%ADtulos-do-documento-de-entrada
---

**Dúvida**

Como definir se o PCC - PIS, COFINS e CSLL - serão rateados ou não pelo número de títulos a pagar de uma nota fiscal de entrada?  
   
 **Ambiente**

Protheus – Compras – A partir da versão 11.80.  
  
**Solução**

Por meio da configuração dos parâmetros **MV\_RATPIS, MV\_RATCOF e MV\_RATCSLL** é possível definir se o PCC serão rateados ou não. As configurações possíveis dos parâmetros são:  
T - Rateia  
F - Não rateia

1 - Acesse o Configurador >Ambientes -> Cadastros -> Parâmetros   
2 - Localize o parâmetro MV\_RATPIS, MV\_RATCOF e MV\_RATCSLL.  
3 - Clique em alterar e informe o conteúdo desejado, conforme a regra de negócio da empresa.
