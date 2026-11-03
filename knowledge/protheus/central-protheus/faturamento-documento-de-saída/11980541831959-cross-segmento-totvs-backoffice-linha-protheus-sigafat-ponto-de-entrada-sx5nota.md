---
article_id: 11980541831959
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: fc367bd74713a07c086f44ac8871f792c7e4a811d401883e2d01be31cce80dda
fetched_at: '2026-06-28T22:38:45.288447+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  SX5NOTA
type: support-article
updated_at: '2023-01-27T13:09:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11980541831959-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-SX5NOTA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **SX5NOTA - Validar séries de NFs**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

A finalidade do ponto de entrada **SX5NOTA** é permitir que o usuário faça uma **validação das séries** das **notas fiscais de saída** que deseja considerar no momento da **geração da NF**.  
  
**LRET:**

* **.T.** - Considera a série da nota fiscal na geração.
* **.F.** - Não considera a série da nota fiscal na geração.

**Exemplo**

```
User Function SX5NOTA()   
  
    Local _cFilial  := Paramixb[1]  //Filial  
    Local _cTabela  := Paramixb[2]  //Tabela da SX5  
    Local _cChave   := Paramixb[3]  //Chave da Tabela na SX5  
    Local _cDescri  := Paramixb[4]  //Conteúdo da Chave indicada  
    Local _lRet     := .F.      
  
    If Alltrim(_cChave) == "A" .Or. Alltrim(_cChave) == "B" //Filtra as séries "A" e "B"  
        _lRet := .T.  
    EndIf  
  
Return _lRet
```

**Saiba Mais**

**[SX5NOTA - Validar séries de NFs](https://tdn.totvs.com/x/wIVn)**
