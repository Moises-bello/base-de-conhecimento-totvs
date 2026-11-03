---
article_id: 4410715532311
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: c8591f2130f8b41a9e7bba33485c439c47d3703373718d2b5b1ee6afc4655048
fetched_at: '2026-06-28T22:39:44.407231+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Ponto de entrada
  na inclusão da prestação de contas
type: support-article
updated_at: '2021-10-14T21:43:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410715532311-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Ponto-de-entrada-na-inclus%C3%A3o-da-presta%C3%A7%C3%A3o-de-contas
---

**Dúvida**Tem algum ponto de entrada para carregar o código da despesa em um campo da tabela SE2 no momento da geração da prestação de contas, quando é incluído o título NF?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  –*Easy Import Control*– Todas versões  
  
**Solução**É possível utilizar o ponto de entrada da função EICFI400, parâmetro **DEP\_GRAVACAO\_TIT**, modificando o array **aTit**.

|  |  |  |  |
| --- | --- | --- | --- |
| Nome | Tipo | Descrição | Referência |
| **DEP\_GRAVACAO\_TIT** | Array of Record | Permite a customização da variável 'aTit', que possui os campos da tabela SE2, antes da gravação do titulo no Financeiro. | aTit |

Exemplo:

```
User function eicfi400()Do case	  
Case PARAMIXB == "DEP_GRAVACAO_TIT"  
------instruções -------  
  
EndCase  
return .t.
```

**Saiba mais**[Ponto de entrada EICFI400](https://tdn.totvs.com/display/public/mp/EICFI400)
