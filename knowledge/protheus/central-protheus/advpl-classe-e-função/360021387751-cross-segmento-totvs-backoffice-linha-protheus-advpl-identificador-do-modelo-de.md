---
article_id: 360021387751
category: ADVPL - Classe e Função
content_hash: 3e01e7dc5c5e1f8c32e20f8a50ad4c4e2778c092b18faa07e482f0af34396266
fetched_at: '2026-06-28T22:40:14.184159+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Identificador
  do modelo de dados
type: support-article
updated_at: '2022-02-07T14:30:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021387751-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Identificador-do-modelo-de-dados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Ao criar um modelo de dados em uma rotina MVC com o mesmo nome do fonte, não é possível usar as operações (incluir, alterar, excluir e etc).  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Causa**Este erro ocorre pelo fato do cliente somente poder compilar funções de usuário, assim sendo, o identificador do modelo de dados não pode ser igual ao nome do fonte.  
Supondo que tenhamos o cenário abaixo:

```
FONTE: MVC001.prx  
MODELO: MPFormModel():New("MVC001")
```

Quando clicado em uma delas, a classe **MPFormModel**() irá procurar por um fonte com de nome MVC001.pr\* para atuar como ponto de entrada, todavia o fonte MVC001.pr\* não é um ponto e sim o fonte principal, fazendo assim com que a rotina não abra as suas operações.  
  
**Solução**Alterar o identificar do modelo de dados para um nome diferente do fonte.

```
FONTE: MVC001.prx  
MODELO: MPFormModel():New("XMVC001")
```

**Saiba mais**  
[AdvPl utilizando MVC](http://tdn.totvs.com/display/public/PROT/AdvPl+utilizando+MVC)  
[MPFormModel](http://tdn.totvs.com/display/public/mp/MPFormModel)  
[MPFormModel](http://tdn.totvs.com/display/public/mp/MPFormModel)
