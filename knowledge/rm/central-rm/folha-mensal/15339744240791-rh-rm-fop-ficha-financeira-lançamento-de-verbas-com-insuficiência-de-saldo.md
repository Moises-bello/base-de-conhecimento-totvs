---
article_id: 15339744240791
category: Folha Mensal
content_hash: aa9f23b7d1763a665226193eddd7c6e7b6c85df749b2cbb003816d76e9b82862
fetched_at: '2026-06-28T22:46:58.220446+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Ficha financeira: Lançamento de verbas com insuficiência de
  saldo '
type: support-article
updated_at: '2025-02-20T20:45:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15339744240791-RH-RM-FOP-Ficha-financeira-Lan%C3%A7amento-de-verbas-com-insufici%C3%AAncia-de-saldo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15339729982871) Tempo aproximado para leitura: **00:02:32 min** **Dúvida**Ao lançar os eventos de folha de pagamento, as verbas estão sendo geradas na aba "Verbas com insuficiência de saldo" dentro da ficha financeira. Por qual motivo isso ocorre?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**As verbas com insuficiência de saldo são lançadas quando há mais valores de desconto do que provento. Dessa forma, no mês seguinte o valor é abatido. 

Isso ocorre quando o funcionário possui o seguinte parâmetro marcado: **'Utiliza Controle de Saldo de Verbas'**, localizado em **Funcionários | Aba Parâmetros**, conforme demonstrado abaixo: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15337613226007)  
  
O controle é realizado através dos eventos com **Código de cálculo 20** e **Código de cálculo 21**. 

Para melhor entendimento, verifique a funcionalidade do campo Utiliza controle de saldo de Verbas:

Este campo disponibiliza o Controle de Saldo de Verbas. As insuficiências são os eventos cujo os descontos são maiores que os proventos. Com este parâmetro marcado, os eventos da mesma prioridade que possuem menor valor são descontados primeiro e o saldo de insuficiência de verbas no pagamento do evento de adiantamento não é descontado.

**Exemplos:**

Se o funcionário está com débito de R$ 700,00 de farmácia conveniada à empresa, e possui total de proventos R$ 500,00 o sistema armazenará o saldo relativo a diferença entre proventos e descontos (R$ 200,00) através da opção Usa Controle de Verbas.

**Observação 1:**

Para visualizar o saldo de Verbas é preciso acessar **Funcionários | Selecione o funcionário | Ficha Financeira - Aba Verbas com Insuficiência de Saldo**, veja:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15338694857367)

**Observação 2:**

Para lançar o débito do mês anterior, é necessário marcar o campo **"Lançar Verbas com Insuficiência de Saldo do mês ou período anterior**" no momento do Lançamento do grupo de eventos, para isso, acesse: **Folha Mensal | Lançamentos | Grupo de eventos**, conforme abaixo: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15338715709207)

**Saiba Mais:**

[RH - RM - FOP - Ficha Financeira](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8607912756631-RH-RM-FOP-Ficha-Financeira)

[Eventos de Cálculo](https://tdn.totvs.com/pages/releaseview.action?pageId=452719284)
