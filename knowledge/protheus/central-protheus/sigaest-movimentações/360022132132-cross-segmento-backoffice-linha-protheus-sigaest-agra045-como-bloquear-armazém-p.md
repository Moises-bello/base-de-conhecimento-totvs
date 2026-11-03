---
article_id: 360022132132
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 126122b808201f783bb563f73683d1f6282c3dba57a7294aa20c634081e5970a
fetched_at: '2026-06-28T22:38:53.884347+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - AGRA045 - Como bloquear
  armazém para movimentações?
type: support-article
updated_at: '2025-03-12T12:17:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022132132-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-AGRA045-Como-bloquear-armaz%C3%A9m-para-movimenta%C3%A7%C3%B5es
---

**Dúvida**Como efetuar o bloqueio de armazém (Local de Estoque) para que não sejam movimentados saldos nele

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Para efetuar o bloqueio do Armazém é necessário incluir o campo reservado **NNR\_MSBLQL** pelo módulo Configurador. Quando ele não existe na tabela, basta criá-lo através do ícone “Campos Reservados”  conforme os passos ilustrados abaixo:

![Criando_campo_NNR_MSBLOQ.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360099810894)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Campo NNR\_MSBLQL só aparece para usuário adm?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12171324016023)

Após a criação do campo, seguir os passos:

* Acesse à rotina **AGRA045 (Locais de Estoque);**
* Selecione o armazém e clique em **“Alterar”;**
* Alterar do campo **“Bloqueado?”** para **“Sim**” (neste caso, o Protheus impedirá de selecionar este armazém em novas movimentações. Exemplo: Rotinas de Movimentações Internas (MATA240/MATA241), Transferências entre Armazéns, etc).

Porém, é importante salientar que as definições, o status e o histórico já gerados para este armazém não são invalidados ou desconsiderados, além de permanecerem na base de dados.

O bloqueio será válido apenas para as novas movimentações em que tentar selecionar o código do armazém bloqueado. Se houver tentativa de quaisquer movimentações envolvendo este armazém será apresentado o HELP REGBLOQ impedindo a movimentação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019205391)

É importante saber que o campo \_msblq é um campo reservado pelo sistema, e por isso somente o usuario adm pode visualizar.

<https://tdn.totvs.com/pages/releaseview.action?pageId=518485706>

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
