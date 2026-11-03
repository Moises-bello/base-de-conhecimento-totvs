---
article_id: 360021138392
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 14e5d81bc4d3e9339dc0c28a2c54fbe8d0e9d971d635a730da38e206d30c585b
fetched_at: '2026-06-28T22:39:20.475496+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Demonstração do ICMS
  ST na Aba da Apuração do Resumo ICMS ST
type: support-article
updated_at: '2024-12-30T14:46:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021138392-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Demonstra%C3%A7%C3%A3o-do-ICMS-ST-na-Aba-da-Apura%C3%A7%C3%A3o-do-Resumo-ICMS-ST
---

**Dúvida**

Não Demonstra os Valores de ICMS ST na Aba da Apuração do ICMS   
**Ambiente**

Microsiga Protheus - Livros Fiscais - A partir da versão 11.80

**Solução**

**Parâmetros:**

**MV\_ESTADO** = preenchido.  
**MV\_USASPED** = .T.  
**MV\_STUF** = Unidades Federativas que devem ser processadas na apuração das entradas e das saídas do ICMS Subst. Tributária.   
**MV\_STUFS** = Unidades Federativas que devem ser processadas na apuração das saídas do ICMS Subst. Tributaria.  
**MV\_SUBTRIB** = preenchido com estado + inscrição estadual (todos os estados que possuírem inscrição estadual para recolhimento do ICMS ST , inclusive seu estado )

**Configuração de TES:**

Cred ICMS ST (F4\_CREDST) = 2 = Retido ST

Campo da F4\_credst = 2

Miscelânia / Apurações / Apuração do icms - mata953

Imprime Credito ST = Não

Relatórios/ Oficiais / Apuração do icms - matr940  
Imprime Credito ST = Não

Assim serão demonstrados na apuração do icms st todos os estados configurados no parâmetro MV\_SUBTRIB
