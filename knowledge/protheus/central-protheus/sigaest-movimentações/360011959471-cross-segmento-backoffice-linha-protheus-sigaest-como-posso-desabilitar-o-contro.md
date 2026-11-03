---
article_id: 360011959471
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 142d14864354dd84ab86e293ef1306515b9291f6ce290319822e1f98aec05cda
fetched_at: '2026-06-28T22:38:53.954660+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como posso desabilitar
  o Controle de Rastreabilidade (Lote - SubLote) no Protheus?
type: support-article
updated_at: '2023-01-25T18:20:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011959471-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-posso-desabilitar-o-Controle-de-Rastreabilidade-Lote-SubLote-no-Protheus
---

**Dúvida**  
Quais os procedimentos ideais para ***desabilitar o controle de Rastro*** (Lote e SubLote) do cadastro de produtos no *Protheus*?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Soluções:**

 - Essa alteração no cadastro do produto, retira o produto do *[conceito de controle de Rastreabilidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)*, somente é possível alterar com o saldo totalmente zerado. Veja os exemplos e boas práticas abaixo:

- Primeiramente deve processar as rotinas Refaz Saldos (MATA300) e Refaz Empenhos (MATA215) para atualização correta dos saldo Atual do produto;

 - Após o processamento avaliar o saldo Físico e dos Lotes do produto, **não é possível alterar caso**, tenha qualquer empenho pendente, pedidos (compra/venda) indicando Lote, reserva de Pedidos de Vendas, etc. Resumindo, na consulta F4 do produto, os campos destacados abaixo devem estar zerados. Constando apenas Saldo disponível e Saldos Atual.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11933596156567)

***CONSULTA MATC060 PARA ANALISAR QUAIS LOTES DISPONÍVIES NO SALDO***

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11933878913815)

- Com esse exemplo acima, pode efetuar uma ***requisição de todo o saldo do Lote,*** ou se preferir, ***efetuar o processo de inventário***, ***zerando o saldo do produto***.

 - Feito o processo requisitando ou inventariando o saldo. confirme o saldo novamente se esta zerado

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11934017490967)

- Alterar o campo **Rastro" (B1\_RASTRO)** para ***"Não Utiliza"*** no Cadastro do Produtos

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11934187862039)

 - ***Para finalizar:*** Efetuar uma movimentação Interna ou Inventário ***Devolvendo o Saldo do produto que foi requisitado anteriormente,*** agora sem o controle de Rastro. Pronto, agora o produto não utiliza mais o controle de Rastro.

**PROCEDIMENTO ALTERNATIVO E QUE PODE SER MAIS EFETIVO**

- Copiar o produto que controla Rastro e criar um novo código sem o controle de Rastro. Veja exemplo abaixo.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11934456868119)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11934532557207)

- Após a cópia do produto utilizar a rotina TRANSFERÊNCIAS MÚLTIPLAS (MATA261) ***destinando todo o saldo do produto que controla Lote ao Produto que não controla Lote***. Caso, desejar, pode Bloquear o cadastro do produto anterior para que não seja mais movimentado.

Observações:

- Caso, efetue o procedimento acima para todos os produtos e não for mais utilizar o Controle de Rastro, mantenha o parâmetro MV\_RASTRO desabilitado.

***Saiba mais:***

[*SIGAEST - Conceito e tabelas de controle de Lote e Endereço no Protheus*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
