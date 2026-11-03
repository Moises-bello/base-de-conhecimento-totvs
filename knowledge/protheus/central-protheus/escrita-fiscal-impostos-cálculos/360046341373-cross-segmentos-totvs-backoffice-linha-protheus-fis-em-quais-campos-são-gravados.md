---
article_id: 360046341373
category: Escrita Fiscal - Impostos - Cálculos
content_hash: eb0b19aa87bff93f7c62b83a3f1eed71b7a48e4756d09183dc93fc53d411b3bf
fetched_at: '2026-06-28T22:39:30.694577+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Em quais campos são
  gravados os valores de INSS via Retenção em Operações de Entrada?
type: support-article
updated_at: '2021-07-29T12:42:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046341373-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Em-quais-campos-s%C3%A3o-gravados-os-valores-de-INSS-via-Reten%C3%A7%C3%A3o-em-Opera%C3%A7%C3%B5es-de-Entrada
---

**Dúvida**Ao dar **entrada** em um documento com calculo de INSS retenção, em quais campos são gravadas as os valores de INSS no Protheus?  
  
**Ambiente**Protheus - Fiscal - A partir da versão 12.1.17  
  
**Solução**

Ao dar **entrada** em um documento fiscal com calculo de retenção de INSS, os valores são gravados nas seguintes tabelas e campos:

**Tabela SE2 - Contas a Pagar**

Base INSS - E2\_BASEINS

Valor do INSS - E2\_INSS

Vlr. Ret. INSS - E2\_VRETINS  
  
**Tabela SF1 - Cabeçalho das Nf de Entrada**Valor INSS - F1\_INSS  
Base de INSS - F1\_BASEINS  
  
**Tabela SD1 - Itens das Nf de Entrada**Alq. INSS - D1\_ALIQINS

Vlr. do INSS - D1\_VALINS  
Base de INSS - D1\_BASEINS  
  
**Tabela SFT - Livro Fiscal Por Item de Nf**Alq. INSS - FT\_ALIQINS  
Valor INSS - FT\_VALINS  
Base INSS - FT\_BASEINS

Configuração para tratamento da Retenção INSS: <https://tdn.totvs.com/pages/releaseview.action?pageId=47908798>
