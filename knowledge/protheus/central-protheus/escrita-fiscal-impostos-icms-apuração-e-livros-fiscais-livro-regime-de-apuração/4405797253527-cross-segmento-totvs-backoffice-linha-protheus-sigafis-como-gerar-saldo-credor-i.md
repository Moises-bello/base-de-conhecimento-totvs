---
article_id: 4405797253527
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: fc84833082991c415c933dc1eca7416ca4b4a789994d2bf4c02dd7052a6ca03b
fetched_at: '2026-06-28T22:39:22.119620+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIS - Como gerar
  saldo credor ICMS ST ? '
type: support-article
updated_at: '2023-11-13T22:43:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405797253527-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIS-Como-gerar-saldo-credor-ICMS-ST
---

**Dúvida**FIS Como gerar saldo credor ICMS ST ?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**  
O saldo credor anterior pode ser levado de forma automática através do parametro MV\_APURANT = .T. e informações no arquivo \*.ST0 na pasta system do Protheus.

A composição do saldo credor será conforme o parametro

MV\_SUBTRIB ou rotina FISA097

Exemplo:

MV\_ESTADO = SP

MV\_SUBTRIB = SP120120120120/MG120120120/RJ12010101

Na composição no arquivo AC210101.St0 referente ao mês de março

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405807794711)

Na apuração do mes de abril

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405807819287)

Emitimos uma nota fiscal de venda no valor de 27,00 de ICMS ST - estado de SP

Nova composição do saldo credor anterior do ICMS ST

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405797013143)

Dessa forma o saldo credor de SP será compensado por notas fiscais emitidas para cliente do estado de SP

O saldo credor do estado de MG será compensado por notas fiscais emitidas para clientes com destino a MG e da mesma forma para o RJ

Não havendo notas fiscais de saídas o saldo credor é mantido ou alterado se houver novas notas fiscais de devoluções.
