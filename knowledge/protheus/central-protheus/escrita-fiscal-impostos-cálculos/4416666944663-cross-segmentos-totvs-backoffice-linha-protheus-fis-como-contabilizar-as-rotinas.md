---
article_id: 4416666944663
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 3df78a683bd8fbf1c32f4c894ab88e8bc7535f117863a1d6009812d6eb7fd773
fetched_at: '2026-06-28T22:39:30.533274+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como contabilizar
  as rotinas MATA910 e MATA920 com lançamento padrão?
type: support-article
updated_at: '2021-12-21T18:05:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416666944663-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-contabilizar-as-rotinas-MATA910-e-MATA920-com-lan%C3%A7amento-padr%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como contabilizar as rotinas MATA910 e MATA920 com lançamento padrão?  
  
**Ambiente**CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Todas as versões  
  
**Solução**

|  |  |
| --- | --- |
| **Produto:** | Microsiga Protheus |
| **Ocorrência:** | Contabilização das rotinas MATA910 e MATA920 com Lançamento Padrão. |
| **Ambiente:** | SIGAFIS |
| **Passo a passo:** | Para a contabilização da rotina **MATA910 (Nota Manual Entrada) /MATA920 (Nota Manual Saída)** utilize a rotina MATA997 (Contabilização), encontrada no módulo **Fiscal / Miscelânea / Acertos**.  A mesma utiliza os códigos de LP 6A7 e 6B7, onde:  **6A7** - Documento de Entrada Manual - Inclusão de Documento Itens  **6B7** - Documento de Saída Manual - Inclusão de Documento Itens  Para que seja possível a contabilização da exclusão das notas é necessário que a contabilização da inclusão das notas tenham sido realizadas e também que esteja configurado no sistema os lançamentos padrões onde:  **6A8** - Documento de Entrada Manual - Exclusão de Documento Itens  **6B8** - Documento de Saída Manual - Exclusão de Documento Itens. |
