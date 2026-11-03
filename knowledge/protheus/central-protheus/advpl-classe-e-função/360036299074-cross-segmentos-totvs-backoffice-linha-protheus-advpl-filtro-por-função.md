---
article_id: 360036299074
category: ADVPL - Classe e Função
content_hash: 0f5693bd8881a13b1da320419f3198dc01370868aaaa86324ff1eff7aaf0f751
fetched_at: '2026-06-28T22:40:19.308683+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Filtro por função
type: support-article
updated_at: '2023-10-19T18:22:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036299074-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Filtro-por-fun%C3%A7%C3%A3o
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Teria um exemplo filtro utilizando uma função?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) - ADVPL - A partir da versão 11.80  
  
**Solução**Crie uma user function e realize suas tratativas conforme o modelo de exemplo abaixo e compile:

```
User function TFil()  
    Local cFil := "SB1->B1_COD == 'MEU PRODUTO' "  
Return cFil
```

Após compilar abra o sistema Protheus  e entre na rotina que utilizara seu filtro.  
Em seguida clique na opção filtro e na opção função digite o nome da user function ex: TFil() que foi compilada conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048330753/mceclip0.png)

Clique em adicionar depois salvar por ultimo clique em aplicar filtros selecionados conforme a imagem abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047444874/mceclip1.png)
