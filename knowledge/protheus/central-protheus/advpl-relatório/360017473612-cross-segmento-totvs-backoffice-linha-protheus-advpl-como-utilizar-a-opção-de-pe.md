---
article_id: 360017473612
category: ADVPL - Relatório
content_hash: 1a19563da8f76306c9549bd62500cf241ca40e247975c5b622c3688ce6e8d098
fetched_at: '2026-06-28T22:40:22.730149+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL -   Como utilizar
  a opção de personalização em relatórios customizados utilizando a classe TReport()
type: support-article
updated_at: '2021-12-29T13:12:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017473612-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-utilizar-a-op%C3%A7%C3%A3o-de-personaliza%C3%A7%C3%A3o-em-relat%C3%B3rios-customizados-utilizando-a-classe-TReport
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:02:00 min**

**Dúvida**Como utilizar a opção de personalização em relatórios customizados utilizando a classe TReport()?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
**Solução**Será necessária a inserção das tabelas utilizadas no array do quarto parâmetro da classe TRSection():

```
oSection := TRSection():New(oReport, cTitle, {"SE1"})
```

Uma vez informada a tabela utilizada, será necessária a utilização dos métodos BeginQuery() e EndQuery(). Os quais também pertencem a classe TRSection():

```
oSection:BeginQuery()  
    // QUERIES AQUI  
oSection:EndQuery()
```

E para estruturação das queries, utilize a pseudofunção BEGINSQL e ENDSQL para incorporar o SQL, assim como a tag %Table:TABLE% e o nome referenciado no array do construtor da classe TRSection():

```
BEGINSQL ALIAS cAlias  
    SELECT E1_NUM, E1_VALOR FROM %Table:SE1% SE1  
ENDSQL
```

**Exemplo**[Personalização de relatório customizado](https://totvssuporte.zendesk.com/attachments/token/xe6hxMtQltQUnXEab9xZ3b8Km/?name=PERSONALIZA%C3%87%C3%83O-DE-RELAT%C3%93RIO-CUSTOMIZADO.7Z.7z)
