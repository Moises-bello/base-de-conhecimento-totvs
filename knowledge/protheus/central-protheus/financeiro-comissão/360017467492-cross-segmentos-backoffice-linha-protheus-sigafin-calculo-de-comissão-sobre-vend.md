---
article_id: 360017467492
category: Financeiro - Comissão
content_hash: f4e9e7de2c8082a11fe5a031fe9ae96b8c9c62a7e871cfedb9badeece0ffdd23
fetched_at: '2026-06-28T22:37:50.862082+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  Calculo de comissão
  sobre vendas
type: support-article
updated_at: '2025-03-19T18:17:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017467492-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Calculo-de-comiss%C3%A3o-sobre-vendas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25839073655063)**Tempo aproximado para leitura: **05:00 min  
  
Dúvida**Como realizar o cálculo de comissão sobre vendas ?   
  
**Ambiente****Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões**  
  
**Solução**  
Segue exemplo de como é calculada a comissão para vendedores com a geração 100% na baixa do título principal, sendo o percentual da comissão definido no Item do pedido de vendas e cadastro de vendedor.

Cadastro de vendedor onde está definido que o Percentual de comissão é de 10% e de 100% na baixa do título a receber.

Inclusão do pedido de venda

O **produto P01** tem cadastrado 5% de comissão - B1\_COMIS.  
O **produto P02** tem cadastrado 2% de comissão - B1\_COMIS.  
O **produto P03** tem cadastrado 2% de comissão - B1\_COMIS.

Primeiro Item :**P01** - **Vlr** Total R$ 1000,00  
Segundo Item:**P02** - **Vlr** Total R$ 2000,00  
Terceiro Item: **P03** - **Vlr** Total R$ 3000,00

Quando o **produto** possui **% comissão,** este passa a ser o mandatório no **cálculo de comissão** do **vendedor**, ou seja, o percentual de 10% do **cadastro do vendedor** não é considerado e sim será considerado o **% de comissão** de cada **produto tabela SD2**.

Então temos:

**Comissão do P01**: R$ 1000,00 \* 5% = R$ 50,00

**Comissão do P02**: R$ 2000,00 \* 2% = R$ 40,00

**Comissão do P01**: R$ 3000,00 \* 2% = R$ 60,00

**Total Venda**: R$ 6000,00

**Total Comissão**: R$ 150,00

Ao baixar o título de R$ 6000,00 gerado pelo **pedido de venda**, será gerado a comissão no valor de R$ 150,00. E o percentual calculado se refere ao **Valor da comissão** pelo total, aplicando a regra de três.

R$ 6000,00 < - > 100%

R$ 150,00 < - > x %

x = 150,00 \* 100 /6000,00

x = 2,5% (Este é o **percentual calculado de comissão**)
