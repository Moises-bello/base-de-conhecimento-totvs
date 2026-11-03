---
article_id: 360011734912
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 1053f9fd6638b3f0c66e5d800e375e29d31cf9c3126ed53d61cc4cc5edb3ab68
fetched_at: '2026-06-28T22:38:53.948556+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como posso desabilitar
  o Controle de Endereçamento dos produtos no Protheus?
type: support-article
updated_at: '2026-05-27T14:29:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011734912-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-posso-desabilitar-o-Controle-de-Endere%C3%A7amento-dos-produtos-no-Protheus
---

**Dúvida**  
Quais os procedimentos ideais para ***desabilitar o controle de Localização*** (B1\_LOCALIZ) do cadastro de produtos no *Protheus*?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

 - Essa alteração no cadastro do produto, retira o produto do *[conceito de controle de Localização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)*, somente é possível alterar com o saldo totalmente zerado. Veja os exemplos e boas práticas abaixo:

- Primeiramente deve processar as rotinas Refaz Saldos (MATA300) e Refaz Empenhos (MATA215) para atualização correta dos saldo Atual do produto;

 - Após o processamento avaliar o saldo Físico e por Endereço do produto, **não é possível alterar caso**, tenha qualquer empenho pendente, pedidos (compra/venda) indicando Lote, reserva de Pedidos de Vendas, etc. Resumindo, na consulta F4 do produto, os campos destacados abaixo devem estar zerados. Constando apenas Saldo disponível e Saldos Atual.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11935986514583)

***CONSULTA SALDO POR ENDEREÇO (MATA226) PARA ANALISAR EM QUAIS ENDEREÇOS CONTÉM SALDO DO PRODUTO***

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11936092992279)

- Com esse exemplo acima, pode efetuar uma ***requisição de todo o saldo no Endereço,*** ou se preferir, ***efetuar o processo de inventário***, ***zerando o saldo do produto no Endereço***.

- Feito o processo requisitando ou inventariando o saldo. confirme o saldo novamente se esta zerado

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11936332524439)**

**-** Alterar o campo **Contr. Endereç " (B1\_LOCALIZ)** para ***"Não"*** no Cadastro do Produtos

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11936429976471)

 - ***Para finalizar:*** Efetuar uma movimentação Interna ou Inventário ***Devolvendo o Saldo do produto que foi requisitado anteriormente,*** agora sem o controle de Localização. Pronto, agora o produto não utiliza mais o controle de Localização.

**PROCEDIMENTO ALTERNATIVO E QUE PODE SER MAIS EFETIVO**

- Copiar o produto que controla Localização e criar um novo código sem o controle de Localização. Veja exemplo abaixo.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11936570961303)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11936617459863)

- Após a cópia do produto utilizar a rotina TRANSFERÊNCIAS MÚLTIPLAS (MATA261) ***destinando todo o saldo do produto que controla Localização ao Produto que não controla Localização***. Caso, desejar, pode Bloquear o cadastro do produto anterior para que não seja mais movimentado.

Observações:

- Caso, efetue o procedimento acima para todos os produtos e não for mais utilizar o Controle de Localização, mantenha o parâmetro MV\_LOCALIZ desabilitado.

**Saiba mais:**

*[MP - SIGAEST - Como desabilitar o Controle de Rastreabilidade (Lote - Sub-lote) no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011959471)*

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
