---
article_id: 16348499749911
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: c5c76369e77fe286763d8d8e1344a67c9c3011344b58bcbf7ab1fd439fac9c12
fetched_at: '2026-06-28T22:38:33.087570+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ponto de Entrada
  M410LDEL
type: support-article
updated_at: '2025-01-10T19:40:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16348499749911-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ponto-de-Entrada-M410LDEL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16348470222103) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **M410LDEL - Validar a exclusão de itens na alteração do PV**.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.  
  
**Solução**

Ponto de Entrada que permite **adicionar validações** para o tratamento de **exclusão de um item do PV**.  
  
**Observação**

O ponto de entrada M410lDel é **executado duas vezes**, é chamado na função **A410ValDel** e esta por sua vez é chamada via MSGetDados na posição 17 (*cDelOk*). De acordo com equipe de Framework este é o **comportamento devido** que ocorre desde a versão 10, onde a execução da função chamada no parâmetro 17 da msgetdados é executada no delok do browse e no bloco de delete do browse.  
Pode-se utilizar a função **PROCNAME()** para validar a fila da chamada e assim só executar uma vez.

**Exemplo**

```
#INCLUDE 'PROTHEUS.CH'  
  
User Function M410LDEL()  
  
    Local lRet := .F.  
  
    If MsgYesNo("Confirma a exclusao da linha?", "PE M410LDEL")  
        lRet := .T.  
        Alert("Passou pelo Ponto de Entrada M410LDEL, a linha sera excluida") //Clicou no Sim  
    Else  
        lRet := .F.  
        Alert("Passou pelo Ponto de Entrada M410LDEL, a linha nao sera excluida") //Clicou no Não  
    EndIf  
  
Return(lRet)
```

**Saiba Mais**

* **[M410lDel - Validar a exclusão de itens na alteração do PV](https://tdn.totvs.com/x/NYZn)**
* **[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Execução do ponto de entrada M410lDel](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413885286807-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Execu%C3%A7%C3%A3o-do-ponto-de-entrada-M410lDel-)**
* **[Função ProcName](https://tdn.totvs.com/x/6IVc)**
