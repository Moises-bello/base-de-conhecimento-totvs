---
article_id: 360016778271
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: d6c5ad3f7e561e20a35ba1e967776499bf93c31621556aad51f33fd19c15ae33
fetched_at: '2026-06-28T22:38:28.536632+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Contabilização
  do custo On-Line no Documento de Saída LP 678
type: support-article
updated_at: '2023-08-30T21:32:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016778271-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Contabiliza%C3%A7%C3%A3o-do-custo-On-Line-no-Documento-de-Sa%C3%ADda-LP-678
---

**Dúvida**

Por que o lançamento contábil de custo não é realizado on line durante a geração do Documento de Saída?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -  todas as versões

**Solução**

A Contabilização do Custo, por padrão, não será gerada On Line.

Somente será gerada **Off Line** pelas rotinas **CTBANFS** ou **MATA331** (Rotina de Contabilização do Custo Médio).

Caso necessite contabilizar o conteúdo dos campo de Custo do item da nota fiscal (**D2\_CUSTO1/2/3/4**), utilize o Lançamento Padronizado **610** - **Contabilização de itens do Documento de Saída**.

**Saiba mais**: [FAT0124\_Contabilização\_Faturamento](https://tdn.totvs.com/x/Yn6ZDg)

####
