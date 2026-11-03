---
article_id: 22530276458903
category: NFe - Nota Fiscal Eletrônica
content_hash: 9c6e50a96caaa2a1b96cf7c0c535054d51a9295185b83475aa2e27aed60b8741
fetched_at: '2026-06-28T22:40:06.782681+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como realizar cancelamento/inutilização
  de uma nota de importação?
type: support-article
updated_at: '2025-06-03T12:15:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22530276458903-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-realizar-cancelamento-inutiliza%C3%A7%C3%A3o-de-uma-nota-de-importa%C3%A7%C3%A3o
---

**Dúvida**Como realizar um cancelamento de nota fiscal de entrada de formulário próprio de importação?   
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - todas as versões

**Solução**

Para que ocorra o cancelamento ou inutilização é necessário que seja criado registro nas Tabelas "SFT e SF3" No qual só é preenchida após a classificação da Nota Fiscal na rotina "MATA103".

Não é necessário transmitir a nota, apenas Classificar.

Uma **pré-nota** no Protheus **é apenas um cadastro** provisionando uma entrada futura no sistema, por esse motivo a digitação da pré-nota não gera financeiro, movimentação de estoque e livros fiscais, resumindo **a nota fiscal ainda não existe no sistema**, o que temos é um cadastro básico. Um dos **requisitos** para utilizar o conceito de **"inutilização/cancelamento"** é **existir** movimentação nos **livros fiscais** (Tabela SF3).

Por este motivo, não é possivel utilizar o conceito de inutilização/cancelamento de notas fiscais para registros de pré-nota.

**Solução** Uma **sugestão** neste cenário é **classificando a pré-nota** utilizando uma **TES** que gere **livros fiscais**, somente dessa maneira poderíamos transmitir o cancelamento no qual necessita da SFT e SF3

Após a nota classificada siga as orientações abaixo:

**- Cancelamento de NFE:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como cancelar (cancelamento) uma nota fiscal eletrônica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018751111--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-cancelar-cancelamento-uma-nota-fiscal-eletr%C3%B4nica?source=search)

**- Inutilização :**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como realizar Inutilização de uma nota fiscal eletrônica ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017458472--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-realizar-Inutiliza%C3%A7%C3%A3o-de-uma-nota-fiscal-eletr%C3%B4nica-?source=search)
