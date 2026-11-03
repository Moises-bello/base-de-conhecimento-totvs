---
article_id: 23800255585687
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 6ca742866760b158711d20900c82c46206538f075b279c1b224c8d4113460039
fetched_at: '2026-06-28T22:38:55.416371+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como utilizar Potência
  de Lote para produtos com Rastro no Protheus?
type: support-article
updated_at: '2025-03-12T12:25:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23800255585687-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-utilizar-Pot%C3%AAncia-de-Lote-para-produtos-com-Rastro-no-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23800239805463) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Como utilizar **Potência de Lote** para produtos com controle de Rastreabilidade no Protheus?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

No Protheus os produtos que utilizam controle de Rastreabilidade podem controlar também sua potência por Lote ou Lote + Sublote. Esse controle permite identificar as características de potência do composto ativo de cada lote de um mesmo produto. Esse tipo de controle é muito utilizado por indústrias do ramo farmacêutico.

**Procedimentos**

Para controlar potência de lote: Informe Sim no campo **Contr. Potenc. (B1\_CPOTENC)** e qual a potência padrão no campo **Potência Pad (B1\_POTENCI).**Print com exemplo abaixo:

![POTENCIA LOTE.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/23800654170519)

Para toda entrada de saldo desses produtos, que crie um novo Lote ou Lote + Sublote e informe a respectiva potência.

Nos movimentos em que é informado um Lote ou Lote + sublote já existente, a informação da potência é automaticamente informada pelo Sistema. As consultas de Lote também apresentam essa informação.

**Exemplo:**

Uma indústria farmacêutica adquire de um fornecedor A, um Quilo de um lote de um determinado composto químico. Neste quilo fornecido, na verdade, somente cinquenta por cento, ou seja, quinhentos gramas do lote são do composto requisitado, e o restante, os outros quinhentos gramas são impurezas.

Assim, a potência deste lote é de 50%.

Já o fornecedor B utiliza outro processo de fabricação e consegue que a potência de seu lote desse mesmo composto químico, seja de 100%, o que significa que, requisitar ao fornecedor B um quilo desse lote corresponde, irá receber exatamente um quilo do composto químico, sem impurezas.

Com essa informação o Sistema pode calcular quanto ele deve requisitar, dependendo do fornecedor, para obter a quantidade que necessita.

Se a produção solicitar um quilo deste composto, é preciso requisitar, na verdade, dois quilos do fornecedor A ou um quilo do fornecedor B.

***Saiba Mais:***

*[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*

*[SIGAEST - Conceito e tabelas de controle de Lote e Endereço no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)*
