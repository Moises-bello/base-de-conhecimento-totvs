---
article_id: 360034226633
category: ADVPL - Classe e Função
content_hash: 49b75b7c3c8bc31a32c70bcd58d50794b0358e405227132debfc5108cf07ca71
fetched_at: '2026-06-28T22:40:17.127056+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Quebrar linha dos
  campos da View (MVC)
type: support-article
updated_at: '2022-06-13T21:13:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034226633-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Quebrar-linha-dos-campos-da-View-MVC
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como colocar um campo por linha em **MVC?**   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Solução**Quando criamos telas em **MVC**, os campos que são apresentados vão ocupando o espaços na tela (VIEW), e acaba ficando uma linha com 2 campos, outra com 1.   
Para colocar um campo em cada linha, utiliza o parâmetro**lInsertLine** igual a **.T.**, do método **AddField** da Classe **FWFormViewStruct.**   
Esse parâmetro indica pulo de linha após o campo.

```
Local oStruZA0 := FwFormStruct(2, "ZA0")  
oStruZA0:aFields[1][18] := .T.
```

**Funcionamento**

**![KCS_MVC.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360043376854/KCS_MVC.gif)**

**Saiba mais  
[FWFormViewStruct](http://tdn.totvs.com/display/framework/FWFormViewStruct)**
