---
article_id: 360023137791
category: Contabilidade Gerencial - Integração EAI PIMS Protheus
content_hash: b710dcfe5a59969a4565b7640c72c1ffd5de59b55b8166990a96c3bf9b57d646
fetched_at: '2026-06-28T22:40:54.152206+00:00'
product: protheus
section_id: 1500001537541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGATCB - Erro na integração de
  conta contábil via EAI
type: support-article
updated_at: '2022-07-29T18:47:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023137791-Cross-Segmento-Backoffice-Linha-Protheus-SIGATCB-Erro-na-integra%C3%A7%C3%A3o-de-conta-cont%C3%A1bil-via-EAI
---

**Ocorrência**

Na integração de conta contábil via EAI retorna mensagem de inconsistência.

Logix: Erro ao receber o retorno da mensagem de "accountantAccount" via integração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020793031/mceclip0.png)

**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade gerencial – A partir da versão 11.80

**Solução**

Isto é ocasionado normalmente porque não foi realizada a configuração da conta no De/para de mensagem unica.

Esta situação pode ocorrer para outras transações que trate informações de cadastro das entidades contábeis do Protheus (Conta contábil, Centro de Custo, Item contábil  e Classe de valor)

Sendo um facilitador o **cadastro do De/Para de mensagens** é possível realizar o relacionamento dos códigos recebidos e associar com os códigos internos do **Protheus**.

Contem os códigos que  trafegam na integração  pertinentes  ao produto que envia as mensagens.

No configurador através do schedule selecione a opção De/para mensagem unica

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020871792/mceclip5.png)

Em seguida é exibida a tela conforme exemplo abaixo, que permite a inclusão, alteração e exclusão de uma configuração de um de/para correspondente a tabela que será utilizada na integração, neste caso a tabela é a CT1.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020795171/mceclip4.png)

Para esta ocorrência, selecionar a opção de alterar e inserir o código da conta contábil, de acordo com a configuração que ja existe no cadastro. Após a inclusão da conta contábil no de/para não ocorrerá a inconsistência

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360020870992/mceclip3.png)
