---
article_id: 10902874192663
category: Folha Mensal
content_hash: d300ee9853abe8d98a0afa84b66afaae211bf1126f6a9e781c80916cc462ece5
fetched_at: '2026-06-28T22:46:58.281990+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Considerar o valor da Previdência Privada na Dedução de IRRF
  13º Salário
type: support-article
updated_at: '2025-02-27T17:47:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10902874192663-RH-RM-FOP-Considerar-o-valor-da-Previd%C3%AAncia-Privada-na-Dedu%C3%A7%C3%A3o-de-IRRF-13%C2%BA-Sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:40 min** **Dúvida**Considerar o valor da Previdência Privada na Dedução de IRRF 13º Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

Para isso é preciso configurar o evento de Previdência Privada com o código de cálculo 442 conforme segue:

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

Saiba mais

[Código de cálculo 422 - Previdência Privada Dedutível de IRRF 13º Salário](https://tdn.totvs.com.br/pages/releaseview.action?pageId=518477966)
