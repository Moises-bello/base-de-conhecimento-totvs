---
article_id: 21536094039831
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: eedb7f1bd4df94a7802d36f0d48edea08ff913872085725b0a91c34d80c68c5c
fetched_at: '2026-06-28T22:38:44.146899+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Preenchimento do campo (E1_FILDEB)
  pelo módulo Faturamento
type: support-article
updated_at: '2024-02-22T12:09:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21536094039831-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Preenchimento-do-campo-E1-FILDEB-pelo-m%C3%B3dulo-Faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21536094034583) Tempo aproximado para leitura: **00:03:00 min****Dúvida**É possível preencher o campo (**E1\_FILDEB**) pelo módulo Faturamento?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12.  
  
**Solução**O campo (**E1\_FILDEB**) é um campo interno do sistema legado da rotina **FINA280**, que foi descontinuada na versão 12.1.17 do Protheus e que não deve ser utilizado para nenhum outro fim, podendo causar impactos em títulos que foram originalmente criados pela rotina **FINA280**.

   
Os títulos gerados pelo módulo Faturamento (**MATA460)** não preenchem o campo em questão, tendo em vista que a rotina de origem  que preenchia o campo foi descontinuada, não é  possível preencher o campo via padrão de sistema.

    
Dúvidas sobre o campo (**E1\_FILDEB**) contate o Suporte Financeiro.  
  
**Saiba Mais:**

**[DSERFINR-3836-FINA460 Valores Acessórios](https://tdn.totvs.com/x/tesTEQ)**
