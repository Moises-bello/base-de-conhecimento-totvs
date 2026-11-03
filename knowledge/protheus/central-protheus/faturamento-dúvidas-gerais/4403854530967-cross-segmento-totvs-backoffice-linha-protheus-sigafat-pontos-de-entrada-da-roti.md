---
article_id: 4403854530967
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 20e9642e02aeb3a7dd0e934241948b1c6003ea921fd7fc78b01506e27adca66b
fetched_at: '2026-06-28T22:38:28.639414+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Pontos de Entrada
  da rotina MATA530
type: support-article
updated_at: '2022-05-11T17:52:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403854530967-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pontos-de-Entrada-da-rotina-MATA530
---

**Dúvida**Quais são os pontos de entrada existentes na rotina de Atualização de Pagamento de Comissões (**MATA530**)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 11.80.  
  
**Solução**

Abaixo a lista com os pontos de entrada existentes na rotina de Atualização de Pagamento de Comissões, e seus endereços de documentação no TDN:

**- MSE2530 -** É chamado antes da atualização do arquivo SE2 (Contas a Pagar) e antes da atualização dos Lançamentos Contábeis: **<https://tdn.totvs.com/x/PIVn>**

**- M530AGL -** Filtro de condições selecionadas: **<https://tdn.totvs.com/x/AYZn>**

**- M530TIT -** Manipulação de dados do título: **<https://tdn.totvs.com/x/AoZn>**

**- M530FIM -** Atualização de data: **<https://tdn.totvs.com/x/z4Vn>**

**- M530DIRF -** Preenchimento dos campos para Dirf no pagamento de Comissão: **<https://tdn.totvs.com/x/MgHnAg>**

**- M530OK -** Atualiza Pagamento de Comissão: **<https://tdn.totvs.com/x/PIZn>**
