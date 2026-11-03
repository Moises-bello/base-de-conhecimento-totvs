---
article_id: 360051710234
category: Faturamento - Cadastros
content_hash: fc6278788ac894976593643c37aa680c46d71609205395a53ca2b7ff723a450c
fetched_at: '2026-06-28T22:38:36.523357+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus)  - SIGAFAT - Uso do campo
  "Observação" (A1_OBSERV)
type: support-article
updated_at: '2023-01-30T18:10:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051710234-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Uso-do-campo-Observa%C3%A7%C3%A3o-A1-OBSERV
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:00 min****Dúvida**Qual o uso para o campo "Observação" (**A1\_OBSERV**)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FAT - todas as versões.

**Solução**O campo "Observação" (**A1\_OBSERV**) do "Cadastro de Clientes" (**MATA030**) é utilizado pelo relatório "Estatísticas de Vendas (cliente x produto)" (**MATR780**), para inserção de informações de cliente em relatório, não foi encontrado outros relatórios que o utilize.  
  
O campo também é utilizado nas rotinas:

* **FATA801** - Rotina de exportação periódica para integração com Neogrid S&OP;
* **TMKA710** - Rotina responsável pela importação do arquivo ftp uMov.me - descontinuada;
* **CRMA540** - Rotina responsável pelo processamento da integração do uMov.Me -  descontinuada.
