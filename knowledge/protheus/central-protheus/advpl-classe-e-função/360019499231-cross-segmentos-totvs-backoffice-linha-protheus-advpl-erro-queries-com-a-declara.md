---
article_id: 360019499231
category: ADVPL - Classe e Função
content_hash: e142cae86fc49e4af08395d5cc58af1024c75595d98a0012bd158c79afd7f53f
fetched_at: '2026-06-28T22:40:19.253580+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro: queries
  com a declaração with'
type: support-article
updated_at: '2022-01-10T13:52:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019499231-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-queries-com-a-declara%C3%A7%C3%A3o-with
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Quando utilizado funções de execução de query no banco e a declaração de pesquisa contém o comando WITH, está sendo gerado erro em tempo de execução:

```
A função ChangeQuery não pode ser utilizada para queries com a palavra reservada WITH. on CHANGEQUERY(APLIB070.PRW)
```

**Ambiente**  
Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Causa**A função ChangeQuery() não reconhece queries que contenham a palavra WITH, por isso a mesma entrava em *loop*.

Como a mesma não é homologada para trabalhar com *queries* que utilizem a declaração WITH, ela passou a verificar a existência do comando na *query* enviada e gerar exceção (error.log) informando que não está apta a trabalhar com *queries* deste tipo.  
  
**Solução**Não utilizar a função ChangeQuery() e nem funções que trabalhem com ela internamente.

Uma das funções que pode ser utilizada com a declaração WITH é a TcGenQry().  
  
**Saiba mais**  
[TCGENQRY](http://tdn.totvs.com/display/tec/TCGenQry)
