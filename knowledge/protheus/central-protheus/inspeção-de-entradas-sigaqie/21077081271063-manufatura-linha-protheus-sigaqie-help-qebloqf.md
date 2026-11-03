---
article_id: 21077081271063
category: Inspeção de Entradas (SIGAQIE)
content_hash: d08f990359d2f0cb96dfc0ed4fac8e3eb8b267f7a3651f5a3ae96341c7405359
fetched_at: '2026-06-28T22:42:27.027860+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAQIE - Help QEBLOQF '
type: support-article
updated_at: '2024-02-15T11:16:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21077081271063-Manufatura-Linha-Protheus-SIGAQIE-Help-QEBLOQF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21077111717399) Tempo aproximado para leitura: **00:00:35 min****Ocorrência**Na rotina **MATA103 - Documento de Entrada** ocorre o *help* **QEBLOQF – Não será possível incluir o produto pois mesmo foi bloqueado para o Fornecedor selecionado devido bloqueio feito pela qualidade na Inspeção de entrada**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Causa**O *help* **QEBLOQF** ocorre na rotina **MATA103** quando o fornecedor está bloqueado por ter o campo **Situação - A5\_SITU** na rotina **MATA061 - Produto x Fornecedor** como **D - Não Habilitado** e também ter o parâmetro **MV\_QBLQFOR - Habilita o bloqueio do Produto x Fornecedor que estiver com status Não Habilitado no QIE (S= Habilita bloqueio, N= Não habilita Bloqueio)** com conteúdo igual a **S - Sim.**  
  
**Solução**  
Para a não ocorrência o *help* **QEBLOQF**, na rotina **MATA061 - Produto x Fornecedor,** o campo **Situação - A5\_SITU** deve estar com conteúdo diferente de **D - Não Habilitado** e/ou o parâmetro **MV\_QBLQFOR** ter o conteúdo igual **N - Não.**
