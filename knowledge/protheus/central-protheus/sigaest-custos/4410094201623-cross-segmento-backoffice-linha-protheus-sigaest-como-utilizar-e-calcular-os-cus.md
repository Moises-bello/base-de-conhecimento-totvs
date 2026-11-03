---
article_id: 4410094201623
category: SIGAEST - CUSTOS
content_hash: 38a6562ca3a599965071a6e58410c8203efa348610cb2f9dddf0985c824980f9
fetched_at: '2026-06-28T22:39:00.792683+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como Utilizar e Calcular
  os Custos em Outras Moedas Utilizando o Parametro MV_MOEDACM - Custo Médio (MATA330)
type: support-article
updated_at: '2023-11-14T20:19:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410094201623-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-Utilizar-e-Calcular-os-Custos-em-Outras-Moedas-Utilizando-o-Parametro-MV-MOEDACM-Custo-M%C3%A9dio-MATA330
---

**Dúvida**

Como calcular o custo em outras moedas utilizando parâmetro MV\_MOEDACM?

**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Para calcular os custos em outras moedas como em dólar, euro ou outras moedas, basta seguir os passos abaixo:

***Uma observação é que o sistema calcula o custo até a 5° moeda, a criação além de outras moedas não afetará o custo do produto, somente terão funcionalidade nos módulos Contabilidade Gerencial e Financeiro.***

1. Configurar o parâmetro MV\_MOEDACM com a moeda que deseja calcular o custo. No padrão o sistema sempre considera a moeda 1 para preencher o custo do produto.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410092817815)

2. Preencher a taxa diária da moeda utilizada quando iniciado o primeiro acesso no dia:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410092929303)

Ou preencher a taxa da moeda referente ao dia no módulo do Compras -> Cadastro -> Moedas -MATA090:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410093576471)

3. Ao fazer um Documento de Entrada pela rotina MATA103, ao finalizar, o campo D1\_CUSTO2 será preenchido automaticamente de acordo com a taxa do dia da emissão da nota fiscal:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410093890199)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410084898839)

4. Ao efetuar uma Movimentação Interna do Estoque, no nosso exemplo será uma requisição, o sistema irá calcular de acordo com o custo médio atual na Moeda 2, o campo B2\_CM2 \* D3\_QUANT, mesmo cálculo utilizado no campo D3\_CUSTO1 na documentação abaixo:

[MP - SIGAEST - Como é calculado o campo D3\_CUSTO1 ao efetuar Movimentos Internos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005527161-MP-SIGAEST-Como-%C3%A9-calculado-o-campo-D3-CUSTO1-ao-efetuar-Movimentos-Internos-)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410094187671)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410094136983)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410085034391)

5. Para calcular o pedido de venda, segue a mesma regra que na movimentação interna do estoque, utilizando o mesmo conceito do artigo de como o sistema calcula o campo D2\_CUSTO1:

[MP - SIGAEST - Como é calculado o campo D2\_CUSTO1 ao efetuar Pedido de Venda?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005465422-MP-SIGAEST-Como-%C3%A9-calculado-o-campo-D2-CUSTO1-ao-efetuar-Pedido-de-Venda-)

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410085520279)

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410101153815)

6. Ao executar o Recálculo do Custo Médio o sistema irá recalcular e reordenar os movimentos que contém nas outras moedas.

Caso tenha dúvidas, se realmente o sistema recalculou, basta validar na tabela de processamento (CV8) e filtrar pela última execução do Custo Médio e avaliar:

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410101304343)

7. Caso queira imprimir o relatório para analisar os custos que foram gerados na segunda moeda, basta imprimir o MATR900 conforme nossa configuração, porém irá alterar apenas o parâmetro abaixo e escolher a moeda desejada:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR900 - Como configurar corretamente o relatório Kardex para análise de Custos e Movimentações?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Como-configurar-corretamente-o-relat%C3%B3rio-Kardex-para-an%C3%A1lise-de-Custos-e-Movimenta%C3%A7%C3%B5es-)

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410085758999)

Observações:

- O exemplo acima foi com base na moeda 2 para atualizar de acordo com o dólar, ou a moeda que estiver no parâmetro MV\_MOEDA2. Porém esse exemplo se adequa para outras moedas até a de número 5.

**Saiba mais:**

*[MP - SIGAEST - Data Width error - Field: B2\_VATU1 / B2\_VATU2 / B2\_VATU3 / B2\_VATU4 / B2\_VATU5. Como resolver?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003491921-MP-SIGAEST-Data-Width-error-Field-B2-VATU1-B2-VATU2-B2-VATU3-B2-VATU4-B2-VATU5-Como-resolver-)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
