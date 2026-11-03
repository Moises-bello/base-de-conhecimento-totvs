---
article_id: 360018934471
category: ADVPL - Ponto de Entrada
content_hash: 7376ab25c15331c20592ebbe48bcc66b3c36a14b9ac884fba4d8991a698a294a
fetched_at: '2026-06-28T22:40:11.749157+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Mensagem Help:
  FWMODELPOS modelo inválido ponto de entrada FT300VLD'
type: support-article
updated_at: '2021-12-29T13:59:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018934471-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Mensagem-Help-FWMODELPOS-modelo-inv%C3%A1lido-ponto-de-entrada-FT300VLD
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Ocorrência**No ponto de entrada FT300VLD quando o retorno é falso (.F.), aparece uma mensagem

Help: FWMODELPOS

Problema: Modelo inválido.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas as versões  
  
**Causa**Ao retornar .F. nas validações MCV  
  
**Solução**O *Help* é padrão do MVC e neste caso precisa ser tratado, pois ao executar pontos de entrada em rotinas MVC e retornar false o formulário, será gerado obrigatoriamente um *Help*.

Essa mensagem é possível de ser customizada, exemplo:

```
#Include 'Protheus.ch'  
  
User Function FT300VLD()  
lRet := .F.  
  
     Help("",1,"FT300VLD",,"seu texto",1) // "Preencher o campo Loja do Prospect."    
   
Return(lRet)
```

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014549111/mceclip1.png)

**Saiba Mais**[Cross Segmento - Backoffice Linha Protheus - ADVPL - Tratamento help ponto de validação MVC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013994911)
