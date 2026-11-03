---
article_id: 6734569355159
category: Materiais - Compras (SIGACOM)
content_hash: 6a545ffad7694cb81f41f2317b8e9821776a6569a96e92f1ed1fcd8cc6c674ad
fetched_at: '2026-06-28T22:41:20.034972+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - Liberação de Documento
  com outra moeda (MATA094)
type: support-article
updated_at: '2026-05-14T16:48:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6734569355159-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-Libera%C3%A7%C3%A3o-de-Documento-com-outra-moeda-MATA094
---

**Dúvida**  
Como funciona na tela de Liberação de Documento (**MATA094**) o valor total do documento que é criado outras moedas ?

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Todas as versões.

**Solução**  
Ao criar um pedido de compra em outra moeda (ex: Euro, Dólar) por padrão o sistema irá mostrar o valor total na liberação do documento em REAL, caso o Aprovador esteja cadastrado na moeda "REAL":

Exemplo:

Pedido de compra Dólar:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33859816305815)

O Padrão ao visualizar a liberação do pedido (MATA094) mostra o valor convertido conforme a taxa:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33859810365847)

Para que seja aprovado na moeda Dolar, é necessário realizar o ajuste abaixo no cadastro de aprovador

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33859816309527)

Após isso mostrará na moeda escolhida:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33859816310295)

***Obs:***

Por padrão, na tela de Aprovação de Documentos, o valor do documento será exibido no valor conforme a moeda do cadastro do Aprovador.

Ou seja, o valor do pedido na moeda que o pedido foi incluído será convertido para o valor da moeda na qual o Aprovador que esta fazendo a aprovação possui em seu cadastro.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
