---
article_id: 360019959152
category: Escrita Fiscal - Impostos - ICMS
content_hash: dc6abf36a990dcfbaddc32beec10a4cd1d5527a96f6d9fc8cbe80d6f76735439
fetched_at: '2026-06-28T22:39:23.997325+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Erro na planilha
  financeira CDV - Dicionário desatualizado'
type: support-article
updated_at: '2021-07-28T17:06:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019959152--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Erro-na-planilha-financeira-CDV-Dicion%C3%A1rio-desatualizado
---

**Dúvida**No pedido de venda/planilha financeira/lançamentos de apuração ao clicar em Valores Declaratórios , o sistema exibe a mensagem anexo: "Dicionário desatualizado - verifique a tabela CDV".   
   
 **Ambiente**Protheus - Fiscal - A partir da versão P12.1.17

**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
 1. Verificar se os campos abaixo estão na tabela CDV

{'CDV\_NUMITE','CDV\_SEQ','CDV\_TPMOVI','CDV\_ID','CDV\_ESPECI','CDV\_FORMUL'};

2.Na SIX deve conter 4 índices

3. Execute o UPDDISTR com o dicionário abaixo salvo na systemload

<https://suporte.totvs.com/portal/p/10098/download#detail/706376>
