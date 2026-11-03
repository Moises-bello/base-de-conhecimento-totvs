---
content_hash: e035a1cc46078efd8b197d298b060972881a32ac2180b3a12c07626f037f36fc
fetched_at: '2026-06-29T00:09:45.952579+00:00'
page_id: '435104531'
product: rm
source: tdn-rm
title: 3930898 DEDUINTEGRACOES-3715 DT Cópia de plano de pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104531
version: 5
---

# Cópia de plano de pagamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Cópia de plano de pagamento |
| **Situação/Requisito:** | Ao copiar um plano de pagamento, era considerado para geração das parcelas do novo plano de pagamento um parcela de referência do plano de pagamento original. A parcela de referência era selecionar apenas pela menor parcela. Através da parcela de referência é calculado o intervalo de tempo entre as datas de vencimento das parcelas do plano de pagamento original na qual é replicado o mesmo intervalo para o plano de pagamento criado.  Sendo assim, ao haver N parcelas de número com N datas de vencimento diferentes, não obrigatoriamente a parcela de referência para o novo plano de pagamento era a de, naturalmente, a menor data de vencimento. |
| **Solução/Implementação:** | O sistema passa a considerar a parcela de referência como sendo a menor parcela do plano original e, dentre estas, a de menor data de vencimento na qual será utilizada como a primeira parcela para o plano de pagamento copiado.  Help: |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
