---
article_id: 1500009253322
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 318c9deab3bbb9ac65e0cfa51f2e18ceafa024a0a4a7b1913312f53548d1534f
fetched_at: '2026-06-28T22:38:43.870670+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Funcionalidade
  do botão Refresh da rotina exclusão de documento de saída MATA521A
type: support-article
updated_at: '2023-07-05T16:49:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009253322-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Funcionalidade-do-bot%C3%A3o-Refresh-da-rotina-exclus%C3%A3o-de-documento-de-sa%C3%ADda-MATA521A
---

**Dúvida**Funcionalidade do botão **Refresh** da rotina exclusão de documento de saída **MATA521A**.  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**

O botão **Refresh** tem a finalidade de reprocessar a comunicação com TSS para transmissão de cancelamento, e consequente exclusão, de Notas que, por algum motivo, não tiveram efetividade no retorno do Sefaz / Prefeitura no momento da primeira tentativa de exclusão. Ao ocorrer o reprocessamento através do **Refresh**, a Nota pode ser cancelada e excluída, ou ter seu status alterado indicando, por exemplo, uma rejeição.  
  
**Observação**: O botão **Refresh** é destinado ao reprocessamento em lote de todas as notas (independente de apresentar em filtro de browser, ou de estar flegada). Caso não seja a intenção, deve-se selecionar a(s) Nota(s) desejada e realizar novamente a tentativa de exclusão para que a Nota em questão seja reprocessada.  
  
**Importante** : Recomendamos o uso do **Schedule**, abordado nesta documentação. O schedule, quando devidamente configurado, terá o mesmo comportamento do "**Refresh**", reprocessando periodicamente as Notas, porém, de forma automática, evitando assim falha humana, visto que não depende de ação do usuário para reprocessar.  
 **Saiba mais: [FATJOBNFE](https://tdn.totvs.com/x/tr44E)**
