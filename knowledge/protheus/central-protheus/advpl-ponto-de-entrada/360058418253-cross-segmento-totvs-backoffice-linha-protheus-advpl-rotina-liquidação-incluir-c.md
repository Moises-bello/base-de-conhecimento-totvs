---
article_id: 360058418253
category: ADVPL - Ponto de Entrada
content_hash: b1183ec8b0fb928ce9a5ed74b33b5ae5030ba66db426d4b39131ce22615fb742
fetched_at: '2026-06-28T22:40:12.873120+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Rotina Liquidação:
  Incluir campo e mostrar conteúdo'
type: support-article
updated_at: '2021-12-30T17:52:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058418253-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Rotina-Liquida%C3%A7%C3%A3o-Incluir-campo-e-mostrar-conte%C3%BAdo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como inserir um campo e mostrar o seu conteúdo na rotina FINA565 quando feito Liquidação?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão P12

**Solução**Terá que usar os pontos de entrada em conjunto.  
**FA565ADDCPO** (incluir o campo).  
**FA565GRVTRB** (incluir o conteúdo).

```
#INCLUDE'TOTVS.CH'  
User Function FA565ADDCPO()  
  
   aAdd(aCampos,{"Teste","C", 10,0})    
   aAdd(aCpoBro,{"Teste",,"E2_TESTE","  "})  
Return  
  
User Function FA565GRVTRB()  
  
  dbSelectArea("TRB")  
  Replace TRB->TESTE With "TESTE"   
Return
```

**Saiba Mais**  
[FA565ADDCPO - Adição de novos campos na exibição da markbrowse](https://tdn.totvs.com/pages/releaseview.action?pageId=6071241)  
[FA565GRVTRB - Abastecimento de arquivo temporário](https://tdn.totvs.com/pages/releaseview.action?pageId=6071242)
