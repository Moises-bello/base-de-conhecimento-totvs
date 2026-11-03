---
article_id: 360055315414
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: db076c2f3bfccb6362633c3aaedc8052fe5f6d5ffbdb3392e7b46e346b66e61f
fetched_at: '2026-06-28T22:36:56.517931+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus- SIGAEEC-  Erro no Embarque
  Tentativa de Registro no Alias EEQ em EOF Stack de chamadas em MSRLOCK. '
type: support-article
updated_at: '2023-10-25T13:25:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055315414-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Erro-no-Embarque-Tentativa-de-Registro-no-Alias-EEQ-em-EOF-Stack-de-chamadas-em-MSRLOCK
---

**Dúvida**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095925493)**

No Easy Export Control (SIGAEEC) integrado aos módulos de Faturamento (SIGAFAT) e Financeiro (SIGAFIN), na rotina de manutenção de processo de embarque que já possua data de embarque informada, ao retirar a data de embarque do processo o sistema apresenta mensagem de impedimento do bloqueio do registro e possibilita apenas a execução de cancelamento da operação com rollback da transação, abortando todo o processo de estorno dos demais títulos no modulo Financeiro. A falha acontece quando o sistema tenta estornar a baixa do titulo financeiro gerado pela nota fiscal de saída emitida no modulo de faturamento.   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – Todas versões

**Solução**Foram implementados os devidos ajustes dos arquivos de processamento da integração de baixa e estorno de baixa de títulos financeiros originados na rotina de embarque durante a retirada da data do embarque. Desta forma, ao retirar a data de embarque do processo, caso haja.

Deve ser atualizado com o pacote DTRADE-5123 e substituído os arquivos Avlinks disponibilizados no anexo do pacote acumulado do comex: [Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Pacote Acumulado Comex](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047332793)
