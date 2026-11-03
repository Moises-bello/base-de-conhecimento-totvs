---
article_id: 360021793471
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 66d1b21cdadc31fdac9258ca44ec2cd42a927fbe0abed9fc50538ec878671e1e
fetched_at: '2026-06-28T22:39:31.041182+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Help F4_CFERR ao cadastrar
  um TES
type: support-article
updated_at: '2021-07-29T12:45:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021793471-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Help-F4-CFERR-ao-cadastrar-um-TES
---

**Dúvida**Ao cadastrar novo TES é apresentado HELP F4\_CFERR.

**Ambiente**Protheus – Livros Fiscais– A partir da versão 12.1.17  
  
   
**Solução**O HELP é apresentado quando inclui um CFOP de saída em um TES de entrada.

Por exemplo:

O campo Cod. do Tipo (F4\_TIPO) foi configurado com código 100 (TES entrada) e ao preencher o campo Cod. Fiscal (F4\_CF) com CFOP 5.102 irá ocorrer a mensagem de Help.

Para que isso não ocorra, informe um CFOP correspondente a operação - Ex: 1.102.
