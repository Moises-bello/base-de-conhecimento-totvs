---
article_id: 34640532862487
category: NFe - Nota Fiscal Eletrônica
content_hash: 65b28bc444e9035aa82e1ea31837fc586a725058921d64525ba56445b24f2978
fetched_at: '2026-06-28T22:40:06.899059+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - 865 Rejeição
  : Total dos pagamentos menor que o total da nota'
type: support-article
updated_at: '2025-09-03T18:21:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34640532862487-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-865-Rejei%C3%A7%C3%A3o-Total-dos-pagamentos-menor-que-o-total-da-nota
---

**Dúvida**  
Como corrigir a rejeição 865 Rejeição : Total dos pagamentos menor que o total da nota?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - Todas as versões

**Causa**  
A rejeição **865** ocorre quando o somatório do valor dos pagamentos *Tag* **vPag - id:YA03 é menor**que o total da nota *Tag***- vNF - id:W16.**  
Esta regra não se aplica para Nota Fiscal de Ajuste, *Tag* **finnfe = 3 - id:B25**e para Nota Fiscal de Devolução **finnfe=4.**

**Solução**

Para corrigir, verifique a soma dos pagamentos e ajude os valores para que o total dos pagamentos iguale o valor da nota, seja ajustando o valor das parcelas, adicionando um desconto se permitido, ou realizando uma das outras soluções descritas nos resultados. 

1. **1.****Verificar a soma dos pagamentos:**

   Some todos os valores informados no grupo de pagamento (tag <pag>) para garantir que o total do pagamento esteja correto.
2. **2.****Ajustar o valor do pagamento:**

   * **Corrija o valor das parcelas ou formas de pagamento:** Se houver um erro no preenchimento, ajude o valor de cada pagamento para que a soma dos valores seja igual ao total da nota.
   * **Adicione um desconto:** Se apropriado, adicione um desconto de forma que o valor total pago corresponda ao valor da nota.

Conforme a nova versão 1.02 da NT2025.001 a validação não ocorrera para notas modelo 55 neste primeiro momento.

Sistema Nota Fiscal Eletrônica NT2025.001 – Simplificação Operacional: Leiaute QR-Code, Resposta Assíncrona Lote 1 NF-e

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34674591208471)
