---
article_id: 17858418999319
category: ADVPL - Classe e Função
content_hash: f12afb64b6150bae7f7420fa27043dfce1cccc682c48aa085886d562c31f4415
fetched_at: '2026-06-28T22:40:20.659764+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - A função Recno abre
  alguma tabela no Protheus?
type: support-article
updated_at: '2023-09-27T19:27:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17858418999319-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-A-fun%C3%A7%C3%A3o-Recno-abre-alguma-tabela-no-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17858411859479) Tempo aproximado para leitura: 00:01:00 min **Dúvida**Há algum exemplo referente a função Modelo2?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

A função Recno() não abre nenhuma tabela e nem a torna ela a área dela ativa.  
  
No Protheus, sempre haverá alguma área selecionada como ativa pois diversas tabelas já são abertas automaticamente quando um ambiente de um módulo é aberto, e uma delas já é posicionada como a ativa, seja a abertura feita manualmente no SmartClient, seja por job, seja por função via RpcSetEnv ou PREPARE ENVIRONMENT.

Ou seja, sempre haverá muitas tabelas abertas e sempre uma delas é selecionada pelo próprio Protheus como área ativa.

Desta forma, a função Recno() se comportará sempre de uma das duas maneiras abaixo:

1) Ao usar o alias explícito já foi automaticamente aberta de uma das formas acima citadas, trará o registro atual da tabela indicada:

```
IF SE1->(Recno())
```

2) Se não for usado o alias explícito, trará o valor do registro correntemente posicionado da tabela aberta na área atual.

```
IF Recno()
```

Recomendamos sempre usar aliás explícito, como inclusive já fez no seu código, por ser uma boa prática de documentação de código e também para evitar trazer dados inesperados de outra tabela caso a tabela do alias explícito não seja a corrente.

**Saiba Mais**

[**RECNO**](https://tdn.totvs.com/display/tec/Recno)
