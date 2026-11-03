---
article_id: 31723369345687
category: Faturamento - Integrações
content_hash: 21c0092e98c596a9e7e9f0a29d5bfc5cbf16bd1e713e9e3ddfc9bc5de1acc8f9
fetched_at: '2026-06-28T22:38:26.523965+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Ponto de entrada GVFLDCJ
type: support-article
updated_at: '2025-04-29T19:08:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31723369345687-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Ponto-de-entrada-GVFLDCJ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31723369306135) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Qual o exemplo do ponto de entrada GVFLDCJ?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

O ponto de entrada GVFLDCJ permite adicionar campos personalizados da tabela de cabeçalho do Orçamento (SCJ) a serem apresentados no Portal Gestão de Vendas.

Estes campos serão utilizados considerados no Resumo do Orçamento e serão enviados com seus valores digitados pelo vendedor para a gravação do Orçamento. Este ponto de entrada é executado no end-point **/api/pgv/customFields/**

**OBS:** Garanta que a LIB do Protheus e a versão do **PGV Core** esteja atualizada.

**Serão permitidos somente campos do tipo:**

* Caractere
* Numérico
* Data

**Não serão permitidos campos do tipo:**

* Lógico
* Memo
* Virtual

**Exemplo:**

```
#INCLUDE "PROTHEUS.CH"
 
//-----------------------------------------------------------
/*/{Protheus.doc} GVFLDCJ
    Este ponto de entrada é chamado pela API de integração
    de campos personalizados, para informar quais campos
    adicionais da tabela SCJ, personalizados ou não, sejam
    considerados pelo PGV além dos padrões
    @type function
    @author Squad CRM/Faturamento
    @since 21/06/2024
    @version 1.0
/*/
//-----------------------------------------------------------
user function GVFLDCJ() as array
    local aSCJ:= {} as array
    aAdd(aSCJ, "CJ_TXMOEDA")
    aAdd(aSCJ, "CJ_FRETAUT")
return aSCJ
```
