---
article_id: 360029392011
category: ADVPL - Classe e Função
content_hash: fff01a3203364f7dea6687b8ec18d8f68137118f72bd3b03715194a02f89fa95
fetched_at: '2026-06-28T22:40:16.734614+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Filtro em browser
  com tabela temporária
type: support-article
updated_at: '2022-03-09T19:08:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029392011-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Filtro-em-browser-com-tabela-tempor%C3%A1ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min  
  
Ocorrência**Quando construo um navegador (browser) com tabela temporária, ao clicar em Filtros, não é exibida a ferramenta de criação de filtros.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Causa**Por motivo do navegador ser construído com uma tabela temporária, o mesmo não consegue recuperar a estrutura dos campos com base no *alias* utilizado.  
  
**Solução**Utilizar o método SetFieldFilter() para adicionar a estrutura dos campos conforme vetor abaixo:

```
aFields[nX][1] := "B1_COD" (nome)  
aFields[nX][2] := "Produto" (título)  
aFields[nX][3] := "C" (tipo de dado)  
aFields[nX][4] := 15  
aFields[nX][5] := 0  
aFields[nX][6] := "@!"
```

**Ssiba mais**  
[FwBrowse](http://tdn.totvs.com/display/public/PROT/FwBrowse)
