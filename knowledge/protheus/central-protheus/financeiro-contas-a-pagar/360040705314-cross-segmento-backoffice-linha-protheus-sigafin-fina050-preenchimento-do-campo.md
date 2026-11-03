---
article_id: 360040705314
category: Financeiro - Contas a Pagar
content_hash: 1210bc20fdaefd1c34810a2964318560d0d56a4396a66c5f25e4761031b56176
fetched_at: '2026-06-28T22:38:07.233765+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN  - FINA050 - Preenchimento
  do campo E2_LINDIG ao invés do E2_CODBAR
type: support-article
updated_at: '2023-06-30T02:16:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040705314-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Preenchimento-do-campo-E2-LINDIG-ao-inv%C3%A9s-do-E2-CODBAR
---

**Dúvida**Como fazer para  preencher o código de barras no campo **E2\_LINDIG** ao invés do **E2\_CODBAR**?  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - SIGAFIN – FINA050 – A partir da versão 11.8

**Solução**No padrão do sistema ao preencher o campo Linha digitável realmente não é preenchido o **E2\_CODBAR**. Será necessário customizar para que isso ocorra.  
Os campos possuem somente no padrão do sistema uma validação para saber se a numeração que está sendo digitada é uma numeração válida, assim como alguns sites/programas fazem validações de números de CPF, onde ao digitar um número 0123456789 irá apresentar número inválido.

**Saiba mais:**  
<http://tdn.totvs.com/display/public/PROT/FIN0052_DESCRICAO_CAMPOS_E2_LINDIG_E_E2_CODBAR>  
Estes campos são validados pela mesma função - **VLDCODBAR()** - a qual está preparada para tratar ambos os valores, porém cada qual de forma independente. Ou seja, o valor de um não é ou será atribuído ao outro.
