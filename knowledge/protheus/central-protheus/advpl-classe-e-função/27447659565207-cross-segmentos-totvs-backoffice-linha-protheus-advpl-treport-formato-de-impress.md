---
article_id: 27447659565207
category: ADVPL - Classe e Função
content_hash: c9c4862569ef640da975bdd3ab7f80be46dce428af0a4f083f06e35485dc70ce
fetched_at: '2026-06-28T22:40:21.653068+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - TReport - Formato
  de impressão Xlsx via Schedule
type: support-article
updated_at: '2024-11-07T18:48:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27447659565207-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-TReport-Formato-de-impress%C3%A3o-Xlsx-via-Schedule
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27447659552535) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**É possível definir a o formato de impressão Xlsx via job de uma customização criada com a classe TReport?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**  
Sim, é possível.

Recentemente foi implementado uma opção no schedule para possibilitar a seleção de layout personalizado no schedule TReport, além disso, foi adicionado o suporte a impressão xlsx via schedule também.

A seleção do tipo é na própria tela do schedule, para funcionar é preciso utilizar uma função static "scheddef" no fonte do relatório.  
Caso o fonte do TReport possua a função, na tela de agendamento será possível fazer essa configuração:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27447672037143)  
  
Exemplo:

```
Static Function Scheddef()  
  
Local aParam  
  
Local aOrd     := {OemToAnsi(" Por Codigo         "),OemToAnsi(" Alfabetica         ")}  
  
aParam := { "R",;                      //Tipo R para relatorio P para processo     
  
"ACA070",;// Pergunte do relatorio, caso nao use passar ParamDef              
  
"SA1",;  // Alias              
  
aOrd,;   //Array de ordens     
  
"Teste SchedDef"}      
  
Return aParam
```

**Saiba mais:**

[Definição de Static Function SchedDef para o Schedule](https://tdn.totvs.com.br/pages/releaseview.action?pageId=36800166)
