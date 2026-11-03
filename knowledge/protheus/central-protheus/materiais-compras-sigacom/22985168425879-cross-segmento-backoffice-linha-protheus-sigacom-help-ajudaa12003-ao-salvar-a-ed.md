---
article_id: 22985168425879
category: Materiais - Compras (SIGACOM)
content_hash: 4322f65f6386f462166d53270a67bcc868bcf3e42ad1b3054dd34b7ba97eafbf
fetched_at: '2026-06-28T22:41:10.591251+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - HELP AJUDA:A12003
  ao salvar a edição da cotação- NFC (PGCA010)
type: support-article
updated_at: '2025-03-12T11:29:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22985168425879-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-HELP-AJUDA-A12003-ao-salvar-a-edi%C3%A7%C3%A3o-da-cota%C3%A7%C3%A3o-NFC-PGCA010
---

**Dúvida**  
HELP AJUDA:A12003 ao salvar a edição da cotação - NFC(PGCA010).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22985198611479)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras/GCT - Protheus Release 12.1.2210.

**Solução:**

O help ocorre quando existem gatilhos indevidos criados para o campo C8\_PRECO, para verificar a existência de gatilhos indevidos deve-se acessar o Configurador > Base de Dados > Gatilhos > Filtrar > Comparar os Filtros e excluir os indevidos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23034644014871)

**Importante:** Por padrão devem existir somente os gatilhos abaixo para o campo em questão, caso existam outros os mesmos deverão ser excluídos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23034647287063)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23034644045463)

**Saiba mais em :**

[Novo Fluxo de Compras: Guia de Referências](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)
