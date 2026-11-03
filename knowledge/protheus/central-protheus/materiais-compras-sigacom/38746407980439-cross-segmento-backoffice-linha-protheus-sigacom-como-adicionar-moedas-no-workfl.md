---
article_id: 38746407980439
category: Materiais - Compras (SIGACOM)
content_hash: 67600715f2a20a0d30017489769dabd51d8813b57f0ddcff54661fa45708610b
fetched_at: '2026-06-28T22:41:07.264883+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Como adicionar moedas
  no workflow no Novo Fluxo de Compras - NFC (PGCA010)?
type: support-article
updated_at: '2026-03-02T18:32:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38746407980439-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Como-adicionar-moedas-no-workflow-no-Novo-Fluxo-de-Compras-NFC-PGCA010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38746735282967) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Como adicionar moedas no workflow no Novo Fluxo de Compras - NFC (PGCA010)?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras/GCT - Protheus Release 12.1.2210.

**Solução**

Para o processo temos o parâmetro MV\_NFCMOED que define quais serão as moedas demonstradas para o preenchimento do fornecedor.

* **MV\_NFCMOED** - Parâmetro que verifica se o cadastro da moeda será utilizado da tabela CTO ou do parâmetro MV\_MOEDA, onde 1=CTO(Default) / 2=MV\_MOEDA

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38746424256407)

Observação: O campo moeda sempre é gerado preenchido com a moeda 1, dessa forma é necessário apagar o preenchimento do campo para selecionar outras moedas.

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
