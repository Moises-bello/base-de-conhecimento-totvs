---
content_hash: c057453aaaa763df4726edc4815249ce8a0efc051abd990953fcfcef413dbe91
fetched_at: '2026-06-29T00:10:01.468240+00:00'
page_id: '452718746'
product: rm
source: tdn-rm
title: Código de cálculo 328 - Previdência Privada Dedutível de IRRF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718746
version: 2
---

Evento Desconto do tipo valor.

O valor a ser deduzido é limitado a 12% da base de IRRF. Caso o valor do evento com CC328 seja menor que 12% da base de IRRF será deduzido o valor total do evento,  caso contrario será deduzido 12% do valor da base de IRRF.

Obs.: O parâmetro "Dedutível de IRRF" não deve estar marcado, pois o próprio CC já trata a dedução.

**Ex.:**

**Evento CC328 com valor inferior a 12% da base de IRRF.**

**Base de IRRF:**

Proventos = 7.273,75

Descontos = 0,00

Valor Dedutível = 0,00

Previdência Privada Total = 750,00

12% da Base Líquida de IRRF: 7.273,75 \* 12% = 872,85

Previdência Privada a Deduzir = 750,00

Base Líquida = 6.523,75

**Evento CC328 com valor superior a 12% da base de IRRF.**

**Base de IRRF:**

Proventos = 7.273,75

Descontos = 0,00

Valor Dedutível = 0,00

Previdência Privada Total = 950,00

12% da Base Líquida de IRRF: 7.273,75 \* 12% = 872,85

Previdência Privada a Deduzir = 872,85

Base Líquida = 6.400,90
