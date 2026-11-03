---
article_id: 360021323411
category: ADVPL - Ponto de Entrada
content_hash: 41dba176bfacbfd1cb0245b49c942c96e8acaa73e712ec9ee3a552b6c11fe40a
fetched_at: '2026-06-28T22:40:11.699516+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Inclusão de campos
  na grid  de fornecedores da geração de cotação  '
type: support-article
updated_at: '2021-12-29T13:36:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021323411-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Inclus%C3%A3o-de-campos-na-grid-de-fornecedores-da-gera%C3%A7%C3%A3o-de-cota%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Ponto de entrada para  incluir campos no grid de fornecedores no momento da geração da cotação?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12  
  
**Solução**O Ponto de Entrada **MT131C8**tem como funcionalidade exibir informações de outros campos no grid de fornecedores no momento da geração da cotação. São exibidos campos da tabela SC8 e campos do tipo MEMO não são exibidos na grid.  
  
**Exemplo**

```
#Include 'Protheus.ch'  
  
User Function MT131C8()  
// O retorno deve começar com uma barra vertical ( | ) e ir intercalando o nomes do campos com barras verticais.   
Local cCamposC8 := "|C8_DATPRF|C8_TAXAFIN"   
  
Return (cCamposC8)
```

**Saiba Mais**[MT131C8 - Exibe informações de outros campos da SC8 no grid de fornecedores](http://tdn.totvs.com/pages/viewpage.action?pageId=329035051)
