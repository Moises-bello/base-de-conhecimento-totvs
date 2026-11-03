---
content_hash: 2aa5d27cf2db370f79947534389693a6b8b5d291e5511da8db0d1204103b56ff
fetched_at: '2026-06-29T00:12:03.526925+00:00'
page_id: '911837876'
product: rm
source: tdn-rm
title: 4) Parametrização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=911837876
version: 4
---

**4.1) Configurar o recebimento com cartão do TPC**

Após a contratação do produto TOTVS Pagamento Cartão, é necessário configurar o recebimento com cartão de crédito no modelo e-commerce Cyber, nosso gateway parceiro nessa jornada de recebimento. Clique [aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=421388865#ModelosE-commerce-CyberSource) para acessar a configuração.

**4.2) Configurar o RM Checkout**

Na próxima etapa, é necessário realizar a configuração do RM Checkout no sistema RM. Lembre-se de que esta etapa deve ser realizada após a integração do RM Checkout com o seu portal próprio. Para entender os requisitos dessa integração, clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=911837820).

* No RM Backoffice, acesse **Ambiente > Parâmetros > TOTVS Gestão Financeira > Contas a Receber > TOTVS RM Checkout**

* No campo "URL do Pagamento", configure com o endereço onde foi configurada a sua página de checkout durante a integração.
* O campo "Método de Pagamento" ficará bloqueado, pois a única opção disponível no momento é o recebimento com cartão via TPC. Futuramente, o RM Checkout dará suporte às soluções de PIX e boletos.
* Em "Recorrência", selecione o módulo de ativação, que define em qual módulo do RM as regras serão verificadas para aplicação da cobrança recorrente (disponível atualmente apenas para o módulo Educacional).
* As configurações podem ser realizadas por coligada ou filial.
* Clique em "Avançar" e conclua o processo.
