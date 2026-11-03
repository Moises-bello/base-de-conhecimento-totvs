---
article_id: 17441035491479
category: Materiais - Compras (SIGACOM)
content_hash: bd468be8e343f49efc9c38404b6bed7a7969bd14d8cb4a2058f69523953a2fe0
fetched_at: '2026-06-28T22:41:17.557850+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - É possível realizar
  a entrada de uma nota de devolução de compras emitida diretamente pelo fornecedor?
type: support-article
updated_at: '2023-09-11T18:37:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17441035491479-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-%C3%89-poss%C3%ADvel-realizar-a-entrada-de-uma-nota-de-devolu%C3%A7%C3%A3o-de-compras-emitida-diretamente-pelo-fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17441023214231) Tempo aproximado para leitura: **00:04:00 min****Ocorrência**Quero realizar a devolução de uma compra para meu fornecedor, porém ele emitiu a NF de devolução. É possível realizar a entrada de uma nota de devolução de compras emitida diretamente pelo fornecedor?  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**Por padrão quando se realizou a entrada na nota de compra, conforme a configuração do TES, informações foram integradas no sistema, como por exemplo o financeiro, o estoque, enfim, as integrações/gerações de informações ocorrem conforme o TES utilizado.  
Nesse cenário, para que sejam "estornadas " essas integrações, no caso de haver uma devolução dessa compra,  é necessário efetuar uma nota de saída a título de devolução da compra, para que o sistema gere um título no contas a pagar do tipo NDF que pode ser utilizado para compensar o saldo restante a pagar, dar saída no estoque dos produtos que entraram na nota. Mas o conceito da saída é o mesmo da entrada, ou seja, as informações serão geradas de acordo com as configurações do TES utilizado nessa saída.  
Baseado nisso, normalmente seria a sua empresa a gerar a nota de saída e o não o seu fornecedor emitir essa saída por você.  
Não conseguimos dar entrada nessa nota de devolução que o seu fornecedor emitiu, pois é necessário você efetuar a saída para regularizar as integrações.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
