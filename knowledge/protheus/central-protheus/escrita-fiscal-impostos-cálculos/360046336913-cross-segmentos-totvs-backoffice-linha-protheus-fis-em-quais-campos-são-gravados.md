---
article_id: 360046336913
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 9af94c20945445edeed9445a5607031ea0e00c9b6cc75aa19e9da9843d2fee27
fetched_at: '2026-06-28T22:39:30.697620+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Em quais campos são
  gravados os valores de INSS via retenção em operações de saída?
type: support-article
updated_at: '2025-12-03T12:43:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046336913-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Em-quais-campos-s%C3%A3o-gravados-os-valores-de-INSS-via-reten%C3%A7%C3%A3o-em-opera%C3%A7%C3%B5es-de-sa%C3%ADda
---

**Dúvida**  
Ao emitir documento de saída com calculo de INSS retenção, em quais campos são gravadas as os valores de INSS no Protheus?  
  
**Ambiente**Protheus - Fiscal - A partir da versão 12.1.17  
  
**Solução**

Ao emitir documento fiscal de saída com calculo de retenção de INSS, os valores são gravados nas seguintes tabelas e campos:

**Tabela SE1 - Contas a Receber**

Valor INSS - E1\_INSS  
Base INSS - E1\_BASEINS

**Tabela SF2 - Cabeçalho das Nf de Saída**

Valor INSS - F2\_VALINSS

Base de INSS - F2\_BASEINS

**Tabela SD2 - Itens de Venda da Nf**

Alq. INSS - D2\_ALIQINS  
Vlr. do INSS - D2\_VALINS

Base de INSS - D2\_BASEINS

**Tabela SFT - Livro Fiscal Por Item de Nf**Alq. INSS - FT\_ALIQINS  
Valor INSS - FT\_VALINS  
Base INSS - FT\_BASEINS

Configuração para tratamento da Retenção INSS: <https://tdn.totvs.com/pages/releaseview.action?pageId=47908798>
