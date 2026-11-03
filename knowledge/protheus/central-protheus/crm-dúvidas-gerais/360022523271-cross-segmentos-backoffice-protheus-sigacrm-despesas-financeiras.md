---
article_id: 360022523271
category: CRM - Dúvidas Gerais
content_hash: 765aae463ab82b0fe4eeae3bc582f9465ec2ca1cfbd0f9ed42cf463996a46ec4
fetched_at: '2026-06-28T22:40:27.445351+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Despesas Financeiras
type: support-article
updated_at: '2024-04-25T11:51:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022523271-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Despesas-Financeiras
---

**Dúvida**

Qual o processo para geração da Despesas Financeiras?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da release 12  
  
  
**Solução**

Introdução sobre o que é **Despesas Financeiras**:

Efetua, de forma automática, o reembolso das despesas financeiras do vendedor/representante comercial durante sua visita ao cliente, como por exemplo combustível, hotel, pedágios, refeições, etc.

Elas são lançadas no apontamento e consideradas como custo.

A partir do processamento dessa rotina, são gerados títulos a pagar a favor do vendedor/representante comercial que apresenta código de fornecedores identificados.

**Processos para geração da despesas dentro do modulo de CRM:**

**1 -** No cadastro do vendedor, é necessário amarrar um fornecedor:

![](http://tdn.totvs.com/download/attachments/364929630/Vendedor-fornecedor.PNG?version=2&modificationDate=1527707801000&api=v2)

**2 -** Ter um apontamento de visita, pois a despesa será gerada considerando estas 2 informações, (vendedor x apontamento):

![](http://tdn.totvs.com/download/attachments/364929630/Apontamento.png?version=1&modificationDate=1527707801000&api=v2)

**3 -** Ao clicar na rotina: **FATA350** de despesa financeira, preencha os parâmetros conforme as orientações de campo, deixar o último parâmetro como implantar CP e dar OK.

![](http://tdn.totvs.com/download/thumbnails/364929630/Paramentos%20Despesa%20Fin.png?version=1&modificationDate=1527707801000&api=v2)

![](http://tdn.totvs.com/download/attachments/364929630/Des.png?version=1&modificationDate=1527707801000&api=v2)

**4 -** Despesas que foram geradas no apontamento, foram processadas corretamente:

![](http://tdn.totvs.com/download/attachments/364929630/Despesas.png?version=1&modificationDate=1527707801000&api=v2)

**5 -** Neste momento o sistema gera os títulos que irão para as contas a pagar:

![](http://tdn.totvs.com/download/attachments/364929630/Contas%20a%20Pagar.png?version=2&modificationDate=1527707801000&api=v2)

**Observação**:

Caso o número de títulos seja gerado como "0", verificar:

-> Se o vendedor possui em seu cadastro a amarração do fornecedor.

-> Se o apontamento de visita está sendo gerado para cliente, pois se estiver sendo gerado para prospect o sistema não considera e não gera a despesa.
