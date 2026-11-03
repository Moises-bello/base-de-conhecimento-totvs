---
article_id: 4411458640535
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: 8e1e279678271d6e3aad05cb7b6a41dbfea89ecf14c3bc3ce77e6a401c447977
fetched_at: '2026-06-28T22:39:22.184976+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -Resumo da Apuração
  do imposto-Valor da UFESP
type: support-article
updated_at: '2021-10-26T02:22:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411458640535-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Resumo-da-Apura%C3%A7%C3%A3o-do-imposto-Valor-da-UFESP
---

**Dúvida**

Sistema gera no relatório MATR940 no resumo da apuração do imposto o valor da UFESP?

**Ambiente**Protheus – Fiscal – A partir da versão 11.80  
  
**Solução**

O relatório monta a mensagem no resumo do relatório utilizando o parâmetro MV\_INDXEST que tem como conteúdo default UFESP

Para gerar o valor da UFE para as demais UF deverá ser criado um parâmetro MV\_INDXEST para cada UF.

Parâmetro MV\_INDXEST = Indexador da Unidade da Federação para Taxas e impostos. (Ex.UFEMG para Minas Gerais)
