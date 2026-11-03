---
article_id: 360023262111
category: Contabilidade Gerencial - Error log
content_hash: c605c85c27a6b09ab11879e618e437c8e3737533ebc96b9095095c57244c8c26
fetched_at: '2026-06-28T22:40:52.023960+00:00'
product: protheus
section_id: 1500001537581
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Error.log de semáforo
  na contabilização
type: support-article
updated_at: '2021-12-10T18:46:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023262111-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Error-log-de-sem%C3%A1foro-na-contabiliza%C3%A7%C3%A3o
---

**Ocorrência**Ao efetuar uma contabilização é apresentado o error.log: on CTBPROCTMP(CTBXSEM.PRW)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021040251/mceclip0.png)

**Ambiente**Protheus - Contabilidade Gerencial - 12.1.17

**Causa**

Este erro é apresentado por conta do arquivo "**\_ctbprocXX.dtc**" estar corrompido.

**Solução**Para solucionar a questão, acesse o diretório do arquivo **\_ctbprocXX.dtc**(Geralmente na pasta system), renomeie-o ou faça um backup e exclua-o do diretório.

\*Sugerimos que efetue o procedimento em ambiente de testes primeiro para validações.

Após isso, o próprio sistema recriará o arquivo de forma consistente e pronto para uso do sistema ao efetuar um novo lançamento, assim, o erro não será mais reproduzido.
