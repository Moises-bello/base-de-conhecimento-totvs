---
article_id: 360024254532
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: a69928294fc7633cb0e4bdd20a56c803ceb89865a4a884208daca768640edcb7
fetched_at: '2026-06-28T22:38:29.886071+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Tabela de preço para pedido
  tipo Beneficiamento
type: support-article
updated_at: '2025-10-21T19:11:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024254532-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Tabela-de-pre%C3%A7o-para-pedido-tipo-Beneficiamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35788021155863) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**

Como funciona a tabela de preço (OMSA010) para pedido tipo B - Utiliza Fornecedor?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT – Todas as versões.

**Solução**

Utilize o parâmetro MV\_PRCPOD3 que define se o preço de venda deve ser apresentado para as operações de remessa para poder de terceiro, por padrão o conteúdo é definido como 1.

Em operações onde o campo Tipo de Pedido (C5\_TABELA) no Pedido de Vendas (MATA410) está definido como tipo "N - Normal", ao alterar para tipo "B - Utiliza Fornecedor" a tabela de preço não é validada.

Para tratar isso basta:

1 - Acessar o Configurador > Ambiente > Cadastros > Parâmetros;

2 - Altere o parâmetro MV\_PRCPOD3 para o conteúdo 2;

3 - Reinicie o Smartclient e efetue o processo novamente.

**Observação:** Esta opção é somente para uso de pedidos de venda do tipo beneficiamento ou tipo normal que utilizem TES com poder de terceiros (F4\_PODER3 = R), o uso do parâmetro somente afetará o pedido de venda.

**Saiba mais:**

[Cross Segmentos - Backoffice Protheus - SIGAFAT - Precificação no módulo Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014623071-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Precifica%C3%A7%C3%A3o-no-m%C3%B3dulo-Faturamento)
