---
article_id: 20052694488855
category: Financeiro
content_hash: b4a8575c15182a25da57c7a6d79378619406df7ecffc9acea2dd7f969d43cecf
fetched_at: '2026-06-28T22:38:02.979050+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA090 - Ponto de
  Entrada F090CPOS - Ordenação dos campos
type: support-article
updated_at: '2023-12-22T11:28:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20052694488855-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA090-Ponto-de-Entrada-F090CPOS-Ordena%C3%A7%C3%A3o-dos-campos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20052694483095) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como ordenar os campos que serão apresentados na tela da rotina FINA090 através do Ponto de Entrada F090CPOS?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Exemplo de utilização:

```
#INCLUDE 'PROTHEUS.CH'  
  
User Function F090CPOS()  
  
    Local aCampos := PARAMIXB  
  
    //Adiciono o campo E2_NUM no array aCampos para ser exibido na MarkBrowse  
    //Adiciona no final  
    Aadd(aCampos, {"E2_NUM","","Numero Tit.","@!"})  
  
    //Adiciona na posição de preferência do browser  
    aCampos[2] := {"E2_FORNECE","","Teste","@!"}  
  
Return aCampos
```

Para adicionar o campo na última coluna do browser utiliza-se a função Aadd, conforme exemplo:

```
    Aadd(aCampos, {"E2_NUM","","Numero Tit.","@!"})
```

Para adicionar o campo na posição/ coluna de sua preferência:

```
 aCampos[2] := {"E2_FORNECE","","Teste","@!"}
```

Onde a posição do array aCampos é a coluna que será manipulada.

**Saiba mais:**

[F090CPOS - Tratamento de Campos](https://tdn.totvs.com/display/public/PROT/F090CPOS-+Tratamento+de+Campos)
