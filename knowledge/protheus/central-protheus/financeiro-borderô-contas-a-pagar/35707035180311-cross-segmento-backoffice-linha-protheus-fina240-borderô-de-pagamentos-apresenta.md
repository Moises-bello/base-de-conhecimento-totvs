---
article_id: 35707035180311
category: 'Financeiro - Borderô contas a Pagar '
content_hash: f754f0ca993415c1f19955f8a89594d81fa53a60cae89a88c20b7685647891ef
fetched_at: '2026-06-28T22:37:34.942052+00:00'
product: protheus
section_id: 35057529029143
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA240 - Borderô de pagamentos
  apresentando erro RECNO
type: support-article
updated_at: '2026-03-04T16:47:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35707035180311-Cross-Segmento-Backoffice-Linha-Protheus-FINA240-Border%C3%B4-de-pagamentos-apresentando-erro-RECNO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35707035166231) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Ao realizar o borderô de pagamentos, é apresentado RECNO.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
O erro RECNO pode ser exibido em decorrência de alguns fatores relacionados à configuração dos parâmetros da rotina:

1. Parâmetro: “Considera Títulos?”

   * **Normais:** considera todos os tipos de títulos, exceto adiantamentos;
   * **Adiantamento:** considera apenas títulos de adiantamento;
   * **Ambos:** considera tanto títulos normais quanto de adiantamento.
2. **Parâmetro:** **“Considera apenas a filial logada ou todas?”**

   * Define se o processamento abrangerá somente a filial atual ou todas as filiais.
3. **Parâmetro: “Considera Forma de Pagamento?”**

   * **Sim:** considera apenas os títulos que possuem **condição de pagamento cadastrada**;
   * **Não:** considera **todos os títulos**, independentemente de possuírem ou não a forma de pagamento cadastrada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35707005778455)
