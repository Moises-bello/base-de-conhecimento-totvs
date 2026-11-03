---
article_id: 360051846753
category: ADVPL - Classe e Função
content_hash: 4b79c50429928b9f6b29ca632bfe495cc6f83d1d301ae02ac2723d6d8ec09976
fetched_at: '2026-06-28T22:40:16.918610+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Grid MVC sobrescrevendo
  valores
type: support-article
updated_at: '2021-11-17T21:10:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051846753-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Grid-MVC-sobrescrevendo-valores
---

**Ocorrência**Tenho uma rotina **MVC** onde ao alterar a linha acima o valor é replicado na linha abaixo.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas as versões  
  
**Causa**O problema ocorre quando utilizamos o método **AddCalc(),**pois a função utilizada no **Calc**retira o posicionamento correto do **grid**e não retorna a posição anterior. O **Calc** depende do posicionamento correto para seu funcionamento.  
  
**Solução**Para resolver este problema basta utilizar as funções **FWSaveRows**() e **FwRestRows**().

Exemplo:

```
aLinhas := FWSaveRows()  
    For nI := 1 To oGrid:Length()  
  
        oGrid:GoLine(nI)  
  
        If(!oGrid:IsDeleted())  
  
            nValTot := oHead:GetValue('ZZ2_VALOR')  
            nRet    += oModel:GetValue('MD_ZZ3DETAIL','ZZ3_TOTAL')  
        Endif  
  
        //oGrid:GoLine(nLine)  
  
    Next nI  
FWRestRows(aLinhas)
```

**Saiba Mais**[FWSaveRows](https://tdn.totvs.com/display/framework/FWSaveRows)  
[FWRestRows](https://tdn.totvs.com/display/framework/FWRestRows)
