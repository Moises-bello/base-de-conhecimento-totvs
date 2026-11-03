---
article_id: 8741919551639
category: Call Center - Telecobrança
content_hash: f3fbb6b8d177bc4cddb226a02e6ef2dd51c823cdce6d9dd26d7dba6b2c1a48f9
fetched_at: '2026-06-28T22:41:28.712965+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - Ponto de Entrada
  TMKA271ACG
type: support-article
updated_at: '2022-09-08T19:25:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8741919551639-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Ponto-de-Entrada-TMKA271ACG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **TMKA271ACG - Filtro de Títulos.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPMS - A partir da release 12.  
  
**Solução**

O ponto de entrada **TMKA271ACG** **filtra os títulos** do atendimento de telecobrança. A tabela ACG (Itens de Telecobrança) está posicionada para que seja feita a validação. O retorno do ponto de entrada deve ser um valor lógico indicando se deve ou não ser a presentado o item.

O ponto de entrada permite filtrar as linhas dos itens dos títulos de telecobrança da tabela ACG na alteração e na visualização do atendimento.  
  
**Exemplo**

```
User Function TMKA271ACG()   
  
    Local lRet := .T.  
  
    Alert('Acessado ponto de entrada TMKA271ACG!')  
  
    //Filtro para não mostrar títulos com ACG_VALOR menor que 150,00  
    If ACG_VALOR < 150  
        lRet := .F.  
    EndIf  
  
Return(lRet)
```

 **Saiba Mais**

**[TMKA271ACG - Filtro de Títulos](https://tdn.totvs.com/x/-5Jn)**

**[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - Ponto de Entrada TK274QRY](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8741901030551-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Ponto-de-Entrada-TK274QRY)**
