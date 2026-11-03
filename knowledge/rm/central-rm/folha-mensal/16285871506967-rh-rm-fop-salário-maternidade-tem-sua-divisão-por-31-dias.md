---
article_id: 16285871506967
category: Folha Mensal
content_hash: f2e7f0aebbe86733245150b8561fe9a5ba3465133b29330524b87cd4e8523ae7
fetched_at: '2026-06-28T22:46:58.189953+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Salário maternidade tem sua divisão por 31 dias
type: support-article
updated_at: '2025-02-12T18:23:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16285871506967-RH-RM-FOP-Sal%C3%A1rio-maternidade-tem-sua-divis%C3%A3o-por-31-dias
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16288203499159)**** Tempo aproximado para leitura: **00:01:36 min**

**Duvida**  
Ao lançar a verba de Salário Maternidade para a funcionária o sistema está dividindo o valor por 31, sendo que todos os outros eventos do envelope são divididos por 30. Como proceder nesse caso?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**

O provento de licença maternidade (código de cálculo 17) sempre terá a sua divisão fixa por 31 dias, isso pode ser alterado, mas não é recomendado pois poderá retornar erro no eSocial.  Nesse caso, para solução, é necessário alterar o cálculo dos outros eventos que compõem salário para que eles fiquem com sua divisão por 31 dias. Dessa forma,  é necessário marcar o seguinte parâmetro localizado em **Configurações | Parametrizador | Folha Normal | Afastamento 1/2:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16288093190295)

Dessa forma os dias trabalhados em mês de afastamento será dividido por 31 dias, da mesma forma que a licença maternidade. Hoje, no sistema, a melhor forma é que todos os proventos façam a sua divisão por 31 dias, pois vão se igualar a licença maternidade, pois dessa forma não será retornado erro no sistema.

**Saiba Mais**

[RM - FOP - Médias: Lançamento de médias de licença maternidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015652991-RM-FOP-M%C3%A9dias-Lan%C3%A7amento-de-m%C3%A9dias-de-licen%C3%A7a-maternidade)
