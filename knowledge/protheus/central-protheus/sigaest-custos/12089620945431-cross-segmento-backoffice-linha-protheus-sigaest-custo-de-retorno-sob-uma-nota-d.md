---
article_id: 12089620945431
category: SIGAEST - CUSTOS
content_hash: 649c045fa0799f58d1745d288007bf65e5b079370a603550ab8807e8d67b6952
fetched_at: '2026-06-28T22:39:00.841437+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Custo de retorno sob
  uma nota de remessa com tipo B sem controle de terceiros
type: support-article
updated_at: '2025-03-12T12:27:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12089620945431-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Custo-de-retorno-sob-uma-nota-de-remessa-com-tipo-B-sem-controle-de-terceiros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:19 min****Dúvida**Existe alguma documentação que explique a configuração e parametrização correta para que o custo médio do produto aplicado na remessa (com tipo B), a NF de retorno tenha o custo exatamente igual ao da remessa (origem) e não como uma nota de entrada, ao considerar a opção "retornar" no documento de entrada?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Ao usar o fluxo de envio para beneficiar e retorno, sem o uso do conceito remessa para terceiros e devolução, o processo ocorre de forma simples com um a nota de saída do envio e uma nota de entrada do retorno, e o custo da entrada dá-se como **qualquer nota de entrada e corretamente ordenado na ordem 100 do recalculo, ignorando o custo de origem.**

Portanto não é considerado erro do custo de devolução em relação ao custo do envio.

Como sugestão, o cliente pode configurar o processo de beneficiamento com remessa e retorno de terceiros, isto indica que o processo de beneficiamento é parte de movimentações internas de produção com suporte a emissão e entradas de notas e sua ordenação se dará na ordem 300, considerando o custo de envio e retorno, além de dar maior visibilidade e controle do estoque com relação aos envios e retornos.

Porem deve-se ficar atento que o cliente não esta fazendo um retorno com beneficiamento e esta tentando cancelar a nota de envio.

Neste caso não temos um processo facilitador de devolução do beneficiamento, e para tanto indicamos que o cliente efetue o processo manual de devolução com uma nota de entrada do Tipo 'D' e para que consiga deverá cadastrar o fornecedor como cliente, e durante a inclusão da nota deverá digitar na linha dos itens o numero da nota origem, a serie e o item da nota origem, desta forma o sistema irá gerar um movimento típico de devolução.

**Saiba mais:**

*[MP - SIGAEST - Como fazer uma análise de Custos no Protheus?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020860771)*

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
