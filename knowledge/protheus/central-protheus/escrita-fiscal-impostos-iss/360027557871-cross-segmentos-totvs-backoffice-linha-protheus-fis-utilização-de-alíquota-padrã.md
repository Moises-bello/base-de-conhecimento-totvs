---
article_id: 360027557871
category: Escrita Fiscal - Impostos - ISS
content_hash: 5a6f4aa9097f66195f29424d380156437c36c272c8380fdcba0fc7c2fb72a8f4
fetched_at: '2026-06-28T22:39:35.262441+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Utilização de alíquota
  padrão de ISS quando o cliente utiliza a rotina FISA052
type: support-article
updated_at: '2021-06-10T13:17:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027557871-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Utiliza%C3%A7%C3%A3o-de-al%C3%ADquota-padr%C3%A3o-de-ISS-quando-o-cliente-utiliza-a-rotina-FISA052
---

**Dúvida**

Cliente utiliza a rotina FISA052 nas entradas mas não deseja que tenha o mesmo efeito na prestação de serviços (saídas - faturamento)

**Ambiente**

Protheus - Faturamento - A partir da versão 11.80  
  
**Solução**

Para clientes que utilizam a rotina FISA052 e não desejam a mesma tratativa em outro módulo, exemplo:

Na prestação de serviços, cliente deve recolher no município prestador e não no município do cliente, destacando as alíquotas diferenciadas via FISA052.

Para destacar a alíquota conforme o parâmetro MV\_MUNIC, será necessário utilizar os seguintes campos:

**C5\_ESTPRES = VAZIO**

**C5\_MUNPRES = VAZIO**

**B1\_MEPLES = EP (estabelecimento do prestador).**
