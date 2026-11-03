---
article_id: 1500002027121
category: SIGAEST - MOVIMENTAÇÕES
content_hash: ab1f396572ad239a34dce9f8d16a8293afb47a10ee29309ae9a17deb3f03e1f7
fetched_at: '2026-06-28T22:38:58.636155+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: MP - SIGAEST - Protheus mudando o número do Sub-Lote na liberação de CQ
type: support-article
updated_at: '2024-10-29T17:28:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002027121-MP-SIGAEST-Protheus-mudando-o-n%C3%BAmero-do-Sub-Lote-na-libera%C3%A7%C3%A3o-de-CQ
---

**Dúvida**

Tenho produtos com controle de Sub-Lote e ao dar baixa de C.Q (MATA175) para o armazém padrão o serial do sub-lote não está seguindo o original. O que fazer neste cenário?

**Ambiente**Microsiga Protheus - Estoque - A partir da versão 12.1.17  
  
**Solução**Para este cenário, bem como transferência entre filiais, o Protheus trata o conceito de Sub-lote da seguinte forma: **"O conceito de Sub-lote é que a cada movimentação ocorrida num produto ele ganhe um novo numero de serial de sub-lote e o parâmetro MV\_MTNLOTE é especifico das rotinas de Transferência Simples ou Múltipla (MATA260 e MATA261), para permitir manter o mesmo serial ao ser transferido de um produto para outro, não tendo a abrangência em todo o sistema."**

Desta forma, rotinas como **Baixa de C.Q (MATA175)** e **Transferência entre Filiais (MATA311,MATA310)** podem mudar o número do sub-lote. Então uma alternativa seria obter um controle de rastreio das movimentações do produto com sub-lote através do relatório MATR435. Segue abaixo um exemplo de emissão deste relatório:

Parametrizações:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001985461)

Resultado:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001985481)

Desta forma podemos ver que o produto PA53 ao dar entrada, foi para o C.Q com sub-lote 000006. Mas logo na liberação assumiu o sub-lote 000007

Para customizar o processo usar o Ponto de Entrada [**XPROXLOT**](https://tdn.totvs.com/pages/releaseview.action?pageId=6089445)(Manipula Numeração do Sub-lote)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
