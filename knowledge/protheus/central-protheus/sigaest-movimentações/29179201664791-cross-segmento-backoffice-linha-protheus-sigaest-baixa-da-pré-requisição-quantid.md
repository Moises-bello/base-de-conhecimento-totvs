---
article_id: 29179201664791
category: SIGAEST - MOVIMENTAÇÕES
content_hash: b35003e870907fe0a816ce37ca9051c6e34ee3af168dd2f6783936bad018803b
fetched_at: '2026-06-28T22:38:54.332433+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Baixa da Pré-requisição
  quantidade em processo de compra como dar andamento na baixa?
type: support-article
updated_at: '2025-01-13T13:52:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29179201664791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Baixa-da-Pr%C3%A9-requisi%C3%A7%C3%A3o-quantidade-em-processo-de-compra-como-dar-andamento-na-baixa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29179201646487) Tempo aproximado para leitura: **00:01:00min****Dúvida**Como realizar a baixa da Pré-requisição, como o parâmetro " Quantidade em processo de compra" com preenchimento?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Quando essa pergunta "Quantidade em processo de compra" esta populada conforme o Print abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29179201648151)

Essa pergunta é populada através de uma solicitação de compras gerada da rotina geração

Pré-requisição, para dar baixa no estoque basta seguir o passo a passo:

**1-** Existe uma configuração na rotina que modifica a visão das informações configurada, seleciona a opção ***F12*** na rotina Baixa da Pré-requisição.

**2-** Quando se configura a pergunta " Quantidade em Processo de compras" configurado conforme a imagem:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29179232514327)

Ao configurar essa pergunta o sistema entende, que será baixa toda a solicitação de compras.

**3-** Ao selecionar a opção acima, você consegui dar baixa Pré-requisição, conforme o Print:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29179201650583)

Dando a baixa, através de uma requisição, o sistema valida que tem uma solicitação de compras em aberto, vinculado a essa Pré-requisição, dessa forma o campo ***B2\_QEMPSA*** fica com a quantidade zerada, dando baixa na Pré-requisição com o  nativo do sistema.

*Saiba Mais:*

[*Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
