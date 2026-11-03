---
article_id: 4411764393751
category: SIGAACD - Automação e Coleta de Dados
content_hash: 7a54539ceeeb8be87ddad940e20d9e7495db0fb4bec7d258391ac8eaa0c36853
fetched_at: '2026-06-28T22:39:12.720308+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Error.log gerando
  perda de conexão e travamento de usuário no Monitor
type: support-article
updated_at: '2021-10-29T12:16:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411764393751-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Error-log-gerando-perda-de-conex%C3%A3o-e-travamento-de-usu%C3%A1rio-no-Monitor
---

**Ocorrência**

O Coletor de Dados se conecta no SIGAACD porém fica perdendo a conexão deixando o usuário preso no monitor. É gerado o error.log THREAD ERROR - stack depth overflow in function FWRETFLAV on FWRETFLAV(FWFLAVOUR.PRW)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Causa**Normalmente este error.log quando envolvido na parte de conexão do coletor é causado por colaterais de customizáveis (Pontos de Entrada, Funções de Usuário, etc).

**Solução**

É recomendável que no error.log, busque pelos termos "U\_" e "XX7" para identificar se existem funções e Pontos de Entrada envolvidos no erro. Com isso, é recomendável que efetue uma testagem eximindo o Sistema destes customizáveis.

Para desabilitá-los, basta:

- No appserver.ini, habilitar a chave IXBLOG com conteúdo NORUN, conforme exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411764334615/mceclip0.png)

Outra forma para garantir que não sobrou nenhuma validação de customizável, a desativação pode ser feita também via Configurador, através do Catálogo de Personalização. Veja no artigo abaixo o detalhamento do processo:

[MP - FRAME - Desabilitar Customizações e Pontos de Entrada pelo Catálogo de Personalização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024863633-MP-FRAME-Desabilitar-Customiza%C3%A7%C3%B5es-e-Pontos-de-Entrada-pelo-Cat%C3%A1logo-de-Personaliza%C3%A7%C3%A3o)

Após isso, provavelmente o problema já não será mais reproduzido. Desta forma, a recomendação seria de uma reavaliação dos customizáveis que apareceram no log do erro para que não impacte no coletor.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*
