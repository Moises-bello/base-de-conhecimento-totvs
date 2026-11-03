---
content_hash: 8c25dfe786a81b8fa469d153ad18ea58e388abeb820e55dccd90a841d6c95561
fetched_at: '2026-06-29T00:10:29.997345+00:00'
page_id: '518477913'
product: rm
source: tdn-rm
title: Código de cálculo 420 - Previdência Privada Dedutível de IRRF Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=518477913
version: 3
---

Evento tipo Desconto, valor.

**Atenção:**

* O valor a ser deduzido é limitado a 12% da base de IRRF. Caso o valor do evento com código de cálculo 420 seja menor que 12% da base de IRRF  Férias, será deduzido o valor total do evento, caso contrário , será deduzido 12% do valor da base de IRRF Férias.
* O parâmetro "Dedutível de IRRF" não deve estar marcado, pois o próprio Código de Cálculo já trata a dedução.

**Exemplos do cálculo:**

**Evento CC420 com valor inferior a 12% da base de IRRF.**

**Base de IRRF:**

Proventos = 7.273,75

Descontos = 0,00

Valor Dedutível = 0,00

Previdência Privada Total = 750,00

12% da Base Líquida de IRRF: 7.273,75 \* 12% = 872,85

Previdência Privada a Deduzir = 750,00

Base Líquida = 6.523,75

**Evento CC420 com valor superior a 12% da base de IRRF.**

**Base de IRRF:**

Proventos = 7.273,75

Descontos = 0,00

Valor Dedutível = 0,00

Previdência Privada Total = 950,00

12% da Base Líquida de IRRF: 7.273,75 \* 12% = 872,85

Previdência Privada a Deduzir = 872,85

Base Líquida = 6.400,90

|  |  |
| --- | --- |
|  | Informações Complementares |

---

[Códigos de Cálculo](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719279)
