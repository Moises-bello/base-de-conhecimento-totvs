---
content_hash: b4dc51741d0e13eeb6adaabcda86a8d7f7f34b807e30466a3ea729bc8e5e7d86
fetched_at: '2026-06-29T00:09:45.995530+00:00'
page_id: '435104736'
product: rm
source: tdn-rm
title: Parâmetros - Contrato - Efetivação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104736
version: 5
---

**Etapa 1 - Consistir na efetivação**

* **Consistir na efetivação as seguintes condições:** Permite o usuário definir quais os impeditivos e alertas na efetivação da venda ou do Aditivo.

Informe para as opções abaixo se o sistema irá impedir, alertar ou não fará consistência:

* + Consistir na efetivação se existe item de venda
  + Consistir na efetivação se existe endereço do cliente
  + Consistir na efetivação se a contabilização é obrigatória
  + Consistir se foi gerado movimento para a(s) comissão(ões) cadastrada(s)

A partir do Release 12.1.2306, do TCGI, as opções desta Etapa são:

Consistir na Efetivação as seguintes condições::

* **Consistir na efetivação se existe endereço do cliente:**
* **Consistir na efetivação se a contabilização é obrigatória:**
* **Consistir se foi gerado movimento para a(s) comissão(ões) cadastrada(s); e**
* **Consistir na efetivação se existe comissão.**

Para cada uma das opções citadas acima, pode-se parametrizar as seguintes ações, que serão realizadas no momento em que o Processo para [Efetivar Contrato](https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Processo+-+Efetivar+Contrato) for executado:

* **Nenhum:** Não realiza nenhuma validação em relação ao item parametrizado com esta ação;
* **Alerta:** Valida se a condição parametrizada é atendida e caso ela não seja atendida, o sistema exibira uma mensagem de Alerta ao usuário e efetivará o contrato mesmo assim; e
* **Impeditivo:** Valida se a condição parametrizada é atendida e caso ela não seja atendida e caso ela não seja atendida o sistema exibira uma mensagem de Erro ao usuário, impedindo que o contrato seja efetivado até que esta condição seja atendida.
