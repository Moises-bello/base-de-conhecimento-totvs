---
article_id: 360052284234
category: RH - Folha de Pagamento
content_hash: 142315db698a31d363eab1e98bbbf8e0c63c020144bfd0ba24576e1650f155b6
fetched_at: '2026-06-28T22:44:16.367622+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema está calculando base de INSS errado
type: support-article
updated_at: '2025-08-11T21:04:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052284234-RH-Linha-Protheus-GPE-Sistema-est%C3%A1-calculando-base-de-INSS-errado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26337684939031) Tempo aproximado para leitura: 00:03:00 min**

**Ocorrência**Sistema está calculando base de INSS errado, trazendo como teto de INSS no Id 0013, valor indevido.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

1) Isso ocorre porque a tabela S001 está populada com linhas a mais do que o padrão, que hoje são 4 linhas, devido a nova tabela de INSS progressiva.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360085582613)

2) Ou se é compartilhada a tabela RCC (Manutenção de Tabelas) e for cadastrado linhas por Filial, sem necessidade. Uma vez compartilhada será visualizada para todas as Filiais. Desta forma o sistema também entende como cadastradas varias linhas e se perde, trazendo limite errado no Id 0013.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084405094)

Exemplo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084405034)

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
