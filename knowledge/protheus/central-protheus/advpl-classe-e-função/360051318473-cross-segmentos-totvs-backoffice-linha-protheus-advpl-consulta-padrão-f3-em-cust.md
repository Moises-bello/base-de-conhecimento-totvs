---
article_id: 360051318473
category: ADVPL - Classe e Função
content_hash: 1e4e8161b4a703086af9b8394d0cc18e65aba22a6539b8ed276abb0bd452014a
fetched_at: '2026-06-28T22:40:18.278960+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Consulta padrão
  (F3) em customização via ACD
type: support-article
updated_at: '2022-01-10T17:51:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051318473-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Consulta-padr%C3%A3o-F3-em-customiza%C3%A7%C3%A3o-via-ACD
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como acionar uma consulta padrão de um campo customizado via ACD

```
@ 02, 02 VtSay "C.Custo..: " VtGet MrnCC F3 "CTT"  
VtRead
```

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Atualmente o VT100 utiliza o VtSetKey com o código 23 da tabela ASCII, que corresponde ao ctrl + w.   
Não há possibilidade de definir outra tecla atualmente.
