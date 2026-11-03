---
article_id: 360021950471
category: ADVPL - Classe e Função
content_hash: d485c671fbc7bdf28db7f188fa119a766aeb1354c55f545b6f8841ec7f0976a9
fetched_at: '2026-06-28T22:40:14.520564+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Cancelamento da
  função Processa() não está funcionando
type: support-article
updated_at: '2024-02-25T13:25:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021950471-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Cancelamento-da-fun%C3%A7%C3%A3o-Processa-n%C3%A3o-est%C3%A1-funcionando
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16414998402071)Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**O cancelamento do processamento de rotinas executadas através da função **Processa**() não está funcionando.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, pois o tratamento de cancelar a execução deve ser realizado pelo usuário:  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

Na chamada da processa deve ser declarada a variável Private **lAbortPrint**:

```
User Function TestPrc(aCampos, oLbx)  
Private lAbortPrint:=.F.  
Processa( {|| U_TestSX3(aCampos) }, "Aguarde...", "Carregando definição dos campos...",.T.)
```

E no laço de processamento deve-se utilizar a variável para abortar o processo:

```
WHILE !Eof() .AND. !lAbortPrint  
IncProc()  
sleep(300)  
PROCESSMESSAGES()   
Aadd(aCampos, {X3_ARQUIVO, X3_ORDEM, X3_CAMPO})  
DbSkip()  
END
```

**Saiba mais**[Processa - Diálogo na execução de processo monitorado](https://tdn.totvs.com/pages/releaseview.action?pageId=727933986)
