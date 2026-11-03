---
article_id: 360020760071
category: ADVPL - Classe e Função
content_hash: d95ba7a9a1406312365ef55c6b9b28f06a295ef1899a158291b3133ea6aa42c9
fetched_at: '2026-06-28T22:40:19.221451+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro: função
  type retorna U em variáveis validas'
type: support-article
updated_at: '2024-01-24T10:59:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020760071-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-fun%C3%A7%C3%A3o-type-retorna-U-em-vari%C3%A1veis-validas
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Ao utilizar a função *Type*() em uma variável sintaticamente correta é retornado "U" (*Undefined*) ao invés do tipo correto:

```
Local aVetor := {}  
Local cType  := Type("aVetor") // RETORNO: "U"
```

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Causa**Este comportamento ocorre devido a uma limitação da função *Type*() já descrita em sua documentação oficial. Uma vez que utilizada uma variável com escopo local (LOCAL) ou estático (*STATIC*), a função irá retornar "U" mesmo que o conteúdo esteja correto.  
  
**Solução**Utilizar a função **ValType**(), dado ao fato que a mesma é a evolução da ***Type***(), assim sendo, conseguirá validar o tipo primitivo de variáveis locais e estáticas.  
  
**Saiba mais**[Valtype](http://tdn.totvs.com/pages/viewpage.action?pageId=24347162)  
[Type](http://tdn.totvs.com/display/tec/Type)
