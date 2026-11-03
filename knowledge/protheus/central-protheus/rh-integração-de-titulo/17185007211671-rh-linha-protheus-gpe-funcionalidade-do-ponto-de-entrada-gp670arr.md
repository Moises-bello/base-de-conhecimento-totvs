---
article_id: 17185007211671
category: RH - Integração de Titulo
content_hash: ed4575ee75ecc3370fbcac41f691ed36bd55eb1cdb00d076e86f98d6780b5a42
fetched_at: '2026-06-28T22:43:36.342610+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Funcionalidade do ponto de entrada GP670ARR
type: support-article
updated_at: '2025-07-15T20:37:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17185007211671-RH-Linha-Protheus-GPE-Funcionalidade-do-ponto-de-entrada-GP670ARR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17185011694103) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Funcionalidade do ponto de entrada GP670ARR

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Solução**Esse Ponto de entrada deve ser utilizado para adicionar, na integração do titulo, campos criados pelo usuário ou que não sejam tratados no de/para na integração do título no padrão.  
  
O PE somente será executado quando estiver sendo efetuada a integração do titulo, e caso isso não ocorra, será apresentado log com os títulos não integrados.

Programa Fonte

```
GPEM670.PRX
```

Temos dois exemplos de utilização :  
  

1) GP670ARR - Integração de Título ( ) --> aCposUsr

Retorno

**aCposUsr**

(array\_of\_record)* Array com os campos criados pelo usuario.

Observações

Retorno: Deve retornar um array com a seguinte estrutura :

aCposUsr: = { {"Campo" , Conteudo,   Nil};

Ex.:  aCposUsr: = {{'E2\_VALOR1' , RC1->RC1\_VALOR \* 0.10 ,Nil};

                               {'E2\_VALOR2' , 100.00 ,   Nil}}   
  
Base: <https://tdn.totvs.com/pages/releaseview.action?pageId=6079137>

2) #include "Protheus.ch"

User Function GP670ARR()

Local aRet := {}

aadd(aRet,{"E2\_HIST",RC1->RC1\_DESCRI,NIL})

aadd(aRet,{"E2\_CCUSTO",RC1->RC1\_CC,NIL})

Return aRet

![GIFGP670ARR.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/17185380405143)

Obs: Anexo PE configurado em prw.

**Saiba Mais:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=6079137>
