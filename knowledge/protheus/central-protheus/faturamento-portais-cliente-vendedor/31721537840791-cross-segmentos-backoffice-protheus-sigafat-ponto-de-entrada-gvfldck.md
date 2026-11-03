---
article_id: 31721537840791
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: d70157145e77fc14e87f5e0d2fb7d7feed285d17b92658fa0d9c81b65c81225c
fetched_at: '2026-06-28T22:38:23.946522+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Ponto de entrada GVFLDCK
type: support-article
updated_at: '2025-04-29T18:56:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31721537840791-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Ponto-de-entrada-GVFLDCK
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31721537811863) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Qual o exemplo do ponto de entrada GVFLDCK?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

O ponto de entrada GVFLDCK permite adicionar campos personalizados da tabela do itens do Orçamento (SCK) a serem apresentados no Portal Gestão de Vendas.

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
/*/{Protheus.doc} GVFLDCK
    Este ponto de entrada é chamado pela API de integração
    de campos personalizados, para informar quais campos
    adicionais da tabela SCK, personalizados ou não, sejam
    considerados pelo PGV além dos padrões
    @type function
    @author Squad CRM/Faturamento
    @since 21/06/2024
    @version 1.0
/*/
//-----------------------------------------------------------
user function GVFLDCK() as array
    local aSCK:= {} as array
    aAdd(aSCK, "CK_FCICOD")
    aAdd(aSCK, "CK_OBS")
return aSCK
```
