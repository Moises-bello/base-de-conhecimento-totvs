---
content_hash: 55f8762b224e1522799d45f75a32f2908f0c748b57d1b9fe647a81b027b5cb8d
fetched_at: '2026-06-29T00:09:29.760091+00:00'
page_id: '425458257'
product: rm
source: tdn-rm
title: Inscrições Canceladas/Excluidas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458257
version: 2
---

Esta tela se refere a visão dos logs de inscrições canceladas ou excluídas. Este log é gerado através do processo de Cancelar/Excluir inscrições.

Campos que podem ser consultados na visão:

* Nome do processo seletivo
* Nome do candidato
* Nome da área ofertada
* Número da inscrição
* Tipo da operação
* Data

Campos que podem ser consultados no detalhe da visão:

* Código.
* Código da coligada.
* ID do processo seletivo.
* Número da inscrição do candidato.
* Código pessoa do candidato.
* Nome do candidato.
* Nome da área de interesse.
* Motivo do cancelamento ou exclusão.
* Tipo da operação (se é cancelamento ou exclusão).
* Data que foi realizado o cancelamento ou exclusão.
* Usuário do sistema que realizou o cancelamento ou exclusão.

Como este serviço do sistema se destina unicamente a consulta dos logs gerados, não será permitido a alteração, inclusão ou edição de nenhum dos dados apresentados.

**Impacto  no processo de cancelamento de área ofertada**

Ao cancelar inscrições através do cancelamento da área ofertada, o motivo do cancelamento/exclusão será preenchido automaticamente pelo sistema como "Área ofertada cancelada".

**Impacto  no serviço Inscrições/Resultados do Portal**

Quando uma inscrição for cancelada ela continuará sendo mostrada para o candidato. Além disso, o quadro onde constam os dados da inscrição apresentará mais dois campos: "Cancelado em" e "Motivo". Dessa forma o candidato será informado quando a inscrição foi cancelada e qual foi o motivo.Esses campos apenas serão mostrados se o status da inscrição for "Inscrição Cancelada" e se houver registro referente ao cancelamento na tabela SPSLOGINSCRICAOPS.

Quando a inscrição for excluída, esta deixará de ser mostrada em Inscrições/Resultados.
