---
article_id: 360028553812
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: e9ac7f458f5caf147ea88fe999e035d5be35af7ab462552e1422282e98123d98
fetched_at: '2026-06-28T22:40:44.448879+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'MP - SIGACTB - ECD Registro J150: Valores zerados 7-VL_CTA e I052 COD_AGL'
type: support-article
updated_at: '2021-04-28T22:06:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028553812-MP-SIGACTB-ECD-Registro-J150-Valores-zerados-7-VL-CTA-e-I052-COD-AGL
---

**Dúvida**

I052 COD\_AGL O código de aglutinação de uma linha detalhe da demonstração contábil deve ser informado em pelo menos um registro I052

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029576811/mceclip0.png)

**Ambiente**  
Microsiga Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
**Causa**

* Veja que o J150 é apresentado com saldo

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029582212/mceclip4.png)

* sistema esta gerando J150 com valor zerado com
* provável que :Conta não possui movimento no período e nem saldo anterior ,com isso o I050 e I052 não esta sendo gerado
* Diante o PGE esta buscando o I052 para o J150 (zerado) que foi gerado

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029576931/mceclip5.png)

* Ao Acesse a visão gerencial e desamarrar as contas contábeis que não possuem saldo anterior e movimento no período (solução paliativa)
* Com isso o sistema não gera o J150(zerado) e o PGE não dá falta o I052
* Posteriormente gere uma nova revisão e verifique se a situação será apresentada

**Solução**

A Issue DSERCTR1-20630 Foi  Liberada abaixo onde foi tratada  J150 zerados

12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=753437> ; 12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=753436> ;

Veja também : [MP - SIGACTB -ECD ERRO BLOCOS J150 7-VL\_CTA e I052 COD\_AGL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028548031-MP-SIGACTB-ECD-ERRO-BLOCOS-J150-7-VL-CTA-e-I052-COD-AGL?source=search)
