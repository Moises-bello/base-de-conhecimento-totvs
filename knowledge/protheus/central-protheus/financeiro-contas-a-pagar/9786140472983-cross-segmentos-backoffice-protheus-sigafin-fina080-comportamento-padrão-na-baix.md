---
article_id: 9786140472983
category: Financeiro - Contas a Pagar
content_hash: 60157f8d0184a5aaffc0f5dc36a4b41d61a32ed192b8462923fa3b1af02b34d6
fetched_at: '2026-06-28T22:38:09.833440+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - SIGAFIN - FINA080 - Comportamento
  padrão na baixa de Pagamento Antecipado '
type: support-article
updated_at: '2022-10-26T14:52:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9786140472983-Cross-Segmentos-Backoffice-Protheus-SIGAFIN-FINA080-Comportamento-padr%C3%A3o-na-baixa-de-Pagamento-Antecipado
---

**Dúvida**Qual é o comportamento padrão ao baixar um Pagamento Antecipado com movimentação bancária no contas a pagar ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA080 - Todas as versões  
  
**Solução**Ao incluir um Pagamento Antecipado utilizando os parâmetros **F12** da rotina **FINA050  Cheque P/ Adiantamento**= Não e **Gera Mov. Banc. S/ Cheque**= Sim , será gerada a movimentação no bancária na emissão do título.

Seguindo o processo padrão, este **PA** aguarda uma futura compensação com uma **NF** por exemplo.

Contudo, caso seja feita a baixa do título de **PA**, o sistema criará uma movimentação a Receber caracterizando-se um retorno do valor ao banco.

Portanto, este procedimento só é recomendado caso a operação seja de retorno do valor pago antecipadamente.

**Saiba Mais:**[Cross Segmento Protheus - Backoffice Linha Protheus - SIGAFIN - Quais os modos de inclusão de PA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004726827-Cross-Segmento-Protheus-Backoffice-Linha-Protheus-SIGAFIN-Quais-os-modos-de-inclus%C3%A3o-de-PA)
