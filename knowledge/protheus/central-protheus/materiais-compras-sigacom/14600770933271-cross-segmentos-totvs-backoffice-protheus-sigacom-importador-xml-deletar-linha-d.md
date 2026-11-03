---
article_id: 14600770933271
category: Materiais - Compras (SIGACOM)
content_hash: e14c4cea0eadf5eadee0741737176327b20fb5c0944dc34ae291e7956a8f33da
fetched_at: '2026-06-28T22:41:13.010561+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM -  Importador XML - Deletar
  linha da Entrada da Nota Fiscal no Monitor
type: support-article
updated_at: '2024-06-11T12:47:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14600770933271-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML-Deletar-linha-da-Entrada-da-Nota-Fiscal-no-Monitor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19230801077655) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

Quando é realizado a importação de um XML e existe um pedido para ser vinculo na rotina do monitor, ele traz todos os itens que constam no pedido, porém um ou mais itens não é necessário para aquela nota em especifico, ao tentar excluir um item foi visto que não é possível realizar este procedimento.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS  COMPRAS-  Versão 12

**Solução**

No monitor ao vincular o pedido de compras, a nova linha gerada é criada pois foi vinculado um item do pedido em que a quantidade é menor, dessa forma é gerada automaticamente essa nova linha com saldo que não esta vinculado a nenhum pedido, para que ele possa vincular um outro PC caso deseje.

Se não quiser que essa nova linha seja gerada, deve-se vincular por Pedido/Item, assim, será perguntado se quer gerar uma nova linha com o saldo, se não quiser, se mantem o que já esta e não gera uma nova linha.

Essa opção de perguntar somente estará por item, pois é perguntado no vinculo de item a item. Por pedido não é perguntado pois ele pode ter N registros e assim ficara alertando item a item, onerando o processo, sendo que ele vinculou por pedido.

Outro ponto, é que no Monitor se faz dessa forma para se manter mais fiel ao XML, pela pre nota.

**Saiba mais em**

[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Integração Importador XML x TOTVS Transmite](http://xn--cross%20segmento%20-%20backoffice%20(linha%20protheus)%20-%20sigacom%20-%20integrao%20importador%20xml%20x%20totvs%20transmite-ulk18b/)

[TC02035 - A140IVPED - Ponto para vincular pedidos de compras ao importar um documento.](https://tdn.totvs.com/pages/releaseview.action?pageId=285649232)

[Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
