---
article_id: 17189352285079
category: SIGAEST - MOVIMENTAÇÕES
content_hash: e5aebc9fef1814201885af326423fd16c8e8d44e3c22f48d8c0e99f83c5e9f62
fetched_at: '2026-06-28T22:38:55.601085+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - HELP SDAJADISTR ao
  tentar estornar movimentações
type: support-article
updated_at: '2026-01-13T15:29:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17189352285079-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-SDAJADISTR-ao-tentar-estornar-movimenta%C3%A7%C3%B5es
---

O erro HELP SDAJADISTR ocorre ao tentar estornar documentos após o endereçamento de produtos via rotina MATA265, que destina o saldo nas localizações. Para resolver, é necessário estornar o endereçamento do saldo para que ele volte a estar disponível para estorno da movimentação inicial. Se o saldo já foi consumido por outros processos, estes também devem ser estornados antes de concluir o estorno inicial.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17189326696471) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**

Ao tentar estonar **Documento de Entrada**, **Movimentações Internas** ou mesmo **Ordens de Produção**, apresenta o ***HELP SDAJADISTR***, como proceder para concluir o estorno?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17189478746135)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

O **HELP SDAJADISTR** é apresentado quando após a movimentação de Entrada e efetuado o processo de endereçamento do Produto pela rotina MATA265 destinando o Saldo nas Localizações.

Nesse cenário, na rotina Endereçamento de Produtos (MATA265) precisa **estornar o Endereçamento do Saldo** que foi movimentado por esse documento, para que o Saldo volte para o status de Saldo a Endereçar. Após efetuado o estorno do Endereçamento não apresenta mais o HELP permitindo concluir o estorno agora da Movimentação inicial.

**Observação Importante:** Caso após ter efetuado o Endereçamento do Saldo, e o Saldo **foi consumido por algum outro processo**, ***também é necessário estornar*** os movimentos posteriores que consumiram o Saldo para que possa concluir o estorno da movimentação inicial que apresenta o HELP SDAJADISTR.

Veja abaixo um passo a passo sobre como efetuar o estorno do Endereçamento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17189724559127)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17189775183511)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17189812827543)

***Saiba Mais:***  
[*Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
