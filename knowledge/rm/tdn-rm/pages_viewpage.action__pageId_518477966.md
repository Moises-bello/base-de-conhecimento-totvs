---
content_hash: 083af1267b44fe49b3cc7edaddea9b418a9c708928017fc8908350eeb41d80b9
fetched_at: '2026-06-29T00:10:30.000592+00:00'
page_id: '518477966'
product: rm
source: tdn-rm
title: Código de cálculo 422 - Previdência Privada Dedutível de IRRF 13º Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=518477966
version: 1
---

Evento tipo Desconto, valor.

**Atenção:**

* O valor a ser deduzido é limitado a 12% da base de IRRF. Caso o valor do evento com código de cálculo 422 seja menor que 12% da base de IRRF 13º Salário, será deduzido o valor total do evento, caso contrário ,será deduzido 12% do valor da base de IRRF.
* O parâmetro "Dedutível de IRRF" não deve estar marcado, pois o próprio Código de Cálculo já trata a dedução.

**Exemplos do cálculo:**

**Evento CC422 com valor inferior a 12% da base de IRRF.**

**Base de IRRF:**

Proventos = 7.273,75

Descontos = 0,00

Valor Dedutível = 0,00

Previdência Privada Total = 750,00

12% da Base Líquida de IRRF: 7.273,75 \* 12% = 872,85

Previdência Privada a Deduzir = 750,00

Base Líquida = 6.523,75

**Evento CC422 com valor superior a 12% da base de IRRF.**

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
