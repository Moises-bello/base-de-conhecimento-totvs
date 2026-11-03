---
article_id: 1500007354522
category: Gestão de Pesquisa e Resultado (GPR)
content_hash: 763eba6ab78a086babd35a34b89bfe9f19374787b397a50fe7609e140d4fb360
fetched_at: '2026-06-28T22:38:22.168804+00:00'
product: protheus
section_id: 1500001539461
source: central-protheus
title: Cross Segmentos- TOTVS Backoffice (Linha Protheus)-SIGAGPR-Erro na tela de
  Pesquisa GPR (500 - Internal Server Error)
type: support-article
updated_at: '2022-05-11T19:52:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007354522-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAGPR-Erro-na-tela-de-Pesquisa-GPR-500-Internal-Server-Error
---

**Ocorrência**Ao efetuar  um teste de pergunta gera o erro interno (500 - Internal Server Error):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500010504741/mceclip0.png)  
  
**Ambiente**Cross Segmentos- TOTVS Backoffice (Linha Protheus)-SIGAGPR - todas as versões.

**Causa**

Além do erro de servidor interno em tela, também é gerado o erro no console:

**variable is not an object  on W\_PGPR001(PGPR000.PRW) 02/06/2017 09:46:05 line : 295**

[TOTVS build: 7.00.191205P-20201210]

Called from CONNECTWEBEX(APWEX010.APL) 01/04/2021 19:01:01 line : 683

Todavia, o erro ocorre em decorrência da falta do cadastro da regra de pesquisa, que o sistema utiliza para validar a entrada do entrevistador a pesquisa.

**Solução**  
Para Solucionar crie o Cadastro de Regras de Pesquisa e posteriormente, associe a regra a pesquisa :  
**Regra de Pesquisa(GPRA080)**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500010206802/mceclip1.png)

**Cadastro de Pesquisa (GPRA010)**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500010505221/mceclip2.png)
