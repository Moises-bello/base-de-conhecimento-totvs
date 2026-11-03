---
article_id: 360016527532
category: ADVPL - Ponto de Entrada
content_hash: b64bf55fbeb20f9f7da28aea61d3460644f2b47a90215fc1b5f803b583d0c24e
fetched_at: '2026-06-28T22:40:11.815928+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada
  FI040ROT
type: support-article
updated_at: '2021-12-29T19:51:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016527532-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-FI040ROT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Como utilizar o ponto de entrada FI040ROT para inclusão de novos itens no menu aRotina?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

```
User Function FI040ROT()  
Local aRotina := AClone(PARAMIXB)  
AAdd(aRotina, {"TESTE 1", "U_MyFunction", 0, 3})  
Return (aRotina)
```

**Retorno**Retorna um **array** **aRotina** com o(s) novo(s) itens do menu que foram adicionados.

**Eventos de chamada do Ponto de Entrada**

```
If ExistBlock("FI040ROT")  
aRotinaNew := ExecBlock("FI040ROT",.F.,.F.,aRotina)  
If (ValType(aRotinaNew) == "A")  
aRotina := aClone(aRotinaNew)  
EndIf  
EndIf
```

Programa Fonte FINA040.PRX

**Observações**Está presente na função **MenuDef()**

**Parâmetros**(**ParamIxb**) = Recebe um **array** **aRotina** com o menu padrão e adiciona novos itens ao menu
