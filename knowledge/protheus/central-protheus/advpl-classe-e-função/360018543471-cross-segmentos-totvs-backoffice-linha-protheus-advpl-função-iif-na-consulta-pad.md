---
article_id: 360018543471
category: ADVPL - Classe e Função
content_hash: a26b6faf0db577a5f5200b1c511e563408056d376b40409f113c291c64144f33
fetched_at: '2026-06-28T22:40:19.412763+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - Função IIF na
  Consulta Padrão '
type: support-article
updated_at: '2022-01-10T21:15:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018543471-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-IIF-na-Consulta-Padr%C3%A3o
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:03:00 min****Dúvida**Ao criar uma expressão de filtro, para utilização na Consulta padrão não esta funcionando.

```
IIF(M->ZA1_GENERO=='R',M-ZA1_TITULO=='TESTE',M->ZA1_TITULO=='TESTE2')
```

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**A instrução funciona normalmente o que pode ocorrer é o valore de memória não está trazendo valor correto ou a sintaxe errada como no exemplo acima, onde a expressão está errada M-ZA1\_TITULO o correto é M->ZA1\_TITULO.  
Observação: Caso persista Atualize a Lib.  
Para validar entre debugando utilizando uma user function para validar os valores:

```
User Function filteste()  
local lret:= .F.  
DBSelectArea("ZA1")  
Dbsetorder(1)  
lret:= IIF(ZA1->ZA1_GENERO=='R',ZA1->ZA1_TITULO=='TESTE',ZA1->ZA1_TITULO=='FIASCO')  
return lret
```

ou executando a user function no filtro:

```
User Function filteste()  
return IIF(ZA1->ZA1_GENERO=='R',ZA1->ZA1_TITULO=='TESTE',ZA1->ZA1_TITULO=='FIASCO')
```

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013874331/mceclip0.png)
