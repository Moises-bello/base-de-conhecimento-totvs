---
article_id: 6864596640151
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: bd20b9442fc240d83765afdca343d222ea8406fbed500c9e839c0fcccd159224
fetched_at: '2026-06-28T22:38:41.179623+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS BackOffice (Linha Protheus) - SIGAFAT – Campos C6_INFAD
  e C6_CODINF no Pedido de Vendas
type: support-article
updated_at: '2022-06-20T15:12:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6864596640151-Cross-Segmentos-TOTVS-BackOffice-Linha-Protheus-SIGAFAT-Campos-C6-INFAD-e-C6-CODINF-no-Pedido-de-Vendas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual o conceito e utilização dos campos C6\_INFAD e C6\_CODINF no Item do Pedido de Vendas?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões

**Solução**O campo **C6\_INFAD** é um campo do tipo **MEMO**, todo campo **MEMO** quando preenchido tem suas informações levadas para a tabela **SYP - Descrição dos Campos Memo**.

Todo campo **MEMO** precisa de um campo transportador para chegar com o seu texto e chave de informação armazenados para a tabela **SYP**. Isso ocorre desta maneira, neste caso , os campos MEMO onde são colocadas as informações não estão na memória de suas respectivas tabelas, então registram sua chave de informação em campos transportadores para que eles transportem pelas tabelas a informação corretamente.

Para ilustrar, note que na tabela SC6, apesar de vermos na tela do sistema e podermos colocar informações nele, na tabela não está gravado o campo MEMO **C6\_INFAD**, só o campo **C6\_CODINF** que recebeu a chave de informação dele:

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6864595236631/mceclip11.png)

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6864581211927/mceclip12.png)

Nesse exemplo, nosso campo de entrada é o **C6\_INFAD**, que passará seu conteúdo para o campo transportador **C6\_CODINF**, que terá como destino os campos **YP\_CHAVE** e **YP\_TEXTO** na tabela de destino dos campos MEMO **SYP**.

Temos a estruturação do transporte de informações desta maneira:

Exemplo: Um pedido de venda salvo que teve no campo **C6\_INFAD** a informação colocada "**TESTE 1**":

**C6\_INFAD (Inf. Ad. Pro) --> C6\_CODINF (Cod. Inf) [LEVA A CHAVE DA INFORMAÇÃO]**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6864433102103/mceclip2.png) ![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6864419680151/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6864434991127/mceclip4.png) ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6864416296087/mceclip1.png)

**C6\_INFAD (Inf. Ad. Pro) --> C6\_CODINF (Cod. Inf) --> YP\_CHAVE [LEVA A CHAVE DA INFORMAÇÃO]**

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6864476859031/mceclip7.png)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6864477089559/mceclip8.png)

**C6\_INFAD (Inf. Ad. Pro) --> C6\_CODINF (Cod. Inf) --> YP\_TEXTO [LEVA A INFORMAÇÃO GRAVADA]**

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6864478206487/mceclip9.png)

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6864493347607/mceclip10.png)

**Tabela SYP - Descrição dos Campos Memo:**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6864474520343/mceclip5.png)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6864476377495/mceclip6.png)

YP\_FILIAL: De qual filial veio a informação (Em branco todas as filiais podem ver, a tabela é compartilhada)

YP\_CHAVE: Chave da informação trazida pelo campo transportador.

YP\_SEQ: Sequência de gravação de informações vindas do mesmo campo (local).

YP\_TEXTO: Texto colocado pelo usuário (será transportador)

YP\_CAMPO: Campo que transportou a variável até a tabela SYP.
