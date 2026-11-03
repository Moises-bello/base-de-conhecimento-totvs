---
article_id: 6922628586775
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 09c19836d1b32ac540cd8d06f1aa64470bf59f5c3c5cf2309a109ec72c9cf49f
fetched_at: '2026-06-28T22:42:00.825918+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Arq. Magnéticos - Como gerar o registro
  G126 - Outros Créditos CIAP - no Sped Fiscal?
type: support-article
updated_at: '2022-06-22T11:01:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6922628586775-Cross-Segmentos-Backoffice-Protheus-Arq-Magn%C3%A9ticos-Como-gerar-o-registro-G126-Outros-Cr%C3%A9ditos-CIAP-no-Sped-Fiscal
---

**Dúvida**Como gerar o registro **G126 - Outros Créditos CIAP** no Sped Fiscal?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**

O registro  **G126 - Outros Créditos CIAP** tem por objetivo discriminar os demais valores a serem apropriados como créditos de **ICMS** de **Ativo Imobilizado** que não foram escriturados nos períodos anteriores, quando a legislação permitir.

Este registro é gerado quando houver valor informado na rotina **Outros Créditos CIAP (FISA125)** para o período de apuração. Todos os dados do registro devem ser informados na rotina  **FISA125** para que o registro seja gerado corretamente no arquivo do **Sped Fiscal**.  
  
O campo **Per. Apuração - F0W\_PERIOD** deve ser preenchido com data dentro do período dos campos de data inicial e final do registro **0000 - Abertura do Arquivo Digital** do arquivo.  
  
Abaixo, segue link com informações quanto a rotina **FISA125** para que o registro seja gerado no padrão.

<https://tdn.totvs.com/display/public/PROT/FIS0066_Outros_Creditos_CIAP>

O registro também pode ser gerado através do ponto de entrada **SPEDG126.**

Para mais informações deste ponto de entrada consultar o link [SPEDG126 - Geração do registro G126 do SPEDFISCAL](https://tdn.totvs.com/pages/releaseview.action?pageId=6077194)
