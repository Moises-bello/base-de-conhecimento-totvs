---
article_id: 38643673155479
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 373e73afa13ad8c17cd5f9e09321793987117e586ff36d8dbd688ced932e87a1
fetched_at: '2026-06-28T22:39:09.721507+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais são as Tabelas
  de Estoque para extração da consulta Genérica  e Relatórios
type: support-article
updated_at: '2026-02-25T20:06:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38643673155479-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-s%C3%A3o-as-Tabelas-de-Estoque-para-extra%C3%A7%C3%A3o-da-consulta-Gen%C3%A9rica-e-Relat%C3%B3rios
---

O artigo esclarece quais tabelas do Protheus (SB9, SD3, SD2, SD1, SB2) são usadas em diferentes rotinas e relatórios de estoque/custos, recomendando o relatório MATR900 para análise detalhada, e fornece links para orientações sobre configuração e descontinuidade de relatórios no sistema.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38643708224663) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Gostaria de saber se tem um DE/PARA de tabelas para qual relatório ou rotina que posso utilizar para ter as informações necessárias?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Para a extração de relatórios relacionados ao estoque, as tabelas mencionadas (**SB9, SD3, SD2, SD1, SB2**) são utilizadas em diferentes rotinas e relatórios. Abaixo estão as informações relevantes:

* **SB9** - Saldos Iniciais (**MATA220**) - **MATR220**  
  **SD3** - Movimentos Internos (**MATA242**, **MATA261**, **MATA250**, **MATA103** (Beneficiamento - com o campo D1\_OP preenchido), **MATA241**, **MATA685**, **MATA681**) - Relatório **MATR300** ou **MATR860** para as rotinas de Manufatura (MATA681, **MATA250**)  
  **SD2** - Documento de Saída (Faturamento - **MATA461**/**MATA410**)  
  **SD1** - Documento de Entrada (Compras - **MATA103**)  
  **SB2** - Saldo Atual (**MATA225**) - Não há um relatório puro de saldo atual, mas há relatórios que mostram como o MATR260 e MATR900

**Consultar desses relatórios no Smart View:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Descontinuidade de Relatórios do Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23374418520087-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Descontinuidade-de-Relat%C3%B3rios-do-Estoque)

O relatório ideal para consultar essas tabelas mencionadas acima, segue o MATR900, segue um boletim da parametrização correta do relatório:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR900 - Como configurar corretamente o relatório Kardex para análise de Custos e Movimentações?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Como-configurar-corretamente-o-relat%C3%B3rio-Kardex-para-an%C3%A1lise-de-Custos-e-Movimenta%C3%A7%C3%B5es)

**Saiba mais:**

[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
