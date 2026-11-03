---
article_id: 29623104654615
category: SIGAEST - SMARTVIEW
content_hash: 45aad6f1d76fbc6458334f6bdf88670810b38d7514fb26349b55d19894a6d349
fetched_at: '2026-06-28T22:38:47.182003+00:00'
product: protheus
section_id: 16108365627287
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - SmartView ESTSV020
  - Posição de Estoque
type: support-article
updated_at: '2026-05-05T19:55:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29623104654615-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-SmartView-ESTSV020-Posi%C3%A7%C3%A3o-de-Estoque
---

O relatório SmartView ESTSV020 - Posição de Estoque apresenta os saldos e empenhos de cada produto em estoque, mostrando também o saldo disponível (saldo menos empenhos). O artigo explica seu objetivo e como configurá-lo no TOTVS Backoffice (Protheus) a partir da versão 12.1.2310, com links para guias detalhados.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29623068845591) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Qual o objetivo do relatorio **SmartView ESTSV020 - Posição de Estoque**, e como configurar?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.2310

**Solução**

O objeto de negocio **Posição de Estoque** emite a posição dos saldos e empenhos de cada produto em estoque. Ele também mostrara o saldo disponível, ou seja, o saldo subtraído dos empenhos.

**Saiba como configurar o relatório clicando na imagem de exemplo abaixo:**

[![image-2024-11-25_13-8-40.png](https://tdn.totvs.com/download/attachments/756453251/image-2024-11-25_13-8-40.png?version=1&modificationDate=1732550921300&api=v2)](https://tdn.totvs.com/x/g48WLQ)

Em relação ao parametro: "Saldo do produto a considerar" possui o mesmo conceito do relatório TReport MATR260 onde:

* **Atual:**O parâmetro “Saldo do produto a considerar?  = Atual”, é a quantidade e valor que se encontra na tabela SB2 campos B2\_VATU1 e B2\_QATU.

* **Fechamento:**Neste caso o relatório irá imprimir a quantidade e valor, respectivamente, dos campos B2\_QFIM e B2\_VFIM1.

* **Movimento:**Quando usamos o parâmetro “Saldo do produto a considerar?  = Movimento ”, devemos também preencher o parâmetro “Data de referência? ”, onde informamos a data que desejamos buscar. Neste caso o relatório utiliza a função "**Calcest**", função contida na rotina "**MATXFUNB**" e também a Stored Procedure 14 para realizar a busca e apresentar as informações, pegando inicialmente o saldo e valor da tabela SB9 e calculando as movimentações que ocorreram no período (SD1, SD2 e SD3) para calcular a quantidade e valor a serem mostrados no relatório

Por exemplo: se o ultimo fechamento foi em Março, se você colocar o saldo a considerar = fechamento, ele vai pegar o B2\_QFIM/VFIM1 provavelmente de quando rodou o custo que preparou os saldos finais de março. Para ver o saldo na data, o mais adequado é Saldo = Movimento e Data de Referencia -> data que quer ver o saldo.

Para mais informações acesse:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR260 - Importância da pergunta "Saldo do produto a considerar?" para correta emissão do relatório](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018559171-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR260-Import%C3%A2ncia-da-pergunta-Saldo-do-produto-a-considerar-para-correta-emiss%C3%A3o-do-relat%C3%B3rio)

**Saiba mais:**

[Como configurar o SmartView](https://tdn.totvs.com/x/8WTCMQ)

[Smart View - ESTSV020 - Posição de Estoque](https://tdn.totvs.com/x/g48WLQ)

[Clique aqui e veja mais artigos sobre Relatórios SmartView do Estoque Custos](https://tdn.totvs.com/x/pwKQLg)
