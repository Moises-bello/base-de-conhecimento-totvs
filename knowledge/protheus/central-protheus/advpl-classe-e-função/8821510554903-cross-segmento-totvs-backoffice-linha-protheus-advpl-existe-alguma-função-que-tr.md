---
article_id: 8821510554903
category: ADVPL - Classe e Função
content_hash: 8eea3c3ab4793c311b6cab818fce40875ed432054d2d22565f8c51763c920681
fetched_at: '2026-06-28T22:40:20.724028+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Existe alguma função
  que traga a quantidade de registros existentes no arquivo - tabela?
type: support-article
updated_at: '2022-09-12T19:51:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8821510554903-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Existe-alguma-fun%C3%A7%C3%A3o-que-traga-a-quantidade-de-registros-existentes-no-arquivo-tabela
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Gostaria de saber se existe alguma função que traga a quantidade de registros existentes no arquivo - tabela?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**Funções que contam quantidade de registros em dados sempre mostram o último recno da tabela.  
Para este tipo de tratativa (query em banco) é muito mais performático utilizar o Count do banco ou ainda utilizar a função MpSysExecScalar, que faz uma query scalar no banco:

```
/*/{Protheus.doc} MPSysExecScalar  
Executa a consulta e retorna a primeira coluna da primeira linha  
no conjunto de resultados retornado pela consulta.  
Colunas ou linhas adicionais são ignoradas.  
  
@param cQuery Consulta a ser executada  
@param cColumn  Nome da coluna a ser retornada  
  
Sample:  
nCount :=MpSysExecScalar("Select Count ( *) MYCOUNT FROM TABELA","MYCOUNT")
```

**Saiba mais**  
[MPSysExecScalar](https://tdn.totvs.com/display/public/framework/MPSysExecScalar)
