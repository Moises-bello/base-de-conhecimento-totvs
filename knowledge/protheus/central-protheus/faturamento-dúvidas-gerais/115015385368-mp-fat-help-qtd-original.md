---
article_id: 115015385368
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 61214a24048e882bbdae83dca3959a2b6c84fc43e3c57a2dd50248e9d77d1d30
fetched_at: '2026-06-28T22:38:31.139464+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT- Help Qtd Original
type: support-article
updated_at: '2021-04-28T15:56:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015385368-MP-FAT-Help-Qtd-Original
---

**Dúvida**  
Ao incluir a quantidade na tela da reserva, ocorre o help Qtd.Original.  
  
**Ambiente**  
Microsiga Protheus -  versão 11 e versão 12  
  
**Solução**  
  
Acesse o SX3 o X3\_WHEN do campo C0\_QTDORIG e retire a informação a informação .F.

Em dicionários de dados padrão, o X3\_WHEN do campo deverá estar em branco.  
  
Por favor, retire a informação do campo, salve as alterações e realize novo teste.  
  
Obs. trata-se de um processo técnico para analistas com conhecimento da estrutura Protheus.
