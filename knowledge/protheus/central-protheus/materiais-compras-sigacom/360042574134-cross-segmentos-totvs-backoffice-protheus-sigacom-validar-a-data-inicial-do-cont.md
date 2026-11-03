---
article_id: 360042574134
category: Materiais - Compras (SIGACOM)
content_hash: 0fd3688c1fd52831fb798aa495e338031a17de6ddc3fb20d4653a93e3860fe26
fetched_at: '2026-06-28T22:41:25.407780+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Validar a data inicial
  do contrato de parceria quando vinculado a AE
type: support-article
updated_at: '2022-05-18T21:25:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042574134-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Validar-a-data-inicial-do-contrato-de-parceria-quando-vinculado-a-AE
---

**Dúvida**Validar a data inicial do contrato de parceria quando vinculado a autorização de entrega (MATA122).  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**A rotina de Autorização de entrega (MATA122) permite vincular em contratos cujo a data de inicio ainda não estão em vigências (exemplo: Data inicio do contrato = 01/01/2090);

Neste caso, o contrato ainda não está apto para ser vinculado a uma AE;

Em seguida, criar o parâmetro **MV\_DTINVLD.**

**Descrição**: Valida a data inicial do contrato de parceria quando ele é vinculado a uma Autorização de entrega. T - Ativado e F - Desativado.

Tipo: **3 - Lógico**
