---
article_id: 39597857835159
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 70fad7ee143af4b89e96cfd43da050883666d05085dcc5bdca4d287704673995
fetched_at: '2026-06-28T22:38:58.528752+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Retorno da mercadoria
  com vinculação da Ordem de Produção (Geração de RE5)
type: support-article
updated_at: '2026-04-08T13:40:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39597857835159-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-Retorno-da-mercadoria-com-vincula%C3%A7%C3%A3o-da-Ordem-de-Produ%C3%A7%C3%A3o-Gera%C3%A7%C3%A3o-de-RE5
---

O sistema TOTVS Protheus gera automaticamente o movimento RE5 ao informar a Ordem de Produção na entrada da nota fiscal, consumindo o material e impedindo seu endereçamento no estoque. Para manter o saldo disponível, a entrada deve ser feita sem vincular à OP, permitindo o endereçamento, o empenho do material e o consumo posterior quando a produção iniciar.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39597834506007) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Por que o produto não permanece disponível para endereçamento em estoque quando o número da Ordem de Produção (OP) é informado no Documento de Entrada no momento do retorno da remessa?  
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões  
  
**Solução**  
  
Quando o número da Ordem de Produção é informado na entrada da nota fiscal, o sistema entende que o material já possui um destino definido.   
  
Ele é considerado um insumo direto da produção e o seu consumo ocorre automaticamente no momento da entrada, o que gera o **movimento RE5**. Devido a essa baixa automática, o saldo não fica disponível no estoque para o endereçamento.   
  
Caso haja a necessidade de manter o material fisicamente no estoque antes da produção, a entrada deve ser efetuada sem vinculação direta à OP, realizando o empenho e o consumo em momento posterior.  
  
**Como manter o saldo disponível para endereçar ?**

1. Realize a entrada da nota fiscal sem informar a Ordem de Produção (OP).
2. Desta forma, o movimento RE5 não será gerado e o material entrará normalmente no estoque, ficando disponível para endereçamento.
3. Faça o Endereçamento, definindo onde o material ficará armazenado fisicamente.
4. Efetue o Empenho do material, o que o deixará reservado e impedirá que seja utilizado por outra OP.
5. Realize o consumo no sistema apenas quando a produção for de fato iniciada.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39597834509463)

**Saiba mais:**  
[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
