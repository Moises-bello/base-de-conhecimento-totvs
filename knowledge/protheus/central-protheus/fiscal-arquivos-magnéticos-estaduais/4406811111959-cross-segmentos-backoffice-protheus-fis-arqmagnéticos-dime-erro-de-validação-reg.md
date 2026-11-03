---
article_id: 4406811111959
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: fdcfc72c63e97ab924c21ff7239cfdc1455e65ea840591d77c68b6d139679a0a
fetched_at: '2026-06-28T22:42:10.740552+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DIME - Erro
  de validação:  Registro 84 - Declaração complementar anual indevida para o período'
type: support-article
updated_at: '2022-08-17T19:29:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406811111959-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DIME-Erro-de-valida%C3%A7%C3%A3o-Registro-84-Declara%C3%A7%C3%A3o-complementar-anual-indevida-para-o-per%C3%ADodo
---

**Ocorrência** **Registro 84** gerado indevidamente no arquivo txt o que ocasiona o seguinte erro de validação: **Registro 84** - Declaração complementar anual indevida   
**Ambiente**Cross Segmento - TOTVS Backoffice (**Linha Protheus**) - A partir da versão **12.1.25.**  
  
**Causa**  
Esse incidente ocorre, pois a terceira wizard de geração do arquivo, referente aos **quadros 80/90** está com dados preenchidos nos campos.

**Solução**  
Para solucionar essa ocorrência, a wizard abaixo não pode estar preenchida com dados.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406810993943/mceclip1.png)

Caso esteja preenchida, o sistema pega os valores da wizard do **registro 84**, mesmo que zerados.   
  
Para não gerar o registro, a wizard acima não deve ser preenchida.  
  
Trecho do fonte:   
  
If !Empty (AllTrim (aWizard[3][3]))  
  //  
  //Pro-labore  
  AtuVlrDime(, "84", "84", "411", Val (aWizard[7][1]), 2)  
  
  
...  
  
  
//Totalizador  
  For nI :=1 To Len (aWizard[7])  
      nTotal    +=    Val (aWizard[7][nI])  
  Next (nI)  
  //  
  //Total  
  AtuVlrDime(, "84", "84", "499", nTotal, 2)
