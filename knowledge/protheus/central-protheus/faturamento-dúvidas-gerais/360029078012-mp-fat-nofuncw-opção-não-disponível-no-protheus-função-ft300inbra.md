---
article_id: 360029078012
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 1ec5a8e5924314fbb75ff760c53ad62658ec86ba7f9cbca2987d990505c8c2e5
fetched_at: '2026-06-28T22:38:31.301208+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Nofuncw - opção não disponível no Protheus - Função - FT300INBRA
type: support-article
updated_at: '2021-11-12T19:34:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029078012-MP-FAT-Nofuncw-op%C3%A7%C3%A3o-n%C3%A3o-dispon%C3%ADvel-no-Protheus-Fun%C3%A7%C3%A3o-FT300INBRA
---

**[*Remover as instruções entre colchetes*]****Ocorrência**

Ao incluir uma oportunidade de vendas (**Fata300**), no Faturamento, ocorre o erro:

**InterFunctionCall: cannot find function FT300INBRA in AppMap on { ||Ft300InBra() }(FWMBROWSE.PRW)13/07/2018 17:01:02**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030662191/mceclip0.png)  
   
 **Ambiente**

Microsiga Protheus - a partir da release 12.1.17.  
   
 **Causa**

A falta de função (**NOFUNCW**), indica que o fonte onde a função foi criada deve estar desatualizado.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Baixe o pacote mais atual da rotina **FATA300**:**<https://suporte.totvs.com/portal/p/10098/download?e=732213>**

2. Aplique o pacote, via TDS, em seu ambiente de testes para validação e posteriormente, no ambiente de prodição.

**Obs:**  A aplicação do pacote deve ser efetuado por um analista que detenha o conhecimento técnico para o procedimento, caso tenha dúvidas de procedimento, entre em contato com a equipe de FrameWork para auxiliá-lo.
