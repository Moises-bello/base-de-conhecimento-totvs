---
article_id: 360022350532
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 3bb018cc58e55ddd16eadba19191184c2b67cf3a8eb92234a942ede885430bbf
fetched_at: '2026-06-28T22:39:30.574224+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Duplicidade de INSS
  na aba duplicata do documento de entrada (MATA103) e Contas a pagar (SE2)
type: support-article
updated_at: '2021-07-29T14:37:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022350532-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Duplicidade-de-INSS-na-aba-duplicata-do-documento-de-entrada-MATA103-e-Contas-a-pagar-SE2
---

**Dúvida**Duplicidade do INSS no documento de entrada após classificar o documento onde o INSS fica duplicado na aba impostos e contas a pagar (SE2)  
   
 **Ambiente**Protheus – A partir da versão 12.1.17  
   
**Solução**

Identificamos que a duplicidade de INSS no documento de entrada (MATA103) somente ocorre quando os parâmetros MV\_VLRETIN e MV\_MININSS igual a 0 ou 0.00

Para não ocorrer mais a duplicidade do INSS, de **forma paliativa** deixe os parâmetros MV\_VLRETIN e MV\_MININSS **0.01**

**\*Importante:****Os parâmetros deverão ser preenchidos com "ponto" e não "vírgula".**
