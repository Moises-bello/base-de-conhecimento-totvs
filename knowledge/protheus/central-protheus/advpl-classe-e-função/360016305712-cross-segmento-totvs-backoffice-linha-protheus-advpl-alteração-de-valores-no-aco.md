---
article_id: 360016305712
category: ADVPL - Classe e Função
content_hash: 614d763fbb05189e7184a0e3ad7b79b5abf0d7b5bb62b7bb115dd1b201d301c0
fetched_at: '2026-06-28T22:40:14.357938+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Alteração de valores
  no aCols da rotina MATA103 via customização '
type: support-article
updated_at: '2022-08-01T19:33:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016305712-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Altera%C3%A7%C3%A3o-de-valores-no-aCols-da-rotina-MATA103-via-customiza%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como manter os valores dos itens alterados via customização na rotina MATA103?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Qualquer alteração de valor via customização, diretamente no aCols da rotina **MATA103,** deverá conter sequencialmente a chamada da função **A103TRIGGER** informando como parâmetro o campo manipulado para possibilitar o cálculo correto dos impostos e atualizações internas do programa.   
Abaixo uma função de usuário de exemplo que atribui o valor fixo de 100 ao campo D1\_VUNIT

```
User Function MA103B01()  
Local nPosVal  
Local nX  
   For nX := 1 To Len(aCols)  
      nPosVal   := AScan(aHeader,{|x| AllTrim(x[2]) == 'D1_VUNIT'})  
      N := nX //Atualiza linha  
      aCols[N, nPosVal] := 100  
      A103Trigger('D1_VUNIT')  
      If ExistTrigger('D1_VUNIT')   
        RunTrigger(2,nX,nil,,'D1_VUNIT')  
        MaColsToFIs(aHeader,aCols,nX,"MT100") //Grava o gatilho no campo caso possua a função MaFisRef   
      EndIf  
   Next nX  
Return nil
```

O exemplo acima percorre e atualiza o campo em todos os itens da nota. É importante observar que a variável **N**(controle da linha do aCols), deve acompanhar a posição que foi alterada.
