---
article_id: 4412354931991
category: Materiais - Compras (SIGACOM)
content_hash: 8799aec5f7215825dd96250a170f742df65e3d230179fe084c0674c45ad09017
fetched_at: '2026-06-28T22:41:11.788543+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Integração
  Gestão de Contratos X Compras
type: support-article
updated_at: '2022-10-26T13:54:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412354931991-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Compras-Integra%C3%A7%C3%A3o-Gest%C3%A3o-de-Contratos-X-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05 min** **Dúvida**

Como realizar a integração do Gestão de Contratos com o Compras?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Versão 12

**Solução**

Para os usuários do ambiente Gestão de Contratos, foi disponibilizado o campo **Filtra Medição**, no cabeçalho da janela **Documento de Entrada - Incluir**, quando selecionado facilita o processo de carga dos pedidos de compras de medições de contratos nos documentos de entrada e pré-notas de entrada.

O campo **Filtra Medição** tem por objetivo filtrar os dados apresentados nas janelas **Selecionar Pedidos de Compras - [F5]** e **Selecionar Pedido de Compras (por itens) - (F6)**, exibindo apenas os pedidos originados das medições de contratos. Além disso, serão apresentados, no canto esquerdo da janela da linha de itens, os campos **Num. Medição** (número de medição), **Num. contrato** (número do contrato) e **Num. Planilha** (número da planilha) relacionados aos pedidos de compras.

IMPORTANTE :

1. A multa ou bonificação é avaliada para cada item do **Documento de Entrada**, como no caso de um que possua três itens, as fórmulas de aplicação de multas ou bonificações são avaliadas três vezes.

2. Para utilizar esse recurso, o documento de entrada deve ter origem no **Pedido de Compras** vinculado à medição de contratos; ou seja, é necessário utilizar o procedimento de recebimento de produtos/serviços do Gestão de Contratos.

A multa é avaliada para cada registro, originado a partir de uma medição e empregado na Nota Fiscal de Entrada.

**Exemplo:**

Um documento de entrada carregou três itens de pedidos de compras com origem em três itens de medições de um contrato.

As expressões da multa serão avaliadas três vezes; ou seja, uma para cada item de medição que originou a nota fiscal.

Saiba mais em : [Integração](https://tdn.totvs.com/x/cS5KEg)
