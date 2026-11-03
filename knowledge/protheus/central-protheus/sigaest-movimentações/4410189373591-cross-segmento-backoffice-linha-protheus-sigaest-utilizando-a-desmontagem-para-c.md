---
article_id: 4410189373591
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 5ce81343ca6ec6f7c1f2ec07494ea9958942b051b74580b7e1608a0c34f496d2
fetched_at: '2026-06-28T22:38:58.437603+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Utilizando a desmontagem
  para controle de saldo na segunda unidade de medida
type: support-article
updated_at: '2025-04-25T19:39:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410189373591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Utilizando-a-desmontagem-para-controle-de-saldo-na-segunda-unidade-de-medida
---

**Dúvida**

Recebo um determinado produto em uma unidade de medida, porém realizo vendas em outra unidade, como posso realizar esse controle?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

|  |
| --- |
| **Importante:** *Antes de cadastrar a segunda unidade de medida em um produto que possua saldo já existente deve-se zerar o saldo do produto(Exemplo: por [inventário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020799592-MP-SIGAEST-Processo-de-Invent%C3%A1rio-Conceito-Exemplo-e-D%C3%BAvidas)), após zerar o saldo pode-se cadastrar a segunda unidade de medida e após isso dar o saldo novamente. Caso o saldo não seja zerado poderá acarretar em problemas futuros no estoque(Exemplo: erros de movimentações futuras e/ou divergência de saldo entre a primeira e segunda unidade).* |

Para cenários que existe a necessidade de controle de duas unidades, podemos usar a seguinte tratativa:

Vamos realizar o cadastro de dois produtos, cada um com uma unidade de medida diferente (B1\_UM) e preencher os campos da segunda unidade de medida que vamos controlar (B1\_SEGUM). Outro ponto importante no cadastro do produto é seu fator de conversão (B1\_CONV) e o tipo de conversão (B1\_TIPCONV).

No exemplo abaixo, realizamos o cadastro do produto "PREGO UN":

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410189366807)

Em seguida realizamos o cadastro do "PREGO CX":

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410195467159)

No exemplo acima, existe uma amarração entre os cadastros, repare que no "PREGO UN" o seu fator de conversão é 10 e o tipo de conversão está como Divisão, pois para converter, é necessário dividir a quantidade em unidades, para as caixas. Já no produto "PREGO CX" é feito a operação inversa, pois é necessário multiplicar (conforme o fator de conversão "10") para converter em UN.

Após o cadastro dos produtos, damos o saldo inicial apenas no produto "PREGO UN":

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410189681047)

OBS: Perceba que ao dar o saldo inicial o sistema já faz o cálculo da segunda unidade de medida​​.

No produto PREGO CX demos um saldo inicial zerado, pois vamos converter de UN para CX.

Após esse processo, vamos na rotina (MATA242 - Desmontagem de Produtos)

![mceclip3.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4410189872151)

**Observação**: O rateio é inserido manualmente, com o percentual do rateio do produto no custo da desmontagem. Independentemente da quantidade de produtos filhos (componentes), o rateio entre os componentes não pode ultrapassar 100%. Veja um detalhamento do rateio **[nesta documentação](https://tdn.totvs.com/pages/releaseview.action?pageId=235592716)**

Após a confirmação, a quantidade foi convertida para a segunda unidade de medida, já existindo saldo caso queira realizar alguma movimentação.

***Observações:*** Também é possível utilizar a rotina Desmontagem de produtos (MATA242) quando temos dois códigos de produtos cadastrados, um para a Unidade e outro para as Caixas, veja o exemplo de uso [clicando aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6027746860567-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-tratar-quando-efetuada-a-compra-de-produto-em-Caixa-por%C3%A9m-vendo-consumo-as-unidades-da-caixa-), ou também no vídeo abaixo.

**Saiba mais:**

*[MP - SIGAEST - MATA242 - Processo de Desmontagem de Produtos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061648474-MP-SIGAEST-MATA242-Processo-de-Desmontagem-de-Produtos)*

[*SIGAEST - Como tratar quando efetuada a compra de produto em Caixa, porém, vendo/consumo as unidades da caixa?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6027746860567-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-tratar-quando-efetuada-a-compra-de-produto-em-Caixa-por%C3%A9m-vendo-consumo-as-unidades-da-caixa-)

[*Exemplo prático de Desmontagem de Produção com rateio*](https://tdn.totvs.com/pages/releaseview.action?pageId=235592716)

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
