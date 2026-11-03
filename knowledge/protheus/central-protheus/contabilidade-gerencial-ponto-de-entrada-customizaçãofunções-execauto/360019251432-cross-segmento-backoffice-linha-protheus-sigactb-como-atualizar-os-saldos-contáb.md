---
article_id: 360019251432
category: Contabilidade Gerencial - Ponto de entrada, Customização,Funções, Execauto
content_hash: 4715181751ee50e0cb4749170db2b56589052e97bdcc2146de0d1a240e555801
fetched_at: '2026-06-28T22:41:00.697107+00:00'
product: protheus
section_id: 1500001548462
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus -  SIGACTB: Como atualizar os saldos
  contábeis via JOB (MV_CTBJOB)?'
type: support-article
updated_at: '2021-11-30T18:46:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019251432-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-atualizar-os-saldos-cont%C3%A1beis-via-JOB-MV-CTBJOB
---

**Dúvida**Como atualizar os saldos contábeis via JOB (MV\_CTBJOB)?

**Ambiente**Protheus – Contabilidade Gerencial –  Até a versão 11.80  
  
  
**Solução**

A opção de atualização de saldos contábeis via JOB é habilitada por meio do parâmetro **MV\_CTBJOB**, que aciona a atualização a partir da tabela **CVO – Fila de saldos**.

No entanto, para o funcionamento desta modalidade o ambiente Protheus deve possuir a **Stored Procedure (CTB150)** instalada. ( Para instalar essa procedure é necessário alterar o parâmetro MV\_CTBSALD para "1", assim na instalação da procedure sera demonstrada processo 04 ao invés de 06.) Porem este mesmo parâmetro não sera considerado para definir se a atualização dos saldos será pela Stored Procedure (CTB150) ou (CTB185).

SAIBA MAIS:

<https://tdn.totvs.com/pages/viewpage.action?pageId=233748084>
